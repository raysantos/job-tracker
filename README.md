# Job Tracker

Ray's job-application tracker, published with GitHub Pages.

The data is AES-256-GCM encrypted (PBKDF2-SHA256, 600k iterations) in `data.enc.json` and decrypted in the browser with a passcode. The plain `data.json` is never committed.

To update: edit your local `data.json`, then run `python3 tools/encrypt.py path/to/data.json <passcode>` and commit `data.enc.json`.
