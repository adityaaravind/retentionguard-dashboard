# RetentionGuard Dashboard

A generic third-party data lifecycle guard dashboard. It shows, in one
place, how customer data should age out, be proven deleted, and be
protected from bulk export — before it can be stolen in a breach.

**All data is synthetic and generated in the browser. No real personal
data, no network calls, no exploit code, and no company is named.**

## Run it in 10 seconds — no install

**Easiest, no download at all:** open the live demo, once GitHub
Pages is turned on for this repo (see below):

https://adityaaravind.github.io/retentionguard-dashboard/

**Easiest, with a download:** download `index.html` from this repo
and double-click it. That's it. No install, no build, no server,
no dependencies — everything runs in your browser, and all data is
synthetic.

**Easiest, from a clone:**

```bash
git clone https://github.com/adityaaravind/retentionguard-dashboard.git
cd retentionguard-dashboard
python3 run.py
```

Or double-click `run.sh` (Mac/Linux) or `run.bat` (Windows) — both
just open `index.html` in your browser.

Want it served over HTTP instead? Run:

```bash
python3 run.py --serve
```

then open http://localhost:8000

### Turn on the live demo (repo owner, one time)

Repo > Settings > Pages > Build and deployment > Source:
**Deploy from a branch**, Branch: `main`, Folder: `/ (root)`.
Save, wait a minute, and the live demo link above will work.
Until that setting is on, the live demo link will show a 404 —
use the download or clone options instead. No workflow file is
needed for this branch deploy; the file in
`.github/workflows/static.yml` in the local copy is an optional
Actions alternative, and workflow files have to be added through
the GitHub web UI, not through the automated push used here.

## What it does

- **Order Vault:** 120 synthetic orders, with a 90-day retention window.
  Run the retention sweep to anonymize orders older than 90 days.
  Returns and refunds stay visible in an exception queue, not a
  silent loophole.
- **Deletion certificate:** each sweep issues a batch certificate
  with a hash chain. Verify it, or simulate tampering and watch
  verification fail.
- **BI Export Guard:** test an export. A bulk personal-data export,
  or a non-parameterized query, is blocked and alerted. A limited,
  parameterized export is allowed.
- **Vendor attestation:** a vendor claim is checked against counts
  and sample records. In the demo, HarborLine flags a 253-record
  mismatch.
- **Breach scope:** pick a compromised system and date range, and
  generate the affected synthetic customers, the exposed fields,
  and a notification draft, with a CSV download.

## Safety and scope

This is a defensive demo. Do not use it with real customer data,
do not connect it to a real identity provider or vendor system, and
do not present synthetic numbers as real incident numbers. The hash
chain in the demo is a simple illustrative hash, not a production
cryptographic proof system.

## Files

- `index.html` — the whole dashboard, standalone, no dependencies
- `docs/` — put the motion-graphic GIF here when you upload it
  through the GitHub web UI (binary files are not pushed by the
  automated connector used for this repo)

## License

MIT — see [LICENSE](LICENSE).
