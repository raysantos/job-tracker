# Job Tracker

Ray's job-application tracker, published with GitHub Pages.

The data is AES-256-GCM encrypted (PBKDF2-SHA256, 600k iterations) in `data.enc.json` and decrypted in the browser with a passcode. The plain `data.json` is never committed.

To update: edit your local `data.json`, then run `python3 tools/encrypt.py path/to/data.json <passcode>` and commit `data.enc.json`.

## Recommended roles (`recommended.json`)

The **Recommended** tab reads `recommended.json` from the repo root. This file is **not encrypted**, because it holds only public job postings. A job-search run can add to it without the passcode. The page loads it only after you unlock.

```json
{
  "updated": "2026-10-14",
  "roles": [
    {
      "id": "mavenclinic-8115319002",
      "company": "Maven Clinic",
      "domain": "mavenclinic.com",
      "role": "Senior Product Designer",
      "where": "New York, hybrid or remote",
      "salary": [175000, 195000],
      "url": "https://job-boards.greenhouse.io/mavenclinic/jobs/8115319002",
      "why": "Why this role fits",
      "family": true,
      "closes": "2026-10-31"
    }
  ]
}
```

- `id` must be unique and stable. Your Approve and Skip choices are saved on each device by `id`, and a role with an `id` the device hasn't seen before counts as a new batch, which opens the tab automatically.
- Roles are ranked in the order they appear in the file.
- `family: true` adds a "Family health" badge. `closes` (optional, `YYYY-MM-DD`) adds a "Closes in X days" badge when the role closes within 7 days.
- Any role whose company and title match an entry in Submitted or In progress is hidden. The tab is hidden when no roles are left.
- Never put private notes here. Anything private belongs in the encrypted `data.json`.
