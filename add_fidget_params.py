#!/usr/bin/env python3
"""Append fidget-toy design parameters to the master CSV (idempotent).

Families:
  gear_*     -> motion_mechanical  (FDM spur-gear design: sizing + spacing)
  bearing_*  -> motion_mechanical  (R188 compact fidget bearing; 608 already present)
  hinge_*    -> design_rules        (print-in-place pin hinge; builds on pip_hinge_clearance)
  fidget_*   -> household_hobby     (bearing seats, snap/click kinematics, infinity hinge, buttons)

Sources: meta-matic & EngineerDog FDM gear guides, AGMA/ISO gear standards,
Boca Bearings fidget guide, Printables print-in-place planetary-fidget makers.

Value column convention: mm -> /10 (cm); deg -> radians; '' -> as-is.
Tuples: (name, unit, expression, comment[, value_override]).
"""
import csv
import math
from pathlib import Path

CSV = Path("BakedBean3D_MasterParams_v4/BakedBean3D_MasterParams_params.csv")

NEW = [
    # --- FDM spur-gear design (general; gear sizing + spacing) ---
    ("gear_pressure_angle", "deg", "20", "Involute pressure angle for FDM/industry gears. 20 deg = stronger teeth, tolerant of center-distance error; 14.5 deg is legacy. Source: AGMA/ISO."),
    ("gear_module_fine", "mm", "1.0", "Fine gear module (small toys/mechanisms). Pitch dia = module x teeth. Two-gear center distance (the 'spacing') = module x (z1+z2)/2. Source: meta-matic/EngineerDog."),
    ("gear_module_standard", "mm", "1.5", "General-purpose FDM gear module (robots, DIY, fidget gear stacks)."),
    ("gear_module_coarse", "mm", "2.0", "Coarse module for higher-torque / robust FDM gears."),
    ("gear_backlash", "mm", "0.30", "Total backlash between two meshing FDM gears printed SEPARATELY (~0.15 mm/gear). Apply as tooth thinning or +center distance; tune to printer. Source: FDM gear guides."),
    ("gear_pip_clearance", "mm", "0.15", "Per-surface clearance for PRINT-IN-PLACE gears (planetary fidgets) at 0.2 mm layer / 0.4 mm nozzle. ~0.1-0.2: tighter binds, looser rattles. Source: Printables PIP-fidget makers."),
    ("gear_addendum_factor", "", "1.0", "Addendum (tooth height above pitch circle) = this x module. ISO standard 1.0. Dimensionless."),
    ("gear_dedendum_factor", "", "1.25", "Dedendum (depth below pitch circle) = this x module; includes root clearance. Dimensionless."),
    ("gear_tip_clearance_factor", "", "0.25", "Tip-to-root clearance = this x module. Whole tooth depth = (addendum+dedendum) = 2.25 x module. Dimensionless."),
    ("gear_min_teeth", "", "12", "Min teeth to avoid undercut on FDM 20 deg gears (theoretical 17; 12-14 OK printed, profile-shift below ~17). Dimensionless count."),

    # --- R188 compact fidget bearing (608 already in CSV) ---
    ("bearing_r188_id", "mm", "6.35", "R188 bearing bore (1/4 in). Compact fidget-spinner bearing vs the larger 608."),
    ("bearing_r188_od", "mm", "12.7", "R188 bearing OD (1/2 in). Source: Boca Bearings fidget guide."),
    ("bearing_r188_width", "mm", "4.76", "R188 bearing width (3/16 in). Verify - some R188 ship 1/8 in (3.18 mm) wide."),

    # --- Fidget assembly + snap/click kinematics ---
    ("fidget_608_bearing_press", "mm", "bearing_608_od - 0.10", "608 bearing press-fit pocket ID for fidget-spinner caps (0.10 mm interference, FDM). For a slip-fit use bearing_608_od + 0.10 instead.", "2.19"),
    ("fidget_r188_bearing_press", "mm", "bearing_r188_od - 0.10", "R188 bearing press-fit pocket ID for compact fidgets (0.10 mm interference).", "1.26"),
    ("fidget_click_pitch", "mm", "6.0", "APPROX - tune. Center-to-center spacing between click/detent stops on a slider or dial fidget; sets the travel-per-click feel."),
    ("fidget_click_bump", "mm", "0.4", "APPROX - tune. Ride-over bump/notch height that produces the tactile snap as a stop passes a detent. ~0.3-0.6 mm in PLA; bigger = stiffer click. See detent_* for a ball-detent click."),
    ("fidget_magnet_snap_gap", "mm", "0.6", "APPROX - tune. Air gap held between moving and fixed magnets at a magnetic-slider click stop so they snap without contacting. Scale with magnet strength; see magnet_* sizes."),

    # --- Print-in-place hinge family (general; builds on pip_hinge_clearance radial) ---
    ("hinge_pin_dia", "mm", "3.0", "Default print-in-place hinge pin diameter. Below ~2 mm gets fragile. Barrel bore = pin + 2x pip_hinge_clearance. Source: Snapmaker/Printables PIP hinge guides."),
    ("hinge_pin_bore", "mm", "hinge_pin_dia + 2 * pip_hinge_clearance", "Print-in-place hinge barrel bore ID = pin dia + 2x radial clearance (pip_hinge_clearance 0.25). 3.0 -> 3.5 mm.", "0.35"),
    ("hinge_knuckle_gap", "mm", "0.40", "Axial (Z) air gap between stacked hinge knuckles so they do not fuse/bind. Use >= 1-2 layer heights; larger than XY pin clearance since Z is discrete. Source: Snapmaker PIP hinge guide."),
    ("hinge_barrel_wall", "mm", "1.6", "Min wall around a hinge barrel bore (~4x line width) for strength."),

    # --- Fidget hinges + clicky buttons ---
    ("fidget_infinity_hinge_gap", "mm", "0.40", "All-around air gap for infinity-cube folding hinges - loose fit so cubes fold freely without separating. Source: Fusion 360 infinity-cube tutorials."),
    ("fidget_button_travel", "mm", "1.0", "APPROX - tune. Depression distance of a printed fidget-cube clicky button before bottoming/clicking. 0.5-1.5 mm; more travel = bigger throw."),
    ("fidget_button_cap_dia", "mm", "8.0", "APPROX. Typical fidget-cube button cap diameter."),
    ("fidget_button_snap_height", "mm", "0.5", "APPROX - tune. Snap-through lip/dome height the button rides over to produce the click. See snapfit_*/detent_* for the underlying mechanism."),
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
        existing = {r["Name"].strip() for r in csv.DictReader(f) if r["Name"].strip()}

    rows, skipped = [], []
    for entry in NEW:
        name, unit, expr, comment = entry[0], entry[1], entry[2], entry[3]
        override = entry[4] if len(entry) > 4 else None
        if name in existing:
            skipped.append(name)
            continue
        value = override if override is not None else value_for(unit, expr)
        rows.append([name, unit, expr, value, comment, "True"])

    if skipped:
        print(f"Skipped {len(skipped)} already-present param(s).")
    if rows:
        with open(CSV, "a", newline="", encoding="utf-8") as f:
            csv.writer(f, lineterminator="\n").writerows(rows)
    print(f"Appended {len(rows)} parameters.")


if __name__ == "__main__":
    main()
