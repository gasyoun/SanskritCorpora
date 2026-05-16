# SanskritCorpora

SanskritCorpora is a metalevel repository for source-bound Sanskrit corpus work, with an initial focus on word-by-word translations.

The purpose of this repository is to keep corpus materials, alignment logic, annotation rules, and scholarly context conceptually separate. A corpus entry should make it clear which layer is being shown: source text, segmentation, transliteration, word gloss, translation, commentary, or workflow metadata.

## Document layers

This `README.md` is the public-facing metadocument. It describes what the project is for and how its materials should be understood.

Operational instructions for people or agents working inside the repository should live in separate working documents, such as `AGENTS.md`, `CLAUDE.md`, `docs/workflow.md`, schemas, validation scripts, or import notes. Those files can be stricter, more procedural, and more tool-specific than this overview.

## Corpus principles

- Keep source text and interpretation distinct.
- Preserve alignment between words, phrases, translations, and notes.
- Prefer explicit metadata over implicit convention.
- Treat uncertainty as data: mark conjectures, alternate readings, and unresolved segmentation.
- Make generated artifacts reproducible from source files whenever possible.

## Intended shape

Future repository structure can separate stable corpus data from tools and working protocol:

- `data/` for corpus sources, aligned passages, and reusable metadata.
- `schemas/` for machine-checkable artifact contracts.
- `scripts/` or `tools/` for import, validation, export, and reporting.
- `docs/` for methodological notes, source policies, and workflow documents.
- `examples/` for small, reviewable sample passages.

The first obligation of the project is clarity: a reader should be able to tell what is source, what is analysis, and what is an operational aid.
