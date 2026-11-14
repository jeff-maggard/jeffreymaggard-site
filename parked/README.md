# Parked (not deployed)

Cloudflare deploys only `site/`, so nothing in this folder is public.

- `media/pi/`, `media/pure-intellect-tutor.*`: Pure Intellect Tutor/Analyzer and the hidden AI course (hidden 14 Nov 2026 at Jeffrey's request).
- `media/tales/`: Qatar University student artwork removed from the Tales of Qatari Heritage page (14 Nov 2026).

To restore: move the files back under `site/media/`, remove `hidden=True` / re-add the banner fields in `tools/content.py`, and run `python3 tools/build.py`.
