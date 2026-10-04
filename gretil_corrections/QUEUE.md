# GRETIL corrections queue — trackable loop

_Created: 2026-10-05 · Last updated: 2026-10-05_

Trackable loop for the GRETIL e-text corrections pipeline: one row per reported locus,
status lifecycle, and a column for GRETIL's reply links. Generated from the canonical
[SanskritSpellCheck GRETIL_UPSTREAM_REPORT.md](https://github.com/drdhaval2785/SanskritSpellCheck/blob/master/detectors/meter/GRETIL_UPSTREAM_REPORT.md)
by [tools/build_queue.py](tools/build_queue.py) — regenerate, never hand-edit the TSV.
Readings' payload stays in the canonical report; the queue tracks only locus + status + reply.

**Gate (row 0): the OUTREACH email itself — DRAFT, UNSENT**
([Uprava/handoffs/OUTREACH_2026-07-10_gretil_etext_corrections.md](https://github.com/gasyoun/Uprava/blob/main/handoffs/OUTREACH_2026-07-10_gretil_etext_corrections.md),
agent never sends; MG @DO). Every locus row sits in `draft-unsent` until that email goes out.

## Snapshot (2026-10-05)

- 71 loci queued: 60 verified + 11 anomalous (no fix proposed), across 7 e-texts
- statuses: draft-unsent 71 · sent 0 · awaiting-gretil 0 · fixed-upstream 0 · wontfix-gretil 0

## Status lifecycle

`draft-unsent` → `sent` (email went out; stamp date in last_touch) → `awaiting-gretil`
(default after send; reply overdue >90d → ping MG) → `fixed-upstream` / `wontfix-gretil`
(link GRETIL's reply URL or quote in `gretil_reply`, flip `last_touch`).

## Files

- [QUEUE.tsv](QUEUE.tsv) — the machine-tractable queue (8 columns, TSV)
- [QUEUE.md](QUEUE.md) — this view (snapshot + protocol)
- [tools/build_queue.py](tools/build_queue.py) — regenerate both from the upstream report (canary: 60+11)

_Гасунс_
