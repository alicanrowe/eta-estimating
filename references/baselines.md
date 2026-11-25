# Measured baselines

Every number here comes from a real run in a one-person furniture and jewelry studio: thread start and finish times, render logs and farm jobs from 17 to 18 November 2026. Times are wall clock, from the moment work starts to the moment a checked result is reported, unless the row says otherwise. Rebuild the table with `python3 scripts/eta.py rebuild` after adding rows to `data/observations.csv`.

## Table (auto-generated)

<!-- AUTO:START -->
| What | n | Typical (p50) | Range (p10 to p90) | Seen |
|---|---|---|---|---|
| `animation_frames_48_chunk` | 3 | 28 min | 19 min to 32 min | 17 min to 33 min (few samples) |
| `animation_label_fix_round` | 2 | 50 min | 15 min to 84 min | 6.0 min to 1.6 h (few samples) |
| `animation_small` | 1 | 42 min | 42 min to 42 min | 42 min to 42 min (few samples) |
| `blender_download_cloud` | 1 | 0.6 min | 0.6 min to 0.6 min | 0.6 min to 0.6 min (few samples) |
| `bombyx_job_piece` | 8 | 7.2 min | 4.2 min to 16 min | 4.1 min to 24 min |
| `book_metal_pages_redo_after_rejection` | 1 | 68 min | 68 min to 68 min | 68 min to 68 min (few samples) |
| `book_rebuild_existing` | 1 | 7.3 min | 7.3 min to 7.3 min | 7.3 min to 7.3 min (few samples) |
| `boot_build_check_kit4` | 3 | 1.7 min | 1.6 min to 1.9 min | 1.6 min to 2.0 min (few samples) |
| `boot_build_kit4` | 1 | 2.8 min | 2.8 min to 2.8 min | 2.8 min to 2.8 min (few samples) |
| `boot_build_v4_tall` | 1 | 2.1 min | 2.1 min to 2.1 min | 2.1 min to 2.1 min (few samples) |
| `boot_design_round4_to_pass` | 3 | 1.6 h | 1.6 h to 1.7 h | 1.6 h to 1.7 h (few samples) |
| `boot_final_render_set_1400px_64spp` | 4 | 28 min | 20 min to 33 min | 18 min to 34 min |
| `boot_r4_piece_thread` | 1 | 1.6 h | 1.6 h to 1.6 h | 1.6 h to 1.6 h (few samples) |
| `boot_r4_strong_pass` | 1 | 42 min | 42 min to 42 min | 42 min to 42 min (few samples) |
| `boot_render_final_set` | 1 | 25 min | 25 min to 25 min | 25 min to 25 min (few samples) |
| `boot_render_preview_5views_parts` | 1 | 9.0 min | 9.0 min to 9.0 min | 9.0 min to 9.0 min (few samples) |
| `boot_render_v4_black_final` | 1 | 21 min | 21 min to 21 min | 21 min to 21 min (few samples) |
| `boot_render_v4_red_final` | 1 | 4.5 min | 4.5 min to 4.5 min | 4.5 min to 4.5 min (few samples) |
| `boot_revision_pass_round4` | 1 | 31 min | 31 min to 31 min | 31 min to 31 min (few samples) |
| `boot_round_9_designs_kit_rebuild` | 1 | 70 min | 70 min to 70 min | 70 min to 70 min (few samples) |
| `bot_render_1300_96_cloud` | 1 | 15 min | 15 min to 15 min | 15 min to 15 min (few samples) |
| `cad_design_feature` | 1 | 76 min | 76 min to 76 min | 76 min to 76 min (few samples) |
| `cad_sdf_foot_marching_cubes` | 1 | 0.2 min | 0.2 min to 0.2 min | 0.2 min to 0.2 min (few samples) |
| `cadcheck_trimesh_fcl_swing` | 1 | 11 min | 11 min to 11 min | 11 min to 11 min (few samples) |
| `callouts_19_of_21` | 1 | 29 min | 29 min to 29 min | 29 min to 29 min (few samples) |
| `clo_remote_import` | 1 | 53 min | 53 min to 53 min | 53 min to 53 min (few samples) |
| `cloud_bpy_setup` | 2 | 1.8 min | 1.1 min to 2.4 min | 1.0 min to 2.5 min (few samples) |
| `cloud_cpu_test_still` | 1 | 2.0 min | 2.0 min to 2.0 min | 2.0 min to 2.0 min (few samples) |
| `cloud_env_setup_bpy` | 1 | 3.0 min | 3.0 min to 3.0 min | 3.0 min to 3.0 min (few samples) |
| `code_freeze_break` | 1 | 3.0 min | 3.0 min to 3.0 min | 3.0 min to 3.0 min (few samples) |
| `collection_fanout_renders` | 1 | 6.0 min | 6.0 min to 6.0 min | 6.0 min to 6.0 min (few samples) |
| `collection_redesign_polish` | 1 | 50 min | 50 min to 50 min | 50 min to 50 min (few samples) |
| `context_render_case_1view_1300px_96spp` | 1 | 1.7 min | 1.7 min to 1.7 min | 1.7 min to 1.7 min (few samples) |
| `context_render_case_3views_1100px` | 1 | 1.5 min | 1.5 min to 1.5 min | 1.5 min to 1.5 min (few samples) |
| `context_render_case_3views_1500px` | 2 | 8.5 min | 8.1 min to 8.9 min | 8.0 min to 9.0 min (few samples) |
| `cycles_3view_strip_1400px_128s_4cpu_75kfaces` | 3 | 1.6 min | 1.6 min to 1.8 min | 1.6 min to 1.8 min (few samples) |
| `cycles_frame_576x720_32s_4cpu` | 1 | 0.3 min | 0.3 min to 0.3 min | 0.3 min to 0.3 min (few samples) |
| `dancer_machine_overhaul` | 1 | 2.3 h | 2.3 h to 2.3 h | 2.3 h to 2.3 h (few samples) |
| `dancers_build_audit` | 14 | 50 min | 26 min to 2.6 h | 24 min to 3.2 h |
| `dancers_example_print_swap` | 1 | 27 min | 27 min to 27 min | 27 min to 27 min (few samples) |
| `dancers_listing_wait` | 3 | 45 min | 35 min to 54 min | 32 min to 56 min (few samples) |
| `dancers_machine_listing_fixes` | 1 | 33 min | 33 min to 33 min | 33 min to 33 min (few samples) |
| `dancers_machine_overhaul` | 17 | 80 min | 56 min to 1.9 h | 42 min to 2.4 h |
| `dancers_machine_tray_remodel` | 1 | 32 min | 32 min to 32 min | 32 min to 32 min (few samples) |
| `dancers_tile_48frame_range_cold` | 3 | 27 min | 19 min to 31 min | 16 min to 32 min (few samples) |
| `design_origami_redesign_concept_to_checked_model` | 1 | 60 min | 60 min to 60 min | 60 min to 60 min (few samples) |
| `design_three_options_to_frozen` | 1 | 50 min | 50 min to 50 min | 50 min to 50 min (few samples) |
| `drive_backup_connector_small_files` | 1 | 1.0 min | 1.0 min to 1.0 min | 1.0 min to 1.0 min (few samples) |
| `drive_backup_direct_resumable_per_gb` | 1 | 6.0 min | 6.0 min to 6.0 min | 6.0 min to 6.0 min (few samples) |
| `drive_backup_via_mac_per_gb` | 2 | 10 min | 7.2 min to 13 min | 6.5 min to 14 min (few samples) |
| `encode_81s_4k` | 1 | 37 min | 37 min to 37 min | 37 min to 37 min (few samples) |
| `encode_final_chunk` | 1 | 7.0 min | 7.0 min to 7.0 min | 7.0 min to 7.0 min (few samples) |
| `env_bpy_venv_install` | 3 | 1.1 min | 0.7 min to 1.8 min | 0.6 min to 2.0 min (few samples) |
| `farm_cost_usd_per_2160f_low` | 7 | $69 | $64 to $71 | $63 to $72 |
| `farm_download` | 1 | 1.6 h | 1.6 h to 1.6 h | 1.6 h to 1.6 h (few samples) |
| `farm_download_2160f_h` | 2 | 2.9 h | 1.9 h to 3.9 h | 1.6 h to 4.2 h (few samples) |
| `farm_download_mac_sleep_stall` | 1 | 2.0 h | 2.0 h to 2.0 h | 2.0 h to 2.0 h (few samples) |
| `farm_download_start_gate` | 1 | 2.2 h | 2.2 h to 2.2 h | 2.2 h to 2.2 h (few samples) |
| `farm_job_end_to_end_h` | 2 | 7.9 h | 6.5 h to 9.3 h | 6.1 h to 9.7 h (few samples) |
| `farm_pack_copy_checksum` | 1 | 6.0 min | 6.0 min to 6.0 min | 6.0 min to 6.0 min (few samples) |
| `farm_render_1728f_overnight_upper_h` | 1 | 8.0 h | 8.0 h to 8.0 h | 8.0 h to 8.0 h (few samples) |
| `farm_render_2160f_low_h` | 4 | 2.0 h | 1.7 h to 2.0 h | 1.6 h to 2.0 h |
| `farm_render_shots_medium` | 2 | 14 min | 11 min to 16 min | 10 min to 16 min (few samples) |
| `farm_tail_last_frames_to_delivery` | 2 | 19 min | 15 min to 23 min | 14 min to 24 min (few samples) |
| `farm_upload_renderbeamer` | 3 | 5.0 min | 5.0 min to 6.2 min | 5.0 min to 6.5 min (few samples) |
| `farm_upload_renderbeamer_headless` | 1 | 1.5 min | 1.5 min to 1.5 min | 1.5 min to 1.5 min (few samples) |
| `farm_web_submit_js` | 1 | 5.0 min | 5.0 min to 5.0 min | 5.0 min to 5.0 min (few samples) |
| `flatwork_final_piece` | 1 | 8.0 min | 8.0 min to 8.0 min | 8.0 min to 8.0 min (few samples) |
| `furniture_cast_piece_cold` | 3 | 10 min | 10 min to 12 min | 10 min to 13 min (few samples) |
| `furniture_motif_design_to_preview` | 1 | 55 min | 55 min to 55 min | 55 min to 55 min (few samples) |
| `furniture_motif_variant_round` | 1 | 32 min | 32 min to 32 min | 32 min to 32 min (few samples) |
| `graphics_small` | 2 | 13 min | 11 min to 15 min | 11 min to 15 min (few samples) |
| `human_gate_active` | 5 | 1.3 min | 0.6 min to 5.6 min | 0.3 min to 8.0 min |
| `human_gate_daytime_away` | 5 | 39 min | 34 min to 67 min | 31 min to 75 min |
| `human_gate_overnight` | 2 | 14.9 h | 14.2 h to 15.6 h | 14.1 h to 15.8 h (few samples) |
| `jacket_build_check` | 1 | 1.8 min | 1.8 min to 1.8 min | 1.8 min to 1.8 min (few samples) |
| `jacket_design_cloud` | 2 | 31 min | 29 min to 33 min | 29 min to 33 min (few samples) |
| `jacket_design_cold` | 2 | 42 min | 35 min to 48 min | 33 min to 50 min (few samples) |
| `jacket_design_full` | 1 | 70 min | 70 min to 70 min | 70 min to 70 min (few samples) |
| `jacket_final_render` | 4 | 7.8 min | 7.3 min to 8.2 min | 7.2 min to 8.2 min |
| `jacket_final_render_pair` | 1 | 2.6 min | 2.6 min to 2.6 min | 2.6 min to 2.6 min (few samples) |
| `jacket_final_render_per_colour` | 1 | 14 min | 14 min to 14 min | 14 min to 14 min (few samples) |
| `jacket_part_sheet_render` | 1 | 8.0 min | 8.0 min to 8.0 min | 8.0 min to 8.0 min (few samples) |
| `jacket_preview_2views` | 1 | 3.5 min | 3.5 min to 3.5 min | 3.5 min to 3.5 min (few samples) |
| `jacket_preview_3view` | 1 | 0.7 min | 0.7 min to 0.7 min | 0.7 min to 0.7 min (few samples) |
| `jacket_r4_design_full` | 1 | 3.0 h | 3.0 h to 3.0 h | 3.0 h to 3.0 h (few samples) |
| `jacket_revision_pass_round4` | 1 | 55 min | 55 min to 55 min | 55 min to 55 min (few samples) |
| `jewelry_batch_finish` | 1 | 19 min | 19 min to 19 min | 19 min to 19 min (few samples) |
| `jewelry_bx_batch4` | 3 | 16 min | 12 min to 30 min | 10 min to 33 min (few samples) |
| `jewelry_c1_piece_render_only` | 8 | 0.9 min | 0.9 min to 1.6 min | 0.8 min to 1.6 min |
| `jewelry_c1_square_4seasons` | 2 | 3.9 min | 3.8 min to 3.9 min | 3.8 min to 4.0 min (few samples) |
| `jewelry_collection_fanout_64` | 1 | 47 min | 47 min to 47 min | 47 min to 47 min (few samples) |
| `jewelry_cuff_cold` | 5 | 25 min | 10 min to 28 min | 5.0 min to 29 min |
| `jewelry_fix_round_21` | 1 | 25 min | 25 min to 25 min | 25 min to 25 min (few samples) |
| `jewelry_piece_cold` | 57 | 7.3 min | 4.2 min to 13 min | 0.9 min to 16 min |
| `jewelry_piece_incl_stall` | 4 | 30 min | 18 min to 43 min | 18 min to 44 min |
| `jewelry_piece_job_cloud` | 1 | 2.5 min | 2.5 min to 2.5 min | 2.5 min to 2.5 min (few samples) |
| `jewelry_piece_job_cloud_cuff` | 1 | 6.0 min | 6.0 min to 6.0 min | 6.0 min to 6.0 min (few samples) |
| `jewelry_piece_machined_cold` | 1 | 1.5 min | 1.5 min to 1.5 min | 1.5 min to 1.5 min (few samples) |
| `jewelry_piece_restart_after_stall` | 3 | 3.5 min | 2.3 min to 4.7 min | 2.0 min to 5.0 min (few samples) |
| `jewelry_piece_warm_rerender` | 25 | 2.5 min | 0.9 min to 5.1 min | 0.8 min to 11 min |
| `jewelry_render_4views_sec` | 49 | 27 s | 21 s to 35 s | 16 s to 43 s |
| `jewelry_sheet_end_to_end` | 1 | 3.2 h | 3.2 h to 3.2 h | 3.2 h to 3.2 h (few samples) |
| `layer_kit_exact_union_ring` | 1 | 6.0 min | 6.0 min to 6.0 min | 6.0 min to 6.0 min (few samples) |
| `layer_kit_finish_ring` | 1 | 10 min | 10 min to 10 min | 10 min to 10 min (few samples) |
| `mac_lag_session_kill` | 1 | 15 min | 15 min to 15 min | 15 min to 15 min (few samples) |
| `mac_setup_walkthrough` | 1 | 4.0 min | 4.0 min to 4.0 min | 4.0 min to 4.0 min (few samples) |
| `material_photo_match` | 1 | 1.8 h | 1.8 h to 1.8 h | 1.8 h to 1.8 h (few samples) |
| `model_fix_and_refarm_prep` | 1 | 15 min | 15 min to 15 min | 15 min to 15 min (few samples) |
| `moth_gem_render_4view` | 8 | 10 min | 9.4 min to 12 min | 9.0 min to 12 min |
| `moth_tool_v3_piece` | 1 | 3.5 min | 3.5 min to 3.5 min | 3.5 min to 3.5 min (few samples) |
| `moth_tool_v3_piece_warm` | 1 | 2.5 min | 2.5 min to 2.5 min | 2.5 min to 2.5 min (few samples) |
| `moth_tool_v3_render_1400_128` | 4 | 3.8 min | 2.0 min to 6.3 min | 2.0 min to 6.5 min |
| `moth_v3_piece_cold` | 1 | 7.0 min | 7.0 min to 7.0 min | 7.0 min to 7.0 min (few samples) |
| `moth_v3_piece_rerun` | 1 | 5.5 min | 5.5 min to 5.5 min | 5.5 min to 5.5 min (few samples) |
| `photo_matched_carving_cad_full` | 1 | 4.5 h | 4.5 h to 4.5 h | 4.5 h to 4.5 h (few samples) |
| `pip_bpy_build123d_setup` | 1 | 2.5 min | 2.5 min to 2.5 min | 2.5 min to 2.5 min (few samples) |
| `platform_concurrency_stall` | 3 | 38 min | 20 min to 80 min | 15 min to 1.5 h (few samples) |
| `platform_concurrency_stall_seen_count` | 1 | 4.0 min | 4.0 min to 4.0 min | 4.0 min to 4.0 min (few samples) |
| `proj_boot_r4_one_boot` | 1 | 2.6 h | 2.6 h to 2.6 h | 2.6 h to 2.6 h (few samples) |
| `proj_design_round_central` | 3 | 73 min | 64 min to 75 min | 62 min to 75 min (few samples) |
| `proj_fanout_piece_design` | 8 | 48 min | 30 min to 67 min | 29 min to 68 min |
| `proj_fanout_piece_redesign_heavy` | 6 | 2.2 h | 2.1 h to 2.3 h | 2.1 h to 2.3 h |
| `proj_first_wave_fail_pct` | 1 | 33 % | 33 % to 33 % | 33 % to 33 % (few samples) |
| `proj_fix_tail` | 1 | 75 min | 75 min to 75 min | 75 min to 75 min (few samples) |
| `proj_kit_and_briefs` | 3 | 14 min | 12 min to 40 min | 11 min to 47 min (few samples) |
| `proj_page_build_merge` | 3 | 40 min | 28 min to 43 min | 25 min to 44 min (few samples) |
| `proj_render_batch4_wave` | 15 | 18 min | 13 min to 26 min | 10 min to 33 min |
| `proj_review_gate_design` | 3 | 4.6 h | 75 min to 14.9 h | 24 min to 17.5 h (few samples) |
| `proj_round_end_to_end` | 4 | 85 min | 65 min to 1.8 h | 62 min to 1.9 h |
| `quote_form_submit_web` | 1 | 49 min | 49 min to 49 min | 49 min to 49 min (few samples) |
| `reel_patch_post_encode` | 1 | 20 min | 20 min to 20 min | 20 min to 20 min (few samples) |
| `reel_pull_frames_drive_composio` | 1 | 6.0 min | 6.0 min to 6.0 min | 6.0 min to 6.0 min (few samples) |
| `reel_studio_finish_1346f_cpu4` | 1 | 25 min | 25 min to 25 min | 25 min to 25 min (few samples) |
| `render_8view_cycles_1000px_48spp` | 2 | 13 min | 10 min to 16 min | 9.3 min to 17 min (few samples) |
| `render_check_round` | 7 | 8.0 min | 6.6 min to 25 min | 4.5 min to 38 min |
| `render_cycles_clay_cpu4` | 1 | 0.2 min | 0.2 min to 0.2 min | 0.2 min to 0.2 min (few samples) |
| `render_cycles_final_1280x1600_cpu4` | 1 | 3.5 min | 3.5 min to 3.5 min | 3.5 min to 3.5 min (few samples) |
| `render_cycles_final_1400x1750_128spp_ao_bevel_cpu4` | 2 | 23 min | 18 min to 28 min | 17 min to 29 min (few samples) |
| `render_fidelity_view_1200_64spp` | 1 | 2.0 min | 2.0 min to 2.0 min | 2.0 min to 2.0 min (few samples) |
| `render_loop_fanout` | 1 | 50 min | 50 min to 50 min | 50 min to 50 min (few samples) |
| `render_machine_3views_1300px_64spp` | 1 | 5.0 min | 5.0 min to 5.0 min | 5.0 min to 5.0 min (few samples) |
| `render_machine_3views_1300px_96spp` | 4 | 10 min | 8.6 min to 11 min | 8.0 min to 12 min |
| `render_sawhorse_view_1000px_48spp` | 3 | 1.1 min | 1.1 min to 1.2 min | 1.1 min to 1.2 min (few samples) |
| `render_sawhorse_view_1100px_64spp` | 3 | 1.9 min | 1.7 min to 2.0 min | 1.6 min to 2.0 min (few samples) |
| `render_shopbot_3view_1300px_96spp` | 4 | 10 min | 9.0 min to 10 min | 8.5 min to 10 min |
| `render_still_cloud_each` | 1 | 5.0 min | 5.0 min to 5.0 min | 5.0 min to 5.0 min (few samples) |
| `render_stills_cloud_set` | 1 | 29 min | 29 min to 29 min | 29 min to 29 min (few samples) |
| `render_tower_4090_reel_1346f_1080x1920_32spp` | 1 | 1.9 h | 1.9 h to 1.9 h | 1.9 h to 1.9 h (few samples) |
| `renderbeamer_restart_to_frames` | 2 | 5.3 min | 1.5 min to 9.1 min | 0.6 min to 10 min (few samples) |
| `renderbeamer_startup` | 1 | 9.0 min | 9.0 min to 9.0 min | 9.0 min to 9.0 min (few samples) |
| `research_sourcing` | 5 | 21 min | 12 min to 42 min | 8.0 min to 46 min |
| `sawhorse_fix_round` | 10 | 28 min | 22 min to 45 min | 19 min to 46 min |
| `sawhorse_variant` | 8 | 36 min | 28 min to 62 min | 22 min to 80 min |
| `scene_render_4core_1000px` | 1 | 0.9 min | 0.9 min to 0.9 min | 0.9 min to 0.9 min (few samples) |
| `scene_render_4core_1600px_96spp` | 1 | 6.0 min | 6.0 min to 6.0 min | 6.0 min to 6.0 min (few samples) |
| `sculpted_cast_plate_pair_round` | 1 | 50 min | 50 min to 50 min | 50 min to 50 min (few samples) |
| `sdf_carved_piece_build` | 1 | 0.6 min | 0.6 min to 0.6 min | 0.6 min to 0.6 min (few samples) |
| `sdf_log_96in_build` | 1 | 0.8 min | 0.8 min to 0.8 min | 0.8 min to 0.8 min (few samples) |
| `setup_pip_bpy_build123d` | 1 | 16 min | 16 min to 16 min | 16 min to 16 min (few samples) |
| `shared_parts_batch` | 2 | 56 min | 51 min to 61 min | 50 min to 62 min (few samples) |
| `shop_bot_final_render_1300_96` | 1 | 12 min | 12 min to 12 min | 12 min to 12 min (few samples) |
| `shop_bot_render_full` | 2 | 24 min | 16 min to 32 min | 14 min to 34 min (few samples) |
| `shop_bot_render_preview` | 1 | 2.1 min | 2.1 min to 2.1 min | 2.1 min to 2.1 min (few samples) |
| `shop_listing_wait` | 1 | 47 min | 47 min to 47 min | 47 min to 47 min (few samples) |
| `shop_machine_check` | 1 | 1.3 min | 1.3 min to 1.3 min | 1.3 min to 1.3 min (few samples) |
| `shop_machine_overhaul` | 1 | 1.6 h | 1.6 h to 1.6 h | 1.6 h to 1.6 h (few samples) |
| `shop_machine_overhaul_thread` | 1 | 75 min | 75 min to 75 min | 75 min to 75 min (few samples) |
| `shop_machine_preview_render` | 1 | 9.0 min | 9.0 min to 9.0 min | 9.0 min to 9.0 min (few samples) |
| `shopbot_build_audit` | 1 | 50 min | 50 min to 50 min | 50 min to 50 min (few samples) |
| `shopbot_check_machine` | 3 | 0.6 min | 0.4 min to 4.9 min | 0.3 min to 6.0 min (few samples) |
| `shopbot_dims_projection` | 1 | 18 min | 18 min to 18 min | 18 min to 18 min (few samples) |
| `shopbot_machine_rebuild` | 2 | 50 min | 47 min to 52 min | 46 min to 53 min (few samples) |
| `shopbot_overhaul` | 1 | 55 min | 55 min to 55 min | 55 min to 55 min (few samples) |
| `shopbot_render_draft` | 2 | 2.9 min | 1.9 min to 3.9 min | 1.6 min to 4.1 min (few samples) |
| `shopbot_render_final` | 12 | 10 min | 9.0 min to 16 min | 7.0 min to 20 min |
| `shopbot_render_full` | 7 | 17 min | 9.1 min to 21 min | 8.5 min to 22 min |
| `site_3d_flicker_fix` | 1 | 85 min | 85 min to 85 min | 85 min to 85 min (few samples) |
| `site_3d_tiles` | 1 | 18 min | 18 min to 18 min | 18 min to 18 min (few samples) |
| `site_batch_deploy` | 2 | 1.9 h | 58 min to 2.8 h | 44 min to 3.0 h (few samples) |
| `site_collection_page` | 1 | 22 min | 22 min to 22 min | 22 min to 22 min (few samples) |
| `site_collection_rebuild` | 1 | 20 min | 20 min to 20 min | 20 min to 20 min (few samples) |
| `site_deploy_live_min` | 1 | 4.0 min | 4.0 min to 4.0 min | 4.0 min to 4.0 min (few samples) |
| `site_deploy_wait` | 1 | 3.3 min | 3.3 min to 3.3 min | 3.3 min to 3.3 min (few samples) |
| `site_page_full_refresh` | 1 | 40 min | 40 min to 40 min | 40 min to 40 min (few samples) |
| `site_page_rebuild` | 1 | 25 min | 25 min to 25 min | 25 min to 25 min (few samples) |
| `site_publish_batch` | 1 | 50 min | 50 min to 50 min | 50 min to 50 min (few samples) |
| `skill_fix_and_publish` | 1 | 12 min | 12 min to 12 min | 12 min to 12 min (few samples) |
| `skill_save_or_small_skill` | 3 | 24 min | 11 min to 89 min | 8.0 min to 1.8 h (few samples) |
| `soft_build_check_furniture` | 1 | 1.8 min | 1.8 min to 1.8 min | 1.8 min to 1.8 min (few samples) |
| `soft_part_redesign_to_0fail` | 1 | 55 min | 55 min to 55 min | 55 min to 55 min (few samples) |
| `storage_cleanup` | 3 | 29 min | 11 min to 75 min | 7.0 min to 86 min (few samples) |
| `thread_feet_pass_total` | 1 | 45 min | 45 min to 45 min | 45 min to 45 min (few samples) |
| `thread_fix_pass_total` | 1 | 50 min | 50 min to 50 min | 50 min to 50 min (few samples) |
| `thread_redesign_iteration_lowres` | 1 | 2.3 min | 2.3 min to 2.3 min | 2.3 min to 2.3 min (few samples) |
| `thread_restyle_sheet_total` | 2 | 38 min | 33 min to 44 min | 32 min to 45 min (few samples) |
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
- **The Mac going to sleep stops the download** (18 Nov evening: about 2 hours lost until the user woke it). For overnight downloads, ask up front for the user's computer to stay awake (caffeinate or Energy settings) and plug in the SSD; treat it as a gate at the start, not mid-job.
- **18 to 19 Nov two-cut job, end to end:** submitted 11:12 AM ET, 16:9 delivered 8:05 PM ET, 9:16 at 8:55 PM ET (about 9.7 hours). About 4 hours of that was the download not starting and then the user's computer sleeping. Once the user's computer was awake the 9:16 frames came down in about 1.6 hours. The first ETAs (3:30 and 5:30 PM ET) were 1.6x to 3.5x short because they assumed the download had started.
- After the last frame lands, a cut whose callouts ran during the download is delivered in 15 to 25 minutes.
- Plan a label clean-up round after the first delivery: moving every label off the objects on both cuts took about 1.5 hours; a single label fix took 6 minutes.
- Callouts on about 20 labels: about 30 minutes. Encoding a 90-second 4K reel with callouts: about 45 minutes in chunks.
- **End to end**, from "go" to a delivered video: about 6 hours for one cut, including one human wait.
- **reel, 20 Nov (1080x1920, Cycles 64 spp adaptive 0.03, MEDIUM, 30 nodes):** full 2,625-frame render about $190 ($0.072/frame). Shot re-renders cost more per frame: 540 frames in 16.5 min for $62.61 ($0.116/frame), 315 frames in 10.5 min for $30.98 ($0.098/frame). Quote shot fixes at about $0.12/frame; the $40 guess for 540 frames came in 57% over.
- **No-click farm route (works, 20 Nov):** renderBeamer headless upload via Remote Control (`Blender -b <blend> --python-expr "from bl_ext.user_default.renderbeamer.headless import run;run()" -- --upload-packed-assets 1 --json-report --fail-on-errors 1`, renderBeamer app running, autosubmit off) takes about 6 s plus about 1 min until the file shows in the web Files page. Then submit from the GarageFarm web manager with Chrome JS: click the .blend, flip the second switch to Full job, tick cameras, edit each range cell in two separate calls (click the td, then set the input with the native value setter + input event + Enter), Submit. About 5 min, no human gate beyond the price OK.
- **Swap re-rendered shots into a finished cut:** about 20 min for 300 to 500 frames (tar on the user's computer, stage, post in 4 chunks, re-encode master + web).
- **Camera gimbal flips** in keyed euler paths showed as whip-pans in 8 of 36 shots; key rotation_quaternion with sign continuity instead. A frame-difference spike scan (mean abs diff of consecutive 108x192 frames, flag > 4x the shot median) catches both flips and lens-blocking splashes before delivery.
- **Volumes:** each volume object costs about 4 s of per-frame setup on the farm even when off screen; key hide_render so a shot only carries its own clouds.
- **Project files rewrite mp4s:** a C2PA manifest box (~6 KB) is inserted into any .mp4 written to the project file store, including the first split part of one. Wrap files in a tar before splitting them for transfer, or the reassembled file differs.
- **Mac disk:** the reel's transfer tars and parts (about 2.3 GB in Downloads) filled the user's computer's disk to 100% on 20 Nov. Clean up _xfer/_out/_parts folders as soon as a transfer is verified.

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

### Mac and web-form traps (19 Nov)
- **Mac lag:** running a Blender patch and a farm upload on the user's computer at the same time made it lag badly. Its session stopped answering for 15 minutes and had to be killed, and the farm submit status was lost. Run one heavy job on the user's computer at a time, and put Mac-side steps behind a check that the session answers.
- **The Mac sleeps mid-download again:** 12:46 PM ET, and it only resumed once the user wrote "go" in that thread, 39 minutes later. Ask for the user's computer to stay awake before any download starts.
- **Supplier web forms fail on submit.** Xometry's large-quote form threw a server error 4 times, and the Materialise form stalled too. The workaround (a normal quote, then each part's manual-quote button) needed the user to drag the files in. Budget 45 to 60 minutes and 1 or 2 human gates for any quote form. The reply is about 2 business days.
- **Overnight downloads on the user's computer stall almost every night** (18 Nov about 10 PM ET, 19 Nov 7:37 PM ET). Treat any Mac-side step after about 7 PM ET as finishing the next morning, unless the user has confirmed the user's computer is staying awake.
- **Project storage full (10 GB):** saves fail once it's full, so check free space before a big render or a book build. The Drive connector here only takes files up to about 3 MB per call, but big files can still go up without the user's computer: open a Drive resumable upload session through the Composio Google Drive proxy (call the tool router proxy endpoint directly to read the `location` header; the account needs full Drive scope), then PUT the whole file to that URL from the container with curl. 62 MB took 4 seconds; 1 GB of superseded files was compressed, uploaded and md5-verified in about 6 minutes (20 Nov).

- **Fast but rejected counts as late.** The book rebuild was handed over in 7 minutes against an ETA of 10, but the user rejected its metal pages: grey case, wrong finishes, callouts on the model. The redo took another 68 minutes. For anything visual the user reviews, add one rejection-and-redo round (about 1 hour) to the late end until the check that runs before delivery has a clean record.
- **Matching a material to a photo** (the felt) passed in the test light and failed in the case light. Check a match in the real scene's lighting before calling it done, and expect 2 or 3 rounds.

- **Paid farm uploads need the user's own words.** The Mac session refused the fix upload until the user typed the exact submit line in that thread, which cost 8 minutes while the user was active. Ask for that exact line together with the price, in one message.
- **Work that waits on a decision card overnight makes no progress.** Site batch 3 (ETA 6 h) never started because its thread was waiting on a storage decision from the user. When an ETA'd job is behind a pending card, the ETA is "after you answer", not a clock time.
- **Fixes multiply.** On 19 Nov the Moth animation ETA (9 to 10 PM ET) was overtaken by four rounds of fixes, one after another: plush clipping, needle, felt, then torn tools. Each needed a new model letter and a new farm job. When the user is still reviewing a design, quote the animation as "about 6 hours after the last fix is OK'd", not as a clock time.

### Platform limits
- Starting threads is sequential at about 3 seconds each, so 90 machines take about 5 minutes just to start.
- **Concurrency stalls (top risk):** on 18 Nov about 43 jewelry render threads started but did nothing for about 90 minutes because the session limit was full. Restarted, each finished in 2 to 5 minutes. Detect them about 3 minutes after starting a batch: a working thread whose last activity equals its start time, or with no checklist, is stalled (`eta.py stallcheck`).
- A shared-code edit without a version bump blocks every render thread until the code is re-frozen (about 3 minutes each time).
- Stalls end on their own as slots free up, but slowly: in the 22:38Z jewelry batch the last 4 of 14 threads started never ran at first; two began after about 15 minutes and two after about 40. A 5-minute piece took 18 to 44 minutes.
- When too many threads run at once, new ones fail to start ("too many threads and sessions are running"). This happened with about 90 threads started within 30 minutes; several threads started then never ran. Plan fan-out in waves of about 40 and say so.

## How past ETAs did
See `data/predictions.csv` and run `python3 scripts/eta.py calibration`. As of 18 Nov 2026: the encode and farm-render ETAs were close (0.7x and 0.8x), the download ETA was 5x too short, and two serial ETAs were overtaken when the work was split across machines.

Update 18 Nov, 3:45 PM ET: 6 closed ETAs, median actual/p50 1.30 (above the 1.2 line); by 5:40 PM ET 7 closed, median 1.40. The sawhorse fix round ran 1.4x and the load and tipping skill 1.7x over p50, both agent work that grew in scope (extra research, extra fix passes). Until calibration comes back under 1.2, multiply the p50 of agent-work steps by 1.3 and quote the p90 as the late end.
- 18 Nov: a combined `pip install bpy build123d` can hang silently (seconds of CPU over 14 min). If it shows no progress after 5 min, kill it and install build123d and bpy separately (2 + 3 min).
- dims.svg by build123d projection scales badly with part count: 142 parts took 17.5 min on 4 cores (Mortisha). Drop small hardware and start it in the background right after check_machine passes.
- 2026-11-18: A container can restart mid-render and silently kill a background job; check frame counts on the share before encoding, and keep each machine's range small enough to redo fast.

- Memory trap (Moth Lancet panels, 19 Nov): trimesh/FCL clipping checks on several 400k-face castings get OOM-killed when a Cycles render runs on the same 15 GB machine, and ProximityQuery against dense neighbour castings (gable motifs, handle) is the heavy part. Run checks after renders, and use FCL min_distance managers instead of sampled proximity.


## Whole projects (21 Nov)
- Source: thread timelines of the Silk Road collection, boots rounds 1 to 4, jackets rounds 3 and 4, the taste skill, and the 18 Nov sawhorse fan-out. Phases are stored as `proj_*` categories; round outcomes in `data/projects.csv`.
- The big surprise: central design time barely scales with piece count (62 to 75 min for 3 to 64 pieces). Fixes and review rounds scale the project, not the piece count.
- The fix tail after a render wave ran 2.3x the wave itself (75 vs 33 min). One piece with a geometry bug (Zaojing clip: 5 voxel retries, then out of memory at 14 GB on a 15 GB machine) set the end.
- The render threads re-used stale outputs ("exists, skipping") on fix reruns, which cost a round of confusion across 11 threads. Clear outputs before a fix wave.
- Boots r3 renders were slower than planned because extra agents shared one 4-core machine. Fan-out means one machine per piece.
- Rejections dominate full-scope time: boots r1 to r3 and jackets r3 were all rejected. Each rejected round costs a review wait (24 min to next day) plus a 60 to 115 min redo. The taste skill (built in 9 min) is the bet to raise the accept rate; r4 verdicts will show it.
- The taste-skill distillation took 9 min (18 min thread). A small skill save is 8 to 24 min.
- 2026-11-22 | cloud CPU (4 cores, bpy 4.2 Cycles) | VIGIL on plinth + block wall, 1080x1920, 96 spp, denoise, no volumes | about 3.5 min per frame (4 plates in 14 min). Collage animatic in PIL + ffmpeg, 372 frames at 1080x1920: about 3 min.
- 2026-11-22 | cloud CPU (4 cores) | Shrine bench reference-reel pass (reel watch, one design change to a parametric piece, cadcheck, 6 Cycles renders at 1800x1200 64 spp, site PR, Drive backup) | about 3 h wall clock from ask to live page. Model rebuild 13 s; carved cadcheck at preview 10 to 12 min; renders about 2 to 4 min each; seatcheck at 15 mm cells about 2.5 h for 10 cases when sharing CPU, and its 7000 s cap killed the first run one case short. Run seatcheck uncapped (nohup) and start it first.
- 2026-11-23 | GarageFarm LOW | VIGIL bloom (1080x1920, 96 spp, haze): upload 8.5 MB about 10 s; 6-frame test 2 min 29 s, $0.11; full 102 frames quoted $1.87; download about 6 s after the farm finishes. Waiting on the owner to finish a renderBeamer update and two logins added about 40 min.
- 2026-11-23 | cloud | Skill publish sweep: dry-run all 20 skill folders with sync.sh about 2.5 min, then 4 real pushes about 1 min. Whole job about 4 min.
- 2026-11-24 | cloud CPU (4 cores, bpy Cycles) | Carved-wood + brass + glass set (tea set: 8 SDF grips, tray, arch, lid; 78 parts) from reel ask to live page: about 6 h wall clock incl. two blind-review rounds. Grip SDF about 1 min each; tray SDF about 4 min; arch 2 min; manifold3d clash check of 78 parts 1 to 2 min; test renders 700x875 48 spp 25 to 80 s; finals 1400x1750 96 spp 3 to 8.5 min each (glass close-up with DOF slowest); site checks + PR + merge about 40 min; Drive backup of 325 MB by direct PUT under 1 min.
- 2026-11-24 | cloud CPU (4 cores, bpy 5.3 Cycles) | Photoreal room stills (photoreal.py, concrete room, light-linked strips, DOF, AgX), Stay chair: test frames 480x600 32 spp about 15 s; finals 1200x1500 192 spp OIDN about 7 min each (3 in 21 min per room). Pulling 60 IG posts via Composio GetAnyAPI under 1 min, about $0.01.
