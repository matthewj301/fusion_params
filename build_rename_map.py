"""
build_rename_map.py
Reads the master Fusion parameter CSV and generates:
  - migration_mapping.csv  (old_name,new_name)
  - Updated expressions using new names (printed as summary)

Run: python params/build_rename_map.py
"""

import csv
import re
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
REPO_ROOT = Path(__file__).parent.parent
PARAMS_DIR = Path(__file__).parent
CSV_IN = PARAMS_DIR / "BakedBean3D_MasterParams_v4" / "BakedBean3D_MasterParams_params.csv"
MAPPING_OUT = PARAMS_DIR / "migration_mapping.csv"

# ---------------------------------------------------------------------------
# Params to skip entirely (will be deleted)
# ---------------------------------------------------------------------------
SKIP_PARAMS = {
    "electronics_m2p5_screw_clearance_hole",
    "electronics_m2p5_hex_standoff_od",
    "magnet_warhammer_base_transport_6x2_pocket_id",
}

# ---------------------------------------------------------------------------
# Renaming logic
# ---------------------------------------------------------------------------

def rename(old: str) -> str:
    """Apply all naming rules to produce a new name. Return old name if no rule matches."""

    # --- Skip bmg_ entirely (keep as-is — they'll be excluded from output) ---
    if old.startswith("bmg_"):
        return old  # caller will skip these

    # ---- Specific one-to-one renames (highest priority) ----
    EXACT = {
        "printer_accuracy_hole_shrink_compensation":          "fdm_hole_shrink",
        "printer_accuracy_outer_dimension_oversize":          "fdm_outer_oversize",
        "printer_accuracy_standard_layer_height":             "fdm_layer_height",
        "printer_accuracy_first_layer_height":                "fdm_first_layer_height",
        "printer_accuracy_extrusion_line_width":              "fdm_line_width",
        "printer_accuracy_elephant_foot_compensation":        "fdm_elephant_foot",
        "printer_accuracy_seam_zseam_protrusion":             "fdm_seam_protrusion",
        "printer_accuracy_minimum_infill_bridging_width":     "fdm_min_infill_width",
        "printer_accuracy_solid_top_layers_for_mating_surface": "fdm_solid_top_layers",
        "tolerance_standard_fine_iso2768_f":                  "tol_fine",
        "tolerance_standard_medium_iso2768_m":                "tol_medium",
        "tolerance_standard_coarse_iso2768_c":                "tol_coarse",
        "tolerance_angular_general_degrees":                  "tol_angular",
        "tolerance_fit_class_fdm_sliding_per_surface":        "fdm_sliding_fit",
        "tolerance_fit_class_fdm_press_per_surface":          "fdm_press_fit",
        "tolerance_fit_class_fdm_interference_per_surface":   "fdm_interference_fit",
        "tolerance_fit_class_iso_h7_g6_running_clearance":    "tol_h7g6_running",
        "hole_geometry_minimum_printable_diameter":           "fdm_min_hole_dia",
        "hole_geometry_horizontal_teardrop_z_offset":         "fdm_teardrop_offset",
        "hole_geometry_fdm_diameter_compensation":            "fdm_hole_compensation",
        "hole_geometry_self_tap_m3_into_plastic_diameter":    "m3_selftap_hole",
        "hole_geometry_self_tap_m4_into_plastic_diameter":    "m4_selftap_hole",
        "hole_geometry_thread_engagement_minimum_length":     "fdm_thread_engage_min",
        "hardware_dowel_pin_fdm_clearance_receiver_hole":     "fdm_dowel_clearance",
        "countersink_metric_flat_head_angle_degrees":         "countersink_angle",
        "thread_fdm_offset_face_per_flank_petg_abs":          "fdm_thread_offset_petg",
        "thread_fdm_offset_face_per_flank_pla":               "fdm_thread_offset_pla",
        "thread_fdm_addon_tolerance_profile_petg":            "fdm_thread_tol_petg",
        "thread_fdm_addon_tolerance_profile_pla":             "fdm_thread_tol_pla",
        "wall_thickness_minimum_functional_2_perimeters":     "fdm_wall_minimum",
        "wall_thickness_recommended_structural_4_perims":     "fdm_wall_structural",
        "wall_thickness_heavy_duty_6_perimeters":             "fdm_wall_heavy",
        "fillet_radius_minimum_internal_stress_relief":       "fdm_fillet_min",
        "fillet_radius_standard_external_cosmetic":           "fdm_fillet_standard",
        "fillet_radius_large_structural_gusset":              "fdm_fillet_large",
        "chamfer_depth_standard_45_degree":                   "fdm_chamfer_standard",
        "chamfer_depth_lead_in_for_pin_insertion":            "fdm_chamfer_leadin",
        "overhang_maximum_angle_from_vertical_standard":      "fdm_overhang_max",
        "overhang_maximum_angle_high_perf_cpap":              "fdm_overhang_max_cpap",
        "bridge_maximum_reliable_span_with_tuning":           "fdm_bridge_max",
        "bridge_long_span_sag_z_compensation":                "fdm_bridge_sag",
        "magnet_pocket_press_fit_clearance_per_side":         "magnet_press_fit",
        "magnet_pocket_glue_gap_clearance_per_side":          "magnet_glue_gap",
        "magnet_pocket_depth_flush_recess":                   "magnet_flush_recess",
        "motion_gt2_belt_pitch":                              "gt2_belt_pitch",
        "motion_gt2_belt_nominal_width":                      "gt2_belt_width",
        "motion_gt2_belt_clamp_slot_extra_width":             "gt2_clamp_extra",
        "motion_gt2_pulley_bore_standard_5mm_shaft":          "gt2_pulley_bore",
        "motion_gt2_idler_bearing_od_f695":                   "f695_bearing_od",
        "motion_gt2_idler_bearing_id_f695":                   "f695_bearing_id",
        "motion_gt2_idler_bearing_width_f695":                "f695_bearing_width",
        "motion_toolhead_carriage_plate_thickness_5mm":       "toolhead_plate_5mm",
        "motion_toolhead_carriage_plate_thickness_4mm":       "toolhead_plate_4mm",
        "cnc_aluminum_6061_stock_plate_thickness_tolerance":  "cnc_plate_tolerance",
        "cnc_aluminum_drilled_hole_oversize":                 "cnc_drilled_oversize",
        "cnc_aluminum_reamed_hole_h7_tolerance_at_5mm":       "cnc_h7_ream_tol",
        "cnc_aluminum_thread_engagement_minimum_diameter_ratio": "cnc_thread_engage_min_ratio",
        "cnc_aluminum_thread_engagement_recommended_ratio":   "cnc_thread_engage_rec_ratio",
        "cnc_aluminum_minimum_wall_for_tapped_hole":          "cnc_min_wall_tap",
        "cnc_aluminum_countersink_m3_flat_head_4mm_plate":    "cnc_m3_csink_4mm",
        "cnc_aluminum_countersink_m3_flat_head_5mm_plate":    "cnc_m3_csink_5mm",
        "cnc_aluminum_pocket_depth_tolerance_typical_service": "cnc_pocket_depth_tol",
        "cnc_aluminum_press_fit_pin_h7_in_6061_5mm":          "cnc_5mm_press_fit_pin",
        "cnc_aluminum_6061_thermal_expansion_per_degree_c":   "cnc_thermal_expansion",
        "material_pla_print_shrink_percent":                  "pla_shrink",
        "material_petg_print_shrink_percent":                 "petg_shrink",
        "material_abs_print_shrink_percent":                  "abs_shrink",
        "material_asa_print_shrink_percent":                  "asa_shrink",
        "material_abs_minimum_chamber_temp_celsius":          "abs_chamber_temp",
        "material_pc_minimum_chamber_temp_celsius":           "pc_chamber_temp",
        "material_tpu_95a_shore_hardness":                    "tpu_95a_hardness",
        "material_tpu_85a_shore_hardness":                    "tpu_85a_hardness",
        "material_6061_fdm_diff_expansion_per_deg_c":         "fdm_6061_diff_expansion",
        "electronics_raspberry_pi_4_5_mount_hole_pitch_x":    "rpi4_mount_pitch_x",
        "electronics_raspberry_pi_4_5_mount_hole_pitch_y":    "rpi4_mount_pitch_y",
        "electronics_raspberry_pi_board_width":               "rpi_board_width",
        "electronics_raspberry_pi_board_length":              "rpi_board_length",
        "electronics_btt_octopus_mount_hole_pitch_x":         "octopus_mount_pitch_x",
        "electronics_btt_octopus_mount_hole_pitch_y":         "octopus_mount_pitch_y",
        "electronics_btt_skr_mini_e3_mount_hole_pitch_x":     "skr_mini_mount_pitch_x",
        "electronics_btt_skr_mini_e3_mount_hole_pitch_y":     "skr_mini_mount_pitch_y",
        "electronics_pcb_edge_clearance_to_wall_minimum":     "pcb_edge_clearance",
        "electronics_din_rail_standard_width":                "din_rail_width",
        "electronics_din_rail_clip_engagement_depth":         "din_rail_clip_depth",
        "electronics_jst_xh_2p54_connector_body_width_2pin":  "jst_xh_2pin_width",
        "electronics_jst_xh_2p54_connector_body_height":      "jst_xh_height",
        "electronics_usb_a_panel_cutout_width":               "usb_a_panel_width",
        "electronics_usb_a_panel_cutout_height":              "usb_a_panel_height",
        "electronics_usb_c_panel_cutout_width":               "usb_c_panel_width",
        "electronics_usb_c_panel_cutout_height":              "usb_c_panel_height",
        "electronics_xt30_panel_cutout_diameter":             "xt30_panel_dia",
        "electronics_xt60_panel_cutout_diameter":             "xt60_panel_dia",
        "electronics_esp32_devkit_board_width":               "esp32_board_width",
        "electronics_esp32_devkit_board_length":              "esp32_board_length",
        "electronics_d1_mini_esp8266_board_width":            "d1mini_board_width",
        "electronics_d1_mini_esp8266_board_length":           "d1mini_board_length",
        "home_auto_us_single_gang_box_internal_width":        "gang_box_internal_width",
        "home_auto_us_single_gang_box_internal_height":       "gang_box_internal_height",
        "home_auto_us_decora_faceplate_cutout_width":         "decora_cutout_width",
        "home_auto_us_decora_faceplate_cutout_height":        "decora_cutout_height",
        "home_auto_conduit_half_inch_knockout_diameter":      "conduit_half_inch_knockout_dia",
        "home_auto_conduit_three_quarter_inch_knockout_dia":  "conduit_three_quarter_inch_knockout_dia",
        "home_auto_sonoff_zbdongle_p_body_width":             "sonoff_zbdongle_p_width",
        "home_auto_sonoff_zbdongle_p_body_length":            "sonoff_zbdongle_p_length",
        "print_in_place_captive_sphere_clearance":            "pip_sphere_clearance",
        "print_in_place_captive_sphere_min_diameter":         "pip_sphere_min_dia",
        "print_in_place_hinge_pin_clearance":                 "pip_hinge_clearance",
        "print_in_place_socket_opening_ratio":                "pip_socket_ratio",
        "dovetail_angle_deg":                                 "dovetail_angle",
        "dovetail_width_base_mm":                             "dovetail_base_width",
        "dovetail_width_top_mm":                              "dovetail_top_width",
        "dovetail_depth_mm":                                  "dovetail_depth",
        "dovetail_clearance_per_surface_mm":                  "dovetail_clearance",
        "dovetail_slide_entry_chamfer_mm":                    "dovetail_chamfer",
        "spring_clip_arm_thickness_mm":                       "spring_clip_thick",
        "spring_clip_arm_width_mm":                           "spring_clip_width",
        "spring_clip_deflection_max_mm":                      "spring_clip_max_flex",
        "spring_clip_hook_depth_mm":                          "spring_clip_hook_depth",
        "container_wall_thickness_food_safe_mm":              "container_wall",
        "container_base_thickness_mm":                        "container_base",
        "container_corner_radius_min_mm":                     "container_corner_r",
        "container_lid_rim_width_mm":                         "container_rim_width",
        "warhammer_base_slot_clearance_fdm":                  "wh_base_slot_clearance",
        "warhammer_base_height_standard":                     "wh_base_height",
        "warhammer_magnetization_base_6x2mm_pocket_id":       "wh_magnet_6x2_pocket_id",
        "warhammer_magnetization_base_6x2mm_pocket_depth":    "wh_magnet_6x2_pocket_depth",
        "warhammer_kill_team_tile_standard_size":             "wh_kilteam_tile_standard_size",
        "warhammer_flying_stand_post_diameter":               "wh_flying_post_diameter",
        "warhammer_flying_stand_post_clearance_hole":         "wh_flying_post_clearance_hole",
        "charger_magsafe_15w_dia":                            "magsafe15w_dia",
        "charger_magsafe_15w_thick":                          "magsafe15w_thick",
        "charger_magsafe_25w_dia":                            "magsafe25w_dia",
        "charger_magsafe_25w_thick":                          "magsafe25w_thick",
        "charger_apple_watch_dia":                            "applewatch_charger_dia",
        "charger_apple_watch_thick":                          "applewatch_charger_thick",
        "phone_case_allowance":                               "phone_case_allowance",
        "phone_universal_cased_width":                        "phone_cased_width",
        "phone_universal_cased_depth":                        "phone_cased_depth",
        "phone_universal_max_height":                         "phone_max_height",
        "phone_universal_max_width":                          "phone_max_width",
        "phone_universal_max_depth":                          "phone_max_depth",
        "tablet_universal_max_height":                        "tablet_max_height",
        "tablet_universal_max_width":                         "tablet_max_width",
        "tablet_universal_max_depth":                         "tablet_max_depth",
        "drinkware_max_body_dia":                             "drink_max_body_dia",
        "drinkware_max_height":                               "drink_max_height",
        "controller_universal_max_width":                     "controller_max_width",
        "controller_universal_max_height":                    "controller_max_height",
        "controller_universal_max_depth":                     "controller_max_depth",
        "edc_bic_pen_body_width":                             "bic_pen_width",
        "edc_bic_pen_length":                                 "bic_pen_length",
        "edc_bic_pen_circular_hole_dia":                      "bic_pen_hole_dia",
        "edc_sharpie_barrel_dia":                             "sharpie_barrel_dia",
        "edc_sharpie_length":                                 "sharpie_length",
        "edc_chapstick_dia":                                  "chapstick_dia",
        "edc_chapstick_height":                               "chapstick_height",
        "edc_bic_lighter_width":                              "bic_lighter_width",
        "edc_bic_lighter_height":                             "bic_lighter_height",
        "edc_bic_lighter_depth":                              "bic_lighter_depth",
        "edc_zippo_width":                                    "zippo_width",
        "edc_zippo_height":                                   "zippo_height",
        "edc_zippo_depth":                                    "zippo_depth",
        "audio_airpods_pro_2_case_width":                     "airpods_pro2_width",
        "audio_airpods_pro_2_case_height":                    "airpods_pro2_height",
        "audio_airpods_pro_2_case_depth":                     "airpods_pro2_depth",
        "card_credit_width":                                  "credit_card_width",
        "card_credit_height":                                 "credit_card_height",
        "card_credit_thick":                                  "credit_card_thick",
        "card_credit_corner_radius":                          "credit_card_corner_radius",
        "card_business_width":                                "business_card_width",
        "card_business_height":                               "business_card_height",
        "card_playing_poker_width":                           "poker_card_width",
        "card_playing_poker_height":                          "poker_card_height",
        "coin_us_penny_dia":                                  "penny_dia",
        "coin_us_penny_thick":                                "penny_thick",
        "coin_us_nickel_dia":                                 "nickel_dia",
        "coin_us_nickel_thick":                               "nickel_thick",
        "coin_us_dime_dia":                                   "dime_dia",
        "coin_us_dime_thick":                                 "dime_thick",
        "coin_us_quarter_dia":                                "quarter_dia",
        "coin_us_quarter_thick":                              "quarter_thick",
        "coin_us_half_dollar_dia":                            "half_dollar_dia",
        "coin_us_half_dollar_thick":                          "half_dollar_thick",
        "coin_us_dollar_dia":                                 "dollar_coin_dia",
        "coin_us_dollar_thick":                               "dollar_coin_thick",
        "cable_usb_c_cable_od":                               "usb_c_cable_od",
        "cable_lightning_cable_od":                           "lightning_cable_od",
        "cable_hdmi_plug_width":                              "hdmi_plug_width",
        "cable_hdmi_plug_height":                             "hdmi_plug_height",
        "cable_displayport_plug_width":                       "dp_plug_width",
        "cable_displayport_plug_height":                      "dp_plug_height",
        "cable_rj45_plug_width":                              "rj45_plug_width",
        "cable_rj45_plug_height":                             "rj45_plug_height",
        "cable_audio_35mm_plug_dia":                          "audio_35mm_plug_dia",
        "cable_audio_35mm_barrel_length":                     "audio_35mm_barrel_length",
        "connector_usb_a_plug_width":                         "usb_a_plug_width",
        "connector_usb_a_plug_height":                        "usb_a_plug_height",
        "connector_usb_c_plug_width":                         "usb_c_plug_width",
        "connector_usb_c_plug_height":                        "usb_c_plug_height",
        "connector_sd_card_width":                            "sd_card_width",
        "connector_sd_card_length":                           "sd_card_length",
        "connector_sd_card_thick":                            "sd_card_thick",
        "connector_microsd_width":                            "microsd_width",
        "connector_microsd_length":                           "microsd_length",
        "connector_microsd_thick":                            "microsd_thick",
        "pegboard_std_hole_dia":                              "pegboard_hole_dia",
        "pegboard_std_hole_spacing":                          "pegboard_hole_spacing",
        "pegboard_std_thickness":                             "pegboard_thickness",
        "pegboard_std_hook_wire_dia":                         "pegboard_hook_wire_dia",
        "pegboard_small_hole_dia":                            "pegboard_small_hole_dia",
        "pegboard_small_thickness":                           "pegboard_small_thickness",
        "pegboard_light_hook_wire_dia":                       "pegboard_light_hook_dia",
        "key_kw1_length":                                     "kw1_key_length",
        "key_kw1_bow_width":                                  "kw1_key_bow_width",
        "key_kw1_blade_thick":                                "kw1_key_blade_thick",
        "key_sc1_length":                                     "sc1_key_length",
        "key_sc1_bow_width":                                  "sc1_key_bow_width",
        "key_sc1_blade_thick":                                "sc1_key_blade_thick",
        "key_split_ring_25mm_od":                             "keyring_25mm_od",
        "key_split_ring_25mm_wire_dia":                       "keyring_25mm_wire_dia",
        "smarthome_echo_dot_5_dia":                           "echo_dot5_dia",
        "smarthome_echo_dot_5_height":                        "echo_dot5_height",
        "smarthome_nest_mini_2_dia":                          "nest_mini2_dia",
        "smarthome_nest_mini_2_height":                       "nest_mini2_height",
        "smarthome_echo_show_5_width":                        "echo_show5_width",
        "smarthome_echo_show_5_height":                       "echo_show5_height",
        "smarthome_echo_show_5_depth":                        "echo_show5_depth",
        "smarthome_kasa_ep10_width":                          "kasa_ep10_width",
        "smarthome_kasa_ep10_height":                         "kasa_ep10_height",
        "smarthome_kasa_ep10_depth":                          "kasa_ep10_depth",
        "smarthome_hue_bridge_width":                         "hue_bridge_width",
        "smarthome_hue_bridge_height":                        "hue_bridge_height",
        "watch_band_width_20mm":                              "watch_band_20",
        "watch_band_width_22mm":                              "watch_band_22",
        "camera_gopro_mount_finger_gap":                      "gopro_mount_finger_gap",
        "camera_gopro_mount_tab_thick":                       "gopro_mount_tab_thick",
        "camera_gopro_mount_screw_dia":                       "gopro_mount_screw_dia",
        "camera_security_tripod_mount_thread_dia":            "tripod_mount_thread_dia",
        "camera_security_tripod_mount_thread_pitch":          "tripod_mount_thread_pitch",
        "battery_aa_holder_slot_dia":                         "aa_holder_slot_dia",
        "battery_aaa_holder_slot_dia":                        "aaa_holder_slot_dia",
        "battery_18650_holder_slot_dia":                      "bat_18650_holder_slot_dia",
    }

    if old in EXACT:
        return EXACT[old]

    # ---- Pattern-based renames ----

    # hole_geometry_m{X}_screw_clearance_diameter → m{X}_thru_hole
    m = re.fullmatch(r"hole_geometry_(m\d+p?\d*)_screw_clearance_diameter", old)
    if m:
        return f"{m.group(1)}_thru_hole"

    # hole_geometry_m{X}_close_fit_diameter → m{X}_close_fit_hole
    m = re.fullmatch(r"hole_geometry_(m\d+p?\d*)_close_fit_diameter", old)
    if m:
        return f"{m.group(1)}_close_fit_hole"

    # boss_geometry_m{X}_outer_diameter → m{X}_boss_od
    m = re.fullmatch(r"boss_geometry_(m\d+p?\d*)_outer_diameter", old)
    if m:
        return f"{m.group(1)}_boss_od"

    # heatset_insert_m{X}_recommended_hole_id → m{X}_heatset_hole
    m = re.fullmatch(r"heatset_insert_(m\d+p?\d*)_recommended_hole_id", old)
    if m:
        return f"{m.group(1)}_heatset_hole"

    # heatset_insert_m{X}_recess_depth → m{X}_heatset_depth
    m = re.fullmatch(r"heatset_insert_(m\d+p?\d*)_recess_depth", old)
    if m:
        return f"{m.group(1)}_heatset_depth"

    # heatset_insert_m{X}_boss_outer_diameter → m{X}_heatset_boss_od
    m = re.fullmatch(r"heatset_insert_(m\d+p?\d*)_boss_outer_diameter", old)
    if m:
        return f"{m.group(1)}_heatset_boss_od"

    # heatset_insert_install_temp_{material}_celsius → heatset_temp_{material}
    m = re.fullmatch(r"heatset_insert_install_temp_(.+)_celsius", old)
    if m:
        return f"heatset_temp_{m.group(1)}"

    # hardware_m{X}_button_head_iso7380_head_diameter → m{X}_button_head_dia
    m = re.fullmatch(r"hardware_(m\d+p?\d*)_button_head_iso7380_head_diameter", old)
    if m:
        return f"{m.group(1)}_button_head_dia"

    # hardware_m{X}_button_head_iso7380_head_height → m{X}_button_head_height
    m = re.fullmatch(r"hardware_(m\d+p?\d*)_button_head_iso7380_head_height", old)
    if m:
        return f"{m.group(1)}_button_head_height"

    # hardware_m{X}_socket_cap_din912_head_diameter → m{X}_socket_head_dia
    m = re.fullmatch(r"hardware_(m\d+p?\d*)_socket_cap_din912_head_diameter", old)
    if m:
        return f"{m.group(1)}_socket_head_dia"

    # hardware_m{X}_socket_cap_din912_head_height → m{X}_socket_head_height
    m = re.fullmatch(r"hardware_(m\d+p?\d*)_socket_cap_din912_head_height", old)
    if m:
        return f"{m.group(1)}_socket_head_height"

    # hardware_m{X}_flat_head_din7991_head_diameter → m{X}_flat_head_dia
    m = re.fullmatch(r"hardware_(m\d+p?\d*)_flat_head_din7991_head_diameter", old)
    if m:
        return f"{m.group(1)}_flat_head_dia"

    # hardware_m{X}_flat_head_din7991_head_height → m{X}_flat_head_height
    m = re.fullmatch(r"hardware_(m\d+p?\d*)_flat_head_din7991_head_height", old)
    if m:
        return f"{m.group(1)}_flat_head_height"

    # hardware_m{X}_hex_nut_iso4032_across_flats → m{X}_hex_nut_af
    m = re.fullmatch(r"hardware_(m\d+p?\d*)_hex_nut_iso4032_across_flats", old)
    if m:
        return f"{m.group(1)}_hex_nut_af"

    # hardware_m{X}_hex_nut_iso4032_height → m{X}_hex_nut_height
    m = re.fullmatch(r"hardware_(m\d+p?\d*)_hex_nut_iso4032_height", old)
    if m:
        return f"{m.group(1)}_hex_nut_height"

    # hardware_m{X}_square_nut_din557_width → m{X}_square_nut_width
    m = re.fullmatch(r"hardware_(m\d+p?\d*)_square_nut_din557_width", old)
    if m:
        return f"{m.group(1)}_square_nut_width"

    # hardware_m{X}_square_nut_din557_height → m{X}_square_nut_height
    m = re.fullmatch(r"hardware_(m\d+p?\d*)_square_nut_din557_height", old)
    if m:
        return f"{m.group(1)}_square_nut_height"

    # hardware_m{X}_washer_iso7089_outer_diameter → m{X}_washer_od
    m = re.fullmatch(r"hardware_(m\d+p?\d*)_washer_iso7089_outer_diameter", old)
    if m:
        return f"{m.group(1)}_washer_od"

    # hardware_m{X}_washer_iso7089_thickness → m{X}_washer_thick
    m = re.fullmatch(r"hardware_(m\d+p?\d*)_washer_iso7089_thickness", old)
    if m:
        return f"{m.group(1)}_washer_thick"

    # hardware_dowel_pin_m{X}_nominal_diameter_h6 → m{X}_dowel_pin_dia
    m = re.fullmatch(r"hardware_dowel_pin_(m\d+p?\d*)_nominal_diameter_h6", old)
    if m:
        return f"{m.group(1)}_dowel_pin_dia"

    # hardware_m{X}_hex_standoff_outer_diameter → m{X}_standoff_od
    m = re.fullmatch(r"hardware_(m\d+p?\d*)_hex_standoff_outer_diameter", old)
    if m:
        return f"{m.group(1)}_standoff_od"

    # hardware_zip_tie_{size}_slot_width → ziptie_{size}_width
    m = re.fullmatch(r"hardware_zip_tie_(.+)_slot_width", old)
    if m:
        return f"ziptie_{m.group(1)}_width"

    # hardware_zip_tie_{size}_slot_thickness → ziptie_{size}_thick
    m = re.fullmatch(r"hardware_zip_tie_(.+)_slot_thickness", old)
    if m:
        return f"ziptie_{m.group(1)}_thick"

    # hardware_m{X}_grub_screw_common_length_mm → m{X}_grub_length
    m = re.fullmatch(r"hardware_(m\d+p?\d*)_grub_screw_common_length_mm", old)
    if m:
        return f"{m.group(1)}_grub_length"

    # nut_trap_m{X}_hex_pocket_across_flats_fdm → m{X}_nut_pocket_af
    m = re.fullmatch(r"nut_trap_(m\d+p?\d*)_hex_pocket_across_flats_fdm", old)
    if m:
        return f"{m.group(1)}_nut_pocket_af"

    # nut_trap_m{X}_hex_pocket_depth_fdm → m{X}_nut_pocket_depth
    m = re.fullmatch(r"nut_trap_(m\d+p?\d*)_hex_pocket_depth_fdm", old)
    if m:
        return f"{m.group(1)}_nut_pocket_depth"

    # nut_trap_m{X}_hex_circumscribed_diameter_fdm → m{X}_nut_pocket_circum
    m = re.fullmatch(r"nut_trap_(m\d+p?\d*)_hex_circumscribed_diameter_fdm", old)
    if m:
        return f"{m.group(1)}_nut_pocket_circum"

    # nut_trap_m{X}_square_pocket_width_fdm → m{X}_sq_nut_pocket_width
    m = re.fullmatch(r"nut_trap_(m\d+p?\d*)_square_pocket_width_fdm", old)
    if m:
        return f"{m.group(1)}_sq_nut_pocket_width"

    # nut_trap_m{X}_square_pocket_depth_fdm → m{X}_sq_nut_pocket_depth
    m = re.fullmatch(r"nut_trap_(m\d+p?\d*)_square_pocket_depth_fdm", old)
    if m:
        return f"{m.group(1)}_sq_nut_pocket_depth"

    # counterbore_m{X}_button_head_pocket_diameter → m{X}_button_cbore_dia
    m = re.fullmatch(r"counterbore_(m\d+p?\d*)_button_head_pocket_diameter", old)
    if m:
        return f"{m.group(1)}_button_cbore_dia"

    # counterbore_m{X}_button_head_pocket_depth → m{X}_button_cbore_depth
    m = re.fullmatch(r"counterbore_(m\d+p?\d*)_button_head_pocket_depth", old)
    if m:
        return f"{m.group(1)}_button_cbore_depth"

    # counterbore_m{X}_socket_cap_pocket_diameter → m{X}_socket_cbore_dia
    m = re.fullmatch(r"counterbore_(m\d+p?\d*)_socket_cap_pocket_diameter", old)
    if m:
        return f"{m.group(1)}_socket_cbore_dia"

    # counterbore_m{X}_socket_cap_pocket_depth → m{X}_socket_cbore_depth
    m = re.fullmatch(r"counterbore_(m\d+p?\d*)_socket_cap_pocket_depth", old)
    if m:
        return f"{m.group(1)}_socket_cbore_depth"

    # countersink_m{X}_flat_head_top_diameter → m{X}_countersink_dia
    m = re.fullmatch(r"countersink_(m\d+p?\d*)_flat_head_top_diameter", old)
    if m:
        return f"{m.group(1)}_countersink_dia"

    # thread_iso_metric_pitch_m{X} → m{X}_thread_pitch
    m = re.fullmatch(r"thread_iso_metric_pitch_(m\d+p?\d*)", old)
    if m:
        return f"{m.group(1)}_thread_pitch"

    # magnet_disc_{size}_outer_diameter → magnet_{size}_od
    m = re.fullmatch(r"magnet_disc_(.+)_outer_diameter", old)
    if m:
        return f"magnet_{m.group(1)}_od"

    # magnet_disc_{size}_height → magnet_{size}_height
    m = re.fullmatch(r"magnet_disc_(.+)_height", old)
    if m:
        return f"magnet_{m.group(1)}_height"

    # motion_mgn{X}_rail_nominal_width → mgn{X}_rail_width
    m = re.fullmatch(r"motion_(mgn\d+[a-z]*)_rail_nominal_width", old)
    if m:
        return f"{m.group(1)}_rail_width"

    # motion_mgn{X}_carriage_block_length → mgn{X}_carriage_length
    m = re.fullmatch(r"motion_(mgn\d+[a-z]*)_carriage_block_length", old)
    if m:
        return f"{m.group(1)}_carriage_length"

    # motion_mgn{X}_carriage_hole_pitch_along_rail → mgn{X}_pitch_along
    m = re.fullmatch(r"motion_(mgn\d+[a-z]*)_carriage_hole_pitch_along_rail", old)
    if m:
        return f"{m.group(1)}_pitch_along"

    # motion_mgn{X}_carriage_hole_pitch_across_rail → mgn{X}_pitch_across
    m = re.fullmatch(r"motion_(mgn\d+[a-z]*)_carriage_hole_pitch_across_rail", old)
    if m:
        return f"{m.group(1)}_pitch_across"

    # motion_gt2_pulley_{size}_outer_diameter → gt2_pulley_{size}_od
    m = re.fullmatch(r"motion_gt2_pulley_(.+)_outer_diameter", old)
    if m:
        return f"gt2_pulley_{m.group(1)}_od"

    # motion_nema17_motor_* → nema17_* (drop motion_ and _motor_)
    m = re.fullmatch(r"motion_(nema17)_motor_(.*)", old)
    if m:
        return f"{m.group(1)}_{m.group(2)}"

    # motion_nema14_motor_* → nema14_*
    m = re.fullmatch(r"motion_(nema14)_motor_(.*)", old)
    if m:
        return f"{m.group(1)}_{m.group(2)}"

    # motion_vslot_* → vslot_*
    m = re.fullmatch(r"motion_(vslot_.*)", old)
    if m:
        return m.group(1)

    # motion_tslot_* → tslot_*
    m = re.fullmatch(r"motion_(tslot_.*)", old)
    if m:
        return m.group(1)

    # motion_beacon_* → beacon_*
    m = re.fullmatch(r"motion_(beacon_.*)", old)
    if m:
        return m.group(1)

    # motion_orbiter_* → orbiter_*
    m = re.fullmatch(r"motion_(orbiter_.*)", old)
    if m:
        return m.group(1)

    # motion_chube_* → chube_*
    m = re.fullmatch(r"motion_(chube_.*)", old)
    if m:
        return m.group(1)

    # motion_can_bus_* → canbus_*
    m = re.fullmatch(r"motion_can_bus_(.*)", old)
    if m:
        return f"canbus_{m.group(1)}"

    # cnc_aluminum_tap_drill_m{X}_diameter → cnc_m{X}_tap_drill
    m = re.fullmatch(r"cnc_aluminum_tap_drill_(m\d+p?\d*)_diameter", old)
    if m:
        return f"cnc_{m.group(1)}_tap_drill"

    # cnc_aluminum_* → cnc_* (general drop of aluminum_)
    m = re.fullmatch(r"cnc_aluminum_(.*)", old)
    if m:
        return f"cnc_{m.group(1)}"

    # warhammer_base_{size}_outer_diameter → wh_base_{size}_od
    m = re.fullmatch(r"warhammer_base_(\d+mm)_outer_diameter", old)
    if m:
        return f"wh_base_{m.group(1)}_od"

    # warhammer_terrain_* → wh_terrain_*
    m = re.fullmatch(r"warhammer_terrain_(.*)", old)
    if m:
        return f"wh_terrain_{m.group(1)}"

    # warhammer_kill_team_* → wh_kilteam_*
    m = re.fullmatch(r"warhammer_kill_team_(.*)", old)
    if m:
        return f"wh_kilteam_{m.group(1)}"

    # warhammer_flying_stand_* → wh_flying_*
    m = re.fullmatch(r"warhammer_flying_stand_(.*)", old)
    if m:
        return f"wh_flying_{m.group(1)}"

    # foam_dart_half_dart_* → halfdart_*
    m = re.fullmatch(r"foam_dart_half_dart_(.*)", old)
    if m:
        return f"halfdart_{m.group(1)}"

    # foam_dart_full_dart_* → fulldart_*
    m = re.fullmatch(r"foam_dart_full_dart_(.*)", old)
    if m:
        return f"fulldart_{m.group(1)}"

    # foam_dart_barrel_bore_half_dart_* → halfdart_barrel_*
    m = re.fullmatch(r"foam_dart_barrel_bore_half_dart_(.*)", old)
    if m:
        return f"halfdart_barrel_{m.group(1)}"

    # foam_dart_flywheel_* → nerf_flywheel_*
    m = re.fullmatch(r"foam_dart_flywheel_(.*)", old)
    if m:
        return f"nerf_flywheel_{m.group(1)}"

    # foam_dart_spring_guide_* → nerf_spring_guide_*
    m = re.fullmatch(r"foam_dart_spring_guide_(.*)", old)
    if m:
        return f"nerf_spring_guide_{m.group(1)}"

    # foam_dart_plunger_tube_* → nerf_plunger_*
    m = re.fullmatch(r"foam_dart_plunger_tube_(.*)", old)
    if m:
        return f"nerf_plunger_{m.group(1)}"

    # phone_iphone_* → iphone*_  (collapse underscores in model name)
    m = re.fullmatch(r"phone_(iphone_\d+(?:_pro(?:_max)?)?)_(.*)", old)
    if m:
        model = m.group(1).replace("_", "")  # iphone16promax
        suffix = m.group(2)
        return f"{model}_{suffix}"

    # phone_galaxy_s24_plus_* → galaxys24plus_*
    m = re.fullmatch(r"phone_(galaxy_s\d+)_(plus|ultra)_(.*)", old)
    if m:
        model = m.group(1).replace("_", "") + m.group(2)  # galaxys24plus
        suffix = m.group(3)
        return f"{model}_{suffix}"

    # phone_galaxy_s24_* (base) → galaxys24_*
    m = re.fullmatch(r"phone_(galaxy_s\d+)_(.*)", old)
    if m:
        model = m.group(1).replace("_", "")  # galaxys24
        suffix = m.group(2)
        return f"{model}_{suffix}"

    # tablet_ipad_air_11_* → ipadair11_*
    m = re.fullmatch(r"tablet_(ipad_air_\d+)_(.*)", old)
    if m:
        model = m.group(1).replace("_", "")  # ipadair11
        return f"{model}_{m.group(2)}"

    # tablet_ipad_pro_11_* → ipadpro11_*
    # tablet_ipad_pro_13_* → ipadpro13_*
    m = re.fullmatch(r"tablet_(ipad_pro_\d+)_(.*)", old)
    if m:
        model = m.group(1).replace("_", "")  # ipadpro11 / ipadpro13
        return f"{model}_{m.group(2)}"

    # tablet_ipad_mini_7_* → ipadmini7_*
    m = re.fullmatch(r"tablet_(ipad_mini_\d+)_(.*)", old)
    if m:
        model = m.group(1).replace("_", "")  # ipadmini7
        return f"{model}_{m.group(2)}"

    # drinkware_coffee_mug_std_* → coffee_mug_*
    m = re.fullmatch(r"drinkware_coffee_mug_std_(.*)", old)
    if m:
        return f"coffee_mug_{m.group(1)}"

    # drinkware_yeti_rambler_20oz_* → yeti20oz_*
    m = re.fullmatch(r"drinkware_yeti_rambler_20oz_(.*)", old)
    if m:
        return f"yeti20oz_{m.group(1)}"

    # drinkware_yeti_rambler_30oz_* → yeti30oz_*
    m = re.fullmatch(r"drinkware_yeti_rambler_30oz_(.*)", old)
    if m:
        return f"yeti30oz_{m.group(1)}"

    # drinkware_stanley_quencher_40oz_* → stanley40oz_*
    m = re.fullmatch(r"drinkware_stanley_quencher_40oz_(.*)", old)
    if m:
        return f"stanley40oz_{m.group(1)}"

    # drinkware_hydro_flask_32oz_* → hydroflask32oz_*
    m = re.fullmatch(r"drinkware_hydro_flask_32oz_(.*)", old)
    if m:
        return f"hydroflask32oz_{m.group(1)}"

    # camera_gopro_hero_12_* → gopro12_*
    m = re.fullmatch(r"camera_gopro_hero_12_(.*)", old)
    if m:
        return f"gopro12_{m.group(1)}"

    # camera_security_ring_indoor_* → ring_indoor_*
    m = re.fullmatch(r"camera_security_ring_indoor_(.*)", old)
    if m:
        return f"ring_indoor_{m.group(1)}"

    # camera_security_ring_stickup_* → ring_stickup_*
    m = re.fullmatch(r"camera_security_ring_stickup_(.*)", old)
    if m:
        return f"ring_stickup_{m.group(1)}"

    # camera_security_ring_doorbell_* → ring_doorbell_*
    m = re.fullmatch(r"camera_security_ring_doorbell_(.*)", old)
    if m:
        return f"ring_doorbell_{m.group(1)}"

    # camera_security_unifi_g4_bullet_* → unifi_g4_bullet_*
    m = re.fullmatch(r"camera_security_unifi_g4_bullet_(.*)", old)
    if m:
        return f"unifi_g4_bullet_{m.group(1)}"

    # camera_security_unifi_g4_instant_* → unifi_g4_instant_*
    m = re.fullmatch(r"camera_security_unifi_g4_instant_(.*)", old)
    if m:
        return f"unifi_g4_instant_{m.group(1)}"

    # camera_security_unifi_g5_flex_* → unifi_g5_flex_*
    m = re.fullmatch(r"camera_security_unifi_g5_flex_(.*)", old)
    if m:
        return f"unifi_g5_flex_{m.group(1)}"

    # paint_citadel_pot_* → citadel_pot_*
    m = re.fullmatch(r"paint_citadel_pot_(.*)", old)
    if m:
        return f"citadel_pot_{m.group(1)}"

    # paint_vallejo_dropper_* → vallejo_dropper_*
    m = re.fullmatch(r"paint_vallejo_dropper_(.*)", old)
    if m:
        return f"vallejo_dropper_{m.group(1)}"

    # paint_army_painter_dropper_* → army_painter_*
    m = re.fullmatch(r"paint_army_painter_dropper_(.*)", old)
    if m:
        return f"army_painter_{m.group(1)}"

    # paint_craft_bottle_2oz_* → craft_paint_2oz_*
    m = re.fullmatch(r"paint_craft_bottle_2oz_(.*)", old)
    if m:
        return f"craft_paint_2oz_{m.group(1)}"

    # battery_tool_milwaukee_m18_* → milwaukee_m18_bat_*
    m = re.fullmatch(r"battery_tool_milwaukee_m18_(.*)", old)
    if m:
        return f"milwaukee_m18_bat_{m.group(1)}"

    # battery_tool_makita_18v_* → makita_18v_bat_*
    m = re.fullmatch(r"battery_tool_makita_18v_(.*)", old)
    if m:
        return f"makita_18v_bat_{m.group(1)}"

    # battery_tool_dewalt_20v_* → dewalt_20v_bat_*
    m = re.fullmatch(r"battery_tool_dewalt_20v_(.*)", old)
    if m:
        return f"dewalt_20v_bat_{m.group(1)}"

    # battery_aa_* → aa_bat_*
    m = re.fullmatch(r"battery_aa_(.*)", old)
    if m:
        return f"aa_bat_{m.group(1)}"

    # battery_aaa_* → aaa_bat_*
    m = re.fullmatch(r"battery_aaa_(.*)", old)
    if m:
        return f"aaa_bat_{m.group(1)}"

    # battery_cr2032_* → cr2032_*
    m = re.fullmatch(r"battery_cr2032_(.*)", old)
    if m:
        return f"cr2032_{m.group(1)}"

    # battery_18650_* → bat_18650_*
    m = re.fullmatch(r"battery_18650_(.*)", old)
    if m:
        return f"bat_18650_{m.group(1)}"

    # electronics_wago_221_lever_nut_body_* → wago221_body_*
    m = re.fullmatch(r"electronics_wago_221_lever_nut_body_(.*)", old)
    if m:
        return f"wago221_body_{m.group(1)}"

    # tool_dewalt_dcd771_drill_* → dewalt_drill_*
    m = re.fullmatch(r"tool_dewalt_dcd771_drill_(.*)", old)
    if m:
        return f"dewalt_drill_{m.group(1)}"

    # tool_milwaukee_m18_drill_* → milwaukee_drill_*
    m = re.fullmatch(r"tool_milwaukee_m18_drill_(.*)", old)
    if m:
        return f"milwaukee_drill_{m.group(1)}"

    # tool_dewalt_dcs391_saw_* → dewalt_saw_*
    m = re.fullmatch(r"tool_dewalt_dcs391_saw_(.*)", old)
    if m:
        return f"dewalt_saw_{m.group(1)}"

    # tool_milwaukee_m18_saw_* → milwaukee_saw_*
    m = re.fullmatch(r"tool_milwaukee_m18_saw_(.*)", old)
    if m:
        return f"milwaukee_saw_{m.group(1)}"

    # tool_dewalt_dcw210_sander_* → dewalt_sander_*
    m = re.fullmatch(r"tool_dewalt_dcw210_sander_(.*)", old)
    if m:
        return f"dewalt_sander_{m.group(1)}"

    # tool_milwaukee_m18_sander_* → milwaukee_sander_*
    m = re.fullmatch(r"tool_milwaukee_m18_sander_(.*)", old)
    if m:
        return f"milwaukee_sander_{m.group(1)}"

    # handtool_screwdriver_* → screwdriver_*
    m = re.fullmatch(r"handtool_screwdriver_(.*)", old)
    if m:
        return f"screwdriver_{m.group(1)}"

    # handtool_hammer_16oz_* → hammer_16oz_*
    m = re.fullmatch(r"handtool_hammer_16oz_(.*)", old)
    if m:
        return f"hammer_16oz_{m.group(1)}"

    # handtool_wrench_adj_{size}_* → adj_wrench_{size}_*
    m = re.fullmatch(r"handtool_wrench_adj_(\w+)_(.*)", old)
    if m:
        return f"adj_wrench_{m.group(1)}_{m.group(2)}"

    # handtool_tape_measure_25ft_* → tape_measure_*
    m = re.fullmatch(r"handtool_tape_measure_25ft_(.*)", old)
    if m:
        return f"tape_measure_{m.group(1)}"

    # handtool_utility_knife_* → utility_knife_*
    m = re.fullmatch(r"handtool_utility_knife_(.*)", old)
    if m:
        return f"utility_knife_{m.group(1)}"

    # handtool_torpedo_level_* → torpedo_level_*
    m = re.fullmatch(r"handtool_torpedo_level_(.*)", old)
    if m:
        return f"torpedo_level_{m.group(1)}"

    # controller_xbox_* → xbox_*
    m = re.fullmatch(r"controller_xbox_(.*)", old)
    if m:
        return f"xbox_{m.group(1)}"

    # controller_ps5_dualsense_* → ps5_*
    m = re.fullmatch(r"controller_ps5_dualsense_(.*)", old)
    if m:
        return f"ps5_{m.group(1)}"

    # controller_switch_pro_* → switch_pro_*
    m = re.fullmatch(r"controller_switch_pro_(.*)", old)
    if m:
        return f"switch_pro_{m.group(1)}"

    # controller_joycon_* → joycon_*
    m = re.fullmatch(r"controller_joycon_(.*)", old)
    if m:
        return f"joycon_{m.group(1)}"

    # remote_apple_tv_siri_* → appletv_remote_*
    m = re.fullmatch(r"remote_apple_tv_siri_(.*)", old)
    if m:
        return f"appletv_remote_{m.group(1)}"

    # remote_fire_tv_* → firetv_remote_*
    m = re.fullmatch(r"remote_fire_tv_(.*)", old)
    if m:
        return f"firetv_remote_{m.group(1)}"

    # remote_roku_voice_pro_* → roku_remote_*
    m = re.fullmatch(r"remote_roku_voice_pro_(.*)", old)
    if m:
        return f"roku_remote_{m.group(1)}"

    # watch_apple_series10_42_* → watch_s10_42_*
    m = re.fullmatch(r"watch_apple_series10_42_(.*)", old)
    if m:
        return f"watch_s10_42_{m.group(1)}"

    # watch_apple_series10_46_* → watch_s10_46_*
    m = re.fullmatch(r"watch_apple_series10_46_(.*)", old)
    if m:
        return f"watch_s10_46_{m.group(1)}"

    # watch_apple_ultra_2_* → watch_ultra2_*
    m = re.fullmatch(r"watch_apple_ultra_2_(.*)", old)
    if m:
        return f"watch_ultra2_{m.group(1)}"

    # twist_lock_bayonet_* → bayonet_*
    m = re.fullmatch(r"twist_lock_bayonet_(.*)", old)
    if m:
        return f"bayonet_{m.group(1)}"

    # bottle_pill_{size}_* → pill_{size}_*
    m = re.fullmatch(r"bottle_pill_(\w+)_(.*)", old)
    if m:
        return f"pill_{m.group(1)}_{m.group(2)}"

    # bottle_nalgene_32oz_* → nalgene_32oz_*
    m = re.fullmatch(r"bottle_nalgene_32oz_(.*)", old)
    if m:
        return f"nalgene_32oz_{m.group(1)}"

    # bottle_eye_drop_15ml_* → eyedrop_15ml_*
    m = re.fullmatch(r"bottle_eye_drop_15ml_(.*)", old)
    if m:
        return f"eyedrop_15ml_{m.group(1)}"

    # bottle_spray_28_400_neck_od → spray_28_400_neck_od
    m = re.fullmatch(r"bottle_(spray_\d+_\d+_\w+)", old)
    if m:
        return m.group(1)

    # media_samsung_t7_ssd_* → samsung_t7_*
    m = re.fullmatch(r"media_samsung_t7_ssd_(.*)", old)
    if m:
        return f"samsung_t7_{m.group(1)}"

    # media_wd_passport_* → wd_passport_*
    m = re.fullmatch(r"media_wd_passport_(.*)", old)
    if m:
        return f"wd_passport_{m.group(1)}"

    # media_sata_25_* → sata_25_*
    m = re.fullmatch(r"media_sata_25_(.*)", old)
    if m:
        return f"sata_25_{m.group(1)}"

    # media_sata_35_* → sata_35_*
    m = re.fullmatch(r"media_sata_35_(.*)", old)
    if m:
        return f"sata_35_{m.group(1)}"

    # media_m2_2280_* → m2_2280_*
    m = re.fullmatch(r"media_m2_2280_(.*)", old)
    if m:
        return f"m2_2280_{m.group(1)}"

    # media_cfexpress_type_b_* → cfexpress_b_*
    m = re.fullmatch(r"media_cfexpress_type_b_(.*)", old)
    if m:
        return f"cfexpress_b_{m.group(1)}"

    # glasses_hard_case_* → glasses_case_*
    m = re.fullmatch(r"glasses_hard_case_(.*)", old)
    if m:
        return f"glasses_case_{m.group(1)}"

    # glasses_folded_* → glasses_folded_* (unchanged)
    m = re.fullmatch(r"glasses_folded_(.*)", old)
    if m:
        return f"glasses_folded_{m.group(1)}"

    # woodscrew_gauge_{NN}_major_diameter_mm → ws{N}_major_dia  (drop leading zero)
    m = re.fullmatch(r"woodscrew_gauge_(\d+)_major_diameter_mm", old)
    if m:
        n = str(int(m.group(1)))
        return f"ws{n}_major_dia"

    # woodscrew_gauge_{NN}_pilot_hole_softwood_mm → ws{N}_pilot_soft
    m = re.fullmatch(r"woodscrew_gauge_(\d+)_pilot_hole_softwood_mm", old)
    if m:
        n = str(int(m.group(1)))
        return f"ws{n}_pilot_soft"

    # woodscrew_gauge_{NN}_pilot_hole_hardwood_mm → ws{N}_pilot_hard
    m = re.fullmatch(r"woodscrew_gauge_(\d+)_pilot_hole_hardwood_mm", old)
    if m:
        n = str(int(m.group(1)))
        return f"ws{n}_pilot_hard"

    # woodscrew_gauge_{NN}_clearance_hole_top_board_mm → ws{N}_clearance
    m = re.fullmatch(r"woodscrew_gauge_(\d+)_clearance_hole_top_board_mm", old)
    if m:
        n = str(int(m.group(1)))
        return f"ws{n}_clearance"

    # woodscrew_gauge_{NN}_countersink_flat_head_diameter_mm → ws{N}_csink_dia
    m = re.fullmatch(r"woodscrew_gauge_(\d+)_countersink_flat_head_diameter_mm", old)
    if m:
        n = str(int(m.group(1)))
        return f"ws{n}_csink_dia"

    # drill_imperial_fractional_{N}_{D}_inch_diameter_mm → drill_{N}_{D}
    # Special case: 1_1 → drill_1
    m = re.fullmatch(r"drill_imperial_fractional_(\d+)_(\d+)_inch_diameter_mm", old)
    if m:
        n, d = m.group(1), m.group(2)
        if n == d:  # e.g. 1_1 → 1/1 → drill_1
            return f"drill_{n}"
        return f"drill_{n}_{d}"

    # key_kw1_* / key_sc1_* handled in EXACT above
    # key_split_ring_* handled in EXACT above

    # Return unchanged if no rule matched
    return old


# ---------------------------------------------------------------------------
# Validate new name format
# ---------------------------------------------------------------------------
NAME_RE = re.compile(r"^[a-z][a-z0-9_]*$")

def validate_name(name: str) -> bool:
    return bool(NAME_RE.fullmatch(name))


# ---------------------------------------------------------------------------
# Token-based whole-word replacement in expressions
# ---------------------------------------------------------------------------

def update_expression(expr: str, rename_map: dict) -> str:
    """Replace old param names in expression with new names (whole-word, longest first)."""
    # Sort by length descending to avoid partial replacements (e.g. m3 before m3p5)
    for old in sorted(rename_map, key=len, reverse=True):
        new = rename_map[old]
        if old == new:
            continue
        # Replace whole-word occurrences only
        expr = re.sub(r"\b" + re.escape(old) + r"\b", new, expr)
    return expr


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    if not CSV_IN.exists():
        print(f"ERROR: CSV not found at {CSV_IN}", file=sys.stderr)
        sys.exit(1)

    rows = []
    with open(CSV_IN, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)

    print(f"Read {len(rows)} params from {CSV_IN.name}")

    # --- Build rename map ---
    rename_map = {}   # old_name -> new_name  (only for included params)
    skipped_bmg = []
    skipped_delete = []
    unchanged = []
    changed = []
    errors = []

    for row in rows:
        old = row["Name"].strip()

        if old in SKIP_PARAMS:
            skipped_delete.append(old)
            continue

        if old.startswith("bmg_"):
            skipped_bmg.append(old)
            continue

        new = rename(old)

        if not validate_name(new):
            errors.append((old, new, "INVALID NAME FORMAT"))
            # Still add to map so expression updates work
            rename_map[old] = new
        else:
            rename_map[old] = new

        if new == old:
            unchanged.append(old)
        else:
            changed.append((old, new))

    # --- Check for duplicate new names ---
    new_names = list(rename_map.values())
    seen = {}
    for old, new in rename_map.items():
        if new in seen:
            errors.append((old, new, f"DUPLICATE — conflicts with {seen[new]}"))
        else:
            seen[new] = old

    # --- Write mapping CSV ---
    with open(MAPPING_OUT, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["old_name", "new_name"])
        for old, new in rename_map.items():
            writer.writerow([old, new])
        # Add deleted params with empty new_name
        for old in skipped_delete:
            writer.writerow([old, "DELETE"])
        for old in skipped_bmg:
            writer.writerow([old, "MOVE_TO_PROJECT"])

    print(f"\nWrote {len(rename_map)} mappings to {MAPPING_OUT.name}")

    # --- Summary ---
    print(f"\n{'='*60}")
    print(f"SUMMARY")
    print(f"{'='*60}")
    print(f"  Total params in CSV:    {len(rows)}")
    print(f"  Renamed:                {len(changed)}")
    print(f"  Unchanged:              {len(unchanged)}")
    print(f"  Skipped (bmg_):         {len(skipped_bmg)}")
    print(f"  Skipped (to delete):    {len(skipped_delete)}")
    print(f"  Errors:                 {len(errors)}")

    if errors:
        print(f"\nERRORS:")
        for old, new, msg in errors:
            print(f"  {old!r} -> {new!r}: {msg}")

    print(f"\nSample renames (first 30):")
    for old, new in changed[:30]:
        print(f"  {old}")
        print(f"    -> {new}")

    # --- Show expression updates ---
    print(f"\nExpression updates (params with references to renamed params):")
    expr_updated = 0
    for row in rows:
        old_name = row["Name"].strip()
        if old_name.startswith("bmg_") or old_name in SKIP_PARAMS:
            continue
        old_expr = row["Expression"].strip()
        new_expr = update_expression(old_expr, rename_map)
        if new_expr != old_expr:
            new_name = rename_map.get(old_name, old_name)
            print(f"  [{new_name}] expr: {old_expr!r} -> {new_expr!r}")
            expr_updated += 1

    print(f"\nTotal params with updated expressions: {expr_updated}")

    if not errors:
        print("\nAll renames valid. migration_mapping.csv is ready.")
    else:
        print(f"\n{len(errors)} errors found — review before proceeding.")

    return len(errors)


if __name__ == "__main__":
    sys.exit(main())
