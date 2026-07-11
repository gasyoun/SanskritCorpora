# SanskritCorpora

_Created: 14-06-2026 · Last updated: 11-07-2026_

SanskritCorpora is a metalevel repository under the [`gasyoun`](https://github.com/gasyoun) account. Its GitHub description is "Word by word translations": the repository is intended to hold source-bound, word-by-word translation material — plus the notes that describe, frame, coordinate, and explain such corpus work — rather than the day-to-day implementation details of a single project.

> Status (11-07-2026): early stub. The repository currently contains only this `README.md` and CI plumbing (see [Current contents](#current-contents) below). The sections after it describe the intended purpose and shape, not material that already exists here.

## Current contents

Everything tracked in the repository today:

- [`README.md`](https://github.com/gasyoun/SanskritCorpora/blob/main/README.md) — this metadocument.
- [`.github/dependabot.yml`](https://github.com/gasyoun/SanskritCorpora/blob/main/.github/dependabot.yml) — Dependabot config for GitHub Actions dependency bumps.
- [`.github/workflows/dependabot-auto-merge.yml`](https://github.com/gasyoun/SanskritCorpora/blob/main/.github/workflows/dependabot-auto-merge.yml) — hands-off auto-merge of green Dependabot PRs.

There is no corpus data, source code, build, or test suite in the repository yet.

## Intended purpose

The repository can hold public-facing metadocuments, cross-repo notes, project identity texts, workflow summaries, and conceptual maps. For Sanskrit corpus work specifically, it is meant to carry notes about source-bound word-by-word translation, text–translation alignment, annotation rules, and scholarly context — the framing layer above the individual corpus and dictionary repositories.

This `README.md` is itself such a public-facing metadocument: it describes the role of the repository at the level above individual codebases. Operational, tool-specific instructions for people or agents working inside a particular repository belong in separate working documents (for example `AGENTS.md`, `CLAUDE.md`, `docs/workflow.md`, schemas, or validation scripts). Those files can be stricter, more procedural, and more tool-specific than this overview.

## Metalevel principles

- Separate project identity from implementation protocol.
- Distinguish public-facing descriptions from agent-facing working rules.
- Prefer explicit metadata over implicit convention.
- Preserve the difference between source material, analysis, commentary, generated artifacts, and workflow notes.
- Make cross-repo assumptions visible instead of leaving them only in chat history.

## Intended shape (not yet present)

As material accumulates, the repository can separate metalevel documents from repo-specific working material. None of these directories exist yet; they are a target layout:

- `docs/` — project overviews, repo maps, methodological notes, and source policies.
- `repos/` — notes tied to individual `gasyoun` repositories.
- `schemas/` — shared machine-checkable artifact contracts, if needed.
- `scripts/` or `tools/` — validation, export, and reporting helpers, if needed.
- `examples/` — small, reviewable samples.

The first obligation of the project is clarity: a reader should be able to tell what is a metadocument, what is a working instruction, what is source material, and what is generated or operational support.

## Related repositories

Word-by-word and aligned Sanskrit corpus work across the wider ecosystem lives in dedicated repositories, including [`Parallel-Sanskrit-Corpora`](https://github.com/gasyoun/Parallel-Sanskrit-Corpora), [`spoken-sanskrit-corpus`](https://github.com/gasyoun/spoken-sanskrit-corpus), and [`telegram-sanskrit-corpus`](https://github.com/gasyoun/telegram-sanskrit-corpus). This repository is the metalevel companion to that work, not a replacement for it.

_Dr. Mārcis Gasūns_
