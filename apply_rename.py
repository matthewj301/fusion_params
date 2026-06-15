#!/usr/bin/env python3
"""Apply the rename mapping to the master parameter CSV.

Reads migration_mapping.csv and transforms BakedBean3D_MasterParams_params.csv:
  - Renames params per mapping
  - Deletes params marked DELETE
  - Extracts params marked MOVE_TO_PROJECT to projects/bmg_extruder.csv
  - Updates expressions to use new names
  - Converts counterbore/nut-trap hardcoded values to expressions

Usage:
    python params/apply_rename.py [--dry-run]
"""

import csv
import re
import sys
from pathlib import Path

PARAMS_DIR = Path(__file__).parent
CSV_IN = PARAMS_DIR / "BakedBean3D_MasterParams_v4" / "BakedBean3D_MasterParams_params.csv"
CSV_OUT = CSV_IN  # overwrite in place
BMG_OUT = PARAMS_DIR / ".." / "projects" / "bmg_extruder.csv"
MAPPING = PARAMS_DIR / "migration_mapping.csv"

HEADER = ["Name", "Unit", "Expression", "Value", "Comment", "Favorite"]

# Counterbore/nut-trap params that should become expressions
# new_name -> expression using new base param names
EXPRESSION_FIXES = {
    "m2_button_cbore_dia":   "m2_button_head_dia + 0.40",
    "m2_button_cbore_depth": "m2_button_head_height + 0.30",
    "m2p5_button_cbore_dia":   "m2p5_button_head_dia + 0.40",
    "m2p5_button_cbore_depth": "m2p5_button_head_height + 0.30",
    "m3_button_cbore_dia":   "m3_button_head_dia + 0.40",
    "m3_button_cbore_depth": "m3_button_head_height + 0.30",
    "m3_socket_cbore_dia":   "m3_socket_head_dia + 0.40",
    "m3_socket_cbore_depth": "m3_socket_head_height + 0.30",
    "m4_button_cbore_dia":   "m4_button_head_dia + 0.40",
    "m4_button_cbore_depth": "m4_button_head_height + 0.30",
    "m5_button_cbore_dia":   "m5_button_head_dia + 0.40",
    "m3_nut_pocket_af":      "m3_hex_nut_af + 0.20",
    "m3_nut_pocket_depth":   "m3_hex_nut_height + 0.20",
    # m3_nut_pocket_circum left as hardcoded — Fusion CSV expressions don't support cos()
    "m3_sq_nut_pocket_width": "m3_square_nut_width + 0.20",
    "m3_sq_nut_pocket_depth": "m3_square_nut_height + 0.20",
    "m4_nut_pocket_af":      "m4_hex_nut_af + 0.20",
    "m4_nut_pocket_depth":   "m4_hex_nut_height + 0.20",
    "m5_nut_pocket_af":      "m5_hex_nut_af + 0.20",
    "m5_nut_pocket_depth":   "m5_hex_nut_height + 0.20",
}


def update_expression(expr, rename_map):
    for old in sorted(rename_map, key=len, reverse=True):
        new = rename_map[old]
        if old == new:
            continue
        expr = re.sub(r"\b" + re.escape(old) + r"\b", new, expr)
    return expr


def main():
    dry_run = "--dry-run" in sys.argv

    # Load mapping
    rename_map = {}
    deletes = set()
    moves = set()
    with open(MAPPING, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            old, new = row["old_name"], row["new_name"]
            if new == "DELETE":
                deletes.add(old)
            elif new == "MOVE_TO_PROJECT":
                moves.add(old)
            else:
                rename_map[old] = new

    # Load CSV
    rows = []
    with open(CSV_IN, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)

    print(f"Loaded {len(rows)} params, {len(rename_map)} renames, {len(deletes)} deletes, {len(moves)} moves")

    # Process
    main_rows = []
    bmg_rows = []
    stats = {"renamed": 0, "deleted": 0, "moved": 0, "expr_fixed": 0, "expr_updated": 0}

    for row in rows:
        name = row["Name"].strip()

        if name in deletes:
            stats["deleted"] += 1
            continue

        if name in moves:
            bmg_rows.append(row)
            stats["moved"] += 1
            continue

        # Rename
        new_name = rename_map.get(name, name)
        if new_name != name:
            stats["renamed"] += 1
        row["Name"] = new_name

        # Update expression references
        old_expr = row["Expression"]
        new_expr = update_expression(old_expr, rename_map)
        if new_expr != old_expr:
            stats["expr_updated"] += 1
        row["Expression"] = new_expr

        # Apply expression fixes for counterbores/nut traps
        if new_name in EXPRESSION_FIXES:
            row["Expression"] = EXPRESSION_FIXES[new_name]
            stats["expr_fixed"] += 1

        main_rows.append(row)

    print(f"\nResults:")
    print(f"  Renamed:          {stats['renamed']}")
    print(f"  Deleted:          {stats['deleted']}")
    print(f"  Moved to BMG:     {stats['moved']}")
    print(f"  Expressions updated (references): {stats['expr_updated']}")
    print(f"  Expressions fixed (counterbores):  {stats['expr_fixed']}")
    print(f"  Main CSV rows:    {len(main_rows)}")
    print(f"  BMG CSV rows:     {len(bmg_rows)}")

    if dry_run:
        print("\n[DRY RUN] No files written.")
        return

    # Write main CSV
    with open(CSV_OUT, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=HEADER)
        writer.writeheader()
        writer.writerows(main_rows)
    print(f"\nWrote {len(main_rows)} params to {CSV_OUT}")

    # Write BMG CSV
    BMG_OUT.parent.mkdir(parents=True, exist_ok=True)
    with open(BMG_OUT, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=HEADER)
        writer.writeheader()
        writer.writerows(bmg_rows)
    print(f"Wrote {len(bmg_rows)} params to {BMG_OUT}")


if __name__ == "__main__":
    main()
