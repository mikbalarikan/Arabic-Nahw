# Türkçe iʿrāb ödev anahtarları: format ve kurallar

Kaynak kitap: /mnt/user-data/uploads/34c4b309-4._K_TAP_ye_il.pdf ("Bakara Sûresi Eşliğinde Kur'ân Dilbilgisi").
PDF sayfa numarası = kitabın basılı sayfa numarası. Her "İRAB BÖLÜMÜ k" tablosundan sonra bir "ÇALIŞMA m" gelir;
orada "Aşağıdaki ilk N ayetin irabını yapınız." der. Ödev = o listedeki 1..N numaralı ayet parçaları.

Kur'ân metni ve morfoloji: /home/claude/data/quran-morphology.txt (Quranic Arabic Corpus).
Satır: `sure:ayet:kelime:parça <TAB> metin <TAB> P|N|V <TAB> özellikler`. Kelime numarası 1'den başlar.
Ekranda gösterilen metin her zaman bu dosyadaki Osmanlı imlası metindir (kitabın imlası değil).

## Çıktı: /home/claude/work/keys/irab<k>.json
```json
{
  "irab": 9, "calisma": 27, "title": "<konu adı, kitaptan, ör. Müşterek İsmi Mevsûl>",
  "items": [
    {
      "n": 1, "ref": "Hac, 22/14", "tr": "<kitaptaki dipnot meali>",
      "src": [[22, 14, 1, 12]],          // [sure, ayet, ilk kelime, son kelime] (dahil). Birden çok ayet için birden çok aralık.
      "words": [
        {"loc": "22:14:1", "parts": [{"t": "إِنَّ", "kb": "inne ve benzerleri", "g": "görevi yok (harf)", "i": "mebni"}]},
        {"loc": "22:14:2", "parts": [{"t": "ٱللَّهَ", "kb": "alem (özel isim)", "g": "innenin ismi", "i": "mansub"}]},
        {"loc": "22:14:3", "parts": [
            {"t": "يُدْخِلُ", "kb": "muzari fiil", "g": "fiil", "i": "merfu"},
            {"t": "(هُوَ)", "hidden": true, "kb": "gizli zamir", "g": "fail", "i": "mebni"}]},
        {"loc": "22:14:5", "parts": [
            {"t": "ءَامَنُ", "kb": "mazi fiil", "g": "fiil", "i": "mebni"},
            {"t": "وا۟", "kb": "muttasıl zamir", "g": "fail", "i": "mebni"}]}
      ]
    }
  ]
}
```
- `words`: aralıktaki HER kelime, sırayla, eksiksiz.
- Bir kelimenin `parts` metinleri (hidden olmayanlar) art arda eklendiğinde morfoloji dosyasındaki kelime metnine (parçaların birleşimi) BİREBİR eşit olmalı.
- Parçalara ayırma: yalnızca kendi görevi olan parçaları ayır: ön ek وَ/فَ (atıf vb.), harfi cer بِ لِ كَ, لَ (tekid/lam), سَ; kelimeye bitişik zamirler (muttasıl zamir: fail, mefûlün bih, muzafun ileyh, mecrur). ال takısı ayrılmaz, kelimeyle birlikte kalır (ör. "ٱل"+"صَّٰلِحَٰتِ" tek parça: "ٱلصَّٰلِحَٰتِ").
- Fiilin faili gizliyse fiilden sonra `{"t":"(هُوَ)","hidden":true,...}` gibi gizli zamir parçası ekle (هُوَ/هِيَ/أَنتَ/أَنَا/نَحْنُ uygun olanı).
- Değerler (kb, g, i) AŞAĞIDAKİ LİSTELERDEN birebir seçilir. Birden fazla cevap kabul edilebiliyorsa liste ver: `"g": ["ma'tuf", "mefûlün bih"]` (ilki asıl cevap).
- Her parça için üç alan zorunlu.

## kb (kelime bilgisi)
isim · alem (özel isim) · mastar · ismi fail · ismi mefûl · ismi işaret · ismi mevsul · soru ismi · munfasıl zamir · muttasıl zamir · gizli zamir · mazi fiil · muzari fiil · emir fiil · harfi cer · atıf harfi · inne ve benzerleri · olumsuzluk edatı · cezm edatı · nasb edatı · soru harfi · diğer harf/edat

Notlar: Allah lafzı ve özel isimler (Mûsâ, Cehennem...) = alem (özel isim). كَانَ ve kardeşleri = mazi fiil (görevi "nakıs fiil (kâne vb.)"). لَمْ, لَا (nehy), إِنْ (şart, cezmediyorsa) = cezm edatı. لَنْ, أَنْ, كَيْ, لِ (ta'lil, muzariyi nasbediyorsa) = nasb edatı. مَا/لَا (nefy) = olumsuzluk edatı. هَلْ, أَ = soru harfi; مَنْ/مَا/كَيْفَ/أَيْنَ soru anlamında = soru ismi. فَ/وَ atıf ise atıf harfi, değilse diğer harf/edat. قَدْ, سَ, سَوْفَ, لَ (tekid), يَا, إِلَّا = diğer harf/edat. Zarf kelimeleri (يَوْمَ، عِنْدَ، تَحْتَ، إِذْ...) = isim.

## g (cümledeki görevi)
mübteda · haber · fiil · fail · naibi fail · mefûlün bih · mefûlün mutlak · mefûlün fîh (zarf) · hal · sıfat · muzafun ileyh · mecrur (harfi cerden sonra) · ma'tuf · bedel · innenin ismi · innenin haberi · nakıs fiil (kâne vb.) · kânenin ismi · kânenin haberi · münada · temyiz · görevi yok (harf)

Notlar: Bütün harfler (harfi cer, atıf, edatlar) = "görevi yok (harf)". Haber/hal/sıfat bir cümle ya da şibhi cümle ise, o cümlenin içindeki kelimeler kendi görevlerini alır (fiil, fail, mecrur...). Ma'tuf: atıf harfinden sonraki kelime; ondan önceki kelimenin görevi de kabul edilsin: `["ma'tuf", "<önceki görev>"]`. Muzaf olan kelime asıl görevini alır (ör. mübteda). Sıla cümlesi içindeki kelimeler kendi görevlerini alır.

## i (irab)
merfu · mansub · mecrur · meczum · mebni

Notlar: Mebni kelimelerde (zamir, ismi işaret, ismi mevsul (müsenna hariç), harfler, mazi ve emir fiil, nûn-u nisve/tekid alan muzari) cevap "mebni"dir (mahalli irab sorulmaz). Takdiri irabda (مُوسَىٰ, هُدًى, ٱلْقَاضِى...) asıl hal yazılır: merfu/mansub/mecrur. Muzari fiil: normal = merfu, nasb edatıyla = mansub, cezm edatıyla/emre cevap = meczum.

## Kontrol
`python3 /home/claude/work/check_keys.py /home/claude/work/keys/irab<k>.json` HATA vermeden bitmeli. İsimlerin irabını morfolojideki NOM/ACC/GEN ile, muzari fiilleri MOOD ile karşılaştırır; parça metinlerinin kelimeyle birleştiğini ve tüm değerlerin listeden olduğunu kontrol eder.
