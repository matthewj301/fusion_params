#!/usr/bin/env python3
"""Append reference dimensions harvested from Maker_Shop_Dimensions_Reference.xlsx
and BB3D_MultiMount_BackEnd_Spec.md into the master parameter CSV.

Only CONFIRMED values are added (no STEP-import placeholders). Heat-set sizes use a
generic ~97%-of-OD rule rather than any single brand's published pilot.

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
    # --- Wall-mount systems (confirmed-only; STEP-import dims deliberately omitted) ---
    ("multiboard_tile_grid", "mm", "25.0", "Multiboard tile grid pitch (1 MU); snap and bolt accessories array on this. Source: multiboard.io"),
    ("multiboard_snap_standoff", "mm", "6.25", "Multiboard offset-snap mount standoff from the tile face. Source: multiboard.io"),
    ("multiboard_tol", "mm", "0.25", "Multiboard bolt/snap fit tolerance. Print 0.2 mm layer / 0.4 mm nozzle to match the ecosystem. Source: multiboard.io"),
    ("multiboard_bin_cu", "mm", "50.0", "Multiboard bin Cell Unit (1 CU) height step. Distinct from the 25 mm tile MU. Source: multiboard.io"),
    ("skadis_grid", "mm", "40.0", "IKEA SKADIS pegboard grid pitch (square). Source: dimensions.com"),
    ("skadis_slot_width", "mm", "5.0", "SKADIS oval slot width. M3 nut (5.5 mm AF) will not pass; accessories use M2/M2.5. Source: justhangingpegboards.com"),
    ("skadis_slot_height", "mm", "15.0", "SKADIS oval slot height."),
    ("gridfinity_grid", "mm", "42.0", "Gridfinity baseplate XY grid pitch. Source: github gridfinity spec"),
    ("gridfinity_z_unit", "mm", "7.0", "Gridfinity Z height unit (1U). Source: github gridfinity spec"),
    ("gridfinity_bin_foot", "mm", "41.5", "Gridfinity bin foot footprint (grid 42 minus 0.5 clearance); 0.25 mm tol. Source: github gridfinity spec"),
    ("gridfinity_baseplate_wall", "mm", "4.65", "Gridfinity baseplate wall height. Source: github gridfinity spec"),
    ("gridfinity_corner_fillet", "mm", "4.0", "Gridfinity bin/baseplate corner fillet radius. Source: github gridfinity spec"),
    ("gridfinity_stack_lip", "mm", "4.4", "Gridfinity stacking lip height. Source: github gridfinity spec"),
    ("hsw_grid", "mm", "42.58", "Honeycomb Storage Wall pitch across two staggered hexes (multi-point holders). Multiboard accepts HSW push-fits. Source: rostap / multiboard.io"),
    ("french_cleat_angle", "deg", "45", "French cleat bevel angle; wall strip and mating part share the 45 deg face. Source: shop standard"),
    ("french_cleat_stock", "mm", "18.3", "French cleat stock thickness = 3/4 in plywood actual. Source: US sheet-goods standard"),
    ("wall_control_grid", "mm", "25.4", "Wall Control metal pegboard hole spacing (1 in); accepts standard 1/4 in hooks. VERIFY exact hole size on your panel."),

    # --- Heat-set inserts, new sizes (generic ~97%-of-OD, NOT a single brand pilot) ---
    ("m2p5_heatset_hole", "mm", "3.30", "M2.5 heat-set hole ID. Generic ~97% of assumed 3.4 mm OD; verify/coupon-test your batch (brand-dependent). Depth = insert length + 0.2 mm."),
    ("m6_heatset_hole", "mm", "7.80", "M6 heat-set hole ID. Generic ~97% of assumed 8.0 mm OD; verify/coupon-test your batch. Depth = insert length + 0.2 mm."),
    ("m8_heatset_hole", "mm", "9.60", "M8 heat-set hole ID. Generic ~97% of assumed 9.9 mm OD; verify/coupon-test your batch. Depth = insert length + 0.2 mm."),
    ("m10_heatset_hole", "mm", "11.70", "M10 heat-set hole ID. Generic ~97% of assumed 12.0 mm OD; verify/coupon-test your batch. Depth = insert length + 0.2 mm."),

    # --- Hex nuts M6/M8/M10 (DIN 934 / ISO 4032) ---
    ("m6_hex_nut_af", "mm", "10.0", "M6 hex nut AF (DIN 934 / ISO 4032). Add ~0.2-0.3 mm for printed pockets."),
    ("m6_hex_nut_height", "mm", "5.2", "M6 hex nut height (ISO 4032)."),
    ("m8_hex_nut_af", "mm", "13.0", "M8 hex nut AF."),
    ("m8_hex_nut_height", "mm", "6.8", "M8 hex nut height."),
    ("m10_hex_nut_af", "mm", "17.0", "M10 hex nut AF."),
    ("m10_hex_nut_height", "mm", "8.4", "M10 hex nut height."),

    # --- Socket-head cap screw heads M6/M8 (DIN 912) ---
    ("m6_socket_head_dia", "mm", "10.0", "M6 socket cap head (DIN 912) OD. Counterbore slightly over head dia for clearance."),
    ("m6_socket_head_height", "mm", "6.0", "M6 socket cap head height."),
    ("m8_socket_head_dia", "mm", "13.0", "M8 socket cap head OD."),
    ("m8_socket_head_height", "mm", "8.0", "M8 socket cap head height."),

    # --- Tap drills M8/M10/M12 (aluminum, 75% thread) ---
    ("cnc_m8_tap_drill", "mm", "6.8", "M8x1.25 tap drill diameter in aluminum (75% thread). Source: ISO 261"),
    ("cnc_m10_tap_drill", "mm", "8.5", "M10x1.5 tap drill diameter in aluminum."),
    ("cnc_m12_tap_drill", "mm", "10.2", "M12x1.75 tap drill diameter in aluminum."),

    # --- Magnets, new sizes ---
    ("magnet_8x3mm_od", "mm", "8.0", "8x3 mm N42-N52 disc magnet OD. Press-fit pocket ~0.1 mm over."),
    ("magnet_8x3mm_height", "mm", "3.0", "8x3 mm magnet height."),
    ("magnet_12x3mm_od", "mm", "12.0", "12x3 mm disc magnet OD. Press-fit pocket ~0.1 mm over."),
    ("magnet_12x3mm_height", "mm", "3.0", "12x3 mm magnet height."),
    ("magnet_15x3mm_od", "mm", "15.0", "15x3 mm disc magnet OD."),
    ("magnet_15x3mm_height", "mm", "3.0", "15x3 mm magnet height."),
    ("magnet_20x2mm_od", "mm", "20.0", "20x2 mm disc magnet OD."),
    ("magnet_20x2mm_height", "mm", "2.0", "20x2 mm magnet height."),

    # --- Bearings (skate/idler staples; F695 already in CSV) ---
    ("bearing_608_id", "mm", "8.0", "608 bearing bore (skate bearing; filament rollers, idlers)."),
    ("bearing_608_od", "mm", "22.0", "608 bearing OD."),
    ("bearing_608_width", "mm", "7.0", "608 bearing width."),
    ("bearing_625_id", "mm", "5.0", "625 bearing bore (common idler)."),
    ("bearing_625_od", "mm", "16.0", "625 bearing OD."),
    ("bearing_625_width", "mm", "5.0", "625 bearing width."),
    ("bearing_623_id", "mm", "3.0", "623 bearing bore (small idler; F623 flanged variant common)."),
    ("bearing_623_od", "mm", "10.0", "623 bearing OD."),
    ("bearing_623_width", "mm", "4.0", "623 bearing width."),
    ("bearing_688_id", "mm", "8.0", "688 bearing bore (compact idler)."),
    ("bearing_688_od", "mm", "16.0", "688 bearing OD."),
    ("bearing_688_width", "mm", "5.0", "688 bearing width."),
    ("bearing_6802_id", "mm", "15.0", "6802 thin-section bearing bore."),
    ("bearing_6802_od", "mm", "24.0", "6802 bearing OD."),
    ("bearing_6802_width", "mm", "5.0", "6802 bearing width."),
    ("bearing_mr105_id", "mm", "5.0", "MR105 mini bearing bore."),
    ("bearing_mr105_od", "mm", "10.0", "MR105 bearing OD."),
    ("bearing_mr105_width", "mm", "4.0", "MR105 bearing width."),

    # --- EMT conduit OD (tube you design around for Maker-Pipe builds) ---
    ("emt_half_inch_od", "mm", "17.93", "1/2 in EMT conduit OD (ID 15.80, wall 1.07). Source: makerpipe/accio"),
    ("emt_three_quarter_inch_od", "mm", "23.42", "3/4 in EMT OD. Most common for Maker-Pipe-style builds."),
    ("emt_one_inch_od", "mm", "29.54", "1 in EMT OD (ID 26.64)."),
    ("emt_one_and_quarter_inch_od", "mm", "38.35", "1-1/4 in EMT OD."),

    # --- Lumber & sheet goods (nominal vs actual) ---
    ("plywood_half_inch_actual", "mm", "11.9", "1/2 in plywood actual thickness (~15/32). Usually 0.5-1 mm under nominal."),
    ("plywood_three_quarter_inch_actual", "mm", "18.3", "3/4 in plywood actual thickness (~23/32). Plan French-cleat stock around this."),
    ("mdf_half_inch_actual", "mm", "12.7", "1/2 in MDF actual thickness. MDF runs closer to nominal than plywood."),
    ("mdf_three_quarter_inch_actual", "mm", "19.0", "3/4 in MDF actual thickness."),
    ("lumber_2x4_thickness", "mm", "38.0", "2x4 softwood actual thickness (1.5 in)."),
    ("lumber_2x4_width", "mm", "89.0", "2x4 softwood actual width (3.5 in)."),
    ("lumber_2x6_width", "mm", "140.0", "2x6 softwood actual width (5.5 in). Thickness same as 2x4 (38 mm)."),
    ("lumber_1x4_width", "mm", "89.0", "1x4 softwood actual width (3.5 in). Thickness 19 mm (3/4 in)."),

    # --- Aluminum extrusion: slot widths + missing series widths ---
    ("vslot_2020_slot_width", "mm", "6.0", "20-series T-slot/V-slot opening; M5 bolt / 6 mm T-nut. V-slot opening ~6.2 mm. Source: wellste"),
    ("vslot_3030_extrusion_width", "mm", "30.0", "3030 extrusion nominal width."),
    ("vslot_3030_slot_width", "mm", "8.0", "3030 slot width (often 8.2); M6 bolt. Some 3030 are 6 mm slot - verify."),
    ("vslot_4040_extrusion_width", "mm", "40.0", "4040 extrusion nominal width."),
    ("vslot_4040_slot_width", "mm", "8.0", "4040 slot width; M8 bolt. Some makers do 10 mm slot - verify."),

    # --- Hand-tool square drives ---
    ("sq_drive_quarter_af", "mm", "6.35", "1/4 in square drive AF (the post a socket slips onto). Always inch-based."),
    ("sq_drive_three_eighth_af", "mm", "9.525", "3/8 in square drive AF."),
    ("sq_drive_half_af", "mm", "12.70", "1/2 in square drive AF."),
    ("sq_drive_three_quarter_af", "mm", "19.05", "3/4 in square drive AF."),
    ("sq_drive_one_inch_af", "mm", "25.40", "1 in square drive AF."),
    ("hex_bit_drive_af", "mm", "6.35", "1/4 in hex bit (insert) AF - driver/impact collet standard."),

    # --- BB3D house mount-rail dovetail (load-bearing wall holder; larger than dovetail_*) ---
    # Flank angle convention: measured from the part face (mating plane). Self-consistent family;
    # reuses dovetail_chamfer for the lead-in. Does NOT touch the legacy dovetail_* small joint.
    ("dovetail_mount_width", "mm", "24.0", "BB3D house mount-rail dovetail width at the wide (face) edge. Load-bearing wall-holder rail, larger than the generic dovetail_* joint. Lock once - never change."),
    ("dovetail_mount_depth", "mm", "6.0", "House mount-rail dovetail engagement depth. Narrow-edge width = 24 - 2*(depth/tan(angle)) ~= 17.1 mm at 60 deg."),
    ("dovetail_mount_angle", "deg", "60", "House mount-rail flank angle measured from the part face (mating plane). 60 deg = 30 deg undercut from vertical: strong lock, prints clean without support."),
    ("dovetail_mount_clearance", "mm", "0.20", "Per-surface slide clearance for the mount rail. Looser than dovetail_clearance (0.12) because the rail is larger and longer-travel."),

    # --- Electronics mounting (extends existing rpi/esp32) ---
    ("rpi_mount_hole_dia", "mm", "2.75", "Raspberry Pi 4/5 mounting hole diameter; M2.5 screws, 3.5 mm in from edges. Source: RPi mechanical spec"),
    ("rpi_pico_board_length", "mm", "51.0", "Raspberry Pi Pico board length. Source: RPi Pico datasheet"),
    ("rpi_pico_board_width", "mm", "21.0", "Raspberry Pi Pico board width."),
    ("rpi_pico_mount_pitch_x", "mm", "47.0", "Pico mounting hole pitch (long axis)."),
    ("rpi_pico_mount_pitch_y", "mm", "11.4", "Pico mounting hole pitch (short axis)."),
    ("rpi_pico_mount_hole_dia", "mm", "2.1", "Pico mounting hole diameter."),
    ("rpi_zero_board_length", "mm", "65.0", "Raspberry Pi Zero / Zero 2 W board length. Source: RPi mechanical spec"),
    ("rpi_zero_board_width", "mm", "30.0", "Raspberry Pi Zero board width."),
    ("rpi_zero_mount_pitch_x", "mm", "58.0", "Pi Zero mounting hole pitch (long axis)."),
    ("rpi_zero_mount_pitch_y", "mm", "23.0", "Pi Zero mounting hole pitch (short axis)."),
    ("din_rail_depth", "mm", "7.5", "TS35 top-hat DIN rail depth (also a 15 mm deep variant). Source: EN 60715"),
    ("header_pitch", "mm", "2.54", "Standard 0.1 in header/breadboard/protoboard pin pitch."),
]


def value_for(unit, expr):
    x = float(expr)
    if unit == "mm":
        v = x / 10.0
    elif unit == "deg":
        return repr(math.radians(x))  # full precision, matches existing deg rows
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
            skipped.append(name)  # idempotent: already present, leave it alone
            continue
        rows.append([name, unit, expr, value_for(unit, expr), comment, "True"])

    if skipped:
        print(f"Skipped {len(skipped)} already-present param(s).")

    if rows:
        with open(CSV, "a", newline="", encoding="utf-8") as f:
            csv.writer(f, lineterminator="\n").writerows(rows)

    print(f"Appended {len(rows)} parameters.")


if __name__ == "__main__":
    main()
