// Copy to site/config.js (or let the build write it from environment variables).
// Both values are in Supabase: Project Settings -> API. The anon key is public by design;
// the database rules in supabase/schema.sql decide who can read and write what.
window.IRAAB_CONFIG = {
  supabaseUrl: "https://YOUR-PROJECT.supabase.co",
  supabaseAnonKey: "YOUR-ANON-KEY",
};
