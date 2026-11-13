#!/usr/bin/env python3
"""Phoneme transcript of a speech clip (wav2vec2-lv-60-espeak-cv-ft, ONNX, CPU).

Used to check that a TTS voice really says the last vowel of each Arabic word
(e.g. ad-darsa, not ad-dars). Model: onnx-community/wav2vec2-lv-60-espeak-cv-ft-ONNX
(model_q4.onnx) + vocab.json from facebook/wav2vec2-lv-60-espeak-cv-ft (Apache-2.0).

Usage: python3 video/tools/phonemes.py MODEL_DIR clip.wav [clip2.wav ...]
"""
import json, subprocess, sys
from pathlib import Path
import numpy as np
import onnxruntime as ort

class Phonemizer:
    def __init__(self, model_dir):
        d = Path(model_dir)
        self.sess = ort.InferenceSession(str(d / "model_q4.onnx"), providers=["CPUExecutionProvider"])
        vocab = json.loads((d / "vocab.json").read_text(encoding="utf-8"))
        self.inv = {v: k for k, v in vocab.items()}
        self.blank = vocab.get("<pad>", 0)

    def __call__(self, wav):
        raw = subprocess.run(["ffmpeg", "-v", "error", "-i", str(wav), "-ac", "1", "-ar", "16000", "-f", "f32le", "-"],
                             check=True, capture_output=True).stdout
        a = np.frombuffer(raw, dtype=np.float32)
        a = (a - a.mean()) / (a.std() + 1e-7)
        names = [i.name for i in self.sess.get_inputs()]
        feed = {names[0]: a[None, :]}
        if "attention_mask" in names:
            feed["attention_mask"] = np.ones((1, len(a)), dtype=np.int64)
        logits = self.sess.run(None, feed)[0][0]
        ids = logits.argmax(-1)
        out, prev = [], None
        for i in ids:
            if i != prev and i != self.blank:
                t = self.inv.get(int(i), "")
                if not t.startswith("<"):
                    out.append(t)
            prev = i
        return " ".join(out)

if __name__ == "__main__":
    p = Phonemizer(sys.argv[1])
    for w in sys.argv[2:]:
        print(Path(w).name, "->", p(w))
