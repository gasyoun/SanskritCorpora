# SYNTHESIS_CORPUS_CLUSTER — week 6 of the 8-week synthesis program

_Created: 13-11-2026 · Last updated: 13-11-2026_

**Handoff:** [H8062](https://github.com/gasyoun/Uprava/blob/main/handoffs/H8062-MiMo_SanskritCorpora_synthesis-w6-corpus-cluster_11.11.26.md) · **Program:** [SYNTHESIS_PROGRAM_8W_2026-11-11.md](https://github.com/gasyoun/Uprava/blob/main/SYNTHESIS_PROGRAM_8W_2026-11-11.md) · **Executor:** MiMo (`xiaomi-token-plan-sgp/mimo-v2.6-pro`), opencode · **Depth:** deep (contradiction graph) · **Code:** equal source

**Scope:** the corpus cluster — DCS (Hellwig's Digital Corpus of Sanskrit as distributed via [`gasyoun/dcs-conllu`](https://github.com/gasyoun/dcs-conllu)), [VisualDCS](https://github.com/gasyoun/VisualDCS) (corpus ingest owner + research archive), [Parallel-Sanskrit-Corpora](https://github.com/gasyoun/Parallel-Sanskrit-Corpora) (alignment layer), [SanskritCorpora](https://github.com/gasyoun/SanskritCorpora) (this metarepo) — claims about **coverage / alignment / representativeness**, code as equal source.

## Corpus inventory (bounded ~25-doc pass, 13-11-2026)

| Source | Size | Read strategy |
|---|---|---|
| [VisualDCS README.md](https://github.com/gasyoun/VisualDCS/blob/main/README.md) | 583 lines | whole — the claims surface (coverage, Pareto, data ceilings) |
| [docs/DCS_SQLITE_CONLLU_CONSUMER_DEEP_MANUAL.md](https://github.com/gasyoun/VisualDCS/blob/main/docs/DCS_SQLITE_CONLLU_CONSUMER_DEEP_MANUAL.md) | 392 lines | whole — doc-of-record; all 22 gotchas live-provenance-linked |
| [docs/SAIS_CONCORDANCE_DCS_2026-09.md](https://github.com/gasyoun/VisualDCS/blob/main/docs/SAIS_CONCORDANCE_DCS_2026-09.md) | 139 lines | whole — suffix-array layer, byte-verified finds |
| [derived-lsc/README.md](https://github.com/gasyoun/VisualDCS/blob/main/derived-lsc/README.md) | 186 lines | whole — LSC pilot protocol + build census |
| [reports/NCC_SK_BLOCK_COVERAGE_2026-10-19.md](https://github.com/gasyoun/VisualDCS/blob/main/reports/NCC_SK_BLOCK_COVERAGE_2026-10-19.md) | 335 lines | §0–§2 (verdict + discriminating counts + export fidelity) |
| [reports/paradigm_attested_build.md](https://github.com/gasyoun/VisualDCS/blob/main/reports/paradigm_attested_build.md) | 52 lines | whole — H1299/H1486/H2294 scope deltas |
| [reports/paradigm_nominal_build.md](https://github.com/gasyoun/VisualDCS/blob/main/reports/paradigm_nominal_build.md) | 62 lines | whole (via README cross-refs, key numbers re-verified) |
| [reports/uttarapada_dict_vs_corpus_divergence.md](https://github.com/gasyoun/VisualDCS/blob/main/reports/uttarapada_dict_vs_corpus_divergence.md) | 171 lines | §denominators + strata + Finding 1 |
| [docs/csl-atlas-migration/DCS_CORPUS_INGESTION_PLAN.md](https://github.com/gasyoun/VisualDCS/blob/main/docs/csl-atlas-migration/DCS_CORPUS_INGESTION_PLAN.md) + [DCS_SCHEMA.md](https://github.com/gasyoun/VisualDCS/blob/main/docs/csl-atlas-migration/DCS_SCHEMA.md) | 162 + 105 lines | whole — migration-era material (superseded banner noted) |
| [roadmap.md](https://github.com/gasyoun/VisualDCS/blob/main/roadmap.md) | 157 lines | whole |
| VisualDCS code: `gen_dcs_lemma_summary.py` / `validate_dcs_lemma_summary.py` / `scripts/verb_total_check.py` / `src/DCS-data-2026/` pipeline | — | code-as-equal-source spot-checks (below) |
| [PSC README.md](https://github.com/gasyoun/Parallel-Sanskrit-Corpora/blob/master/README.md) | 65 lines | whole |
| [H4707_DCS_PARALLELS_QA_BASELINE_15-09-2026.md](https://github.com/gasyoun/Parallel-Sanskrit-Corpora/blob/master/H4707_DCS_PARALLELS_QA_BASELINE_15-09-2026.md) | 64 lines | whole — parallels baseline |
| [H6070_SA_RU_ALIGNER_EVALUATION_04-10-2026.md](https://github.com/gasyoun/Parallel-Sanskrit-Corpora/blob/master/H6070_SA_RU_ALIGNER_EVALUATION_04-10-2026.md) | 34 lines | whole — honest-negative aligner eval |
| PSC code: [`tools/build_baseline.py`](https://github.com/gasyoun/Parallel-Sanskrit-Corpora/blob/master/tools/build_baseline.py), [`tools/align_sa_ru.py`](https://github.com/gasyoun/Parallel-Sanskrit-Corpora/blob/master/tools/align_sa_ru.py), [`tests/test_aligner.py`](https://github.com/gasyoun/Parallel-Sanskrit-Corpora/blob/master/tests/test_aligner.py) + `data/*.json` | — | executed (below) |
| [SanskritCorpora README.md](https://github.com/gasyoun/SanskritCorpora/blob/main/README.md) + [gretil_corrections/QUEUE.md](https://github.com/gasyoun/SanskritCorpora/blob/main/gretil_corrections/QUEUE.md) | 106 + 30 lines | whole |
| [dcs-conllu](https://github.com/gasyoun/dcs-conllu) tree + `lookup/chapter-info.xml` dating (via LSC) | — | structure probe |
| Cross-surfaces: Uprava [DATA_LAYERS_CENSUS.md](https://github.com/gasyoun/Uprava/blob/main/DATA_LAYERS_CENSUS.md) DCS rows · [ARTICLES.md](https://github.com/gasyoun/Uprava/blob/main/ARTICLES.md) A38/A40/A57 rows · [WhitneyRoots README](https://github.com/gasyoun/WhitneyRoots/blob/main/README.md) root counts | — | selected rows |

**Method:** bounded extraction per surface (no >100 KB whole-file reads needed — the cluster's docs are compact); every item carries `file:<line>` or §-cite; 152-FZ fence respected. VisualDCS read via GitHub API (25 GB repo not cloned on this host). **Code-as-equal-source:** four executed spot-checks + four arithmetic re-derivations (below).

## Themes

1. **Vintage discipline is the cluster's dominant defect class.** Three corpus generations circulate under one label "DCS counts": the 2021 relational export (≈4.57M annotated tokens, `10.csv`), the M9 Leonchenko-era archive (4,550,704 tokens / 59,282 lemmas quoted by [csl-guides](https://github.com/gasyoun/VisualDCS/blob/main/docs/DCS_SQLITE_CONLLU_CONSUMER_DEEP_MANUAL.md#:320)), and the 2026 CoNLL-U master (5,688,416 tokens / 98,606 attested lemma_ids). Same lemma, both "DCS": `ca` 174,415 (master) vs 155,088 (archive), `tad` 197,087 vs 151,248 ([manual:163](https://github.com/gasyoun/VisualDCS/blob/main/docs/DCS_SQLITE_CONLLU_CONSUMER_DEEP_MANUAL.md)). The manual's rule is absolute — *never mix vintages in one denominator* — yet the org's **canonical consumer asset** `dcs_lemma_summary.json` (83,239 lemmas, [README:106](https://github.com/gasyoun/VisualDCS/blob/main/README.md)) is still built from the 2021 dump while A38 instructs "cite 98,606 (2026), not 83,239 (2021)" ([ARTICLES.md:342](https://github.com/gasyoun/Uprava/blob/main/ARTICLES.md)).
2. **Every count is instrument-scoped; sample claims die corpus-wide.** `DCS_FORMAT_COMPARISON.md`'s "older UD inventory, no `SCONJ`" is one chapter's truth; corpus-wide `upos='SCONJ'` = 31,499 tokens ([manual:149](https://github.com/gasyoun/VisualDCS/blob/main/docs/DCS_SQLITE_CONLLU_CONSUMER_DEEP_MANUAL.md), G17). G2's `feat_case='Cpd'` = 841,052 (all-POS) vs G19's 724,676 (NOUN/ADJ = 24.2%) — same feature, two universes ([manual:339](https://github.com/gasyoun/VisualDCS/blob/main/docs/DCS_SQLITE_CONCLU_CONSUMER_DEEP_MANUAL.md), [:356](https://github.com/gasyoun/VisualDCS/blob/main/docs/DCS_SQLITE_CONLLU_CONSUMER_DEEP_MANUAL.md)). The paradigm trainer admits 7,689 roots at floor ≥2 ([paradigm_attested_build.md](https://github.com/gasyoun/VisualDCS/blob/main/reports/paradigm_attested_build.md)) while E46 counts 8,054/11,096 — reconciled only on the 6,454-root overlap, `mismatch=0`.
3. **Honest negatives are shipped as artifacts, not smoothed.** The NCC `स्क` block verdict is *NOT RECOVERABLE from the bundled 2022 database*, with the export-fidelity proof (152,526 records, 0 title diffs, 26 body diffs) that turns a suspicion into a measured absence ([NCC_SK_BLOCK_COVERAGE](https://github.com/gasyoun/VisualDCS/blob/main/reports/NCC_SK_BLOCK_COVERAGE_2026-10-19.md)). The SA↔RU aligner report's verdict line is «цель ≥0.9 НЕ достигнута» — 0.03–0.13 measured over 8/8 stop-budget attempts, diagnosis + repair path landed ([H6070:5](https://github.com/gasyoun/Parallel-Sanskrit-Corpora/blob/master/H6070_SA_RU_ALIGNER_EVALUATION_04-10-2026.md)). Aorist/Perfect are published as **bounds** with direction stated, not as counts.
4. **Encoding and citation-form conventions manufacture findings.** The H1328 naïve join matched 29% and *looked like research*; after anusvāra/avagraha/MW-markup folding it was 33% — the 4-point gap pure convention noise ([manual:190–201](https://github.com/gasyoun/VisualDCS/blob/main/docs/DCS_SQLITE_CONCLU_CONSUMER_DEEP_MANUAL.md)). The mirror discipline: fold orthography, **never** morphology (`sena`/`senā` are distinct lemmas — 5 vs 1,075 tokens; 1,289 `form_variant` pairs are *diagnoses*, never absences).
5. **Corpus absence ≠ lexical absence; the corpus "suggests, never decides".** The uttarapada census's dictionary-only stratum (10,387 finals) is 86% MW hapax — a *kośa-only lexical stratum*, not ghost words ([uttarapada:49,84](https://github.com/gasyoun/VisualDCS/blob/main/reports/uttarapada_dict_vs_corpus_divergence.md)); and even where both sides attest a final (6,249), first-member vocabularies barely overlap (median Jaccard 0.00; 56% share zero). G1 shows famous works hide inside others (Bhagavadgītā under `MBh, 6, BhaGī N`, 10,547 tokens; Nala inside MBh) — name lookups lie ([manual:338](https://github.com/gasyoun/VisualDCS/blob/main/docs/DCS_SQLITE_CONLLU_CONSUMER_DEEP_MANUAL.md)).
6. **Coverage assets are Pareto-skewed and epistemic-status-gated.** 5 verb-form categories cover 77.6% of 781,616 examples; 11 cover 94.9% ([README:489](https://github.com/gasyoun/VisualDCS/blob/main/README.md)); top-6 Whitney roots ≈28% of attested root-token mass. Every derived cell ships its epistemic status: `cellEvidence` `formation-attested` vs `defaulted` (degenerate 0%/100% by construction, asserted at build), `m_unsandhiedreconstructed` flags (68.0% of nominal grid), treebank arcs only 3.9% of tokens (G3).
7. **The alignment layer is weak-gold on both axes.** Parallel-passage GOOD pairs (14,557 of 154,033) are machine-derived verdicts — "treat GOOD as weak gold until a human spot-check wave" ([H4707:61](https://github.com/gasyoun/Parallel-Sanskrit-Corpora/blob/master/H4707_DCS_PARALLELS_QA_BASELINE_15-09-2026.md)); LSC's n=30 human gold is still an empty annotation sheet; the SA↔RU tool's only strong result is its block-structure micro case.

## Agreements

1. **The 2026 master is clean and pinned.** All 5,688,416 tokens resolve the spine join, 0 orphans, 0 NULL `lemma_id` ([manual §3](https://github.com/gasyoun/VisualDCS/blob/main/docs/DCS_SQLITE_CONLLU_CONSUMER_DEEP_MANUAL.md)); SAIS's four corpus counts (48,167,032 B · 5,688,416 · 754,726 · 270) match the manual's live row counts exactly ([SAIS «Measured»](https://github.com/gasyoun/VisualDCS/blob/main/docs/SAIS_CONCORDANCE_DCS_2026-09.md)) — a second, independent instrument agreeing on the universe.
2. **2021 is NOT superseded** (H686 verdict, carried in DATA_LAYERS_CENSUS): 6 texts + 1,761 lemma IDs exist only in 2021; keep both generations, 2026 canonical.
3. **Bounds-not-exact for the past re-split, stated the same way on every surface** — Aorist 12,054 lower bound (≥1.13% leakage), Perfect 77,229 upper bound (≥3.54% Impf contamination); README, [paradigm_attested_build.md](https://github.com/gasyoun/VisualDCS/blob/main/reports/paradigm_attested_build.md) and A38's corrected §6 now agree (the "too sparse" claim is retracted everywhere: denominator 1.60%→17.25%).
4. **Universe-closure is asserted, not assumed** — nominal grid + Cpd + untagged = 2,996,410 = the whole NOUN/ADJ universe, asserted at build time (G20's NULL-safe complement rule exists because the H1472 build lost 8,542 tokens to it).
5. **Vintage mixing is prohibited on every consumer surface** — manual §4.3, kosha's own builder warning ("any residual excess is a DCS-vintage mismatch"), and H4707's segment-vs-rows reconciliation (501,231 segments vs registry `rows: 506,787` = raw lines incl. ~5.5k blanks, [H4707:22](https://github.com/gasyoun/Parallel-Sanskrit-Corpora/blob/master/H4707_DCS_PARALLELS_QA_BASELINE_15-09-2026.md)).
6. **Instrument independence is practiced**: the LSC graded ranking's control ρ = −0.013 vs the frequency-shift baseline (not a re-description of frequency change), and the SAIS `find` was byte-verified *and* SQL-verified on both build boxes.

## Disagreements (contradiction graph)

### Claim forks across cluster surfaces

| # | Fork | A cite | B cite | State |
|---|---|---|---|---|
| 1 | Lemma inventory in circulation: 83,239 (canonical consumer asset, 2021) vs 98,606 (2026 attested lemma_ids) vs 180,176 (lemma dictionary rows) vs 91,406 (2021 attested) | `README:106` ([VisualDCS](https://github.com/gasyoun/VisualDCS/blob/main/README.md)) | [manual:65](https://github.com/gasyoun/VisualDCS/blob/main/docs/DCS_SQLITE_CONCLU_CONSUMER_DEEP_MANUAL.md), [:140](https://github.com/gasyoun/VisualDCS/blob/main/docs/DCS_SQLITE_CONCLU_CONSUMER_DEEP_MANUAL.md) | **Reconciled in the manual** (rows-vs-occurring; 91,406→98,606 Jaccard 89.3%) **but live downstream**: A38 says cite 98,606 while kosha/csl-atlas read the 83,239/83,277-era feeds — see open `[T]`-1 |
| 2 | `feat_case='Cpd'` = 841,052 (G2, all-POS) vs 724,676 (G19, NOUN/ADJ-only = 24.2%) | [manual:339](https://github.com/gasyoun/VisualDCS/blob/main/docs/DCS_SQLITE_CONCLU_CONSUMER_DEEP_MANUAL.md) | [manual:356](https://github.com/gasyoun/VisualDCS/blob/main/docs/DCS_SQLITE_CONLLU_CONSUMER_DEEP_MANUAL.md) | **open** — same feature label, two universes; the 116,376-token difference (non-NOUN/ADJ Cpd) is nowhere reconciled; every surface warns "decide the denominator" but none pairs the two figures. Discriminant query named in `[R]`-2 |
| 3 | Bhagavadgītā 1.1 opening: G1 says the Gītā is present (10,547 tokens under `MBh, 6, BhaGī N`) vs SAIS: the string `dharmakṣetre` occurs **exactly once** in the whole 5.69M-token stream — at SkPur (Rkh) Revākhaṇḍa 143, "the famous Gītā 1.1 opening quoted inside the Skandapurāṇa" | [manual:338](https://github.com/gasyoun/VisualDCS/blob/main/docs/DCS_SQLITE_CONCLU_CONSUMER_DEEP_MANUAL.md) | [SAIS:116–118](https://github.com/gasyoun/VisualDCS/blob/main/docs/SAIS_CONCORDANCE_DCS_2026-09.md) | **open** — if BhaGī 1 carries the standard opening, the count would be ≥2; either DCS's Gītā recension lacks/renames verse 1.1 or form orthography (`dharma-kṣetre` hyphenated vs sandhied) hides it. Discriminant query named in `[R]`-1 |
| 4 | Whitney hub: 930 roots vs 935; "713 DCS-attested" vs "755/935 linked" | [VisualDCS README:403](https://github.com/gasyoun/VisualDCS/blob/main/README.md) | [manual:266,278](https://github.com/gasyoun/VisualDCS/blob/main/docs/DCS_SQLITE_CONCLU_CONSUMER_DEEP_MANUAL.md) + [WhitneyRoots README](https://github.com/gasyoun/WhitneyRoots/blob/main/README.md) (its own README uses both: "930-root crosswalk" vs "935-root hub") | **open, likely key-space** (crosswalk rows incl. homonyms vs lexicon hub; attested-tokens vs linked-lemmas) — but no surface states the pairing |
| 5 | LSC build census 754,561 / 5,687,226 / 90,331 distinct lemmas vs master 754,726 / 5,688,416 / 98,606 | [derived-lsc:76](https://github.com/gasyoun/VisualDCS/blob/main/derived-lsc/README.md) | manual §2 | **partially explained** — 17 chapters carry no `dcsTimeSlot` and are excluded (explains −165 sentences/−1,190 tokens); the 8,275-lemma gap is a string-vs-`lemma_id` key-space difference, not stated anywhere. Low stakes (LSC is self-contained) |
| 6 | Verb totals 781,616 (Excel) / 781,618 (`timws.csv`) / 745,394 (87-cell browser) / 741,782 (retracted mis-sum) | [README:71,199,416](https://github.com/gasyoun/VisualDCS/blob/main/README.md) | A38 correction record | **resolved & gated** — documented ±2/±10 reconciliations, `scripts/verb_total_check.py` re-derives from bytes; the 741,782 mis-sum is retracted |
| 7 | `dcs_texts_clean.json` 288 texts vs corpus `text` table 270 vs 2021's 246 vs parallels export 245 source files | [README data-assets](https://github.com/gasyoun/VisualDCS/blob/main/README.md) | manual §2/§4.1, [H4707:22](https://github.com/gasyoun/Parallel-Sanskrit-Corpora/blob/master/H4707_DCS_PARALLELS_QA_BASELINE_15-09-2026.md) | **instrument-scoped, documented per instrument** — but 288's provenance (2021-era tense profiles) is not labelled at point of use; G1 warns text-count lookups lie anyway |
| 8 | csl-guides `corpus-attestation.mdx` quotes 4,550,704 tokens / 59,282 lemmas ("corpus totals") — archive-vintage — while the master is 5,688,416 / 98,606 | [manual:320](https://github.com/gasyoun/VisualDCS/blob/main/docs/DCS_SQLITE_CONCLU_CONSUMER_DEEP_MANUAL.md) | §4.3 rule | **in the wild downstream** — a §4.3 violation surface; Cologne-side fix routes to W7 (H8063) |

### Parallel/alignment-layer forks

| # | Fork | State |
|---|---|---|
| 9 | kosha registry `rows: 506,787` vs measured 501,231 source segments | ✅ reconciled in-report (raw lines incl. blanks) |
| 10 | "GOOD = verified full match" label vs the report's own risk row ("machine-derived, not human gold — treat GOOD as weak gold") | ✅ honest caveat shipped; the *word* GOOD still over-promises to a skimming consumer |
| 11 | SA↔RU accuracy goal ≥0.9 vs measured 0.03–0.13 (24-config sweep; positional prior "does not cure") | ✅ honest negative, stop 8/8; repair path = bilingual content lexicon (not onomasticon) or pad-level reframe with 100-verse human gold |

## Open questions

**Research `[R]`:**
- `[R]`-1 **BhaGī 1.1 discriminant** (fork 3): run `SELECT form, m_unsandhied FROM token … JOIN chapter … WHERE chapter.ref LIKE 'BhaGī 1%'` and byte-search `dharma-kṣetre`/`dharmakṣetre`/`kuru-kṣetre` in the SAIS `T.bin` — does DCS's Gītā open at 1.1, and in which orthography? (Needs the 920 MB master or the 287 MB Release — not on this host; query is paste-ready for the next VisualDCS lane.)
- `[R]`-2 **Cpd denominator pairing** (fork 2): one query — `SELECT upos, COUNT(*) FROM token WHERE feat_case='Cpd' GROUP BY upos` — closes the 841,052 vs 724,676 pairing; then G2/G19 should cross-link.
- `[R]`-3 **Whitney 930/935·713/755 pairing** (fork 4): one sentence in the WhitneyRoots README (or the manual) naming the key spaces would retire it.
- `[R]`-4 **Human gold for GOOD parallels** (theme 7): the H4707 spot-check wave (3 rows hand-verified so far) is the weak-gold upgrade path; sample design exists (frozen 200-row set).

**In-task `[T]`:**
- `[T]`-1 **Re-vintage `dcs_lemma_summary.json` to DCS-2026** (fork 1) — the canonical consumer asset is the last 2021-vintage surface; A38/A40 denominators depend on it. Owner: VisualDCS lane (`gen_dcs_lemma_summary.py` re-point + `validate_dcs_lemma_summary.py` re-pin). **Route as a new @DO, not silently.**
- `[T]`-2 **SA↔RU aligner repair** (fork 11): bilingual content lexicon (mw_ru / L4 glossary) + hunalign scheme, or reframe pad↔sentence within verse groups + 100-verse human gold.
- `[T]`-3 **LSC human gold n=30** — annotation sheet shipped empty (`lsc_human_gold_sample.tsv`); MG annotates personally (already a GTD row upstream, not duplicated here).
- `[T]`-4 **TANS 193-texts genre/date dataset** — the landing page's one planned widget; no dataset exists, so genre/date claims over those 193 texts are impossible today ([roadmap.md](https://github.com/gasyoun/VisualDCS/blob/main/roadmap.md) residual).
- `[T]`-5 **csl-guides archive-vintage totals** (fork 8) — label or rebase at the W7 Cologne pass (H8063 scope).

## Retractions / corrections ledger (cluster-internal)

- A38 §4.4 mis-sum 741,782 → **781,618** and §6 "too sparse" → **17.25%** bucket (H1486; both retracted in-repo, `README:71-77` supersedes).
- "Gītā absent from DCS — MBh 6 omits adhyāyas 23–40" (kosha `datasets.json` premise) → **corrected**: ref-relabeling, Gītā present, 10,547 tokens (manual G1, H1407 adversarial pass). *Caution: fork 3 now tests the opening verse of that presence claim.*
- LSC gap claim "0 Sanskrit in the 81-paper LSC family" → **superseded 10-08-2026** (family is 236 papers, one Sanskrit entry: Hariharan & Mortensen 2026, morphology-level) — claim narrowed, not dropped ([derived-lsc:1-9](https://github.com/gasyoun/VisualDCS/blob/main/derived-lsc/README.md)).
- "no `SCONJ` in the UD inventory" (format-comparison sample) → sample-scoped; corpus-wide 31,499 (G17).
- "2021 dump superseded by 2026" assumption → **NOT superseded** (H686): 2021-only texts/lemmas kept.
- H5137 concordance-index estimate 105 MB → **487 MB measured** (4.9× over; SA+LCP dominate) — estimate discipline correction in [SAIS](https://github.com/gasyoun/VisualDCS/blob/main/docs/SAIS_CONCORDANCE_DCS_2026-09.md).

## Code spot-checks (equal source, 13-11-2026)

| # | Check | Result |
|---|---|---|
| 1 | `python -m pytest tests/` (PSC) | ✅ **5/5 PASS** (0.25 s) — aligner harness green at HEAD |
| 2 | `data/dcs-parallels-baseline/baseline_summary.json` ↔ H4707 headline table | ✅ byte-exact parity: 245 files · 501,231 segments · 154,033 matches · GOOD 14,557 / PARTLY 139,476 · malformed 0 · recall 1.00/0.985 |
| 3 | `python tools/build_baseline.py --check` (frozen-sample recall) | ⚠️ **BLOCKED on this host** — the 59 MB source (`VisualDCS/…/PARA/Polnorazmernye/`) is local-only on the archive machine; the builder follows the sibling-checkout convention. Evidence limitation, not a defect; re-run on a machine with the sibling checkout |
| 4 | `build_baseline.py` code ↔ report semantics (`pair_hash`, GOOD/PARTLY counters, seed 4707, malformed counter) | ✅ consistent — deterministic builder matches the report's method row |
| 5 | Arithmetic re-derivations (by hand from cited figures): nominal closure 2,263,192+724,676+8,542 = **2,996,410** ✓ · past-split 12,054+4,046+77,229 = **93,329** ✓ · Pareto (233,079+157,003)/781,616 = **49.91%** ✓ · GOOD share 14,557/154,033 = **9.45%** ✓ | ✅ all four close |
| 6 | SAIS corpus counts vs manual row counts (independent instrument) | ✅ exact match on 5,688,416 / 754,726 / 270 |

No cite drift found on sampled load-bearing rows. Deeper falsification (re-running joins against the 920 MB master) is out of the W6 budget — the discriminant queries are named above instead.

## Residuals (→ GTD same pass)

1. `[R]`-1/`[R]`-2 discriminant queries require the DCS master on-host — one @DO row ("VisualDCS: run BhaGī-opening + Cpd-by-upos discriminants, paste results into forks 2–3").
2. `[T]`-1 re-vintage of `dcs_lemma_summary.json` — one @DO row (A38/A40 dependency).
3. `[T]`-2..`[T]`-5 are already-live upstream tracks (SA↔RU repair, LSC gold = MG, TANS dataset, W7 csl-guides label) — referenced, **not duplicated**.
4. `build_baseline.py --check` re-run on an archive machine with the VisualDCS sibling checkout — folded into the residual-1 @DO row.

_Dr. Mārcis Gasūns_
