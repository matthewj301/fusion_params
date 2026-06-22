#!/usr/bin/env python3
"""Append US wall-plate / light-switch / single-gang-box reference dimensions to
the master parameter CSV. Idempotent: names already present are skipped.

Sources: US electrical device standards (NEMA WD-6 / typical decorator + toggle
cover plates and single-gang device boxes). Values are nominal; verify against
the specific plate/box brand for tight fits.

Naming: component-first. `wallplate_*` = the cover (face) plate + classic toggle
opening; `decora_*` = the Decora/rocker rectangular opening; `gang_box_*` = the
metal/plastic device box + the device yoke (strap) that screws into it.
`decora_` and `gang_box_` are already registered to electronics_mounting in
split_params.py; `wallplate_` was added there.

Value column convention (matches existing rows):
  mm  -> Expression / 10   (Fusion internal cm)
  deg -> radians(Expression)
  ''  -> Expression        (dimensionless)
"""
import csv
import math
from pathlib import Path

CSV = Path("BakedBean3D_MasterParams_v4/BakedBean3D_MasterParams_params.csv")

# (name, unit, expression, comment)
NEW = [
    # --- Cover (wall) plate face — single-gang ---
    ("wallplate_std_width", "mm", "70.0", "US standard single-gang switch/outlet cover plate width (2.75 in)."),
    ("wallplate_std_height", "mm", "114.0", "US standard cover plate height (4.50 in)."),
    ("wallplate_jumbo_width", "mm", "79.5", "US oversized/jumbo cover plate width (3.13 in)."),
    ("wallplate_jumbo_height", "mm", "124.0", "US oversized/jumbo cover plate height (4.88 in)."),
    ("wallplate_thickness", "mm", "3.0", "Cover plate thickness, nominal. Typical range 2.5-5 mm (0.10-0.20 in)."),

    # --- Mounting / screw spacing (same for toggle and Decora plates) ---
    ("wallplate_screw_pitch", "mm", "70.0", "Cover-plate mounting screw spacing, vertical center-to-center (2.756 in). Same for toggle and Decora/rocker plates. Screw thread = #6-32."),
    ("wallplate_screw_clearance", "mm", "3.7", "Clearance hole for the #6-32 device screw (major dia ~3.5 mm). ~0.144 in close clearance; open to 3.8 for printed parts."),

    # --- Classic toggle-switch opening ---
    ("wallplate_toggle_slot_width", "mm", "10.0", "Classic toggle-switch opening width (0.40 in)."),
    ("wallplate_toggle_slot_height", "mm", "25.4", "Classic toggle-switch opening height (1.00 in)."),

    # --- Decora / rocker opening ---
    ("decora_cutout_width", "mm", "33.3", "Decora/rocker switch plate rectangular opening width (1.31 in)."),
    ("decora_cutout_height", "mm", "66.7", "Decora/rocker switch plate rectangular opening height (2.63 in)."),

    # --- Single-gang device box + yoke (strap) ---
    ("gang_box_yoke_screw_span", "mm", "83.3", "Single-gang device yoke (strap) mounting-ear screw spacing, hole-to-hole (3.28 in). This is the bracket that screws into the box; #6-32."),
    ("gang_box_single_width", "mm", "50.0", "Single-gang box opening width, approximate (2.0 in)."),
    ("gang_box_single_height", "mm", "76.0", "Single-gang box opening height, approximate (3.0 in)."),
    ("gang_box_depth_min", "mm", "63.5", "Single-gang box depth, shallow end (2.5 in). Depth varies 2.5-3.5 in by box."),
    ("gang_box_depth_max", "mm", "88.9", "Single-gang box depth, deep end (3.5 in)."),
]


def value_for(unit, expr):
    x = float(expr)
    if unit == "mm":
        v = x / 10.0
    elif unit == "deg":
        return repr(math.radians(x))
    else:
        v = x
    s = f"{v:.6f}".rstrip("0").rstrip(".")
    return s if s else "0"


def main():
    with open(CSV, newline="", encoding="utf-8") as f:
        existing = {row["Name"].strip() for row in csv.DictReader(f) if row["Name"].strip()}

    rows, skipped = [], []
    for name, unit, expr, comment in NEW:
        if name in existing:
            skipped.append(name)
            continue
        rows.append([name, unit, expr, value_for(unit, expr), comment, "True"])

    if skipped:
        print(f"Skipped {len(skipped)} already-present param(s): {', '.join(skipped)}")

    if rows:
        with open(CSV, "a", newline="", encoding="utf-8") as f:
            csv.writer(f, lineterminator="\n").writerows(rows)

    print(f"Appended {len(rows)} parameters.")


if __name__ == "__main__":
    main()
