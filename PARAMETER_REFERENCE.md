# BakedBean3D Master Parameters Reference

Coverage map of the Fusion 360 master parameter library. **Check here (or grep the CSV) before researching new dimensions** — avoid duplicating existing coverage.

- **Total parameters:** 1011 (regenerated 2026-06-23)
- **Source of truth:** `BakedBean3D_MasterParams_v4/BakedBean3D_MasterParams_params.csv` (6-column Fusion format: Name, Unit, Expression, Value, Comment, Favorite)
- **This file is generated** — do not hand-edit. Run `python gen_reference.py` after `split_params.py`. Edit the `WISHLIST` block in the generator to change coverage-gap notes.
- **Naming:** component-first, snake_case, no `_mm`/ISO suffixes (e.g. `m3_button_head_dia`, `iphone16pro_width`). See `migration_mapping.csv` for old→new.

Params are imported per project from the themed split CSVs (`split/`). Tiers below match `split_params.py`.

---

## `design_rules` — 149 params  ·  _Tier 1 · always import_

FDM tolerances, fit classes, walls, fillets, chamfers, overhangs, bridges, joints, locking mechanisms, materials

- **fdm** (51) — `fdm_6061_diff_expansion`, `fdm_bridge_max`, `fdm_bridge_sag`, `fdm_chamfer_leadin`, `fdm_chamfer_standard`, `fdm_dowel_clearance`, `fdm_draft_angle`, `fdm_elephant_foot` … (+43 more)
- **dovetail** (10) — `dovetail_angle`, `dovetail_base_width`, `dovetail_chamfer`, `dovetail_clearance`, `dovetail_depth`, `dovetail_mount_angle`, `dovetail_mount_clearance`, `dovetail_mount_depth` … (+2 more)
- **bayonet** (8) — `bayonet_channel_depth`, `bayonet_clearance_radial`, `bayonet_engagement_depth`, `bayonet_entry_slot_width`, `bayonet_ramp_angle`, `bayonet_rotation_angle`, `bayonet_tab_count`, `bayonet_tab_height`
- **quarterturn** (8) — `quarterturn_clearance`, `quarterturn_detent_depth`, `quarterturn_head_dia`, `quarterturn_head_thick`, `quarterturn_keyhole_length`, `quarterturn_keyhole_width`, `quarterturn_panel_thick`, `quarterturn_stud_dia`
- **snapfit** (8) — `snapfit_beam_length`, `snapfit_beam_thick`, `snapfit_beam_width`, `snapfit_clearance`, `snapfit_entry_angle`, `snapfit_hook_depth`, `snapfit_retention_angle`, `snapfit_root_fillet`
- **camlock** (7) — `camlock_cam_dia`, `camlock_cam_thick`, `camlock_clearance`, `camlock_eccentricity`, `camlock_lever_length`, `camlock_pivot_dia`, `camlock_slot_width`
- **detent** (7) — `detent_ball_dia`, `detent_bore_depth`, `detent_bore_dia`, `detent_dimple_depth`, `detent_dimple_dia`, `detent_spring_length`, `detent_spring_thick`
- **snaplatch** (7) — `snaplatch_arm_length`, `snaplatch_arm_thick`, `snaplatch_arm_width`, `snaplatch_clearance`, `snaplatch_hook_depth`, `snaplatch_lift_tab_height`, `snaplatch_lip_thick`
- **asm** (5) — `asm_cnc_to_cnc_clearance`, `asm_fdm_to_cnc_clearance`, `asm_fdm_to_fdm_clearance`, `asm_stackup_budget_cnc`, `asm_stackup_budget_fdm`
- **tol** (5) — `tol_angular`, `tol_coarse`, `tol_fine`, `tol_h7g6_running`, `tol_medium`
- **abs** (4) — `abs_chamber_temp`, `abs_shrink`, `abs_tensile`, `abs_tg`
- **container** (4) — `container_base`, `container_corner_r`, `container_rim_width`, `container_wall`
- **hinge** (4) — `hinge_barrel_wall`, `hinge_knuckle_gap`, `hinge_pin_bore`, `hinge_pin_dia`
- **pip** (4) — `pip_hinge_clearance`, `pip_socket_ratio`, `pip_sphere_clearance`, `pip_sphere_min_dia`
- **spring** (4) — `spring_clip_hook_depth`, `spring_clip_max_flex`, `spring_clip_thick`, `spring_clip_width`
- **petg** (3) — `petg_shrink`, `petg_tensile`, `petg_tg`
- **pla** (3) — `pla_shrink`, `pla_tensile`, `pla_tg`
- **asa** (2) — `asa_shrink`, `asa_tg`
- **tpu** (2) — `tpu_85a_hardness`, `tpu_95a_hardness`
- **countersink** (1) — `countersink_angle`
- **pc** (1) — `pc_chamber_temp`
- **tool** (1) — `tool_dewalt_dcs391_blade_dia`

---

## `fasteners` — 150 params  ·  _Tier 1 · always import_

M2-M10 hardware, heat-set inserts, nut traps, counterbores, magnets, zip ties

- **m3** (33) — `m3_boss_od`, `m3_button_cbore_depth`, `m3_button_cbore_dia`, `m3_button_head_dia`, `m3_button_head_height`, `m3_close_fit_hole`, `m3_countersink_dia`, `m3_dowel_pin_dia` … (+25 more)
- **m4** (24) — `m4_boss_od`, `m4_button_cbore_depth`, `m4_button_cbore_dia`, `m4_button_head_dia`, `m4_button_head_height`, `m4_close_fit_hole`, `m4_countersink_dia`, `m4_dowel_pin_dia` … (+16 more)
- **magnet** (21) — `magnet_10x2mm_height`, `magnet_10x2mm_od`, `magnet_10x3mm_height`, `magnet_10x3mm_od`, `magnet_12x3mm_height`, `magnet_12x3mm_od`, `magnet_15x3mm_height`, `magnet_15x3mm_od` … (+13 more)
- **m2** (17) — `m2_2280_height`, `m2_2280_length`, `m2_2280_width`, `m2_boss_od`, `m2_button_cbore_depth`, `m2_button_cbore_dia`, `m2_button_head_dia`, `m2_button_head_height` … (+9 more)
- **m5** (17) — `m5_boss_od`, `m5_button_cbore_dia`, `m5_button_head_dia`, `m5_button_head_height`, `m5_close_fit_hole`, `m5_dowel_pin_dia`, `m5_flat_head_dia`, `m5_heatset_hole` … (+9 more)
- **m2p5** (14) — `m2p5_boss_od`, `m2p5_button_cbore_depth`, `m2p5_button_cbore_dia`, `m2p5_button_head_dia`, `m2p5_button_head_height`, `m2p5_close_fit_hole`, `m2p5_heatset_hole`, `m2p5_hex_nut_af` … (+6 more)
- **m6** (9) — `m6_boss_od`, `m6_close_fit_hole`, `m6_heatset_hole`, `m6_hex_nut_af`, `m6_hex_nut_height`, `m6_socket_head_dia`, `m6_socket_head_height`, `m6_thread_pitch` … (+1 more)
- **m8** (5) — `m8_heatset_hole`, `m8_hex_nut_af`, `m8_hex_nut_height`, `m8_socket_head_dia`, `m8_socket_head_height`
- **ziptie** (4) — `ziptie_2p5mm_thick`, `ziptie_2p5mm_width`, `ziptie_3p5mm_thick`, `ziptie_3p5mm_width`
- **heatset** (3) — `heatset_temp_abs_asa`, `heatset_temp_petg`, `heatset_temp_pla`
- **m10** (3) — `m10_heatset_hole`, `m10_hex_nut_af`, `m10_hex_nut_height`

---

## `motion_mechanical` — 128 params  ·  _Tier 2 · per project_

MGN rails, GT2 belts, ball bearings, NEMA motors, extrusion, CNC process params

- **cnc** (50) — `cnc_5mm_press_fit_pin`, `cnc_blank_oversize`, `cnc_datum_face_depth`, `cnc_drilled_oversize`, `cnc_edge_break`, `cnc_em_2mm_dia`, `cnc_em_3175_corner_r`, `cnc_em_3175_dia` … (+42 more)
- **bearing** (21) — `bearing_608_id`, `bearing_608_od`, `bearing_608_width`, `bearing_623_id`, `bearing_623_od`, `bearing_623_width`, `bearing_625_id`, `bearing_625_od` … (+13 more)
- **gear** (10) — `gear_addendum_factor`, `gear_backlash`, `gear_dedendum_factor`, `gear_min_teeth`, `gear_module_coarse`, `gear_module_fine`, `gear_module_standard`, `gear_pip_clearance` … (+2 more)
- **gt2** (7) — `gt2_belt_pitch`, `gt2_belt_width`, `gt2_clamp_extra`, `gt2_pulley_16t_od`, `gt2_pulley_20t_od`, `gt2_pulley_80t_od`, `gt2_pulley_bore`
- **nema17** (7) — `nema17_body_width`, `nema17_bolt_pattern_center_to_center`, `nema17_bolt_size`, `nema17_face_boss_diameter`, `nema17_shaft_diameter`, `nema17_shaft_flat_depth`, `nema17_shaft_length_standard`
- **vslot** (7) — `vslot_2020_extrusion_width`, `vslot_2020_slot_width`, `vslot_2040_extrusion_width`, `vslot_3030_extrusion_width`, `vslot_3030_slot_width`, `vslot_4040_extrusion_width`, `vslot_4040_slot_width`
- **mgn12h** (4) — `mgn12h_carriage_length`, `mgn12h_pitch_across`, `mgn12h_pitch_along`, `mgn12h_rail_width`
- **f695** (3) — `f695_bearing_id`, `f695_bearing_od`, `f695_bearing_width`
- **mgn9h** (3) — `mgn9h_pitch_across`, `mgn9h_pitch_along`, `mgn9h_rail_width`
- **nema14** (3) — `nema14_body_width`, `nema14_bolt_pattern_center_to_center`, `nema14_shaft_diameter`
- **alu** (2) — `alu_6061_density`, `alu_6061_service_max`
- **beacon** (2) — `beacon_probe_body_outer_diameter`, `beacon_probe_body_total_length`
- **orbiter** (2) — `orbiter_v25_filament_path_offset_from_mount`, `orbiter_v25_motor_mount_bolt_pattern`
- **toolhead** (2) — `toolhead_plate_4mm`, `toolhead_plate_5mm`
- **canbus** (1) — `canbus_cable_chain_slot_width`
- **chube** (1) — `chube_hotend_collet_outer_diameter`
- **mgn15h** (1) — `mgn15h_rail_width`
- **mgn7h** (1) — `mgn7h_rail_width`
- **tslot** (1) — `tslot_m3_nut_slot_clearance_width`

---

## `electronics_mounting` — 60 params  ·  _Tier 2 · per project_

PCBs, header pitch, connectors, panel cutouts, DIN rail, home automation

- **rpi** (12) — `rpi_board_length`, `rpi_board_width`, `rpi_mount_hole_dia`, `rpi_pico_board_length`, `rpi_pico_board_width`, `rpi_pico_mount_hole_dia`, `rpi_pico_mount_pitch_x`, `rpi_pico_mount_pitch_y` … (+4 more)
- **wallplate** (9) — `wallplate_jumbo_height`, `wallplate_jumbo_width`, `wallplate_screw_clearance`, `wallplate_screw_pitch`, `wallplate_std_height`, `wallplate_std_width`, `wallplate_thickness`, `wallplate_toggle_slot_height` … (+1 more)
- **gang** (7) — `gang_box_depth_max`, `gang_box_depth_min`, `gang_box_internal_height`, `gang_box_internal_width`, `gang_box_single_height`, `gang_box_single_width`, `gang_box_yoke_screw_span`
- **usb** (4) — `usb_a_panel_height`, `usb_a_panel_width`, `usb_c_panel_height`, `usb_c_panel_width`
- **din** (3) — `din_rail_clip_depth`, `din_rail_depth`, `din_rail_width`
- **wago221** (3) — `wago221_body_depth`, `wago221_body_height`, `wago221_body_width_2way`
- **conduit** (2) — `conduit_half_inch_knockout_dia`, `conduit_three_quarter_inch_knockout_dia`
- **d1mini** (2) — `d1mini_board_length`, `d1mini_board_width`
- **decora** (2) — `decora_cutout_height`, `decora_cutout_width`
- **esp32** (2) — `esp32_board_length`, `esp32_board_width`
- **jst** (2) — `jst_xh_2pin_width`, `jst_xh_height`
- **octopus** (2) — `octopus_mount_pitch_x`, `octopus_mount_pitch_y`
- **rpi4** (2) — `rpi4_mount_pitch_x`, `rpi4_mount_pitch_y`
- **skr** (2) — `skr_mini_mount_pitch_x`, `skr_mini_mount_pitch_y`
- **sonoff** (2) — `sonoff_zbdongle_p_length`, `sonoff_zbdongle_p_width`
- **header** (1) — `header_pitch`
- **pcb** (1) — `pcb_edge_clearance`
- **xt30** (1) — `xt30_panel_dia`
- **xt60** (1) — `xt60_panel_dia`

---

## `devices` — 121 params  ·  _Tier 2 · per project_

phones, tablets, watches, controllers, remotes, chargers, smart home, cameras

- **watch** (11) — `watch_band_20`, `watch_band_22`, `watch_s10_42_depth`, `watch_s10_42_height`, `watch_s10_42_width`, `watch_s10_46_depth`, `watch_s10_46_height`, `watch_s10_46_width` … (+3 more)
- **ring** (8) — `ring_doorbell_depth`, `ring_doorbell_height`, `ring_doorbell_width`, `ring_indoor_depth`, `ring_indoor_height`, `ring_indoor_width`, `ring_stickup_dia`, `ring_stickup_height`
- **unifi** (7) — `unifi_g4_bullet_dia`, `unifi_g4_bullet_length`, `unifi_g4_instant_depth`, `unifi_g4_instant_height`, `unifi_g4_instant_width`, `unifi_g5_flex_dia`, `unifi_g5_flex_height`
- **phone** (6) — `phone_case_allowance`, `phone_cased_depth`, `phone_cased_width`, `phone_max_depth`, `phone_max_height`, `phone_max_width`
- **echo** (5) — `echo_dot5_dia`, `echo_dot5_height`, `echo_show5_depth`, `echo_show5_height`, `echo_show5_width`
- **airpods** (3) — `airpods_pro2_depth`, `airpods_pro2_height`, `airpods_pro2_width`
- **appletv** (3) — `appletv_remote_depth`, `appletv_remote_height`, `appletv_remote_width`
- **controller** (3) — `controller_max_depth`, `controller_max_height`, `controller_max_width`
- **firetv** (3) — `firetv_remote_depth`, `firetv_remote_height`, `firetv_remote_width`
- **galaxys24** (3) — `galaxys24_depth`, `galaxys24_height`, `galaxys24_width`
- **galaxys24plus** (3) — `galaxys24plus_depth`, `galaxys24plus_height`, `galaxys24plus_width`
- **galaxys24ultra** (3) — `galaxys24ultra_depth`, `galaxys24ultra_height`, `galaxys24ultra_width`
- **ipadair11** (3) — `ipadair11_depth`, `ipadair11_height`, `ipadair11_width`
- **ipadmini7** (3) — `ipadmini7_depth`, `ipadmini7_height`, `ipadmini7_width`
- **ipadpro11** (3) — `ipadpro11_depth`, `ipadpro11_height`, `ipadpro11_width`
- **ipadpro13** (3) — `ipadpro13_depth`, `ipadpro13_height`, `ipadpro13_width`
- **iphone15** (3) — `iphone15_depth`, `iphone15_height`, `iphone15_width`
- **iphone15pro** (3) — `iphone15pro_depth`, `iphone15pro_height`, `iphone15pro_width`
- **iphone15promax** (3) — `iphone15promax_depth`, `iphone15promax_height`, `iphone15promax_width`
- **iphone16** (3) — `iphone16_depth`, `iphone16_height`, `iphone16_width`
- **iphone16pro** (3) — `iphone16pro_depth`, `iphone16pro_height`, `iphone16pro_width`
- **iphone16promax** (3) — `iphone16promax_depth`, `iphone16promax_height`, `iphone16promax_width`
- **joycon** (3) — `joycon_depth`, `joycon_height`, `joycon_width`
- **kasa** (3) — `kasa_ep10_depth`, `kasa_ep10_height`, `kasa_ep10_width`
- **ps5** (3) — `ps5_depth`, `ps5_height`, `ps5_width`
- **roku** (3) — `roku_remote_depth`, `roku_remote_height`, `roku_remote_width`
- **switch** (3) — `switch_pro_depth`, `switch_pro_height`, `switch_pro_width`
- **tablet** (3) — `tablet_max_depth`, `tablet_max_height`, `tablet_max_width`
- **xbox** (3) — `xbox_depth`, `xbox_height`, `xbox_width`
- **applewatch** (2) — `applewatch_charger_dia`, `applewatch_charger_thick`
- **hue** (2) — `hue_bridge_height`, `hue_bridge_width`
- **magsafe15w** (2) — `magsafe15w_dia`, `magsafe15w_thick`
- **magsafe25w** (2) — `magsafe25w_dia`, `magsafe25w_thick`
- **nest** (2) — `nest_mini2_dia`, `nest_mini2_height`
- **tripod** (2) — `tripod_mount_thread_dia`, `tripod_mount_thread_pitch`

---

## `workshop` — 108 params  ·  _Tier 2 · per project_

pegboard & wall systems (Multiboard/SKADIS/Gridfinity/HSW/French cleat), shop stock (EMT/lumber/sheet), power & hand tools, batteries, keys

- **dewalt** (12) — `dewalt_20v_bat_max_4ah_height`, `dewalt_20v_bat_max_4ah_length`, `dewalt_20v_bat_max_4ah_width`, `dewalt_drill_height`, `dewalt_drill_length`, `dewalt_drill_width`, `dewalt_sander_height`, `dewalt_sander_length` … (+4 more)
- **milwaukee** (11) — `milwaukee_drill_height`, `milwaukee_drill_length`, `milwaukee_drill_width`, `milwaukee_m18_bat_cp2_height`, `milwaukee_m18_bat_cp2_length`, `milwaukee_m18_bat_cp2_width`, `milwaukee_sander_height`, `milwaukee_sander_length` … (+3 more)
- **pegboard** (7) — `pegboard_hole_dia`, `pegboard_hole_spacing`, `pegboard_hook_wire_dia`, `pegboard_light_hook_dia`, `pegboard_small_hole_dia`, `pegboard_small_thickness`, `pegboard_thickness`
- **adj** (6) — `adj_wrench_10in_jaw_width`, `adj_wrench_10in_length`, `adj_wrench_6in_jaw_width`, `adj_wrench_6in_length`, `adj_wrench_8in_jaw_width`, `adj_wrench_8in_length`
- **gridfinity** (6) — `gridfinity_baseplate_wall`, `gridfinity_bin_foot`, `gridfinity_corner_fillet`, `gridfinity_grid`, `gridfinity_stack_lip`, `gridfinity_z_unit`
- **sq** (5) — `sq_drive_half_af`, `sq_drive_one_inch_af`, `sq_drive_quarter_af`, `sq_drive_three_eighth_af`, `sq_drive_three_quarter_af`
- **emt** (4) — `emt_half_inch_od`, `emt_one_and_quarter_inch_od`, `emt_one_inch_od`, `emt_three_quarter_inch_od`
- **lumber** (4) — `lumber_1x4_width`, `lumber_2x4_thickness`, `lumber_2x4_width`, `lumber_2x6_width`
- **multiboard** (4) — `multiboard_bin_cu`, `multiboard_snap_standoff`, `multiboard_tile_grid`, `multiboard_tol`
- **aa** (3) — `aa_bat_dia`, `aa_bat_length`, `aa_holder_slot_dia`
- **aaa** (3) — `aaa_bat_dia`, `aaa_bat_length`, `aaa_holder_slot_dia`
- **bat** (3) — `bat_18650_dia`, `bat_18650_holder_slot_dia`, `bat_18650_length`
- **hammer** (3) — `hammer_16oz_handle_dia`, `hammer_16oz_head_width`, `hammer_16oz_length`
- **kw1** (3) — `kw1_key_blade_thick`, `kw1_key_bow_width`, `kw1_key_length`
- **makita** (3) — `makita_18v_bat_lxt_5ah_height`, `makita_18v_bat_lxt_5ah_length`, `makita_18v_bat_lxt_5ah_width`
- **sc1** (3) — `sc1_key_blade_thick`, `sc1_key_bow_width`, `sc1_key_length`
- **screwdriver** (3) — `screwdriver_handle_dia`, `screwdriver_overall_length`, `screwdriver_shaft_dia`
- **skadis** (3) — `skadis_grid`, `skadis_slot_height`, `skadis_slot_width`
- **tape** (3) — `tape_measure_depth`, `tape_measure_height`, `tape_measure_width`
- **torpedo** (3) — `torpedo_level_height`, `torpedo_level_length`, `torpedo_level_width`
- **utility** (3) — `utility_knife_depth`, `utility_knife_length`, `utility_knife_width`
- **cr2032** (2) — `cr2032_dia`, `cr2032_thick`
- **french** (2) — `french_cleat_angle`, `french_cleat_stock`
- **keyring** (2) — `keyring_25mm_od`, `keyring_25mm_wire_dia`
- **mdf** (2) — `mdf_half_inch_actual`, `mdf_three_quarter_inch_actual`
- **plywood** (2) — `plywood_half_inch_actual`, `plywood_three_quarter_inch_actual`
- **hex** (1) — `hex_bit_drive_af`
- **hsw** (1) — `hsw_grid`
- **wall** (1) — `wall_control_grid`

---

## `household_hobby` — 151 params  ·  _Tier 2 · per project_

drinkware, EDC, cards, coins, paint, Warhammer, foam darts, bottles, cables, storage

- **wh** (14) — `wh_base_25mm_od`, `wh_base_32mm_od`, `wh_base_40mm_od`, `wh_base_50mm_od`, `wh_base_60mm_od`, `wh_base_height`, `wh_base_slot_clearance`, `wh_flying_post_clearance_hole` … (+6 more)
- **fidget** (9) — `fidget_608_bearing_press`, `fidget_button_cap_dia`, `fidget_button_snap_height`, `fidget_button_travel`, `fidget_click_bump`, `fidget_click_pitch`, `fidget_infinity_hinge_gap`, `fidget_magnet_snap_gap` … (+1 more)
- **sata** (7) — `sata_25_height_std`, `sata_25_height_thin`, `sata_25_length`, `sata_25_width`, `sata_35_height`, `sata_35_length`, `sata_35_width`
- **bic** (6) — `bic_lighter_depth`, `bic_lighter_height`, `bic_lighter_width`, `bic_pen_hole_dia`, `bic_pen_length`, `bic_pen_width`
- **glasses** (6) — `glasses_case_height`, `glasses_case_length`, `glasses_case_width`, `glasses_folded_depth`, `glasses_folded_height`, `glasses_folded_width`
- **nerf** (6) — `nerf_flywheel_gap_half_dart_standard`, `nerf_flywheel_motor_can_worker_artifact_od`, `nerf_plunger_id_19mm`, `nerf_plunger_id_25mm`, `nerf_plunger_wall_thickness`, `nerf_spring_guide_rod_diameter_standard`
- **pill** (6) — `pill_13dram_dia`, `pill_13dram_height`, `pill_20dram_dia`, `pill_20dram_height`, `pill_30dram_dia`, `pill_30dram_height`
- **halfdart** (5) — `halfdart_barrel_performance`, `halfdart_barrel_slam_fire`, `halfdart_body_length`, `halfdart_body_outer_diameter`, `halfdart_tip_outer_diameter`
- **usb** (5) — `usb_a_plug_height`, `usb_a_plug_width`, `usb_c_cable_od`, `usb_c_plug_height`, `usb_c_plug_width`
- **credit** (4) — `credit_card_corner_radius`, `credit_card_height`, `credit_card_thick`, `credit_card_width`
- **cfexpress** (3) — `cfexpress_b_height`, `cfexpress_b_thick`, `cfexpress_b_width`
- **coffee** (3) — `coffee_mug_base_dia`, `coffee_mug_height`, `coffee_mug_top_dia`
- **fulldart** (3) — `fulldart_body_outer_diameter`, `fulldart_overall_length`, `fulldart_tip_outer_diameter`
- **gopro** (3) — `gopro_mount_finger_gap`, `gopro_mount_screw_dia`, `gopro_mount_tab_thick`
- **gopro12** (3) — `gopro12_depth`, `gopro12_height`, `gopro12_width`
- **microsd** (3) — `microsd_length`, `microsd_thick`, `microsd_width`
- **nalgene** (3) — `nalgene_32oz_body_dia`, `nalgene_32oz_height`, `nalgene_32oz_mouth_dia`
- **samsung** (3) — `samsung_t7_depth`, `samsung_t7_height`, `samsung_t7_width`
- **sd** (3) — `sd_card_length`, `sd_card_thick`, `sd_card_width`
- **wd** (3) — `wd_passport_depth`, `wd_passport_height`, `wd_passport_width`
- **zippo** (3) — `zippo_depth`, `zippo_height`, `zippo_width`
- **army** (2) — `army_painter_dia`, `army_painter_height`
- **audio** (2) — `audio_35mm_barrel_length`, `audio_35mm_plug_dia`
- **business** (2) — `business_card_height`, `business_card_width`
- **chapstick** (2) — `chapstick_dia`, `chapstick_height`
- **citadel** (2) — `citadel_pot_dia`, `citadel_pot_height`
- **craft** (2) — `craft_paint_2oz_dia`, `craft_paint_2oz_height`
- **dime** (2) — `dime_dia`, `dime_thick`
- **dollar** (2) — `dollar_coin_dia`, `dollar_coin_thick`
- **dp** (2) — `dp_plug_height`, `dp_plug_width`
- **drink** (2) — `drink_max_body_dia`, `drink_max_height`
- **eyedrop** (2) — `eyedrop_15ml_dia`, `eyedrop_15ml_height`
- **half** (2) — `half_dollar_dia`, `half_dollar_thick`
- **hdmi** (2) — `hdmi_plug_height`, `hdmi_plug_width`
- **hydroflask32oz** (2) — `hydroflask32oz_body_dia`, `hydroflask32oz_height`
- **nickel** (2) — `nickel_dia`, `nickel_thick`
- **penny** (2) — `penny_dia`, `penny_thick`
- **poker** (2) — `poker_card_height`, `poker_card_width`
- **quarter** (2) — `quarter_dia`, `quarter_thick`
- **rj45** (2) — `rj45_plug_height`, `rj45_plug_width`
- **sharpie** (2) — `sharpie_barrel_dia`, `sharpie_length`
- **stanley40oz** (2) — `stanley40oz_base_dia`, `stanley40oz_height`
- **vallejo** (2) — `vallejo_dropper_dia`, `vallejo_dropper_height`
- **yeti20oz** (2) — `yeti20oz_height`, `yeti20oz_lip_dia`
- **yeti30oz** (2) — `yeti30oz_height`, `yeti30oz_lip_dia`
- **lightning** (1) — `lightning_cable_od`
- **spray** (1) — `spray_28_400_neck_od`

---

## `imperial_drills` — 64 params  ·  _Tier 3 · specialized_

fractional drill bit table (1/64" to 1")

- **drill** (64) — `drill_1`, `drill_11_16`, `drill_11_32`, `drill_11_64`, `drill_13_16`, `drill_13_32`, `drill_13_64`, `drill_15_16` … (+56 more)

---

## `wood_screws` — 80 params  ·  _Tier 3 · specialized_

gauges #0-#20 with pilot/clearance/countersink

- **ws10** (5) — `ws10_clearance`, `ws10_csink_dia`, `ws10_major_dia`, `ws10_pilot_hard`, `ws10_pilot_soft`
- **ws11** (5) — `ws11_clearance`, `ws11_csink_dia`, `ws11_major_dia`, `ws11_pilot_hard`, `ws11_pilot_soft`
- **ws12** (5) — `ws12_clearance`, `ws12_csink_dia`, `ws12_major_dia`, `ws12_pilot_hard`, `ws12_pilot_soft`
- **ws14** (5) — `ws14_clearance`, `ws14_csink_dia`, `ws14_major_dia`, `ws14_pilot_hard`, `ws14_pilot_soft`
- **ws2** (5) — `ws2_clearance`, `ws2_csink_dia`, `ws2_major_dia`, `ws2_pilot_hard`, `ws2_pilot_soft`
- **ws3** (5) — `ws3_clearance`, `ws3_csink_dia`, `ws3_major_dia`, `ws3_pilot_hard`, `ws3_pilot_soft`
- **ws4** (5) — `ws4_clearance`, `ws4_csink_dia`, `ws4_major_dia`, `ws4_pilot_hard`, `ws4_pilot_soft`
- **ws5** (5) — `ws5_clearance`, `ws5_csink_dia`, `ws5_major_dia`, `ws5_pilot_hard`, `ws5_pilot_soft`
- **ws6** (5) — `ws6_clearance`, `ws6_csink_dia`, `ws6_major_dia`, `ws6_pilot_hard`, `ws6_pilot_soft`
- **ws7** (5) — `ws7_clearance`, `ws7_csink_dia`, `ws7_major_dia`, `ws7_pilot_hard`, `ws7_pilot_soft`
- **ws8** (5) — `ws8_clearance`, `ws8_csink_dia`, `ws8_major_dia`, `ws8_pilot_hard`, `ws8_pilot_soft`
- **ws9** (5) — `ws9_clearance`, `ws9_csink_dia`, `ws9_major_dia`, `ws9_pilot_hard`, `ws9_pilot_soft`
- **ws0** (4) — `ws0_clearance`, `ws0_major_dia`, `ws0_pilot_hard`, `ws0_pilot_soft`
- **ws1** (4) — `ws1_clearance`, `ws1_major_dia`, `ws1_pilot_hard`, `ws1_pilot_soft`
- **ws16** (4) — `ws16_clearance`, `ws16_major_dia`, `ws16_pilot_hard`, `ws16_pilot_soft`
- **ws18** (4) — `ws18_clearance`, `ws18_major_dia`, `ws18_pilot_hard`, `ws18_pilot_soft`
- **ws20** (4) — `ws20_clearance`, `ws20_major_dia`, `ws20_pilot_hard`, `ws20_pilot_soft`

---

## Coverage gaps (not yet in the set)

Candidates to add when a project needs them — recorded so we don't re-research the same gaps.

- **Batteries:** Ryobi ONE+, Bosch 18V, Milwaukee M12, DeWalt FLEXVOLT, larger XC/HO variants; C/D/9V/21700/CR123A cells; **battery dock-rail/slide interfaces (must be measured off a physical pack — not derivable from the envelope).**
- **Power tools:** jigsaws, recip saws, impact drivers/wrenches, multi-tools, routers, angle grinders; Ryobi/Bosch tool bodies.
- **Hand tools:** socket sets/ratchets, wire strippers, crimpers, clamps (bar/spring/C).
- **Wall systems:** slatwall slot profile; verify Wall Control hole size on the physical panel.
- **Devices:** Steam Deck, Switch Lite, Samsung/Garmin/Fitbit watches, more remotes (Samsung/LG/Harmony), HomePod Mini, Nest Hub.
- **Connectors/media:** Micro/Mini-USB, USB-B, CompactFlash, M.2 2230/2242, coax (RG6/RG59).
- **Hobby/household:** Tamiya/Scale75/AK paints, mason jars, essential-oil bottles, MTG/Pokemon card decks, more pill-bottle drams.

---

## Adding new parameters

1. Add rows to the master CSV (component-first names, Expression as a bare number, Value in cm — see `params/CLAUDE.md`). Scripted adds: pattern after `add_reference_dims.py`.
2. `python validate_params.py` — name format, units, duplicates, reference resolution.
3. `python split_params.py` — regenerate themed files. **New name prefix? Add it to the right `*_PREFIXES` set first**, or it silently falls into `design_rules`.
4. `python gen_reference.py` — regenerate this file.
5. Upload changed split CSVs to Admin Project > Parameters in Fusion; commit the submodule.
