# Controller board dimensions

Mechanical/mounting dataset for **78** 3D-printer controller, toolhead, SBC, and
accessory boards — built for parametric CAD mount design. Researched 2026-06-25.

## Files

| File | Role |
|---|---|
| `btt.yaml` | BigTreeTech — mainboards, EBB toolhead CAN, CB1/CB2, U2C, KNOMI (23) |
| `fysetc.yaml` | Fysetc — Spider/Cheetah/S6/Catalyst/SB CAN/UCAN/Mini12864 (13) |
| `other_manufacturers.yaml` | Duet, MKS, Mellow, LDO, Huvud (22) |
| `expansion_accessory.yaml` | TMC drivers, PT100/PT1000 amps, accelerometers, relays, SSR, buck/MOSFET (20) |
| `controller_boards.json` | **Generated** aggregate of all of the above — use this in code/scripts |
| `CONTROLLER_BOARDS.md` | **Generated** human-readable reference (summary table + per-board detail) |
| `gen_boards.py` | Regenerates the `.json` and `.md` from the YAML. Run after editing any YAML. |

**The YAML files are the source of truth.** Edit them, then run `python gen_boards.py`.
Do not hand-edit the `.json` / `.md`.

## Schema (per board)

```yaml
- id:            # unique, snake_case, manufacturer-prefixed
  manufacturer:
  name:
  category:      # mainboard | toolhead_can | sbc | usb_can_bridge | driver_module
                 # | thermocouple_amp | accelerometer | relay | ssr | buck_converter
                 # | mosfet | sensor | accessory
  pcb:
    length_mm:   # X = longer edge
    width_mm:    # Y = shorter edge
    thickness_mm:
  mounting:
    screw:           # M-size that fits the holes (null if header-mounted only)
    hole_dia_mm:
    pattern:         # rectangular | L-shaped | linear | 2-hole | 3-hole | none | other
    pitch_x_mm:      # center-to-center along X
    pitch_y_mm:      # center-to-center along Y
    hole_count:
    holes_xy_mm:     # optional: [[x,y], ...] from PCB bottom-left corner (read notes — some use a drawing datum)
    inset_from_edge_mm:
    notes:
  thickness_clearance:
    standoff_height_mm:        # recommended clearance under the board
    component_height_top_mm:   # tallest component / module body height above board
  connectors:
    notes:           # which edge carries power / steppers / USB / etc.
  sources: []        # datasheet / GitHub hardware repo / drawing URLs
  confidence:        # high | medium | low
  verify_notes:      # what the human should double-check before cutting
```

## Reading the data — important conventions

- **`confidence`** is load-bearing:
  - `high` — from a vendor CAD file or dimensioned drawing. Print-ready.
  - `medium` — PCB outline authoritative, but hole **pitch** inferred / not vendor-published.
  - `low` — size and/or holes not found in any authoritative source. **Measure before cutting.**
- **`hole_dia_mm`** is usually inferred from the screw callout (M3→3.2, M2.5→2.7); vendor SIZE
  drawings rarely annotate the bore. Treat as nominal clearance.
- **`thickness_mm`** defaults to 1.6 (standard PCB) where unstated.
- **`holes_xy_mm`** origin is the PCB bottom-left corner *unless the board's notes say it is
  referenced to a drawing datum* (several BTT toolhead boards are) — always read the note.
- For tight-tolerance work, pull the vendor **STEP/Gerber** named in `sources` — the dataset
  captures the design intent, not a substitute for the manufacturer's CAD.

## Known shared / copied footprints (call-outs in the data)

- BTT **Octopus** and **Octopus Pro** share one footprint (160×100 outline, 150×90 pitch).
- Fysetc **Spider** line copies the **Voron 2.4/Trident** mount; **Cheetah V2/V3** copies the
  **Creality Ender 3/5** mount; **Catalyst** is a **Voron 0** board.
- The **StepStick / Pololu** carrier (15.24×20.32 mm, header-mounted) is shared by TMC2208/2209/5160
  plug-ins and the BTT MAX31865.
- The **43.84 mm 2-hole** spacing recurs on Mellow SHT36 and LDO Nitehawk-36 (a real toolhead-PCB
  standard); the **NEMA17 31×31** pattern is confirmed only for SHT42, MKS THR42, HuvudTiny, EBB42.

## Coverage gaps flagged by research (low confidence — verify with calipers)

- BTT **U2C V3** appears not to exist (V1.x / V2.x only); "3" in listings = 3 CAN outputs.
- BTT **EBB SB2209 RP2040** — no official size drawing; dims inferred from CAN sibling.
- Fysetc **Catalyst**, **SB CAN toolhead**, **Spider King** hole pitch — not authoritatively published.
- Mellow **Fly-UTOC**, **Gemini/CDY**, LDO **Nitehawk-SB/36** — STEP/PDF didn't yield clean PCB outlines.
- 1-/2-channel relay clones, Fotek SSR exact bore, heatbed MOSFET hole pitch — non-standardized clones.
