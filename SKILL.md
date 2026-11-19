---
name: eta-estimating
description: Use whenever you give a time estimate or ETA (renders, render-check loops, fan-out across machines, farm animations, CAD, site work, sign-ins and other waits on the user): estimate from measured baselines, answer with a range in the user's time zone, log it, and update the baselines when the work finishes.
metadata:
  author: Alican Rowe (@alicanrowe)
---

# ETA estimating

Give ETAs from measured durations, not from feel. Every ETA is a range with clock times, names what could push it late, and gets checked against what actually happened so the next one is better.

## Where the data is
- Live copy, shared by every thread of the project: a shared project folder (for example `<project-files>/eta-estimating/`) (use this when it exists, and write new data here).
- Otherwise the copy bundled with this skill: `data/observations.csv` (measured durations), `data/predictions.csv` (past ETAs and how they did), `references/baselines.md` (the table plus what each row means).
- `scripts/eta.py` does the maths. It needs only Python 3.

- If neither is on hand (for example the skill was saved without its files), get them from the GitHub repo `alicanrowe/eta-estimating`, or fall back to the quick baselines below.

Read `references/baselines.md` before the first ETA in a conversation. Paths to `scripts/` and `data/` below are relative to whichever copy you use.

## Quick baselines (18 Nov 2026; the table in the data copy is newer if it differs)
| Step | Typical | Range seen |
|---|---|---|
| Jewelry piece, own cloud machine, cold start to checked report | 9 min | 4 to 16 min |
| Heavy jewelry piece (5 to 6 million triangles, e.g. cuffs) | 26 min | 18 to 29 min |
| Re-render on a machine already set up | 3 min | 1.5 to 7 min |
| The 4-view Cycles render inside that | 27 s | 16 to 43 s |
| Furniture variant: model, render-check loop, sheet | 36 min | 21 to 80 min |
| One render-check round (few settings, 3 to 5 test frames) | 8 min | 4.5 to 16 min |
| Render-check round that rebuilds a material system | 38 min | 30 to 40 min |
| Preview still on a 4-core cloud machine, no GPU | 2 min | |
| Farm: pack and copy / renderBeamer upload per file | 6 min / 6 min | 5 to 7 min |
| Farm render, 2160 frames 4K, Cycles 256, LOW priority | 2 h, about $69 | 1.6 to 2 h, $63 to $70 |
| Farm frame download, 2160 x 8 MB at about 2.3 MB/s | 2 to 4 h | 4.2 h seen |
| Callouts on about 20 labels / encode a 90 s 4K reel | 30 min / 45 min | |
| Farm job end to end, "go" to delivered video | 6 h | |
| Web feature built and live (deploy about 3 min) | 27 min | |
| Research or sourcing | 29 min | 18 to 46 min |
| Small skill save / small graphic or teaser | 16 min / 13 min | 8 to 24 / 11 to 15 min |
| User answers while active / daytime away / asked after 4 PM | 1 min / 47 min / next morning | 0.3 to 2 min / 31 to 75 min / 14 to 16 h |
| Fan-out thread stalled by the concurrency limit (until restarted) | 90 min | |
| Shared code changed without a version bump (render threads blocked) | 3 min | |
| Sawhorse r8 re-render, design kept (8 images 1000 px, 32 spp, 4-core cloud, mesh 0.09 + checks) | 15 min per full pass; 50 min thread incl. pip setup 3 min, 3 passes | 18 Nov |
| v2 stand render, one piece per machine (3 views 1400 px, 128 spp Cycles CPU, 4-core cloud, ~22k faces) | 3.3 min render (re-render after a central fix: 3.0 min render, 4 min end to end); ~13 min thread incl. pip bpy 1 min, checks and overlap test | 18 Nov |
| Moth v3 stand render, round 2 high-poly (~196k faces, 3 views 1400 px, 128 spp, 4-core cloud) | 6.2 min render (fix1 rerun 5.8 min, fix4 184k faces 4.1 min) + fabcheck under 1 min; ~9 min end to end (job sheet guessed up to 25) | 18 Nov |
| Moth tool render, one piece per machine (serpent fork; 3 views 1400 px, 128 spp, 4-core cloud): v2 ~10k faces / v3 ~46k faces | v2 63 s render; v3 91 to 97 s render + fabcheck under 1 min; ~3 to 4 min thread end to end, pip bpy already cached (job sheet guessed 4 to 12 min) | 18 Nov |
| c1 cuff, 4 seasons on one machine (c1-v1, 6.1M tris, VOXO 0.05, 4 views 720 px 24 spp, 4-core cloud) | 3.0 to 3.2 min per season, 12 min for all 4; ~15 min thread incl. pip bpy setup ~1 min | 18 Nov |
| c1 square, 4 seasons of one design on one machine (TO 2400, VOXO 0.045, 4-core cloud) | 1.2 min per piece, 4.9 min for all 4; ~13 min thread incl. pip setup 6.3 min | 18 Nov |
| c1 bug_clip, 4 seasons on one machine (c1-v1, TO 2400, VOXO 0.045, 4-core cloud) | 1.5 min per piece, 6.0 min for all 4; pip setup 1.5 min; ~16 min thread | 18 Nov |
| c1 vein_clip, 4 seasons on one machine (c1-v1, TO 2400, VOXO 0.045, 4-core cloud) | 1.7 min per piece, 6.7 min for all 4; pip setup ~2 min; ~18 min thread | 18 Nov |
| Farm download of two 2160-frame jobs (39 GB) at about 1.2 MB/s | 9 h | |
| renderBeamer cold start (plugin download) / restart to first frames | 9 min / 10 min | |
| Gotcha: renderBeamer auto-download can be off; then nothing downloads. Check it first | | 1 h lost 18 Nov |
| Gotcha: if the Renders SSD is unplugged mid-download, renderBeamer keeps failing (I/O error) until restarted; restart to first frames 35 s, then about 2.5 MB/s | | |

## Making an ETA
1. **Split the job into steps** and mark each one:
   - *agent work* (modelling, coding, writing, checking),
   - *machine time* (a render, a farm job, an upload or download, a deploy),
   - *gate* (anything that waits on the user: an OK, a sign-in, unlocking a computer, freeing the screen, connecting a folder, paying).
2. **Look up each step**: `python3 scripts/eta.py stats <category>`. Use p50 for the early end and p90 for the late end.
   - Fewer than 4 samples: use the observed min times 0.8 to the max times 1.5, and say the data is thin.
   - No matching category: take the nearest one, widen it by half, and say there's no direct data.
3. **Add the loop rounds.** A new look or design takes 3 to 6 render-check rounds; a settled pipeline takes 1 or 2. When per-piece checks feed fixes back into shared code, add one central-fix round (10 to 20 min) and a full re-render wave.
4. **Concurrency stalls are the top ETA risk for fan-out.** On 18 Nov about 43 render threads started but sat idle for about 90 minutes because too many sessions were running; once restarted each finished in 2 to 5 minutes. Until every piece is confirmed running, the late end of any fan-out ETA is "+90 min".
   - **Detect:** about 3 minutes after starting a batch, list the threads (`list_threads`, state working). A thread whose `last_activity_at` still equals its `created_at`, or that has posted no checklist, or that shows a "too many threads and sessions" error, is stalled. `python3 scripts/eta.py stallcheck threads.json` flags them from a saved listing.
   - **Prevent:** start in waves of about 40, start the next wave only as the last one finishes, and keep heavy pieces in the first wave.
   - **Recover:** restart stalled threads as others finish; a restarted piece is a warm job (2 to 5 min). Re-issue the ETA once, saying how many stalled.
5. **Fan-out across machines**: `python3 scripts/eta.py fanout --n <pieces> --cat <category> --cap 40`. A batch ends when its slowest piece ends. Starting threads takes about 3 s each, and above roughly 40 running at once new threads may fail to start, so plan in waves. Put heavy pieces (for example cuffs) in their own class.
6. **Transfers**: `python3 scripts/eta.py transfer --frames <n> --mb <MB per frame> --rate <MB/s>`, then plan up to twice that. Downloads of farm frames were the worst-estimated step so far (5x over).
7. **Gates, by the user's clock**:
   - User active right now: 1 to 2 minutes.
   - Daytime, user away: 30 to 75 minutes.
   - Asked after about 4 PM in the user's time zone: the answer usually comes after 8 AM the next day.
   Ask for every gate you can see up front, at the start, so they don't land mid-job.
8. **Add it up**: serial steps add; parallel branches take the longest one. Keep the early end (all p50, no surprises) and the late end (p90s plus the gates) separate. Don't add p90s of many small steps blindly: for 5 or more independent steps, late end = sum of p50 + the largest single (p90 minus p50) + gates.

## Saying it
- Give a range in the user's time zone (for this project, New York time): "between 12:40 and 1:15 PM ET".
- In one sentence, name what sets the late end ("the cuffs are the slow ones", "the download from the farm", "it needs your OK on the price").
- If a gate is on the path, lead with it: what you need from the user and by when, and what the ETA becomes if it comes later.
- Never a single point, never "soon", never "a few minutes" without a clock time.
- If work is already running, base the rest on its measured progress (frames done per minute, pieces done so far), not the plan.

## Keeping it honest
1. **Log every ETA you give**: `python3 scripts/eta.py predict "<what>" --p50 <min> --p90 <min> --source "<thread>"`.
2. **When a step passes its late end**, re-estimate from what has actually happened and tell the user the new range once. Don't post every small slip.
2a. **When newer work pushes an accepted job back, its ETA has changed.** Tell the user in one line what is waiting, why, and the new range, in the same turn you park it. Keep it on your checklist marked paused, and resume it as soon as the urgent work ends. Log it with the request-handoffs skill's `ledger.py park` if the project keeps a request ledger. A job with no update for two hours counts as parked.
3. **When the work finishes**:
   - `python3 scripts/eta.py resolve <id> <actual minutes>`
   - add each measured step: `python3 scripts/eta.py add <category> <value> --source "<thread>" --note "<what was different>"` (minutes; categories ending `_h` are hours, `_sec` seconds, `_usd` dollars). Make a new category when nothing fits, named `<area>_<what>` in lower case.
   - `python3 scripts/eta.py rebuild`, and add a line to `references/baselines.md` if you learned something a number can't say (a new trap, a new limit).
4. Check `python3 scripts/eta.py calibration` now and then. If the median actual/p50 drifts above 1.2, the baselines are optimistic: widen future ranges and note why.
5. Measure from real timestamps (thread start and finish, log lines, file times, farm job pages), never from memory.

## Traps already seen
- Estimating a render job from the render time: the render was 20 to 40 s, the job was 8 to 16 min. Setup and checking dominate.
- Estimating farm download as a quick step: 2160 frames of 16-bit PNG is about 17 GB, 2 to 4 hours at about 2.3 MB/s.
- ETAs given for serial work on one machine go stale the moment the work is split across machines. Re-issue the ETA when the plan changes.
- A step that needs the user's screen or computer (unlocked Mac, Blender UI, a connected folder or drive) is a gate even when it looks like machine work. A session on the user's computer stops when it sleeps (18 Nov: a renderBeamer start sat for 70 minutes); ask them to keep it awake, and never plan renders there: renders run on cloud machines or a farm.
- Farm downloads can be switched off in the downloader's settings; then nothing arrives and nothing errors. Check that frames are landing a few minutes after starting, and estimate from the measured rate (1.2 MB/s seen, so 39 GB took about 9 hours).
- A job widened past what the user asked (a redesign when they asked for matching pictures) blows the ETA and gets thrown away. Estimate the scope the user's words give (request-handoffs `brief`), not the plan.
- Fan-out above the platform's concurrency limit doesn't fail loudly: threads start and then never run. Check that every piece actually started.
- A design round parked silently behind urgent shop-floor questions: it sat at "not started" for two hours with no ETA, and when the user asked where it was, the thread said it had never been asked. Parking is an ETA change; say it out loud (step 2a).
