# Controller board dimensions — moved to the hardware database

The 3D-printer **controller / toolhead / SBC / accessory board mounting dimensions**
(95 boards: BTT, Fysetc, Duet, MKS, Mellow, LDO, Huvud, and Voron/Klipper community
PCBs) now live in the dedicated, canonical hardware-database repo:

> **`3d-printer-hardware-database`** → `controller_boards/`
> https://github.com/BakedBean3D/3d-printer-hardware-database

That repo is the **single source of truth.** This data was previously duplicated here
in a nested YAML format; it was removed to prevent the two copies drifting apart.

## Consuming the data from this repo

### Option A — local symlink (default on this machine)

Both repos are siblings under `~/git`, so this directory contains a relative symlink:

```
controller_boards/canonical -> ../../3d-printer-hardware-database/controller_boards
```

Read the data through it directly:

```python
import yaml
boards = []
import glob
for f in glob.glob("controller_boards/canonical/*.yaml"):
    boards += yaml.safe_load(open(f)) or []
# or the prebuilt aggregate:
import json
boards = json.load(open("controller_boards/canonical/controller_boards.json"))
```

If the sibling repo isn't checked out, clone it next to this one:

```bash
git clone git@github.com:BakedBean3D/3d-printer-hardware-database.git ~/git/3d-printer-hardware-database
```

### Option B — git submodule (portable, for other machines)

```bash
git submodule add git@github.com:BakedBean3D/3d-printer-hardware-database.git hardware-db
# data at: hardware-db/controller_boards/
```

## Format

Flat-list YAML per manufacturer (`bigtreetech.yaml`, `fysetc.yaml`, `community.yaml`,
`modules.yaml`, …), plus a generated `controller_boards.json` aggregate and
`CONTROLLER_BOARDS.md` reference. Schema and conventions are documented in the hardware
database's `README.md` ("Controller board fields") and its `controller_boards/` directory.

Key conventions for parametric CAD use:
- `pcb_length_mm` = X (longer edge), `pcb_width_mm` = Y (shorter edge).
- `mount_holes_xy` = `[[x,y], …]` from the PCB bottom-left corner (read each entry's `notes`).
- `null` = genuinely unknown — **never assume 0**.
- `confidence`: `high` (vendor/community CAD) · `medium` (outline firm, pitch inferred) ·
  `low` (measure before cutting).

## Note on the Fusion master-parameter library

A handful of board mounting pitches already live as flat Fusion parameters in
`BakedBean3D_MasterParams_v4/split/electronics_mounting.csv` (e.g. `octopus_mount_pitch_x`,
`skr_mini_mount_pitch_y`). Those stay as-is for direct Fusion import; the hardware database
is the richer, authoritative geometry source for everything else.
