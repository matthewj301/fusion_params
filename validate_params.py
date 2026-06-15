#!/usr/bin/env python3
"""Validate the master parameter CSV for name format, duplicates, units, and references.

Supports both the 6-column Fusion native format (Name, Unit, Expression, Value, Comment, Favorite)
and the legacy 4-column format (Name, Expression, Unit, Comment).

Usage:
    python3 validate_params.py [--csv PATH]

Defaults:
    --csv  BakedBean3D_MasterParams_v4/BakedBean3D_MasterParams_params.csv
"""

import argparse
import csv
import re
import sys
from pathlib import Path

PARAM_NAME_RE = re.compile(r"^[a-z][a-z0-9_]*$")
FUSION_NATIVE_UNITS = {"mm", "cm", "in", "deg", "rad", ""}
DIMENSIONLESS_UNITS = {"count", "x", "%", "ratio", "°C", "A", "µm/mm"}
VALID_UNITS = FUSION_NATIVE_UNITS | DIMENSIONLESS_UNITS
UNIT_SUFFIXES = {"mm", "cm", "deg", "rad"}
FUSION_BUILTINS = {
    "cos", "sin", "tan", "acos", "asin", "atan", "atan2",
    "sqrt", "abs", "ceil", "floor", "round", "min", "max",
    "exp", "log", "log10", "pow", "mod", "sign", "truncate",
}

FUSION_6COL_HEADER = ["Name", "Unit", "Expression", "Value", "Comment", "Favorite"]
LEGACY_4COL_HEADER = ["Name", "Expression", "Unit", "Comment"]


def extract_references(expression):
    tokens = set(re.findall(r"[a-z][a-z0-9_]{2,}", str(expression)))
    return tokens - UNIT_SUFFIXES - FUSION_BUILTINS


def main():
    parser = argparse.ArgumentParser(description="Validate master parameter CSV")
    parser.add_argument(
        "--csv",
        default="BakedBean3D_MasterParams_v4/BakedBean3D_MasterParams_params.csv",
    )
    args = parser.parse_args()

    csv_path = Path(args.csv)
    if not csv_path.exists():
        print(f"ERROR: {csv_path} not found", file=sys.stderr)
        sys.exit(1)

    params = []
    errors = []
    seen = {}

    with open(csv_path, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        header = reader.fieldnames

        if header[:6] == FUSION_6COL_HEADER:
            fmt = "fusion6"
        elif header[:4] == LEGACY_4COL_HEADER:
            fmt = "legacy4"
        else:
            print(f"ERROR: unrecognized header: {header}", file=sys.stderr)
            sys.exit(1)

        for row_num, row in enumerate(reader, start=2):
            name = row["Name"].strip()
            if not name:
                continue

            if fmt == "fusion6":
                expr = row["Expression"].strip()
                unit = row["Unit"].strip()
            else:
                expr = row["Expression"].strip()
                unit = row["Unit"].strip()

            if not PARAM_NAME_RE.match(name):
                errors.append(f"  Row {row_num}: invalid name '{name}'")
            if name in seen:
                errors.append(
                    f"  Row {row_num}: duplicate '{name}' (first at row {seen[name]})"
                )
            if unit not in VALID_UNITS:
                errors.append(f"  Row {row_num}: invalid unit '{unit}'")
            if not expr:
                errors.append(f"  Row {row_num}: missing expression for '{name}'")

            seen[name] = row_num
            params.append({"name": name, "expression": expr, "row": row_num})

    all_names = set(seen.keys())
    for p in params:
        refs = extract_references(p["expression"])
        missing = refs - all_names
        if missing:
            errors.append(
                f"  Row {p['row']}: '{p['name']}' references undefined: {', '.join(sorted(missing))}"
            )

    if errors:
        print(f"FAILED — {len(errors)} error(s):", file=sys.stderr)
        for e in errors:
            print(e, file=sys.stderr)
        sys.exit(1)

    base = sum(1 for p in params if not extract_references(p["expression"]))
    derived = len(params) - base
    print(f"OK — {len(params)} parameters ({base} base, {derived} derived) [{fmt} format]")


if __name__ == "__main__":
    main()
