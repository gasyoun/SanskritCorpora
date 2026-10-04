#!/usr/bin/env python3
"""build_queue.py — regenerate QUEUE.tsv + QUEUE.md from the canonical upstream report.

Source of truth: SanskritSpellCheck detectors/meter/GRETIL_UPSTREAM_REPORT.md
(60 verified loci + 11 anomalous across 7 e-texts, human-adjudicated 10-07-2026).
The queue never duplicates the readings' payload — it tracks locus + status + reply.

Usage: build_queue.py [path-to-GRETIL_UPSTREAM_REPORT.md]
Exits 1 unless the parse reproduces the report's own counts (60 verified + 11 anomalous).
"""
import re, sys, datetime, pathlib

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

REPORT_DEFAULT = "/Users/mac/Documents/GitHub/SanskritSpellCheck/detectors/meter/GRETIL_UPSTREAM_REPORT.md"
EXPECTED_VERIFIED, EXPECTED_ANOMALOUS = 60, 11
OUTREACH_REF = "OUTREACH_2026-07-10_gretil_etext_corrections.md"
OUTREACH_URL = "https://github.com/gasyoun/Uprava/blob/main/handoffs/OUTREACH_2026-07-10_gretil_etext_corrections.md"
REPORT_URL = "https://github.com/drdhaval2785/SanskritSpellCheck/blob/master/detectors/meter/GRETIL_UPSTREAM_REPORT.md"


def parse(src: str):
    rows = []  # (gretil_file, class, locus)
    cur_file = None
    table_class = None
    lines = src.splitlines()
    for i, line in enumerate(lines):
        m = re.match(r"^## \d+\. `([^`]+)`", line)
        if m:
            cur_file, table_class, seen_header = m.group(1), None, False
            continue
        if line.startswith("## "):
            cur_file, table_class = None, None
            continue
        if not cur_file:
            continue
        if line.startswith("| Locus"):
            header = line.lower()
            table_class = "anomalous" if "note" in header else "verified"
            seen_header = True
            continue
        if line.startswith("|"):
            first = line.strip("|").split("|")[0].strip()
            if not first or set(first) <= set("- "):
                continue
            cls = table_class or "verified"  # headerless continuation rows inherit
            rows.append((cur_file, cls, first))
            continue
        if line.startswith("Anomalous:"):
            block = [line]
            # the inline anomaly list wraps onto following lines until a blank line
            for nxt in lines[i + 1:]:
                if not nxt.strip():
                    break
                block.append(nxt)
            for loc in re.findall(r"\b(\d+\.\d+)\b", " ".join(block)):
                rows.append((cur_file, "anomalous", loc))
    return rows


def main():
    report = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else REPORT_DEFAULT)
    src = report.read_text()
    raw = parse(src)
    seen, rows = set(), []
    for gf, cls, loc in raw:
        key = (gf, cls, loc)
        if key in seen:
            continue
        seen.add(key)
        rows.append((gf, cls, loc))
    nv = sum(1 for r in rows if r[1] == "verified")
    na = len(rows) - nv
    if (nv, na) != (EXPECTED_VERIFIED, EXPECTED_ANOMALOUS):
        sys.exit(f"CANARY FAIL: parsed {nv} verified + {na} anomalous, "
                 f"expected {EXPECTED_VERIFIED}+{EXPECTED_ANOMALOUS} — report format drifted, fix the parser")
    here = pathlib.Path(__file__).resolve().parents[1]
    today = datetime.date.today().isoformat()
    with open(here / "QUEUE.tsv", "w") as f:
        f.write("locus_id\tgretil_file\tclass\tlocus\tstatus\treported_ref\tgretil_reply\tlast_touch\n")
        for i, (gf, cls, loc) in enumerate(rows, 1):
            f.write(f"G{i:03d}\t{gf}\t{cls}\t{loc}\tdraft-unsent\t{OUTREACH_REF}\t\t{today}\n")
    files = sorted(set(r[0] for r in rows))
    (here / "QUEUE.md").write_text(f"""# GRETIL corrections queue — trackable loop

_Created: {today} · Last updated: {today}_

Trackable loop for the GRETIL e-text corrections pipeline: one row per reported locus,
status lifecycle, and a column for GRETIL's reply links. Generated from the canonical
[SanskritSpellCheck GRETIL_UPSTREAM_REPORT.md]({REPORT_URL})
by [tools/build_queue.py](tools/build_queue.py) — regenerate, never hand-edit the TSV.
Readings' payload stays in the canonical report; the queue tracks only locus + status + reply.

**Gate (row 0): the OUTREACH email itself — DRAFT, UNSENT**
([Uprava/handoffs/OUTREACH_2026-07-10_gretil_etext_corrections.md]({OUTREACH_URL}),
agent never sends; MG @DO). Every locus row sits in `draft-unsent` until that email goes out.

## Snapshot ({today})

- {len(rows)} loci queued: {nv} verified + {na} anomalous (no fix proposed), across {len(files)} e-texts
- statuses: draft-unsent {len(rows)} · sent 0 · awaiting-gretil 0 · fixed-upstream 0 · wontfix-gretil 0

## Status lifecycle

`draft-unsent` → `sent` (email went out; stamp date in last_touch) → `awaiting-gretil`
(default after send; reply overdue >90d → ping MG) → `fixed-upstream` / `wontfix-gretil`
(link GRETIL's reply URL or quote in `gretil_reply`, flip `last_touch`).

## Files

- [QUEUE.tsv](QUEUE.tsv) — the machine-tractable queue (8 columns, TSV)
- [QUEUE.md](QUEUE.md) — this view (snapshot + protocol)
- [tools/build_queue.py](tools/build_queue.py) — regenerate both from the upstream report (canary: 60+11)

_Гасунс_
""")
    print(f"OK: {len(rows)} rows ({nv} verified + {na} anomalous), {len(files)} e-texts")


if __name__ == "__main__":
    main()
