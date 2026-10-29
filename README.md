# RetentionGuard Dashboard

A generic third-party data lifecycle guard dashboard. It shows, in one
place, how customer data should age out, be proven deleted, and be
protected from bulk export — before it can be stolen in a breach.

**All data is synthetic and generated in the browser. No real personal
data, no network calls, no exploit code, and no company is named.**

## Open it

Open `index.html` in a browser, or enable GitHub Pages for this repo
(main branch, root folder). No build step, no dependencies.

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

## LinkedIn title

Recommended: **“The best data breach is the data that was already gone.”**

Alternatives:

- “I built RetentionGuard, a dashboard that makes data deletion provable, not just promised.”
- “Your vendor said they deleted your customers' data. Can they prove it?”
- “Retention is a security control, not a paperwork promise.”

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
