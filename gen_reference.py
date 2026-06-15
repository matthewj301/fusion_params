#!/usr/bin/env python3
"""Generate PARAMETER_REFERENCE.md from the themed split CSVs.

The reference is a coverage map — "check here before researching to avoid duplicating
existing coverage." Generating it from the split files means it can never drift from the
actual parameter set. Run after split_params.py.

Usage:
    python3 gen_reference.py
"""
import csv
import datetime
from pathlib import Path

SPLIT_DIR = Path("BakedBean3D_MasterParams_v4/split")
CSV_PATH = Path("BakedBean3D_MasterParams_v4/BakedBean3D_MasterParams_params.csv")
OUT = Path("PARAMETER_REFERENCE.md")

# Tiered display order + one-line descriptions (kept in sync with split_params.py)
THEMES = [
    ("design_rules", "Tier 1 · always import", "FDM tolerances, fit classes, walls, fillets, chamfers, overhangs, bridges, joints, locking mechanisms, materials"),
    ("fasteners", "Tier 1 · always import", "M2-M10 hardware, heat-set inserts, nut traps, counterbores, magnets, zip ties"),
    ("motion_mechanical", "Tier 2 · per project", "MGN rails, GT2 belts, ball bearings, NEMA motors, extrusion, CNC process params"),
    ("electronics_mounting", "Tier 2 · per project", "PCBs, header pitch, connectors, panel cutouts, DIN rail, home automation"),
    ("devices", "Tier 2 · per project", "phones, tablets, watches, controllers, remotes, chargers, smart home, cameras"),
    ("workshop", "Tier 2 · per project", "pegboard & wall systems (Multiboard/SKADIS/Gridfinity/HSW/French cleat), shop stock (EMT/lumber/sheet), power & hand tools, batteries, keys"),
    ("household_hobby", "Tier 2 · per project", "drinkware, EDC, cards, coins, paint, Warhammer, foam darts, bottles, cables, storage"),
    ("imperial_drills", "Tier 3 · specialized", "fractional drill bit table (1/64\" to 1\")"),
    ("wood_screws", "Tier 3 · specialized", "gauges #0-#20 with pilot/clearance/countersink"),
]

MAX_EXAMPLES = 8  # example names shown per family before eliding

# Curated coverage gaps — what's deliberately NOT yet in the set (preserved across regens).
WISHLIST = """\
## Coverage gaps (not yet in the set)

Candidates to add when a project needs them — recorded so we don't re-research the same gaps.

- **Batteries:** Ryobi ONE+, Bosch 18V, Milwaukee M12, DeWalt FLEXVOLT, larger XC/HO variants; C/D/9V/21700/CR123A cells; **battery dock-rail/slide interfaces (must be measured off a physical pack — not derivable from the envelope).**
- **Power tools:** jigsaws, recip saws, impact drivers/wrenches, multi-tools, routers, angle grinders; Ryobi/Bosch tool bodies.
- **Hand tools:** socket sets/ratchets, wire strippers, crimpers, clamps (bar/spring/C).
- **Wall systems:** slatwall slot profile; verify Wall Control hole size on the physical panel.
- **Devices:** Steam Deck, Switch Lite, Samsung/Garmin/Fitbit watches, more remotes (Samsung/LG/Harmony), HomePod Mini, Nest Hub.
- **Connectors/media:** Micro/Mini-USB, USB-B, CompactFlash, M.2 2230/2242, coax (RG6/RG59).
- **Hobby/household:** Tamiya/Scale75/AK paints, mason jars, essential-oil bottles, MTG/Pokemon card decks, more pill-bottle drams.
"""


def family_of(name):
    """Group key: first underscore token, but keep size-led hardware (m3_, ws9_, wago221_)
    together with their second token so families stay meaningful."""
    parts = name.split("_")
    return parts[0] if len(parts) == 1 else parts[0]


def load_theme(theme):
    path = SPLIT_DIR / f"{theme}.csv"
    if not path.exists():
        return []
    with open(path, newline="", encoding="utf-8") as f:
        return [r["Name"].strip() for r in csv.DictReader(f) if r["Name"].strip()]


def render_families(names):
    fams = {}
    for n in sorted(names):
        fams.setdefault(family_of(n), []).append(n)
    lines = []
    for fam, members in sorted(fams.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        shown = ", ".join(f"`{m}`" for m in members[:MAX_EXAMPLES])
        more = f" … (+{len(members) - MAX_EXAMPLES} more)" if len(members) > MAX_EXAMPLES else ""
        lines.append(f"- **{fam}** ({len(members)}) — {shown}{more}")
    return lines


def main():
    total = sum(1 for r in csv.DictReader(open(CSV_PATH, encoding="utf-8")) if r["Name"].strip())
    today = datetime.date.today().isoformat()

    out = []
    out.append("# BakedBean3D Master Parameters Reference")
    out.append("")
    out.append("Coverage map of the Fusion 360 master parameter library. **Check here (or grep the CSV) before "
               "researching new dimensions** — avoid duplicating existing coverage.")
    out.append("")
    out.append(f"- **Total parameters:** {total} (regenerated {today})")
    out.append(f"- **Source of truth:** `BakedBean3D_MasterParams_v4/BakedBean3D_MasterParams_params.csv` "
               f"(6-column Fusion format: Name, Unit, Expression, Value, Comment, Favorite)")
    out.append("- **This file is generated** — do not hand-edit. Run `python gen_reference.py` after "
               "`split_params.py`. Edit the `WISHLIST` block in the generator to change coverage-gap notes.")
    out.append("- **Naming:** component-first, snake_case, no `_mm`/ISO suffixes (e.g. `m3_button_head_dia`, "
               "`iphone16pro_width`). See `migration_mapping.csv` for old→new.")
    out.append("")
    out.append("Params are imported per project from the themed split CSVs (`split/`). Tiers below match "
               "`split_params.py`.")
    out.append("")

    for theme, tier, desc in THEMES:
        names = load_theme(theme)
        out.append("---")
        out.append("")
        out.append(f"## `{theme}` — {len(names)} params  ·  _{tier}_")
        out.append("")
        out.append(f"{desc}")
        out.append("")
        out.extend(render_families(names))
        out.append("")

    out.append("---")
    out.append("")
    out.append(WISHLIST)
    out.append("---")
    out.append("")
    out.append("## Adding new parameters")
    out.append("")
    out.append("1. Add rows to the master CSV (component-first names, Expression as a bare number, "
               "Value in cm — see `params/CLAUDE.md`). Scripted adds: pattern after `add_reference_dims.py`.")
    out.append("2. `python validate_params.py` — name format, units, duplicates, reference resolution.")
    out.append("3. `python split_params.py` — regenerate themed files. **New name prefix? Add it to the right "
               "`*_PREFIXES` set first**, or it silently falls into `design_rules`.")
    out.append("4. `python gen_reference.py` — regenerate this file.")
    out.append("5. Upload changed split CSVs to Admin Project > Parameters in Fusion; commit the submodule.")
    out.append("")

    OUT.write_text("\n".join(out), encoding="utf-8")
    print(f"Wrote {OUT} — {total} params across {len(THEMES)} themes.")


if __name__ == "__main__":
    main()
