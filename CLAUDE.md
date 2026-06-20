# CLAUDE.md — The Writing Pipeline (Session Orientation)

> **Read this first.** You are a fresh Claude Code session with no memory of prior work.
> This file orients you. After reading it, read the governing documents in `docs/` before
> doing anything. Do not start building. Nothing in the design is authorized or built yet.

## 1. What this repo is

The build home for **The Writing Pipeline** — a complete system for taking Kenneth
Granberry's writing from research to publication (essays, books, and other publications)
reliably. It unifies a **front half** (research → architecture → draft) and a **back half**
(audit → revise → version) over one source of truth, operated here in Claude Code.

The finding behind the whole project: the design of Kenneth's existing writing systems is
sound, but roughly a third of their instructions are deterministic work — counting,
exhaustive search, verification, versioning — assigned to a chat model that cannot do it
reliably. **The pipeline moves that mechanical substrate to deterministic tools and keeps
every act of judgment and authorization with the author.**

## 2. Read these first (in `docs/`)

- **`TheWritingPipeline_SystemBlueprint_v0_2`** — the system design. *A draft for markup;
  nothing in it is authorized or built yet.*
- **`TheWritingPipeline_DecisionQuestionnaire`** — the open decisions; the P0 items finalize
  the blueprint to v0.3.
- **`TMM_WritingSystem_ReformMemo_v0_1`** — the audit-half diagnosis and reforms, absorbed
  into the blueprint.
- **Source systems:** `TMM_Writing_System_v1_7`, `EB_WritingMachine_OperationalReference_v1_13`.
- **Source materials:** `The_Wise_Life_Compendium`; and, if working them, the
  `What the Mirror Does Not See` manuscript + session-close.

If any are missing, ask Kenneth to add them. Do not proceed from memory or summary.

## 3. The operating model

- Work in Claude Code over this repo. Conversation for thinking, judgment, and drafting;
  deterministic tooling for counting, search, verification, register generation, versioning.
- **Authorization spine (absolute):** propose → Kenneth authorizes → implement one item at a
  time. Tools detect and verify; they never implement. Appreciation is not authorization.
- **No memory between sessions.** The repo is the memory. Keep this file and the registers
  current so the next session opens oriented.
- **Confidentiality:** manuscripts and compendia are unpublished and confidential. Never
  send manuscript content to any external service. (See the confidentiality option in §6.)

## 4. The settled design (refine via the blueprint; do not relitigate)

- **Five-stage lifecycle, per unit:** Compendium → **Architecture (Brief + structure)** →
  Draft → Audit → Version.
- **The Brief lives inside the Architecture**, as its specification section. Work-level
  constraints (voice palette, governing creative principle, status-tag legend, protected
  strings) are inherited from a work-level layer, not restated per unit.
- **A layered engine:** Engine (shared tools) · Work Profile (per book/series) ·
  Publication-Type Profile (essay, chapter, book, short-form, prompt sequence).
- **Cross-cutting registers, generated not hand-maintained:** claim/source index, governing
  vocabulary, phrase frequency, reserved/held, say/withhold, structural & tonal maps.
- **Reliability boundary:** spec-adherence, tag-fidelity, coverage, traceability, and
  verification become reliable; the prose itself stays variable — author and model judgment.

## 5. What to do first, in order (do NOT skip to building)

1. Greet Kenneth and confirm you have read the governing docs. Surface anything missing.
2. Confirm the **confidentiality option** (see §6): Option 1 = manuscripts live in this
   private repo; Option 2 = manuscripts stay local, `works/` git-ignored.
3. With authorization, **scaffold the repo** in one commit: `docs/`, `pipeline/`,
   `registers/`, `works/` (plus the `.gitignore` the chosen option requires).
4. Work the **P0 questionnaire items** to finalize the Blueprint to **v0.3**.
5. Then **Phase 0 — paper, no code:** the Measurement Standard (the paragraph definition),
   the Mechanical/Hybrid/Judgment tagging, the Motto decision, the Architecture template.
6. Only after Phase 0 is settled, begin Phase 1 tooling. Nothing is built before its
   governing decision is authorized.

## 6. Open decisions (current state)

**Decided:**
- Operating model = Claude Code over this repo.
- Scope = the complete drafting + auditing pipeline, for essays, books, and other publications.
- The Brief sits inside the Architecture.

**Proposed, awaiting Kenneth's ruling (the P0 set):**
- System name: *The Writing Pipeline.*
- Publication types: essay · chapter · full book · newsletter/short-form · prompt sequence · other.
- Pilot: *The Wise Life*, essay form.
- Paragraph / measurement definition: to be supplied, or proposed from how *Mirror* and
  *The Wise Life* are structured.
- **Motto gloss — unresolved:** the website says *Humanity*; the manuscripts and systems say
  *Civilization* (in *Mirror*, 24 to 2). One decision, then protect the chosen string.
- ***The Wise Life* "open gate" — unresolved:** the volume of testimony (names the center
  fully / reaches it by negative image / never names it). It gates first writing and that
  book's Voice Palette.
- Tag-fidelity rules: how each status tag may be rendered — `[TEXT]` attributed,
  `[CONTESTED]` hedged, `[SYNTH]` owned as connective claim, `[HYP]` never asserted as
  established.
- The Mechanical / Hybrid / Judgment cut (Reform Memo Appendix B).
- Division of labor (judgment in conversation; deterministic operations as tools).

**Confidentiality option (1 or 2): unresolved — ask before scaffolding.**

## 7. How to work with the author (from his own writing system)

- He uses you as a **mental exercise machine**: give honest pushback, not agreement. The most
  useful turns are the ones that hold a line.
- Voice: literary, grave, precise. **No filler** — do not use "genuinely," "honestly," or
  "straightforward" as empty intensifiers. No sermons, no AI-disclaimers, and do not tell him
  to rest or assume it is late; he rises before dawn.
- Answer substantively. Do not narrate your own process. Do not relitigate settled decisions.
- Authorization above all: never alter a settled artifact without explicit approval; flag any
  override for the record rather than evaluating it.

## 8. Hard rules

- Tools never implement. The author authorizes. Implement one item at a time, confirming after
  each.
- Protect permanent strings once set (the Motto once decided; any passage marked final).
- Manuscripts and compendia are confidential — keep them out of public repos and never send
  them to any external service.
- No memory persists between sessions. Update this file and the registers at session close so
  the next session opens current.

---

*Save this file as `CLAUDE.md` at the repository root — Claude Code reads it automatically at
session open — or upload it at the start of each session. It is orientation, not a governing
document; it authorizes nothing.*
