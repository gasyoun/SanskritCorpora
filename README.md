# SanskritCorpora

SanskritCorpora is a metalevel repository for Gasuns' repos. It is a place for files that describe, frame, coordinate, and explain repository-level work rather than the day-to-day implementation details of a single project.

The repository can include public-facing metadocuments, cross-repo notes, project identity texts, workflow summaries, and conceptual maps. For Sanskrit corpus work, it may also hold notes about source-bound word-by-word translation, alignment, annotation rules, and scholarly context.

## Document layers

This `README.md` is itself a public-facing metadocument. It describes the role of the repository at the level above individual codebases.

Operational instructions for people or agents working inside a particular repository should live in separate working documents, such as `AGENTS.md`, `CLAUDE.md`, `docs/workflow.md`, schemas, validation scripts, or import notes. Those files can be stricter, more procedural, and more tool-specific than this overview.

## Metalevel principles

- Separate project identity from implementation protocol.
- Distinguish public-facing descriptions from agent-facing working rules.
- Prefer explicit metadata over implicit convention.
- Preserve the difference between source material, analysis, commentary, generated artifacts, and workflow notes.
- Make cross-repo assumptions visible instead of leaving them only in chat history.

## Intended shape

Future repository structure can separate metalevel documents from repo-specific working material:

- `docs/` for project overviews, repo maps, methodological notes, and source policies.
- `repos/` for notes tied to individual Gasuns repositories.
- `schemas/` for shared machine-checkable artifact contracts, if needed.
- `scripts/` or `tools/` for validation, export, and reporting helpers, if needed.
- `examples/` for small, reviewable samples.

The first obligation of the project is clarity: a reader should be able to tell what is a metadocument, what is a working instruction, what is source material, and what is generated or operational support.
