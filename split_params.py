#!/usr/bin/env python3
"""Split the master parameter CSV into themed files for selective Fusion import.

Reads the combined CSV and outputs individual themed CSVs into a 'split/' directory.
The combined CSV remains the source of truth.

Usage:
    python3 split_params.py
"""

import csv
import re
from pathlib import Path

CSV_PATH = Path("BakedBean3D_MasterParams_v4/BakedBean3D_MasterParams_params.csv")
OUT_DIR = Path("BakedBean3D_MasterParams_v4/split")

CORE_FDM_PREFIXES = {
    "printer_accuracy_", "tolerance_", "hole_geometry_", "boss_geometry_",
    "heatset_insert_", "counterbore_", "nut_", "hardware_", "thread_",
    "motion_", "electronics_", "cnc_", "magnet_", "woodscrew_", "drill_",
    "print_in_place_", "twist_lock_", "dovetail_", "spring_clip_",
    "container_", "material_", "foam_", "wall_", "fillet_", "chamfer_",
    "warhammer_",
}

ELECTRONICS_DEVICES_PREFIXES = {
    "phone_", "tablet_", "charger_", "watch_", "controller_", "remote_",
    "smarthome_", "camera_security_", "audio_",
}

WORKSHOP_PREFIXES = {
    "pegboard_", "tool_", "handtool_", "battery_tool_", "battery_",
    "key_",
}

KITCHEN_EDC_PREFIXES = {
    "drinkware_", "bottle_", "edc_",
}

HOBBY_PREFIXES = {
    "paint_", "camera_gopro", "camera_gopro_",
}

STORAGE_CONNECTORS_PREFIXES = {
    "media_", "connector_", "cable_", "card_", "coin_", "glasses_",
}


def classify(name):
    for prefix in CORE_FDM_PREFIXES:
        if name.startswith(prefix):
            return "core_fdm"
    for prefix in ELECTRONICS_DEVICES_PREFIXES:
        if name.startswith(prefix):
            return "electronics_devices"
    for prefix in WORKSHOP_PREFIXES:
        if name.startswith(prefix):
            return "workshop"
    for prefix in KITCHEN_EDC_PREFIXES:
        if name.startswith(prefix):
            return "kitchen_edc"
    for prefix in HOBBY_PREFIXES:
        if name.startswith(prefix):
            return "hobby"
    for prefix in STORAGE_CONNECTORS_PREFIXES:
        if name.startswith(prefix):
            return "storage_connectors"
    # Camera params that aren't security cameras
    if name.startswith("camera_"):
        return "hobby"
    return "core_fdm"


THEME_DESCRIPTIONS = {
    "core_fdm": "Core FDM — printer accuracy, tolerances, fasteners, heat-sets, hardware, motion, electronics, CNC, magnets, wood screws, drill bits, joints, containers, materials",
    "electronics_devices": "Electronics & Devices — phones, tablets, chargers, watches, game controllers, remotes, smart home, security cameras, audio accessories",
    "workshop": "Workshop — pegboard, power tools, hand tools, tool batteries, standard batteries, keys",
    "kitchen_edc": "Kitchen & EDC — drinkware, bottles, everyday carry (pens, lighters, chapstick)",
    "hobby": "Hobby & Creative — paint supplies, cameras, GoPro mounts",
    "storage_connectors": "Storage & Connectors — storage media, USB/HDMI/audio cables, cards, coins, glasses",
}


def main():
    if not CSV_PATH.exists():
        raise FileNotFoundError(f"{CSV_PATH} not found")

    OUT_DIR.mkdir(exist_ok=True)

    buckets = {}
    with open(CSV_PATH, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row["Name"].strip()
            if not name:
                continue
            theme = classify(name)
            buckets.setdefault(theme, []).append(row)

    for theme, rows in sorted(buckets.items()):
        out_path = OUT_DIR / f"{theme}.csv"
        with open(out_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["Name", "Expression", "Unit", "Comment"])
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
