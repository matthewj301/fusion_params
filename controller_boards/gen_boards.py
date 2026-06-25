#!/usr/bin/env python3
"""Generate controller_boards.json (aggregate) and CONTROLLER_BOARDS.md (reference)
from the per-manufacturer YAML source files.

Source of truth = the *.yaml files (btt, fysetc, other_manufacturers, expansion_accessory).
Do not hand-edit the generated .json / .md — edit the YAML and re-run:  python gen_boards.py
"""
import yaml, json, os

HERE = os.path.dirname(os.path.abspath(__file__))
SRC_FILES = ["btt.yaml", "fysetc.yaml", "other_manufacturers.yaml", "expansion_accessory.yaml"]

CONF_RANK = {"high": 0, "medium": 1, "low": 2}


def load():
    boards = []
    for f in SRC_FILES:
        path = os.path.join(HERE, f)
        if not os.path.exists(path):
            continue
        doc = yaml.safe_load(open(path)) or {}
        for b in (doc.get("boards") or []):
            b["_source_file"] = f
            boards.append(b)
    return boards


def g(b, *keys, default=None):
    """Nested get."""
    cur = b
    for k in keys:
        if not isinstance(cur, dict):
            return default
        cur = cur.get(k)
        if cur is None:
            return default
    return cur


def fmt(v):
    return "" if v is None else v


def write_json(boards):
    out = os.path.join(HERE, "controller_boards.json")
    clean = []
    for b in boards:
        c = {k: v for k, v in b.items() if not k.startswith("_")}
        c["_source_file"] = b["_source_file"]
        clean.append(c)
    with open(out, "w") as fh:
        json.dump({"boards": clean, "count": len(clean)}, fh, indent=2)
    return out


def md_table(boards):
    rows = []
    rows.append("| Board | Cat | PCB L×W (mm) | Thick | Screw | Hole Ø | Pattern | Pitch X×Y (mm) | Holes | Conf |")
    rows.append("|---|---|---|---|---|---|---|---|---|---|")
    for b in boards:
        L = g(b, "pcb", "length_mm"); W = g(b, "pcb", "width_mm")
        lw = f"{fmt(L)}×{fmt(W)}" if (L or W) else "—"
        thick = fmt(g(b, "pcb", "thickness_mm"))
        screw = fmt(g(b, "mounting", "screw"))
        hd = fmt(g(b, "mounting", "hole_dia_mm"))
        pat = fmt(g(b, "mounting", "pattern"))
        px = g(b, "mounting", "pitch_x_mm"); py = g(b, "mounting", "pitch_y_mm")
        pitch = f"{fmt(px)}×{fmt(py)}" if (px or py) else "—"
        hc = fmt(g(b, "mounting", "hole_count"))
        conf = b.get("confidence", "")
        name = b.get("name", b.get("id"))
        rows.append(f"| {name} | {b.get('category','')} | {lw} | {thick} | {screw} | {hd} | {pat} | {pitch} | {hc} | {conf} |")
    return "\n".join(rows)


def write_md(boards):
    out = os.path.join(HERE, "CONTROLLER_BOARDS.md")
    from collections import Counter, defaultdict
    conf = Counter(b.get("confidence") for b in boards)
    by_mfr = defaultdict(list)
    for b in boards:
        by_mfr[b.get("manufacturer", "?")].append(b)

    lines = []
    lines.append("# 3D Printer Controller Board Dimensions")
    lines.append("")
    lines.append("Mechanical / mounting reference for parametric CAD mount design. "
                 "**Generated** from the YAML source files in this directory — do not hand-edit; "
                 "run `python gen_boards.py` after editing the `*.yaml`.")
    lines.append("")
    lines.append(f"- **Total boards:** {len(boards)}")
    lines.append(f"- **Confidence:** {conf.get('high',0)} high · {conf.get('medium',0)} medium · {conf.get('low',0)} low")
    lines.append(f"- **Source files:** `btt.yaml`, `fysetc.yaml`, `other_manufacturers.yaml`, `expansion_accessory.yaml`")
    lines.append("- **Aggregate for code:** `controller_boards.json`")
    lines.append("")
    lines.append("## Conventions")
    lines.append("")
    lines.append("- **length_mm = X** (longer edge), **width_mm = Y** (shorter edge).")
    lines.append("- **pitch_x/pitch_y** = center-to-center mounting-hole spacing.")
    lines.append("- **holes_xy_mm** (where present) = each hole `[x, y]` from the PCB **bottom-left corner** "
                 "unless that board's `notes`/`verify_notes` say otherwise (some are referenced to a drawing datum — read the note).")
    lines.append("- **hole_dia_mm** is usually inferred from the screw size (M3→3.2, M2.5→2.7) — vendor SIZE drawings rarely annotate the bore. Treat as nominal clearance.")
    lines.append("- **thickness_mm** defaults to 1.6 (standard PCB) where unstated.")
    lines.append("- **Confidence:** `high` = from vendor CAD/dimensioned drawing; `medium` = PCB size authoritative but hole pitch inferred; `low` = size/holes not authoritatively found — **measure before cutting.**")
    lines.append("- Always read each board's `verify_notes` before committing geometry. For tight tolerances, pull the vendor STEP/Gerber.")
    lines.append("")
    lines.append("## All boards")
    lines.append("")
    lines.append(md_table(sorted(boards, key=lambda b: (b.get("manufacturer",""), b.get("name","")))))
    lines.append("")

    for mfr in sorted(by_mfr):
        lines.append(f"## {mfr}")
        lines.append("")
        for b in sorted(by_mfr[mfr], key=lambda b: b.get("name","")):
            lines.append(f"### {b.get('name')}  ·  `{b.get('id')}`")
            lines.append("")
            lines.append(f"- **Category:** {b.get('category')}  ·  **Confidence:** {b.get('confidence')}")
            L = g(b,'pcb','length_mm'); W = g(b,'pcb','width_mm'); T = g(b,'pcb','thickness_mm')
            lines.append(f"- **PCB:** {fmt(L)} × {fmt(W)} mm, {fmt(T)} mm thick")
            m = b.get("mounting") or {}
            lines.append(f"- **Mounting:** {fmt(m.get('hole_count'))}× {fmt(m.get('screw'))} (Ø{fmt(m.get('hole_dia_mm'))}), "
                         f"pattern {fmt(m.get('pattern'))}, pitch {fmt(m.get('pitch_x_mm'))}×{fmt(m.get('pitch_y_mm'))} mm")
            if m.get("holes_xy_mm"):
                lines.append(f"  - holes (x,y mm): {m['holes_xy_mm']}")
            if m.get("notes"):
                lines.append(f"  - notes: {m['notes']}")
            sh = g(b,'thickness_clearance','standoff_height_mm'); ch = g(b,'thickness_clearance','component_height_top_mm')
            if sh is not None or ch is not None:
                lines.append(f"- **Clearance:** standoff {fmt(sh)} mm, top component {fmt(ch)} mm")
            cn = g(b,'connectors','notes')
            if cn:
                lines.append(f"- **Connectors:** {cn}")
            if b.get("verify_notes"):
                lines.append(f"- **⚠ Verify:** {b['verify_notes']}")
            for s in (b.get("sources") or []):
                lines.append(f"- src: {s}")
            lines.append("")
    with open(out, "w") as fh:
        fh.write("\n".join(lines))
    return out


if __name__ == "__main__":
    boards = load()
    j = write_json(boards)
    m = write_md(boards)
    print(f"{len(boards)} boards -> {os.path.basename(j)}, {os.path.basename(m)}")
