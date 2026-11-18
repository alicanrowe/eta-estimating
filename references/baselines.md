# Measured baselines

Every number here comes from a real run in a one-person furniture and jewelry studio: thread start and finish times, render logs and farm jobs from 17 to 18 November 2026. Times are wall clock, from the moment work starts to the moment a checked result is reported, unless the row says otherwise. Rebuild the table with `python3 scripts/eta.py rebuild` after adding rows to `data/observations.csv`.

## Table (auto-generated)

<!-- AUTO:START -->
| What | n | Typical (p50) | Range (p10 to p90) | Seen |
|---|---|---|---|---|
| `animation_small` | 1 | 42 min | 42 min to 42 min | 42 min to 42 min (few samples) |
| `cad_design_feature` | 1 | 76 min | 76 min to 76 min | 76 min to 76 min (few samples) |
| `callouts_19_of_21` | 1 | 29 min | 29 min to 29 min | 29 min to 29 min (few samples) |
| `cloud_cpu_test_still` | 1 | 2.0 min | 2.0 min to 2.0 min | 2.0 min to 2.0 min (few samples) |
| `code_freeze_break` | 1 | 3.0 min | 3.0 min to 3.0 min | 3.0 min to 3.0 min (few samples) |
| `encode_81s_4k` | 1 | 37 min | 37 min to 37 min | 37 min to 37 min (few samples) |
| `encode_final_chunk` | 1 | 7.0 min | 7.0 min to 7.0 min | 7.0 min to 7.0 min (few samples) |
| `farm_cost_usd_per_2160f_low` | 5 | $69 | $64 to $70 | $63 to $70 |
| `farm_download_2160f_h` | 1 | 4.2 h | 4.2 h to 4.2 h | 4.2 h to 4.2 h (few samples) |
| `farm_job_end_to_end_h` | 1 | 6.1 h | 6.1 h to 6.1 h | 6.1 h to 6.1 h (few samples) |
| `farm_pack_copy_checksum` | 1 | 6.0 min | 6.0 min to 6.0 min | 6.0 min to 6.0 min (few samples) |
| `farm_render_1728f_overnight_upper_h` | 1 | 8.0 h | 8.0 h to 8.0 h | 8.0 h to 8.0 h (few samples) |
| `farm_render_2160f_low_h` | 4 | 2.0 h | 1.7 h to 2.0 h | 1.6 h to 2.0 h |
| `farm_upload_renderbeamer` | 2 | 5.8 min | 5.2 min to 6.3 min | 5.0 min to 6.5 min (few samples) |
| `graphics_small` | 2 | 13 min | 11 min to 15 min | 11 min to 15 min (few samples) |
| `human_gate_active` | 4 | 1.1 min | 0.5 min to 1.8 min | 0.3 min to 2.0 min |
| `human_gate_daytime_away` | 4 | 47 min | 33 min to 69 min | 31 min to 75 min |
| `human_gate_overnight` | 2 | 14.9 h | 14.2 h to 15.6 h | 14.1 h to 15.8 h (few samples) |
| `jewelry_cuff_cold` | 4 | 26 min | 20 min to 28 min | 18 min to 29 min |
| `jewelry_piece_cold` | 27 | 8.8 min | 7.1 min to 15 min | 4.1 min to 16 min |
| `jewelry_piece_restart_after_stall` | 3 | 3.5 min | 2.3 min to 4.7 min | 2.0 min to 5.0 min (few samples) |
| `jewelry_piece_warm_rerender` | 6 | 3.1 min | 1.8 min to 5.5 min | 1.5 min to 6.8 min |
| `jewelry_render_4views_sec` | 44 | 27 s | 21 s to 34 s | 16 s to 43 s |
| `mac_setup_walkthrough` | 1 | 4.0 min | 4.0 min to 4.0 min | 4.0 min to 4.0 min (few samples) |
| `platform_concurrency_stall` | 1 | 1.5 h | 1.5 h to 1.5 h | 1.5 h to 1.5 h (few samples) |
| `render_check_round` | 7 | 8.0 min | 6.6 min to 25 min | 4.5 min to 38 min |
| `research_sourcing` | 4 | 29 min | 19 min to 43 min | 18 min to 46 min |
| `sawhorse_variant` | 8 | 36 min | 28 min to 62 min | 22 min to 80 min |
| `site_deploy_wait` | 1 | 3.3 min | 3.3 min to 3.3 min | 3.3 min to 3.3 min (few samples) |
| `skill_save_or_small_skill` | 2 | 16 min | 9.6 min to 22 min | 8.0 min to 24 min (few samples) |
| `storage_cleanup` | 2 | 18 min | 9.2 min to 27 min | 7.0 min to 29 min (few samples) |
| `web_feature_build` | 1 | 27 min | 27 min to 27 min | 27 min to 27 min (few samples) |
<!-- AUTO:END -->

## What the numbers mean

### Jewelry pieces, one per cloud machine (Blender make.py, 4-view square)
- **Cold start, small piece** (studs, clips, ears, rings, necklaces, earrings): typically 8 to 9 minutes from thread start to checked report, 6 to 16 minutes in practice. That is machine setup and code checksum check (about 4 minutes), make.py geometry (1 to 3 minutes), the 4-view Cycles render (16 to 36 seconds, it is never the bottleneck) and the reference check and write-up (1 to 3 minutes).
- **Cuffs** (5 to 6 million triangles): 18 to 29 minutes cold. Plan them as a separate, slower class.
- **Warm re-render** on a machine that is already set up: 1.5 to 7 minutes.
- **The render itself** (4 views, Cycles): 16 to 43 seconds. Triangle count and glass add a little. Do not estimate from render time; setup and checking dominate.
- **A batch finishes when its slowest piece finishes**, and when per-piece checks find a shared-code problem, add a central fix round (about 10 to 20 minutes) plus a full re-render wave.

### Sawhorse variants (model, render-check loop, sheet), one per machine
- 21 to 55 minutes for seven of eight variants, typically about 31 to 40 minutes. The heaviest (carved all over) took about 80 minutes. Count about 8 minutes per render-check round and 3 to 6 rounds.

### Render-check rounds on a look (materials, grain, lighting)
- A round that changes a few settings and renders 3 to 5 test frames plus a sheet: 8 to 16 minutes.
- A round that rebuilds a whole material system (dozens of materials): 30 to 40 minutes.

### Animation on GarageFarm (via renderBeamer)
- Pack, copy to the user's computer, checksum: about 6 minutes. Upload through renderBeamer: 5 to 7 minutes per file (needs the user's computer unlocked and the screen free).
- Render, LOW priority, 2160 frames at 2160 x 3840, Cycles 256 samples: about 1.5 to 2 hours, about $63 to $70 per cut. A 1,728-frame cut finished overnight. A heavier two-cut job (2,808 frames) was quoted at about $284.
- **Download is the trap.** About 8 MB per 16-bit PNG frame at about 2.3 MB/s means roughly 2 hours of pure transfer for 2160 frames, and it took about 4 hours in practice because the last frames trail behind. An earlier ETA of "50 minutes" for this step was 5 times too short.
- Callouts on about 20 labels: about 30 minutes. Encoding a 90-second 4K reel with callouts: about 45 minutes in chunks.
- **End to end**, from "go" to a delivered video: about 6 hours for one cut, including one human wait.

### Cloud machines without a GPU
- A preview test frame takes about 2 minutes on a 4-core cloud machine. A full-quality animation frame is estimated at 40 to 60 minutes (not measured yet), which is why animations go to the farm.

### Site and tooling work
- A web feature built, pushed and live (for example the WebGL fractal engine with 6 presets): about 27 minutes, of which the deploy wait is about 3 minutes.
- Saving or packaging a small skill: 8 to 24 minutes. Research and sourcing (hinges, wood scans, a production plan, a site style scan): 18 to 46 minutes. Small graphics or a teaser: 11 to 15 minutes. A short explainer animation: about 42 minutes. A new CAD add-on design: about 76 minutes.

### Human gates (the biggest source of error)
- **the user active in the app:** decision cards, sign-ins and OKs come back in 20 seconds to 2 minutes. A connector sign-in by link took 2 minutes.
- **Daytime, the user away:** 30 to 75 minutes (unlock the user's computer, free the screen, connect a folder; 55 minutes for computer folder access on 18 Nov).
- **Evening into the next morning:** 14 to 16 hours. An OK asked for after about 4 PM ET usually comes back after 8 AM ET.
- Any step that needs the user's screen, a sign-in, a payment OK, or a folder grant is a gate. Put the gate first in the plan when possible, and never put a gate in the middle of the critical path without saying so.

### Platform limits
- Starting threads is sequential at about 3 seconds each, so 90 machines take about 5 minutes just to start.
- **Concurrency stalls (top risk):** on 18 Nov about 43 jewelry render threads started but did nothing for about 90 minutes because the session limit was full. Restarted, each finished in 2 to 5 minutes. Detect them about 3 minutes after starting a batch: a working thread whose last activity equals its start time, or with no checklist, is stalled (`eta.py stallcheck`).
- A shared-code edit without a version bump blocks every render thread until the code is re-frozen (about 3 minutes each time).
- When too many threads run at once, new ones fail to start ("too many threads and sessions are running"). This happened with about 90 threads started within 30 minutes; several threads started then never ran. Plan fan-out in waves of about 40 and say so.

## How past ETAs did
See `data/predictions.csv` and run `python3 scripts/eta.py calibration`. As of 18 Nov 2026: the encode and farm-render ETAs were close (0.7x and 0.8x), the download ETA was 5x too short, and two serial ETAs were overtaken when the work was split across machines.
