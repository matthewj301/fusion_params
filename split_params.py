#!/usr/bin/env python3
"""Split the master parameter CSV into themed files for selective Fusion import.

Reads the combined CSV and outputs individual themed CSVs into a 'split/' directory.
The combined CSV remains the source of truth.

Structure:
  Tier 1 (always import): design_rules, fasteners
  Tier 2 (per project): motion_mechanical, electronics_mounting, devices, workshop, household_hobby
  Tier 3 (specialized): imperial_drills, wood_screws

Usage:
    python3 split_params.py
"""

import csv
from pathlib import Path

CSV_PATH = Path("BakedBean3D_MasterParams_v4/BakedBean3D_MasterParams_params.csv")
OUT_DIR = Path("BakedBean3D_MasterParams_v4/split")

# Tier 1 — Always Import
DESIGN_RULES_PREFIXES = {
    "fdm_", "tol_", "pip_", "bayonet_", "dovetail_", "spring_clip_", "hinge_",
    "container_", "snapfit_", "snaplatch_", "detent_", "quarterturn_", "camlock_",
    "asm_",
}
DESIGN_RULES_EXACT = {
    "countersink_angle",
}

FASTENERS_PREFIXES = {
    "m2_", "m2p5_", "m3_", "m4_", "m5_", "m6_", "m8_", "m10_",
    "magnet_", "ziptie_", "heatset_temp_",
}

# Tier 2 — Import Per Project
MOTION_MECHANICAL_PREFIXES = {
    "mgn", "gt2_", "gear_", "f695_", "bearing_", "nema", "vslot_", "tslot_",
    "beacon_", "orbiter_", "chube_", "canbus_", "toolhead_",
    "cnc_", "alu_",
}

ELECTRONICS_MOUNTING_PREFIXES = {
    "rpi", "octopus_", "skr_mini_", "pcb_", "din_rail_",
    "jst_", "usb_a_panel_", "usb_c_panel_", "xt30_", "xt60_",
    "wago", "esp32_", "d1mini_", "header_",
    "gang_box_", "decora_", "conduit_", "sonoff_",
}

DEVICES_PREFIXES = {
    "iphone", "galaxy", "ipad", "phone_", "tablet_",
    "magsafe", "applewatch_charger_",
    "watch_", "xbox_", "ps5_", "switch_pro_", "joycon_",
    "controller_max_",
    "appletv_remote_", "firetv_remote_", "roku_remote_",
    "echo_", "nest_mini", "kasa_", "hue_bridge_",
    "ring_indoor_", "ring_stickup_", "ring_doorbell_",
    "unifi_", "tripod_mount_",
    "airpods_",
}

WORKSHOP_PREFIXES = {
    "pegboard_", "multiboard_", "skadis_", "gridfinity_", "hsw_",
    "french_cleat_", "wall_control_",
    "emt_", "plywood_", "mdf_", "lumber_",
    "sq_drive_", "hex_bit_",
    "dewalt_drill_", "milwaukee_drill_",
    "dewalt_saw_", "milwaukee_saw_",
    "dewalt_sander_", "milwaukee_sander_",
    "screwdriver_", "hammer_", "adj_wrench_",
    "tape_measure_", "utility_knife_", "torpedo_level_",
    "milwaukee_m18_bat_", "makita_18v_bat_", "dewalt_20v_bat_",
    "aa_bat_", "aaa_bat_", "cr2032_", "bat_18650_",
    "aa_holder_", "aaa_holder_", "bat_18650_holder_",
    "kw1_", "sc1_", "keyring_",
}

HOUSEHOLD_HOBBY_PREFIXES = {
    "coffee_mug_", "yeti", "stanley", "hydroflask",
    "drink_max_",
    "bic_pen_", "bic_lighter_", "sharpie_", "chapstick_",
    "zippo_",
    "credit_card_", "business_card_", "poker_card_",
    "penny_", "nickel_", "dime_", "quarter_", "half_dollar_", "dollar_coin_",
    "citadel_", "vallejo_", "army_painter_", "craft_paint_",
    "gopro", "wh_",
    "halfdart_", "fulldart_", "nerf_", "fidget_",
    "pill_", "nalgene_", "eyedrop_", "spray_",
    "usb_a_plug_", "usb_c_plug_", "usb_c_cable_",
    "lightning_cable_", "hdmi_plug_", "dp_plug_",
    "rj45_plug_", "audio_35mm_",
    "sd_card_", "microsd_", "samsung_t7_", "wd_passport_",
    "sata_", "m2_2280_", "cfexpress_",
    "glasses_",
}

# Tier 3 — Specialized Reference
IMPERIAL_DRILLS_PREFIXES = {"drill_"}
WOOD_SCREWS_PREFIXES = {"ws"}

# Materials go into design_rules
MATERIAL_PREFIXES = {
    "pla_", "petg_", "abs_", "asa_", "pc_chamber_",
    "tpu_",
}


def classify(name):
    # Tier 3 first (most specific)
    for prefix in IMPERIAL_DRILLS_PREFIXES:
        if name.startswith(prefix):
            return "imperial_drills"
    for prefix in WOOD_SCREWS_PREFIXES:
        if name.startswith(prefix):
            return "wood_screws"

    # Materials → design_rules
    for prefix in MATERIAL_PREFIXES:
        if name.startswith(prefix):
            return "design_rules"

    # Tier 1
    if name in DESIGN_RULES_EXACT:
        return "design_rules"
    for prefix in DESIGN_RULES_PREFIXES:
        if name.startswith(prefix):
            return "design_rules"
    for prefix in FASTENERS_PREFIXES:
        if name.startswith(prefix):
            return "fasteners"

    # Tier 2
    for prefix in MOTION_MECHANICAL_PREFIXES:
        if name.startswith(prefix):
            return "motion_mechanical"
    for prefix in ELECTRONICS_MOUNTING_PREFIXES:
        if name.startswith(prefix):
            return "electronics_mounting"
    for prefix in DEVICES_PREFIXES:
        if name.startswith(prefix):
            return "devices"
    for prefix in WORKSHOP_PREFIXES:
        if name.startswith(prefix):
            return "workshop"
    for prefix in HOUSEHOLD_HOBBY_PREFIXES:
        if name.startswith(prefix):
            return "household_hobby"

    # Fallback
    return "design_rules"


THEME_DESCRIPTIONS = {
    "design_rules": "[Tier 1] Design Rules — FDM tolerances, fit classes, walls, fillets, chamfers, overhangs, bridges, joints, materials",
    "fasteners": "[Tier 1] Fasteners — M2-M6 hardware specs, heat-set inserts, nut traps, counterbores, magnets, zip ties",
    "motion_mechanical": "[Tier 2] Motion & Mechanical — MGN rails, GT2 belts, ball bearings, NEMA motors, extrusion, CNC process params",
    "electronics_mounting": "[Tier 2] Electronics Mounting — PCBs, header pitch, connectors, panel cutouts, DIN rail, home automation",
    "devices": "[Tier 2] Devices — phones, tablets, watches, controllers, remotes, chargers, smart home, cameras",
    "workshop": "[Tier 2] Workshop — pegboard & wall systems (Multiboard/SKADIS/Gridfinity/HSW/French cleat), shop stock (EMT/lumber/sheet), power & hand tools, batteries, keys",
    "household_hobby": "[Tier 2] Household & Hobby — drinkware, EDC, cards, coins, paint, Warhammer, foam darts, bottles, cables, storage",
    "imperial_drills": "[Tier 3] Imperial Drills — fractional drill bit table (1/64\" to 1\")",
    "wood_screws": "[Tier 3] Wood Screws — gauges #0-#20 with pilot/clearance/countersink",
}


def main():
    if not CSV_PATH.exists():
        raise FileNotFoundError(f"{CSV_PATH} not found")

    OUT_DIR.mkdir(exist_ok=True)

    buckets = {}
    fieldnames = None
    with open(CSV_PATH, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        for row in reader:
            name = row["Name"].strip()
            if not name:
                continue
            theme = classify(name)
            buckets.setdefault(theme, []).append(row)

    # Remove stale split files that no longer match any theme
    existing_csvs = set(OUT_DIR.glob("*.csv"))
    expected_csvs = {OUT_DIR / f"{theme}.csv" for theme in buckets}
    for stale in existing_csvs - expected_csvs:
        stale.unlink()
        print(f"  Removed stale: {stale.name}")

    for theme, rows in sorted(buckets.items()):
        out_path = OUT_DIR / f"{theme}.csv"
        with open(out_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
        desc = THEME_DESCRIPTIONS.get(theme, theme)
        print(f"  {out_path.name}: {len(rows)} params — {desc}")

    total = sum(len(rows) for rows in buckets.values())
    print(f"\nTotal: {total} params across {len(buckets)} files")

    # Verify no params lost
    with open(CSV_PATH, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        original_count = sum(1 for row in reader if row["Name"].strip())
    if total != original_count:
        print(f"WARNING: mismatch! CSV has {original_count}, split has {total}")
    else:
        print("Verification passed: all params accounted for.")


if __name__ == "__main__":
    main()
