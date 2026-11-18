# Measured baselines

Every number here comes from a real run in a one-person furniture and jewelry studio: thread start and finish times, render logs and farm jobs from 17 to 18 November 2026. Times are wall clock, from the moment work starts to the moment a checked result is reported, unless the row says otherwise. Rebuild the table with `python3 scripts/eta.py rebuild` after adding rows to `data/observations.csv`.

## Table (auto-generated)

<!-- AUTO:START -->
| What | n | Typical (p50) | Range (p10 to p90) | Seen |
|---|---|---|---|---|
| `animation_frames_48_chunk` | 3 | 28 min | 19 min to 32 min | 17 min to 33 min (few samples) |
| `animation_small` | 1 | 42 min | 42 min to 42 min | 42 min to 42 min (few samples) |
| `blender_download_cloud` | 1 | 0.6 min | 0.6 min to 0.6 min | 0.6 min to 0.6 min (few samples) |
| `cad_design_feature` | 1 | 76 min | 76 min to 76 min | 76 min to 76 min (few samples) |
| `callouts_19_of_21` | 1 | 29 min | 29 min to 29 min | 29 min to 29 min (few samples) |
| `cloud_bpy_setup` | 2 | 1.8 min | 1.1 min to 2.4 min | 1.0 min to 2.5 min (few samples) |
| `cloud_cpu_test_still` | 1 | 2.0 min | 2.0 min to 2.0 min | 2.0 min to 2.0 min (few samples) |
| `code_freeze_break` | 1 | 3.0 min | 3.0 min to 3.0 min | 3.0 min to 3.0 min (few samples) |
| `cycles_frame_576x720_32s_4cpu` | 1 | 0.3 min | 0.3 min to 0.3 min | 0.3 min to 0.3 min (few samples) |
| `dancers_listing_wait` | 1 | 56 min | 56 min to 56 min | 56 min to 56 min (few samples) |
| `dancers_machine_overhaul` | 12 | 76 min | 53 min to 1.5 h | 42 min to 1.5 h |
| `dancers_tile_48frame_range_cold` | 3 | 27 min | 19 min to 31 min | 16 min to 32 min (few samples) |
| `drive_backup_via_mac_per_gb` | 1 | 14 min | 14 min to 14 min | 14 min to 14 min (few samples) |
| `encode_81s_4k` | 1 | 37 min | 37 min to 37 min | 37 min to 37 min (few samples) |
| `encode_final_chunk` | 1 | 7.0 min | 7.0 min to 7.0 min | 7.0 min to 7.0 min (few samples) |
| `env_bpy_venv_install` | 3 | 1.1 min | 0.7 min to 1.8 min | 0.6 min to 2.0 min (few samples) |
| `farm_cost_usd_per_2160f_low` | 7 | $69 | $64 to $71 | $63 to $72 |
| `farm_download_2160f_h` | 1 | 4.2 h | 4.2 h to 4.2 h | 4.2 h to 4.2 h (few samples) |
| `farm_download_start_gate` | 1 | 2.2 h | 2.2 h to 2.2 h | 2.2 h to 2.2 h (few samples) |
| `farm_job_end_to_end_h` | 1 | 6.1 h | 6.1 h to 6.1 h | 6.1 h to 6.1 h (few samples) |
| `farm_pack_copy_checksum` | 1 | 6.0 min | 6.0 min to 6.0 min | 6.0 min to 6.0 min (few samples) |
| `farm_render_1728f_overnight_upper_h` | 1 | 8.0 h | 8.0 h to 8.0 h | 8.0 h to 8.0 h (few samples) |
| `farm_render_2160f_low_h` | 4 | 2.0 h | 1.7 h to 2.0 h | 1.6 h to 2.0 h |
| `farm_upload_renderbeamer` | 2 | 5.8 min | 5.2 min to 6.3 min | 5.0 min to 6.5 min (few samples) |
| `graphics_small` | 2 | 13 min | 11 min to 15 min | 11 min to 15 min (few samples) |
| `human_gate_active` | 4 | 1.1 min | 0.5 min to 1.8 min | 0.3 min to 2.0 min |
| `human_gate_daytime_away` | 4 | 47 min | 33 min to 69 min | 31 min to 75 min |
| `human_gate_overnight` | 2 | 14.9 h | 14.2 h to 15.6 h | 14.1 h to 15.8 h (few samples) |
| `jewelry_batch_finish` | 1 | 19 min | 19 min to 19 min | 19 min to 19 min (few samples) |
| `jewelry_c1_piece_render_only` | 5 | 0.9 min | 0.9 min to 0.9 min | 0.8 min to 1.0 min |
| `jewelry_c1_square_4seasons` | 1 | 3.8 min | 3.8 min to 3.8 min | 3.8 min to 3.8 min (few samples) |
| `jewelry_cuff_cold` | 5 | 25 min | 10 min to 28 min | 5.0 min to 29 min |
| `jewelry_piece_cold` | 56 | 7.2 min | 4.2 min to 12 min | 0.9 min to 16 min |
| `jewelry_piece_restart_after_stall` | 3 | 3.5 min | 2.3 min to 4.7 min | 2.0 min to 5.0 min (few samples) |
| `jewelry_piece_warm_rerender` | 18 | 3.8 min | 0.9 min to 5.7 min | 0.8 min to 11 min |
| `jewelry_render_4views_sec` | 49 | 27 s | 21 s to 35 s | 16 s to 43 s |
| `jewelry_sheet_end_to_end` | 1 | 3.2 h | 3.2 h to 3.2 h | 3.2 h to 3.2 h (few samples) |
| `mac_setup_walkthrough` | 1 | 4.0 min | 4.0 min to 4.0 min | 4.0 min to 4.0 min (few samples) |
| `moth_tool_v3_piece_warm` | 1 | 2.5 min | 2.5 min to 2.5 min | 2.5 min to 2.5 min (few samples) |
| `pip_bpy_build123d_setup` | 1 | 2.5 min | 2.5 min to 2.5 min | 2.5 min to 2.5 min (few samples) |
| `platform_concurrency_stall` | 1 | 1.5 h | 1.5 h to 1.5 h | 1.5 h to 1.5 h (few samples) |
| `platform_concurrency_stall_seen_count` | 1 | 4.0 min | 4.0 min to 4.0 min | 4.0 min to 4.0 min (few samples) |
| `render_8view_cycles_1000px_48spp` | 2 | 13 min | 10 min to 16 min | 9.3 min to 17 min (few samples) |
| `render_check_round` | 7 | 8.0 min | 6.6 min to 25 min | 4.5 min to 38 min |
| `render_machine_3views_1300px_64spp` | 1 | 5.0 min | 5.0 min to 5.0 min | 5.0 min to 5.0 min (few samples) |
| `render_machine_3views_1300px_96spp` | 3 | 10 min | 8.4 min to 10 min | 8.0 min to 10 min (few samples) |
| `render_sawhorse_view_1000px_48spp` | 3 | 1.1 min | 1.1 min to 1.2 min | 1.1 min to 1.2 min (few samples) |
| `render_sawhorse_view_1100px_64spp` | 2 | 1.8 min | 1.6 min to 1.9 min | 1.6 min to 1.9 min (few samples) |
| `render_shopbot_3view_1300px_96spp` | 1 | 10 min | 10 min to 10 min | 10 min to 10 min (few samples) |
| `renderbeamer_restart_to_frames` | 1 | 10 min | 10 min to 10 min | 10 min to 10 min (few samples) |
| `renderbeamer_startup` | 1 | 9.0 min | 9.0 min to 9.0 min | 9.0 min to 9.0 min (few samples) |
| `research_sourcing` | 4 | 29 min | 19 min to 43 min | 18 min to 46 min |
| `sawhorse_fix_round` | 10 | 28 min | 22 min to 45 min | 19 min to 46 min |
| `sawhorse_variant` | 8 | 36 min | 28 min to 62 min | 22 min to 80 min |
| `scene_render_4core_1000px` | 1 | 0.9 min | 0.9 min to 0.9 min | 0.9 min to 0.9 min (few samples) |
| `sdf_carved_piece_build` | 1 | 0.6 min | 0.6 min to 0.6 min | 0.6 min to 0.6 min (few samples) |
| `setup_pip_bpy_build123d` | 1 | 16 min | 16 min to 16 min | 16 min to 16 min (few samples) |
| `shared_parts_batch` | 2 | 56 min | 51 min to 61 min | 50 min to 62 min (few samples) |
| `shop_bot_final_render_1300_96` | 1 | 12 min | 12 min to 12 min | 12 min to 12 min (few samples) |
| `shop_machine_check` | 1 | 1.3 min | 1.3 min to 1.3 min | 1.3 min to 1.3 min (few samples) |
| `shop_machine_overhaul_thread` | 1 | 75 min | 75 min to 75 min | 75 min to 75 min (few samples) |
| `shop_machine_preview_render` | 1 | 9.0 min | 9.0 min to 9.0 min | 9.0 min to 9.0 min (few samples) |
| `shopbot_check_machine` | 3 | 0.6 min | 0.4 min to 4.9 min | 0.3 min to 6.0 min (few samples) |
| `shopbot_dims_projection` | 1 | 18 min | 18 min to 18 min | 18 min to 18 min (few samples) |
| `shopbot_machine_rebuild` | 2 | 50 min | 47 min to 52 min | 46 min to 53 min (few samples) |
| `shopbot_overhaul` | 1 | 55 min | 55 min to 55 min | 55 min to 55 min (few samples) |
| `shopbot_render_draft` | 2 | 2.9 min | 1.9 min to 3.9 min | 1.6 min to 4.1 min (few samples) |
| `shopbot_render_final` | 7 | 10 min | 9.6 min to 11 min | 8.9 min to 11 min |
| `shopbot_render_full` | 1 | 8.5 min | 8.5 min to 8.5 min | 8.5 min to 8.5 min (few samples) |
| `site_3d_tiles` | 1 | 18 min | 18 min to 18 min | 18 min to 18 min (few samples) |
| `site_deploy_wait` | 1 | 3.3 min | 3.3 min to 3.3 min | 3.3 min to 3.3 min (few samples) |
| `skill_save_or_small_skill` | 3 | 24 min | 11 min to 89 min | 8.0 min to 1.8 h (few samples) |
| `storage_cleanup` | 2 | 18 min | 9.2 min to 27 min | 7.0 min to 29 min (few samples) |
| `thread_feet_pass_total` | 1 | 45 min | 45 min to 45 min | 45 min to 45 min (few samples) |
| `thread_redesign_iteration_lowres` | 1 | 2.3 min | 2.3 min to 2.3 min | 2.3 min to 2.3 min (few samples) |
| `thread_restyle_sheet_total` | 2 | 38 min | 33 min to 44 min | 32 min to 45 min (few samples) |
| `tool_family_round_rebuild` | 1 | 42 min | 42 min to 42 min | 42 min to 42 min (few samples) |
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
- **The download does not start by itself.** On 18 Nov the renders finished about 1:55 PM ET but no frame moved until 4:05 PM ET: renderBeamer's auto-download had been switched off the day before and the user's computer had gone to sleep. Check that frames are landing within 10 minutes of the farm finishing, and count the start as a gate (Mac awake, renderBeamer open).
- The second download ran at about 1.2 MB/s, half the earlier 2.3 MB/s: 39 GB for two 2160-frame cuts is about 9 hours. Use `eta.py transfer --rate 1.2` for the late end.
- Callouts on about 20 labels: about 30 minutes. Encoding a 90-second 4K reel with callouts: about 45 minutes in chunks.
- **End to end**, from "go" to a delivered video: about 6 hours for one cut, including one human wait.

### Cloud machines without a GPU
- A preview test frame takes about 2 minutes on a 4-core cloud machine. A full-quality animation frame is estimated at 40 to 60 minutes (not measured yet), which is why animations go to the farm.
- Sawhorse r8 still set (Thorn, 18 Nov): mesh at VOX 0.09 plus 8 stills at 1200 px, 64 spp, CPU Cycles on a 4-core cloud machine took about 18 minutes; the same 8 at 500 px, 16 spp took about 2 minutes. Setup (pip install bpy 5.3 and mesh libs) about 2 minutes.

### Site and tooling work
- A web feature built, pushed and live (for example the WebGL fractal engine with 6 presets): about 27 minutes, of which the deploy wait is about 3 minutes.
- Saving or packaging a small skill: 8 to 24 minutes. Research and sourcing (hinges, wood scans, a production plan, a site style scan): 18 to 46 minutes. Small graphics or a teaser: 11 to 15 minutes. A short explainer animation: about 42 minutes. A new CAD add-on design: about 76 minutes.

- **Backup to Google Drive through the user's computer folder:** about 14 minutes per GB end to end (tar.gz, split into 24 MB parts because file copies to the device cap at 25 MB, reassemble and md5-verify on the user's computer). 1.8 GB took about 25 minutes on 18 Nov.

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

Update 18 Nov, 3:45 PM ET: 6 closed ETAs, median actual/p50 1.30 (above the 1.2 line); by 5:40 PM ET 7 closed, median 1.40. The sawhorse fix round ran 1.4x and the load and tipping skill 1.7x over p50, both agent work that grew in scope (extra research, extra fix passes). Until calibration comes back under 1.2, multiply the p50 of agent-work steps by 1.3 and quote the p90 as the late end.
- 18 Nov: a combined `pip install bpy build123d` can hang silently (seconds of CPU over 14 min). If it shows no progress after 5 min, kill it and install build123d and bpy separately (2 + 3 min).
- dims.svg by build123d projection scales badly with part count: 142 parts took 17.5 min on 4 cores (Mortisha). Drop small hardware and start it in the background right after check_machine passes.
