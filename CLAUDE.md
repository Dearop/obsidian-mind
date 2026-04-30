# Obsidian Mind

Personal Obsidian vault -- an external brain for work notes, decisions, performance tracking, and Claude context.

## Skills & Capabilities

This vault has [obsidian-skills](https://github.com/kepano/obsidian-skills) installed in `.claude/skills/`. Follow these skill conventions:

> Note: `reference/` (singular) is the vault's content folder for codebase knowledge and architecture docs. `references/` (plural) in the items below refers to skill-local support files inside `.claude/skills/.../references/`.

- **obsidian-markdown**: Obsidian-flavored markdown -- wikilinks, embeds, callouts, properties. See the skill-local `references/` files in `.claude/skills/obsidian-markdown/` for callout types, embed syntax, and property specs. Always prefer `[[wikilinks]]` over markdown links.
- **obsidian-cli**: CLI commands for vault operations when Obsidian is running. See CLI section below.
- **json-canvas**: Create `.canvas` files with nodes, edges, and visual layouts. See the skill-local `references/EXAMPLES.md` in `.claude/skills/json-canvas/`.
- **obsidian-bases**: Create `.base` files with views, filters, and formulas. Bases core plugin is enabled. See the skill-local `references/FUNCTIONS_REFERENCE.md` in `.claude/skills/obsidian-bases/`.
- **defuddle**: Extract clean markdown from web pages via `defuddle parse <url> --md`.
- **qmd**: Semantic search across the vault via [QMD](https://github.com/tobi/qmd). Use PROACTIVELY before reading files -- `qmd query "..."` for hybrid search, `qmd search "..."` for keyword, `qmd vsearch "..."` for semantic. Falls back to grep/glob if QMD not installed.

### Custom Slash Commands

Defined in `.claude/commands/`. See [[Skills]] for full documentation.

| Command | Purpose |
|---------|---------|
| `/om-standup` | Morning kickoff -- load context, review yesterday, surface tasks, priorities |
| `/om-dump` | Freeform capture -- dump anything, gets routed to the right notes |
| `/om-wrap-up` | Full session review -- verify notes, indexes, links, suggest improvements |
| `/om-humanize` | Voice-calibrated editing -- make notes sound like you, not AI |
| `/om-weekly` | Weekly synthesis -- cross-session patterns, North Star alignment, uncaptured wins |
| `/om-capture-1on1` | Capture 1:1 meeting transcript into structured vault note |
| `/om-incident-capture` | Capture incident from Slack channels/DMs into structured vault notes |
| `/om-slack-scan` | Deep scan Slack channels/DMs for evidence |
| `/om-peer-scan` | Deep scan a peer's GitHub PRs for review prep |
| `/om-review-brief` | Generate review brief (manager or peer version) |
| `/om-self-review` | Write self-assessment for review tool -- projects, competencies, principles |
| `/om-review-peer` | Write peer review -- projects, principles, performance summary |
| `/om-vault-audit` | Audit indexes, links, orphans, stale context |
| `/om-vault-upgrade` | Import content from an existing vault into this obsidian-mind instance |
| `/om-prep-1on1` | Prep for an upcoming 1:1 -- load person context, open items, suggested agenda |
| `/om-meeting` | Prep for any meeting by topic -- subject-forward briefing with open items and considerations |
| `/om-intake` | Process meeting notes inbox -- classify and route to the right vault notes |
| `/om-project-archive` | Move completed project from active/ to archive/, update indexes |

## Vault Structure

| Folder | Purpose | Key Files |
|--------|---------|-----------|
| `Home.md` | **Vault entry point** -- embedded Base views, quick links | Open this first |
| `vault-manifest.json` | **Template metadata** -- version, infrastructure vs user content boundaries, frontmatter schemas, version fingerprints | Used by `/om-vault-upgrade` for migration |
| `CHANGELOG.md` | **Version history** -- tracks template releases (v1--v3.3) with what changed | Reference for upgrade paths |
| `bases/` | **All Bases centralized** -- dynamic views for navigation | `Work Dashboard`, `Incidents`, `People Directory`, `1-1 History`, `Review Evidence`, `Competency Map`, `Research Wiki`, `Templates` |
| `work/` | Work notes index | `Index.md` (detailed MOC) |
| `work/active/` | **Current projects only** (1-3 files) | Move here when starting, move to archive when done |
| `work/archive/YYYY/` | Completed work organized by year | Grows over time |
| `work/incidents/` | Incident docs (main note + RCA + deep dive + drafts) | Per-incident grouping |
| `work/1-1/` | 1:1 meeting notes (accumulate weekly) | Named `<Person> YYYY-MM-DD.md` |
| `work/meetings/` | **Meeting notes inbox** -- staging area for raw exports, processed by `/om-intake` | Drop files, run `/om-intake` |
| `perf/` | Performance framework, brag doc | `Brag Doc.md` (index) |
| `perf/brag/` | Quarterly brag notes | One per quarter, e.g. `Q1 2025.md` |
| `perf/competencies/` | Atomic competency notes (link targets) | One note per competency |
| `perf/evidence/` | PR deep scans, data extracts for reviews | Named `<Person> PRs - <Period>.md` |
| `perf/<cycle>/` | Review cycle briefs + artifacts | Review briefs (private, manager, peer) |
| `brain/` | Claude's operational knowledge | `Memories.md`, `Key Decisions.md`, `Patterns.md`, `Gotchas.md`, `Skills.md`, `North Star.md` |
| `org/` | Organizational knowledge index | `People & Context.md` (MOC) |
| `org/people/` | Atomic person notes | One note per person |
| `org/teams/` | Team notes as graph nodes | One note per team |
| `research/` | **LLM-maintained research wiki** -- sources, concepts, entities, syntheses, open questions | `Index.md` (catalog), `Log.md` (activity), `Overview.md` |
| `research/sources/` | One page per processed paper/article/book | Source summaries with metadata |
| `research/concepts/` | Topics, methods, frameworks, theories | Concept definitions with math background |
| `research/entities/` | Proof systems, tools, projects (non-person entities) | Named entity pages |
| `research/syntheses/` | Literature reviews, comparisons, reading maps | Higher-level analysis |
| `research/open_questions/` | Unresolved questions, research gaps | Follow-up prompts |
| `raw/` | **Immutable source material** -- papers, articles, books, assets | Do not edit; read and cite only |
| `reference/` | Codebase knowledge, architecture maps | Flow docs, architecture docs |
| `thinking/` | Scratchpad for drafts and reasoning | Named `YYYY-MM-DD-topic.md` |
| `templates/` | Obsidian templates | `Work Note.md`, `Decision Record.md`, `Research Source.md`, `Research Concept.md`, `Research Entity.md`, `Research Synthesis.md`, `Research Open Question.md`, etc. |
| `.claude/commands/` | 18 slash commands | See command table above |
| `.claude/agents/` | 9 subagents | See subagents table below |
| `.claude/scripts/` | Hook scripts | `session-start.sh`, `classify-message.py`, `validate-write.py`, `pre-compact.sh` |
| `.claude/skills/` | Obsidian + QMD skills | Loaded automatically via Skill tool |

## Obsidian CLI

When Obsidian is running, prefer CLI over raw filesystem. It provides vault-aware search, backlink discovery, and property management. Fall back to filesystem when Obsidian is not running.

```bash
obsidian read file="Note Name"                    # Read a note
obsidian create name="Name" content="..." silent   # Create without opening
obsidian append file="Name" content="..."          # Append to note
obsidian search query="text" limit=10              # Vault-aware search
obsidian backlinks file="Name"                     # Discover connections
obsidian tags sort=count counts                    # List all tags
obsidian tasks daily todo                          # Open tasks
obsidian daily:read                                # Today's daily note
obsidian property:set name="status" value="done" file="Name"
obsidian orphans                                   # Unlinked notes
```

`file=` resolves like a wikilink (by name). `path=` for exact path from root. Use `silent` to prevent files from opening. Run `obsidian help` for full reference.

## Session Workflow

### Starting a Substantial Session

The `SessionStart` hook automatically injects rich context: vault file listing, North Star goals, active work, recent git changes, open tasks, and triggers a QMD re-index. Most context is already loaded -- you don't need to manually read files.

**Shortcut**: Run `/om-standup` for a structured morning kickoff that reads everything and presents a summary with suggested priorities.

If doing it manually:

1. Read `Home.md` -- vault entry point with embedded dashboards
2. Read `brain/North Star.md` -- ground suggestions in current goals
3. Check `work/Index.md` -- see active projects and recent notes
4. Scan `brain/Memories.md` -- index of memory topics, then read relevant topic notes
5. `obsidian tasks daily todo` -- see pending items

### Ending a Substantial Session

**When the user says "wrap up", "let's wrap", "wrapping up", or similar -- invoke `/om-wrap-up` automatically.** This runs a full review of the session.

If `/om-wrap-up` is not invoked, at minimum do these before wrapping up:

1. **Archive completed projects**: `git mv` from `work/active/` to `work/archive/YYYY/`, update `status: completed` (or use `/om-project-archive`)
2. Update `work/Index.md` if new notes or decisions were created
3. Update the relevant brain topic note (`brain/Key Decisions.md`, `brain/Patterns.md`, `brain/Gotchas.md`) with key learnings
4. Update `org/People & Context.md` if org knowledge changed
5. Update `perf/Brag Doc.md` if wins or impact were achieved
6. Offer to update `brain/North Star.md` if goals shifted or new focus emerged
7. Verify all new notes link to at least one existing note (orphans are bugs)
8. If work demonstrates competencies, add competency links to the work note's `## Related`
9. Run `/om-vault-audit` if the session created many notes

Skip steps that don't apply. The goal is transferring durable knowledge from conversation to vault state.

### Thinking Workflow

Use `thinking/` for drafts, reasoning, and analysis before writing final notes. **Thinking notes are scratchpads, not storage.** They exist to help you reason -- once the reasoning produces durable knowledge, promote it to proper notes and delete the scratchpad.

1. Create a thinking note: `thinking/YYYY-MM-DD-descriptive-name.md`
2. Use the Thinking Note template
3. Reason through the problem, analyze options, draft content
4. Promote findings to atomic notes in the correct folder (not one monolith -- one note per distinct concept)
5. Delete the thinking note -- it served its purpose
6. If the thinking process itself is worth preserving (unusual), keep it but link to the promoted notes

### Creating Notes

1. **Always use YAML frontmatter** with at minimum `date`, `description` (~150 chars), `tags`, and type-specific fields. Work notes and incidents also need `quarter` (e.g., `Q1-2026`). Incidents need `ticket`, `severity`, `role`.
2. **Use templates** from `templates/`. Fill `{{placeholders}}` with real values.
3. **Place files correctly**:
   - **Active** work notes, decisions, peer review prep -- `work/active/`
   - **Completed** work notes -- `work/archive/YYYY/` (by year)
   - Incident docs -- `work/incidents/`
   - 1:1 meeting notes -- `work/1-1/`
   - Performance content -- `perf/` (cycle subfolder for review briefs)
   - PR evidence -- `perf/evidence/`
   - Competency definitions -- `perf/competencies/`
   - People -- `org/people/`
   - Teams -- `org/teams/`
   - Claude operational context -- `brain/`
   - Codebase knowledge -- `reference/`
   - Drafts -- `thinking/`
   - Vault root: `Home.md`, `CLAUDE.md`, `AGENTS.md`, `GEMINI.md`, `vault-manifest.json`, `CHANGELOG.md`, `CONTRIBUTING.md`, `README.md`, `LICENSE`, `.gitignore`. No user notes at root.
4. **Name files descriptively.** Use the note title as filename.

### Note Types

| Type | Location | Naming | Key Sections |
|------|----------|--------|--------------|
| Work note | `work/active/` (then `archive/YYYY/` when done) | Descriptive title | Context, What/Why, Links, Related |
| Incident | `work/incidents/` | Ticket number or descriptive title | Context, Root Cause, Timeline, Impact, Analysis, Related |
| 1:1 note | `work/1-1/` | `<Person> YYYY-MM-DD.md` | Key Takeaways, Action Items, Quotes, What to Watch, Related |
| PR analysis | `perf/evidence/` | `<Person> PRs - <Period>.md` | PR Count, Projects, Quality, Growth, Full Table |
| Review brief | `perf/<cycle>/` | `<Cycle> Review Brief.md` | Arc, Impact, Competencies, Documentation Trail |
| Person note | `org/people/` | Full name | Role & Team, Relationship, Key Moments, Notes |
| Team note | `org/teams/` | Team name | Members, Scope, Interactions |
| Competency | `perf/competencies/` | Competency name | Definition, level criteria, Evidence (via backlinks) |
| Brain note | `brain/` | Topic name | Topic-specific content |
| Research source | `research/sources/` | Paper/article title | Summary, Key Claims, Methods, Connections, Open Questions |
| Research concept | `research/concepts/` | Concept name | Definition, Why It Matters, Math Background, Evidence, Related |
| Research entity | `research/entities/` (systems) or `org/people/` (researchers) | Entity name | Who/What, Relevance, Associated Sources, Related |
| Research synthesis | `research/syntheses/` | Comparison/map title | Thesis, Takeaways, Comparison, Evidence, Tensions |
| Research question | `research/open_questions/` | Question title | Question, Current Evidence, Missing Evidence, Follow-ups |

### Linking -- This Is Critical

**Graph-first, not folder-first.** Folders help browse in the sidebar. Links help discover through connections. Both matter, but links are the primary organizational tool.

**A note without links is a bug.** When creating a note, the FIRST thing to do after writing content is add wikilinks. Every new note must link to at least one existing note.

**Atomicity rule**: Before writing or appending to any note, ask: "Does this cover multiple distinct concepts that could be separate nodes?" If a note has or would have 3+ independent sections that don't need each other to make sense, split into atomic notes that link to each other.

Note types have graph roles:
- **Evidence nodes** (work notes, 1:1s, PR analyses): add outbound links to concepts they demonstrate
- **Concept nodes** (competencies, patterns): stay definitional -- evidence arrives via backlinks
- **Index nodes** (Index, Brag Doc, Memories, People & Context): actively curate links -- they're navigational
- **Person nodes** (org/people/): link to projects, teams, evidence. Receive backlinks from work notes.

Link syntax:
- `[[Note Title]]` -- standard wikilink
- `[[Note Title|display text]]` -- aliased link
- `[[Note Title#Heading]]` -- deep link to section
- `![[Note Title]]` -- embed content inline
- `[[Note Title#^block-id]]` -- link to specific block

#### When to Link

- **Work note <-> Decision**: bidirectional links
- **Work note -> Competency**: in `## Related`, link to competencies demonstrated
- **Work note -> Team**: in `## Related`, link to team(s) involved
- **Work note -> Person**: link people involved (especially in 1:1 notes)
- **Person -> PR analysis**: link to their evidence file if one exists
- **Brag Doc -> Work note**: every entry links to evidence
- **Memories -> Source**: every memory links to where it was learned
- **Index -> Everything**: `work/Index.md` links to all work notes
- **North Star -> Projects**: active focus areas link to project work notes

### Maintaining Indexes

Update these when creating or archiving notes:

- **`work/Index.md`** -- add to Active Projects or Recent Notes, move completed to Archive
- **`brain/Memories.md`** -- index of memory topics. Add new memories to the relevant topic note, not here.
- **`brain/Skills.md`** -- register vault-specific workflows and slash commands
- **`org/People & Context.md`** -- update when people, teams, or org structure changes
- **`perf/Brag Doc.md`** -- log wins with links to evidence, add new quarters as needed
- **`research/Index.md`** -- catalog of research wiki pages, organized by type (sources, concepts, entities, syntheses, open questions)
- **`research/Log.md`** -- append-only chronological log of research wiki activity (ingests, queries, lint passes)

### Decision Records

1. Create in `work/` using the Decision Record template
2. Link from the work note(s) that led to the decision
3. Add to the Decisions Log table in `work/Index.md`
4. If significant, note in `brain/Key Decisions.md`

### Wins & Achievements

When significant work is completed, add to `perf/Brag Doc.md` with links to the work note(s). Categorize under Impact, Technical Growth, Collaboration, or Feedback.

## North Star

`brain/North Star.md` is a living document of goals and focus areas.

- **Read it** at the start of substantial sessions
- **Reference it** when suggesting priorities or trade-offs
- **Update it** when the user signals a shift in goals
- Both the user and Claude write to it

## Tags Convention

Use tags in frontmatter (not inline):

- **Type**: `work-note`, `decision`, `perf`, `thinking`, `north-star`, `competency`, `person`, `team`, `brain`
- **Index**: `index`, `moc`
- **Status** (frontmatter field): `active`, `completed`, `archived`, `proposed`, `accepted`, `deprecated`
- **Team** (frontmatter field on people + work notes): your team names, e.g. `Backend`, `Platform`, `Mobile`
- **Cycle** (frontmatter field on review-related notes): `h2-2024`, `h1-2025`, etc.
- **Person** (frontmatter field on evidence notes): full name of the person
- **Project**: as needed, e.g. `project/auth-refactor`

## Properties for Querying

Beyond tags, use these frontmatter properties to enable search and Bases views:

- `cycle: h2-2024` -- find all review material for a cycle
- `person: "Jane Smith"` -- find all evidence related to a person
- `team: Backend` -- find all notes related to a team
- `status: active` -- find active projects
- `quarter: Q1-2026` -- find all work for a quarter (used by Work Dashboard Base)
- `ticket: TICKET-123` -- find incident by ticket number
- `severity: high` -- incident severity
- `role: incident-lead` -- your role in an incident

## Memory System

**All project memories live in the vault.** The `~/.claude/` MEMORY.md is an auto-loaded index that points to vault locations. The `~/.claude/` MEMORY.md is the only file that should exist there -- it is an auto-loaded index. Never create additional memory files in that directory.

| System | Location | Purpose |
|--------|----------|---------|
| **MEMORY.md** | `~/.claude/projects/.../memory/MEMORY.md` | Auto-loaded index only. Pointers to vault notes. |
| **Vault memories** | `brain/` topic notes | Git-tracked, Obsidian-browsable, linked. All durable knowledge lives here. |

When asked to "remember" something:
1. Find or create the appropriate `brain/` topic note (Gotchas, Patterns, Key Decisions, etc.)
2. Add the knowledge there with a wikilink to context
3. Update `brain/Memories.md` index if a new topic note was created
4. Do NOT create additional files in `~/.claude/projects/.../memory/` beyond MEMORY.md -- they are not version-controlled

## Agent Guidelines

### Graph-First Thinking

- **Folders group by purpose, links group by meaning.** A note lives in ONE folder (its home) but links to MANY notes (its context).
- When creating a note, add wikilinks FIRST. A note without links is a bug.
- Prefer bidirectional links: if A links to B, B should link back to A (unless B is a concept node that receives backlinks passively).
- Before creating a new subfolder, ask: "Can I solve this with a tag, a property, or a link instead?" Folders are for browsing convenience, not for categorization.
- After every substantial session, verify new notes have at least one inbound link.

### Where to Put Things

- **Writing about a person?** -- `org/people/`
- **Writing about a team?** -- `org/teams/`
- **Writing about how the codebase works?** -- `brain/` (Patterns, Gotchas, Key Decisions)
- **Writing about what Claude should remember?** -- `brain/Memories.md` topic notes
- **Capturing a 1:1 meeting?** -- `work/1-1/`
- **Deep scanning PRs for review?** -- `perf/evidence/`
- **Creating review briefs?** -- `perf/<cycle>/`
- **Tracking active project work?** -- `work/active/`
- **Capturing an incident?** -- `work/incidents/` (use `/om-incident-capture`)
- **Dumping unstructured info?** -- use `/om-dump` to auto-classify and route everything
- **Ingesting a research paper/article?** -- `research/sources/`, update `research/Index.md` and `research/Log.md`
- **Writing about a research concept/method?** -- `research/concepts/`
- **Writing about a researcher?** -- `org/people/` (with `type: person` and researcher tags)
- **Writing about a proof system/tool/lab?** -- `research/entities/`
- **Comparing or synthesizing research?** -- `research/syntheses/`
- **Noting a research gap or open question?** -- `research/open_questions/`
- **Dropping raw source material?** -- `raw/` (immutable -- never edit files here)

### Don't Mix Contexts

When capturing data from Slack, DMs, or meetings:
- **Project evidence** (PRs, technical decisions, delivery) -- goes to the relevant `work/` note
- **Review prep** (peer selection, manager strategy, brag framing) -- goes to review-related notes in `perf/` or `work/`
- **People dynamics** (feedback, relationships, career) -- goes to `org/people/` notes
- **Personal conversations** -- only capture if review-relevant; otherwise skip

## Subagents

Specialized agents in `.claude/agents/` for heavy operations. They run in isolated context windows.

| Agent | Purpose | Invoked by |
|-------|---------|------------|
| `brag-spotter` | Finds uncaptured wins and competency gaps | `/om-wrap-up`, `/om-weekly` |
| `context-loader` | Loads all vault context about a person, project, or concept | Direct |
| `cross-linker` | Finds missing wikilinks, orphans, broken backlinks | `/om-vault-audit` |
| `people-profiler` | Bulk creates/updates person notes from Slack profiles | `/om-incident-capture` |
| `review-prep` | Aggregates all performance evidence for a review period | `/om-review-brief` |
| `slack-archaeologist` | Full Slack reconstruction -- every message, thread, profile | `/om-incident-capture` |
| `vault-librarian` | Deep vault maintenance -- orphans, broken links, stale notes | `/om-vault-audit` |
| `review-fact-checker` | Verifies every claim in a review draft against vault sources | `/om-self-review`, `/om-review-peer` |
| `vault-migrator` | Classifies, transforms, and migrates content from a source vault | `/om-vault-upgrade` |

## Hooks

Five lifecycle hooks in `.claude/settings.json`:

| Hook | When | What |
|------|------|------|
| SessionStart | On startup/resume | QMD re-index, inject North Star, active work, recent changes, tasks, file listing |
| UserPromptSubmit | Every message | Classifies content (decision, incident, win, 1:1, architecture, person, project update) and injects routing hints |
| PostToolUse | After writing `.md` | Validates frontmatter, checks for wikilinks |
| PreCompact | Before context compaction | Backs up session transcript to `thinking/session-logs/` |
| Stop | End of every session | Lightweight checklist reminder: archive, update indexes, check orphans. For thorough review, use `/om-wrap-up` instead. |

## Research Wiki

The `research/` section is an LLM-maintained research wiki for interests, study plans, and research papers. The `raw/` directory holds immutable source material.

### Research operating principles

1. **Do not edit raw sources.** Files in `raw/` are source-of-truth inputs. Read, summarize, and cite them -- never rewrite or rename.
2. **The wiki is the working knowledge base.** Pages in `research/` reflect current synthesized understanding. When new evidence arrives, update existing pages instead of creating isolated summaries.
3. **Knowledge should compound.** Good answers, comparisons, and research notes should be filed back into `research/syntheses/`. Prefer maintaining strong canonical pages over many redundant ones.
4. **Be explicit about uncertainty.** Distinguish facts, interpretations, hypotheses, and open questions. Record disagreements instead of flattening them.
5. **Keep the research index and log current.** `research/Index.md` is the catalog, `research/Log.md` is the chronological record. Any meaningful ingest or synthesis should update both.

### Research ingest workflow

1. Locate the source in `raw/`.
2. Read the source, extract metadata (title, authors, year, source kind).
3. Create or update the page in `research/sources/`.
   - **For papers**: full formal breakdown — state definitions, theorems, and key equations in LaTeX. Cite section/page numbers. Include complexity/performance bounds. Be rigorous, not hand-wavy.
   - **For lighter sources** (articles, talks, podcasts): summary-focused, less formal.
4. Update affected pages in `research/concepts/`, `research/entities/`, `research/syntheses/`, `research/open_questions/`.
5. Add wikilinks between the new source and related pages.
6. Check `research/Contradictions.md` — if the source disagrees with existing wiki content, add an entry.
7. Update `research/Index.md` and append to `research/Log.md`.
8. **Suggest next papers** — after each ingest, recommend what to read next and flag missing sources.
9. **Ingest one source at a time** with user review. No batch processing.

### Research lint workflow (every 10 sources)

1. Check for orphan pages, broken links, duplicate/near-duplicate content.
2. Review and resolve `research/Contradictions.md` — move resolved entries to the Resolved section.
3. Identify concepts repeatedly mentioned but lacking their own page.
4. Check for stale summaries superseded by newer sources.
5. Verify index coverage and backlink health.
6. Suggest missing sources and next papers based on gaps in the wiki.
7. Append a lint summary to `research/Log.md`.

### Research frontmatter

Research pages use these additional properties beyond the standard `date`, `description`, `tags`:

- Source pages: `type: source`, `status`, `source_kind`, `raw_path`, `authors`, `year`, `related`
- Concept pages: `type: concept`, `related`
- Entity pages: `type: entity`, `entity_kind`, `related`
- Synthesis pages: `type: synthesis`, `status`, `related`
- Open question pages: `type: open_question`, `related`

## Rules

- Never modify `.obsidian/` config files unless explicitly asked.
- Preserve existing frontmatter when editing notes.
- Git sync is handled by the user's preferred method (obsidian-git, manual commits, etc.) -- don't configure git hooks or auto-commit.
- When asked to "remember" something, write to the relevant `brain/` topic note with a link to context. Never create memory files in `~/.claude/` -- they are not git-tracked.
- Prefer Obsidian CLI over filesystem when Obsidian is running.
- **Always invoke Obsidian skills via the Skill tool** before doing vault work. Load `obsidian-markdown` when creating/editing `.md` files. Load `obsidian-cli` when running vault commands. Load `obsidian-bases` or `json-canvas` when working with those file types.
- Always check for and suggest connections between notes.
- Every note must have a `description` field (~150 chars). Claude fills this automatically.
- **Zero data loss**: when reorganizing, always use `git mv`. Never delete without explicit user confirmation.
