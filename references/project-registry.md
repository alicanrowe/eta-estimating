# Project registry: format and rules

A project with many threads forgets things: a thread stalls one step before delivery, and a week later nobody can say where the work is. The registry is one Markdown file, shared by every thread, that lists every project and deliverable. Keep it next to the live data copy as `PROJECTS.md`. It names private projects, so it is never published with the skill.

## Columns
| Project | Look / how the user might describe it | Folder | Thread | Status | Next / waiting on |
|---|---|---|---|---|---|
| Example reel | 90 s vertical reel; white grass, red water, black sky | `example-reel/` | Make example reel `<thread id>` | done: final in Drive `Backups/2026-11-19 Example reel/` | update the site page |

- **Look** is the column that saves you: write the colours, setting, materials and piece names the user would use to describe it.
- **Status**: `active`, `waiting on <user>`, `stalled`, `review` (delivered, waiting for the verdict), `done`, `parked` (the user said not now). Say where the final output is once it exists.
- Group rows by area (videos, jewelry, furniture, wearables, tools, admin). One row per thing the user would ask about by name; fan-out render threads go under their parent, not as rows.

## Rules
1. Before answering "where is X" or "ETA for X", search the registry by name and by look, then open the row's thread and folder.
2. When a thread starts work on a project or deliverable, add or update its row in the same turn.
3. When it finishes, parks or blocks, update status and next step in the same turn.
4. A row marked `active` with no thread activity for 2 hours is stalled: resume it or tell the user.
5. Re-read the file just before editing, change only your rows, and re-read it about 10 seconds after saving (shared folders can lag).
6. The coordinator seeds the registry from the folders and the full thread list (paged, not just recent threads), and checks it when a request comes in.
