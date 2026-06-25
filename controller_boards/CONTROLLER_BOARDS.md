# 3D Printer Controller Board Dimensions

Mechanical / mounting reference for parametric CAD mount design. **Generated** from the YAML source files in this directory — do not hand-edit; run `python gen_boards.py` after editing the `*.yaml`.

- **Total boards:** 78
- **Confidence:** 38 high · 27 medium · 13 low
- **Source files:** `btt.yaml`, `fysetc.yaml`, `other_manufacturers.yaml`, `expansion_accessory.yaml`
- **Aggregate for code:** `controller_boards.json`

## Conventions

- **length_mm = X** (longer edge), **width_mm = Y** (shorter edge).
- **pitch_x/pitch_y** = center-to-center mounting-hole spacing.
- **holes_xy_mm** (where present) = each hole `[x, y]` from the PCB **bottom-left corner** unless that board's `notes`/`verify_notes` say otherwise (some are referenced to a drawing datum — read the note).
- **hole_dia_mm** is usually inferred from the screw size (M3→3.2, M2.5→2.7) — vendor SIZE drawings rarely annotate the bore. Treat as nominal clearance.
- **thickness_mm** defaults to 1.6 (standard PCB) where unstated.
- **Confidence:** `high` = from vendor CAD/dimensioned drawing; `medium` = PCB size authoritative but hole pitch inferred; `low` = size/holes not authoritatively found — **measure before cutting.**
- Always read each board's `verify_notes` before committing geometry. For tight tolerances, pull the vendor STEP/Gerber.

## All boards

| Board | Cat | PCB L×W (mm) | Thick | Screw | Hole Ø | Pattern | Pitch X×Y (mm) | Holes | Conf |
|---|---|---|---|---|---|---|---|---|---|
| Adafruit MAX31865 PT100/PT1000 RTD amplifier (PID 3328/3648) | thermocouple_amp | 24.38×22.86 | 1.6 | M2.5 | 2.54 | 2-hole | 22.86×0.0 | 2 | high |
| BTT ADXL345 V2.0 (USB-C, onboard RP2040) | accelerometer | 28.25×15.5 | 1.6 | M3 |  | 2-hole | 15.5× | 2 | high |
| BTT MAX31865 V2.0 PT100/PT1000 RTD amplifier | thermocouple_amp | 20.32×15.24 | 1.6 |  |  | none(header-mounted) | 15.24×2.54 | 0 | high |
| BTT Relay V1.2 module | relay | 80.32×36.19 | 1.6 | M3 | 3.2 | rectangular | 74.17×29.21 | 4 | high |
| BTT S2DW V1.0 (LIS2DW, USB-C) | accelerometer | 28.25×15.5 | 1.6 | M3 |  | 2-hole | 15.5× | 2 | high |
| BTT Smart Filament Sensor (SFS) V1.0 | sensor | 75.0×30.0 |  | M3 | 3.2 | rectangular | 56.75×20.35 | 4 | high |
| BTT TMC5160T Plus V1.0 external high-power stepper driver | driver_module | 50.0×50.0 | 1.6 | M3 | 3.2 | rectangular | 42.0×42.0 | 4 | high |
| CB1 | sbc | 55.0×40.0 | 1.6 | M2.5 | 2.7 | rectangular | 48.0×33.0 | 4 | medium |
| CB2 | sbc | 55.0×40.0 | 1.6 | M2.5 | 2.7 | rectangular | 48.0×33.0 | 4 | medium |
| EBB SB2209 CAN V1.0 | toolhead_can | 68.54×42.45 | 1.6 | M3 | 3.2 | linear | 12.78×12.03 | 2 | high |
| EBB SB2209 CAN V1.0 (RP2040) | toolhead_can | 68.54×42.45 | 1.6 | M3 | 3.2 | linear | 12.78×12.0 | 2 | low |
| EBB SB2240 CAN V1.0 | toolhead_can | 68.54×42.45 | 1.6 | M3 | 3.2 | linear | 12.78×12.02 | 2 | high |
| EBB36 CAN V1.x | toolhead_can | 51.4×37.0 | 1.6 | M3 | 3.2 | linear | 43.85×0 | 2 | medium |
| EBB42 CAN V1.x | toolhead_can | 40.0×40.0 | 1.6 | M3 | 3.2 | rectangular | 31.0×31.0 | 4 | high |
| KNOMI | accessory | 37.86×34.53 | 1.6 |  |  | other-describe | — | 0 | high |
| KNOMI 2 | accessory | 41.12×38.48 | 1.6 |  |  | other-describe | — | 0 | high |
| Kraken (V1.0/V1.1) | mainboard | 200.0×113.0 | 1.6 | M3 | 3.2 | rectangular | 193.0×106.03 | 4 | medium |
| Manta E3EZ | mainboard | 120.0×90.81 | 1.6 | M3 | 3.2 | other-describe | — | 4 | medium |
| Manta M4P | mainboard | 160.0×95.0 | 1.6 | M3 | 3.2 | other-describe | 97.0×84.2 | 4 | medium |
| Manta M5P | mainboard | 137.39×95.0 | 1.6 | M3 | 3.2 | rectangular | ×86.5 | 4 | medium |
| Manta M8P V1.1 | mainboard | 169.93×102.74 | 1.6 | M3 | 3.2 | other-describe | — | 6 | medium |
| Manta M8P V2.0 | mainboard | 169.93×102.74 | 1.6 | M3 | 3.2 | other-describe | — | 6 | medium |
| Octopus Pro V1.x (V1.0/V1.1) | mainboard | 160.0×100.0 | 1.6 | M3 | 3.2 | rectangular | 150.0×90.0 | 4 | high |
| Octopus V1.1 | mainboard | 160.0×100.0 | 1.6 | M3 | 3.2 | rectangular | 150.0×90.0 | 4 | high |
| SKR 3 | mainboard | 109.67×84.3 | 1.6 | M3 | 3.2 | rectangular | 101.85×76.3 | 4 | high |
| SKR 3 EZ | mainboard | 109.67×84.3 | 1.6 | M3 | 3.2 | rectangular | 101.85×76.3 | 4 | high |
| SKR Mini E3 V3 | mainboard | 103.75×70.25 | 1.6 | M3 | 3.2 | other-describe | — | 6 | medium |
| SKR Pico | mainboard | 85.0×56.0 | 1.6 | M2.5 | 2.75 | rectangular | 58.0×49.0 | 4 | high |
| U2C V2 (V2.0/V2.1) | usb_can_bridge | 85.45×25.35 | 1.6 | M3 |  | rectangular | ×19.23 | 4 | medium |
| U2C V3 | usb_can_bridge | — |  |  |  |  | — |  | low |
| Duet 2 WiFi / Ethernet | mainboard | 123.0×100.0 | 1.6 | M3 | 4.2 | rectangular | 92.0×115.0 | 4 | high |
| Duet 3 Mainboard 6HC | mainboard | 140.0×134.0 | 1.6 | M3 | 4.3 | rectangular | 124.0×130.0 | 4 | high |
| Duet 3 Mainboard 6XD | mainboard | 140.0×115.0 | 1.6 | M3 | 4.3 | rectangular | 104.5×129.5 | 4 | high |
| Duet 3 Mini 5+ | mainboard | 123.0×100.0 | 1.6 | M3 | 4.3 | rectangular | 92.0×115.0 | 4 | high |
| Duet 3 Toolboard 1LC | toolhead_can | 54.0×47.0 | 1.6 | M3 | 3.2 | rectangular | 34.0×34.0 | 4 | high |
| Duet3D PT100 temperature daughterboard v1.1 | thermocouple_amp | 31.74×26.16 | 1.6 |  | 2.54 | 2-hole | 38.5×0.0 | 2 | high |
| Fotek SSR-25DA solid state relay (SSR-DA series body) | ssr | 57.4×44.8 | 28.0 | M4 | 4.8 | 2-hole | 47.6×0.0 | 2 | medium |
| Catalyst V2.0 | mainboard | — | 1.6 | M3 | 3.2 | rectangular | — | 4 | low |
| Cheetah V2.0 | mainboard | 101.5×72.0 | 1.6 | M3 | 3.2 | rectangular | — | 4 | medium |
| Cheetah V3.0 | mainboard | 101.5×72.0 | 1.6 | M3 | 3.2 | rectangular | — | 4 | medium |
| Mini12864 Panel (RGB) V2.1 | accessory | 104.99×47.0 | 1.6 | M3 | 3.2 | rectangular | 41.0×93.0 | 4 | high |
| S6 V1.2 | mainboard | 117.0×87.0 | 1.6 | M3 | 3.2 | rectangular | — |  | medium |
| SB CAN Toolhead (V1.1 / V1.3) | toolhead_can | — | 1.6 | M3 | 3.2 | rectangular | — | 2 | low |
| Spider King V1.0 | mainboard | 177.0×108.0 | 1.6 | M3 | 3.2 | rectangular | — |  | medium |
| Spider Pro V1.2 | mainboard | 179.0×109.0 | 1.6 | M3 | 3.2 | rectangular | 92.0×92.0 | 4 | high |
| Spider V1.x | mainboard | 155.3×76.5 | 1.6 | M3 | 3.2 | rectangular | — | 4 | medium |
| Spider V2.2 | mainboard | 155.3×76.5 | 1.6 | M3 | 3.2 | rectangular | — | 4 | medium |
| Spider V3 (V3.0) | mainboard | 155.3×76.5 | 1.6 | M3 | 3.2 | rectangular | — | 4 | medium |
| Spider V3.0 H7 | mainboard | 155.3×76.5 | 1.6 | M3 | 3.2 | rectangular | — | 4 | medium |
| UCAN V1.0 | usb_can_bridge | — | 1.6 |  |  | other | — | 0 | low |
| 3D printer heatbed MOSFET power module (25A) | mosfet | 60.0×50.0 | 1.6 | M3 | 3.2 | rectangular | — | 4 | medium |
| GY-291 ADXL345 accelerometer breakout | accelerometer | 20.4×15.8 | 1.6 | M3 | 3.0 | 2-hole | 15.0×0.0 | 2 | medium |
| LM2596 adjustable buck converter module | buck_converter | 43.2×21.0 | 1.6 | M3 |  | 2-hole | — | 2 | medium |
| Mini-360 DC-DC buck converter module | buck_converter | 22.0×17.0 | 1.6 |  |  | none | — | 0 | medium |
| TMC2208 StepStick driver module | driver_module | 20.32×15.24 | 1.6 |  |  | none(header-mounted) | 15.24×2.54 | 0 | high |
| TMC5160 plug-in StepStick driver module | driver_module | 20.32×15.24 | 1.6 |  |  | none(header-mounted) | 15.24×2.54 | 0 | medium |
| 1-channel 5V relay module | relay | 50.0×26.0 | 1.6 | M3 | 3.1 | 2-hole | — | 2 | low |
| 2-channel 5V relay module | relay | 50.5×38.5 | 1.6 | M3 | 3.1 | rectangular | — | 4 | low |
| 4-channel 5V relay module | relay | 71.0×45.0 | 1.6 | M3 | 3.1 | rectangular | 66.7×40.0 | 4 | medium |
| TMC2209 StepStick / SilentStepStick driver module | driver_module | 20.32×15.24 | 1.6 |  |  | none(header-mounted) | 15.24×2.54 | 0 | high |
| HartK Stealthburner Toolhead PCB | toolhead_can | — | 1.6 | M3 | 3.2 | other | — |  | low |
| Huvud (original) | toolhead_can | 48.0×45.0 | 1.6 | M3 | 3.2 | rectangular | 37.0×40.0 | 4 | high |
| HuvudTiny | toolhead_can | 42.0×42.0 | 1.6 | M3 | 3.2 | rectangular | 31.0×31.0 | 4 | high |
| LDO Leviathan (V1.2/V1.3) | mainboard | 170.0×100.0 | 1.6 | M3 | 3.2 | rectangular | 160.0×90.0 | 4 | high |
| LDO Nitehawk-36 | toolhead_can | — | 1.6 | M3 | 3.2 | other | 43.84× |  | low |
| LDO Nitehawk-SB | toolhead_can | — | 1.6 | M3 | 3.2 | other | — |  | low |
| MKS CANable V2.0 | usb_can_bridge | 45.0×16.2 | 1.6 | M2 | 2.2 | rectangular | 34.7×12.6 | 4 | high |
| MKS Monster8 V2.0 | mainboard | 160.0×90.0 | 1.6 | M3 | 3.2 | rectangular | 152.0×82.0 | 4 | medium |
| MKS Robin Nano V3.x | mainboard | 110.0×84.0 | 1.6 | M3 | 3.4 | rectangular | 102.0×76.5 | 4 | high |
| MKS SKIPR V1.0 | mainboard | 160.0×100.0 | 1.6 | M3 | 3.2 | rectangular | 152.0×92.0 | 4 | high |
| MKS THR42 V1.0 | toolhead_can | 42.0×42.0 | 1.6 | M3 | 3.2 | rectangular | 31.0×31.0 | 4 | high |
| Fly Gemini V2/V3 (formerly Fly-CDY) | mainboard | — | 1.6 | M3 | 3.2 | rectangular | 143.0×78.0 | 4 | low |
| Fly Super8 | mainboard | 155.58×109.68 | 1.6 | M3 | 3.2 | rectangular | 149.38×103.45 | 4 | high |
| Fly-SHT36 (v1) | toolhead_can | 51.27×36.26 | 1.6 | M3 | 3.2 | linear | 43.84×0.0 | 2 | high |
| Fly-SHT36 v2.0 | toolhead_can | 51.27×45.67 | 1.6 | M3 | 3.2 | linear | 43.84×0.0 | 2 | high |
| Fly-SHT42 | toolhead_can | 42.0×42.0 | 1.6 | M3 | 3.2 | rectangular | 31.0×31.0 | 4 | high |
| Fly-UTOC (UTOC-1 / UTOC-3) | usb_can_bridge | 85.45×19.23 | 1.6 | M2 |  | rectangular | 79.33× | 4 | low |
| Slice Engineering PT1000/PT100 RTD amplifier (does not exist as a PCB) | thermocouple_amp | — |  |  |  | other | — | 0 | low |

## Adafruit

### Adafruit MAX31865 PT100/PT1000 RTD amplifier (PID 3328/3648)  ·  `adafruit_max31865`

- **Category:** thermocouple_amp  ·  **Confidence:** high
- **PCB:** 24.38 × 22.86 mm, 1.6 mm thick
- **Mounting:** 2× M2.5 (Ø2.54), pattern 2-hole, pitch 22.86×0.0 mm
  - holes (x,y mm): [[1.27, 2.54], [24.13, 2.54]]
  - notes: Two mounting tabs at the screw-terminal end. PCB body 24.38 x 22.86 mm; OVERALL incl. tabs 27.94 x 25.4 mm. Decide whether your mount uses the body or the tabbed outline. Holes Ø2.54 mm = M2.5, NOT M3.
- **Clearance:** standoff  mm, top component 3.0 mm
- **Connectors:** Two 2-pin 3.5 mm screw terminals (RTD); 9-pin 0.1in breakout header (VIN/3V3/GND/CLK/SDO/SDI/CS/RDY).
- **⚠ Verify:** Outline and Ø2.54 holes from Adafruit fab print p.30 (high). Screw size medium: Adafruit/distributor text inconsistent (M2.5 vs M3); physical bore = 2.54 mm => M2.5. PT1000 sibling 3648 is the identical PCB.
- src: https://cdn-learn.adafruit.com/downloads/pdf/adafruit-max31865-rtd-pt100-amplifier.pdf
- src: https://www.adafruit.com/product/3328

## BIGTREETECH

### BTT ADXL345 V2.0 (USB-C, onboard RP2040)  ·  `btt_adxl345_v2`

- **Category:** accelerometer  ·  **Confidence:** high
- **PCB:** 28.25 × 15.5 mm, 1.6 mm thick
- **Mounting:** 2× M3 (Ø), pattern 2-hole, pitch 15.5× mm
  - notes: 2-hole M3 mount at 15.5 mm spacing (GY-291 compatible). Ships with M3 screws + rubber rings. Exact hole diameter not given in manual; the separate "...V2.0-SIZE.pdf" in the repo has full coords if needed.
- **Connectors:** USB-C (USB 2.0), onboard RP2040, BOOT button, reserved solder pads. No accelerometer pin header.
- **⚠ Verify:** Board size (28.25 x 15.5 / 33.25 overall) and 15.5 mm hole pitch high (official manual p.5). Exact hole diameter low (not stated). Absolute hole coords medium.
- src: https://github.com/bigtreetech/ADXL345
- src: https://global.bttwiki.com/ADXL345.html

### BTT MAX31865 V2.0 PT100/PT1000 RTD amplifier  ·  `btt_max31865`

- **Category:** thermocouple_amp  ·  **Confidence:** high
- **PCB:** 20.32 × 15.24 mm, 1.6 mm thick
- **Mounting:** 0×  (Ø), pattern none(header-mounted), pitch 15.24×2.54 mm
  - notes: NO mounting holes. Uses the standard StepStick/stepper-driver footprint (manual states it "adopts the same package of motor drive module") and plugs into a spare SPI-capable stepper-driver socket via 2x 1x8 headers. Do NOT design a screw bracket for this board.
- **Connectors:** 2x 1x8 0.1in headers; screw terminal for RTD wires; DIP switch for 2/3/4-wire & PT100/PT1000.
- **⚠ Verify:** 15.24 x 20.32 from official manual p.5; header-mounted, no screw holes.
- src: https://github.com/bigtreetech/BIGTREETECH-MAX31865
- src: https://raw.githubusercontent.com/bigtreetech/BIGTREETECH-MAX31865/master/BIGTREETECH%20MAX31865%20V2.0/BIGTREETECH%20MAX31865%20V2.0%20Manual.pdf

### BTT Relay V1.2 module  ·  `btt_relay_v1_2`

- **Category:** relay  ·  **Confidence:** high
- **PCB:** 80.32 × 36.19 mm, 1.6 mm thick
- **Mounting:** 4× M3 (Ø3.2), pattern rectangular, pitch 74.17×29.21 mm
  - holes (x,y mm): [[3.075, 3.49], [77.245, 3.49], [3.075, 32.7], [77.245, 32.7]]
  - notes: 80.32 x 36.19 mm, 4 holes at 74.17 x 29.21 mm pitch (from official drawing). HIGH-VOLTAGE board (85-265 VAC) - keep mount clear of AC conductors. Corner coords derived by centering the hole rectangle in the outline.
- **Connectors:** LV side: 5V_IN/GND, two S/G signal pairs, 5V+RST, GND/TX/RX upload header (STC15W201S MCU). HV side: AC in (L/N), switched AC out (LOT), +Vo/-Vo 5V/3W.
- **⚠ Verify:** L x W and 74.17 x 29.21 mm hole pitch from official manual (high). Screw size M3 inferred (medium); hole diameter + thickness inferred (low). Corner coords derived.
- src: https://github.com/bigtreetech/BIGTREETECH-Relay-V1.2
- src: https://raw.githubusercontent.com/bigtreetech/BIGTREETECH-Relay-V1.2/master/BIGTREETECH%20Relay%20V1.2/BIGTREETECH%20Relay%20V1.2/Relay%20V1.2-Operating%20Instruction.pdf

### BTT S2DW V1.0 (LIS2DW, USB-C)  ·  `btt_s2dw_v1`

- **Category:** accelerometer  ·  **Confidence:** high
- **PCB:** 28.25 × 15.5 mm, 1.6 mm thick
- **Mounting:** 2× M3 (Ø), pattern 2-hole, pitch 15.5× mm
  - notes: Mechanically interchangeable with the BTT ADXL345 V2.0 - identical PCB outline and 15.5 mm 2-hole M3 mount; only the sensor IC differs (LIS2DW).
- **Connectors:** USB-C (USB 2.0), RP2040, BOOT button, reserved solder pads.
- **⚠ Verify:** Shares dimension drawing with ADXL345 V2.0 (high on size + 15.5 mm pitch). Hole diameter not stated (low). Generic/Annex "LIS2DW USB board" is effectively this board - no distinct Annex-branded LIS2DW PCB exists.
- src: https://github.com/bigtreetech/LIS2DW

### BTT Smart Filament Sensor (SFS) V1.0  ·  `btt_sfs_v1`

- **Category:** sensor  ·  **Confidence:** high
- **PCB:** 75.0 × 30.0 mm,  mm thick
- **Mounting:** 4× M3 (Ø3.2), pattern rectangular, pitch 56.75×20.35 mm
  - holes (x,y mm): [[9.125, 4.825], [65.875, 4.825], [9.125, 25.175], [65.875, 25.175]]
  - notes: Enclosed module 75 x 30 x 29.55 mm. 4 M3 holes at 56.75 x 20.35 mm pitch. Filament inlet/throat axis at 13.99 mm from the left mounting-hole line. Often mounted via just 2 of the 4 holes. Corner coords derived (centered).
- **Clearance:** standoff  mm, top component 29.55 mm
- **Connectors:** Inline 1.75 mm filament path, PC4-M6 push-fit couplings top+bottom (bowden). Encoder/motion sensor, 7 mm detection length. 3.3-5V, 3-wire JST output.
- **⚠ Verify:** Overall size, M3, 20.35 mm fixed hole spacing, 56.75 mm and 13.99 mm filament offset all from the official dimensional drawing (high). Corner coords derived.
- src: https://github.com/bigtreetech/smart-filament-detection-module
- src: https://raw.githubusercontent.com/bigtreetech/smart-filament-detection-module/master/V1.0/manual/smart%20filament%20sensor%20module%20manual201125.pdf

### BTT TMC5160T Plus V1.0 external high-power stepper driver  ·  `btt_tmc5160t_plus`

- **Category:** driver_module  ·  **Confidence:** high
- **PCB:** 50.0 × 50.0 mm, 1.6 mm thick
- **Mounting:** 4× M3 (Ø3.2), pattern rectangular, pitch 42.0×42.0 mm
  - holes (x,y mm): [[4.0, 4.0], [46.0, 4.0], [4.0, 46.0], [46.0, 46.0]]
  - notes: Bare PCB 50 x 50 mm, four corner holes inset 4.0 mm per the official dimensional drawing. Overall with integrated heatsink ~58 x 50 x 28 mm; with case ~64 x 56 x 32.55 mm. Ships with M3x8 hardware.
- **Clearance:** standoff  mm, top component 28.0 mm
- **Connectors:** 5-pole screw terminal (MOTOR 1B/2B/1A/2A + HVIN GND/8-60V); 16-pin drive connector + FFC EZ-driver connector on bottom edge; 2-pin 24V fan header; SPI/UART/standalone jumpers. Two large 560uF caps. VIO must not exceed 24V despite 60V motor supply.
- **⚠ Verify:** 50x50 PCB and 4.0 mm corner inset are from the official drawing (high). Derived 42 mm pitch and M3 are medium; hole diameter and 1.6 mm thickness inferred (low). STEP file in repo can confirm exact hole coords.
- src: https://github.com/bigtreetech/BIGTREETECH-Stepper-Motor-Driver/blob/master/TMC5160T%20Plus/BIGTREETECH%20TMC5160T%20Plus%20User%20Manual.pdf
- src: https://bttwiki.com/TMC5160TPlus.html

## BigTreeTech

### CB1  ·  `btt_cb1`

- **Category:** sbc  ·  **Confidence:** medium
- **PCB:** 55.0 × 40.0 mm, 1.6 mm thick
- **Mounting:** 4× M2.5 (Ø2.7), pattern rectangular, pitch 48.0×33.0 mm
  - holes (x,y mm): [[3.5, 3.5], [51.5, 3.5], [3.5, 36.5], [51.5, 36.5]]
  - notes: BTT wiki: product size 40 x 55 mm, "mounting size" 33 x 48 mm. The 33 x 48 rectangle IS the mounting-hole pitch and is the Raspberry Pi CM4 standard 4-hole pattern (CB1 is CM4-form-factor compatible). 3.5 mm inset on all sides is self-consistent ((55-48)/2 and (40-33)/2). hole_dia 2.7 and M2.5 from the RPi CM4 datasheet. holes_xy computed (origin = bottom-left). FORM FACTOR: board-to-board / CM4-style module (two 100-pin BTB connectors on underside), NOT a SODIMM edge card.

- **Clearance:** standoff 5 mm, top component  mm
- **Connectors:** Underside: two 100-pin micro BTB connectors mating to a CM4-style carrier (Manta, Pi4B adapter). 40-pin GPIO header on top edge.

- **⚠ Verify:** Board size 40 x 55 and mounting 33 x 48 authoritative (BTT wiki). Hole diameter, M2.5, 3.5 mm inset, 1.6 mm thickness inferred from CM4 compatibility, NOT explicitly published by BTT. holes_xy computed.

- src: https://global.bttwiki.com/CB1.html
- src: https://datasheets.raspberrypi.com/cm4/cm4-datasheet.pdf

### CB2  ·  `btt_cb2`

- **Category:** sbc  ·  **Confidence:** medium
- **PCB:** 55.0 × 40.0 mm, 1.6 mm thick
- **Mounting:** 4× M2.5 (Ø2.7), pattern rectangular, pitch 48.0×33.0 mm
  - holes (x,y mm): [[3.5, 3.5], [51.5, 3.5], [3.5, 36.5], [51.5, 36.5]]
  - notes: BTT wiki: product size 40 x 55 mm, "mounting size" 33 x 48 mm, explicitly "compatible with Raspberry Pi CM4 form factor". Same footprint as CB1. RK3566 SoC. Board-to-board module, NOT SODIMM. hole_dia / M2.5 / inset from CM4 datasheet; holes_xy computed.

- **Clearance:** standoff 5 mm, top component  mm
- **Connectors:** Underside: two 100-pin high-speed BTB connectors (CM4-compatible carrier). Same mating as CB1.

- **⚠ Verify:** 40 x 55 and 33 x 48 authoritative (BTT wiki). Hole dia 2.7, M2.5, 3.5 mm inset, 1.6 mm thickness inferred from CM4 compatibility, not explicitly published by BTT.

- src: https://global.bttwiki.com/CB2.html
- src: https://github.com/bigtreetech/docs/blob/master/docs/CB2.md
- src: https://datasheets.raspberrypi.com/cm4/cm4-datasheet.pdf

### EBB SB2209 CAN V1.0  ·  `btt_ebb_sb2209_can`

- **Category:** toolhead_can  ·  **Confidence:** high
- **PCB:** 68.54 × 42.45 mm, 1.6 mm thick
- **Mounting:** 2× M3 (Ø3.2), pattern linear, pitch 12.78×12.03 mm
  - holes (x,y mm): [[17.62, 17.19], [30.4, 29.22]]
  - notes: Two M3 holes in a diagonal pattern matching the Voron StealthBurner toolhead PCB mount. Coordinates are relative to the board's DRAWING DATUM (+X/+Y origin marked bottom-right of the SIZE drawing), NOT a board corner - sign/orientation must be reconciled with your CAD origin. The hole-to-hole vector dX=12.78, dY=12.03 is the reliable invariant and matches SB2240.

- **Clearance:** standoff 5 mm, top component  mm
- **Connectors:** Top edge: VIN/GND/CAN-H/CAN-L + HE0 heater; near-top RST/BOOT/DC_IN/ USB_5V/USB-C. Left/lower edges: SPI_OUT, NPN/Proximity, FAN headers, TH0 thermistor, 120R term jumper. Datum/accel reference at bottom-right.

- **⚠ Verify:** 68.54 x 42.45 mm and both hole centers (17.62,17.19 and 30.40,29.22 from drawing datum) read from official SIZE PDF. Hole-to-hole dX 12.78 / dY 12.03 matches SB2240. DATUM is the drawing's +X/+Y origin (bottom-right), NOT a board corner - verify orientation. thickness and hole_dia assumed.

- src: https://github.com/bigtreetech/EBB/blob/master/EBB%20SB2240_2209%20CAN/SB2209/Hardware/BIGTREETECHEBB%20SB2209%20CAN%20V1.0_SIZE.pdf
- src: https://global.bttwiki.com/EBB%202240%202209%20CAN.html

### EBB SB2209 CAN V1.0 (RP2040)  ·  `btt_ebb_sb2209_rp2040`

- **Category:** toolhead_can  ·  **Confidence:** low
- **PCB:** 68.54 × 42.45 mm, 1.6 mm thick
- **Mounting:** 2× M3 (Ø3.2), pattern linear, pitch 12.78×12.0 mm
  - notes: BTT did NOT publish a dimensional SIZE PDF for the RP2040 variant (repo folder has only a Pin PDF). It is purpose-built for and physically interchangeable with the Voron StealthBurner / the SB2209 CAN sibling, so outline and 2-hole mount are TAKEN to match that sibling (68.54 x 42.45, hole-to-hole dX=12.78 / dY~12.0). Confirm physically before relying on hole XY.

- **Clearance:** standoff 5 mm, top component  mm
- **Connectors:** Same family layout as SB2209 CAN: top edge VIN/GND/CAN-H/CAN-L + HE0; sides carry SPI_OUT, Proximity, FAN, endstop, PT100/TH0; ADXL345 onboard (RP2040 variant). USB-C present.

- **⚠ Verify:** NO official dimensional drawing exists for the RP2040 variant. All PCB/mount figures are INFERRED from the StealthBurner-interchangeable SB2209 CAN. DO NOT machine to these without physical verification.

- src: https://github.com/bigtreetech/EBB/blob/master/EBB%20SB2209%20CAN%20(RP2040)/Hardware/EBB%20SB2209%20CAN%20V1.0%EF%BC%88RP2040%EF%BC%89-Pin.pdf
- src: https://global.bttwiki.com/EBB%202209%20CAN%20RP2040.html

### EBB SB2240 CAN V1.0  ·  `btt_ebb_sb2240`

- **Category:** toolhead_can  ·  **Confidence:** high
- **PCB:** 68.54 × 42.45 mm, 1.6 mm thick
- **Mounting:** 2× M3 (Ø3.2), pattern linear, pitch 12.78×12.02 mm
  - holes (x,y mm): [[12.02, 17.22], [24.8, 29.24]]
  - notes: Same physical outline and StealthBurner 2-hole mount as SB2209 CAN. Absolute hole X-values differ from SB2209 (12.02/24.80 vs 17.62/30.40) ONLY because the drawing datum is placed at a different X reference; the hole-to-hole vector (dX=12.78, dY=12.02) is IDENTICAL to SB2209 CAN, so the boards are interchangeable on the StealthBurner. Reconcile datum before using absolute coords. Difference vs SB2209 is the integrated TMC2240 driver (vs TMC2209).

- **Clearance:** standoff 5 mm, top component  mm
- **Connectors:** Identical family layout to SB2209 CAN (top: VIN/GND/CAN-H/CAN-L + HE0; sides: SPI_OUT, Proximity, FAN, TH0, 120R).

- **⚠ Verify:** 68.54 x 42.45 mm and hole centers (12.02,17.22 and 24.80,29.24 from drawing datum) read from official SIZE PDF. Hole-to-hole dX 12.78 / dY 12.02 matches SB2209 CAN exactly (confirms interchangeable mount). Absolute X offset differs due to datum placement only. thickness/hole_dia assumed.

- src: https://github.com/bigtreetech/EBB/blob/master/EBB%20SB2240_2209%20CAN/SB2240/Hardware/BIGTREETECH%20EBB%20SB2240%20CAN%20%20V1.0_SIZE.pdf
- src: https://global.bttwiki.com/EBB%202240%202209%20CAN.html

### EBB36 CAN V1.x  ·  `btt_ebb36_can_v1`

- **Category:** toolhead_can  ·  **Confidence:** medium
- **PCB:** 51.4 × 37.0 mm, 1.6 mm thick
- **Mounting:** 2× M3 (Ø3.2), pattern linear, pitch 43.85×0 mm
  - notes: NEMA-style rounded/keyed outline. BTT publishes only 2x M3 holes at 43.85 mm center-to-center spacing (per official SIZE PDF + wiki). Holes sit on lower ears flanking the connector edge; absolute hole XY is NOT published (only c-to-c). Width 51.40 mm (wiki nominal 51.5 x 37).

- **Clearance:** standoff 5 mm, top component  mm
- **Connectors:** Bottom edge carries main connectors (HE0, FAN, etc.); USB and CAN/power on board. I2C/PT1000/RST/BOOT labeled on PCB. Stepper connects via a separate edge.

- **⚠ Verify:** 51.40 mm width and 43.85 mm hole spacing confirmed (official SIZE PDF + wiki). Exact hole XY NOT extractable (only c-to-c published). thickness 1.6 and hole_dia 3.2 assumed.

- src: https://github.com/bigtreetech/EBB/blob/master/EBB%20CAN%20V1.1%20and%20V1.2%20(STM32G0B1)/EBB36%20CAN%20V1.1%20and%20V1.2/Hardware/BIGTREETECH%20EBB36%20CAN%20V1.1-SIZE.pdf
- src: https://global.bttwiki.com/EBB%2036%20CAN.html

### EBB42 CAN V1.x  ·  `btt_ebb42_can_v1`

- **Category:** toolhead_can  ·  **Confidence:** high
- **PCB:** 40.0 × 40.0 mm, 1.6 mm thick
- **Mounting:** 4× M3 (Ø3.2), pattern rectangular, pitch 31.0×31.0 mm
  - holes (x,y mm): [[4.5, 4.5], [35.5, 4.5], [4.5, 35.5], [35.5, 35.5]]
  - notes: Clean 40 x 40 board, 4x M3 in a 31 x 31 square grid (matches a NEMA17-ish bolt grid). SIZE drawing annotates a 4.00 mm edge dimension. NOTE the ambiguity: holes_xy here assume 31 mm span centered on the 40 mm board (-> 4.5 mm inset to center); the drawing's 4.00 mm could instead be edge-to-center (-> holes at 4.0/35.0, span 32). Use pitch 31.0 as the primary load-bearing figure and reconcile the 4.0 vs 4.5 inset before machining.

- **Clearance:** standoff 5 mm, top component  mm
- **Connectors:** Bottom edge: HE0, FAN1 outputs. Top edge: VBUS/USB and CAN. Endstop/ PT100/I2C/BLTouch labeled around perimeter. Stepper via dedicated connector.

- **⚠ Verify:** 40 x 40, 31 x 31 four-hole pattern, 4x M3, 4.00 mm edge dim all annotated on official SIZE PDF + wiki. CONFLICT: 4.00 mm reads as edge-to-center vs as-drawn -> holes_xy (4.5/35.5) computed on the centered-span interpretation. 31 mm c-to-c is firm. thickness assumed.

- src: https://github.com/bigtreetech/EBB/blob/master/EBB%20CAN%20V1.1%20and%20V1.2%20(STM32G0B1)/EBB42%20CAN%20V1.1%20and%20V1.2/Hardware/BIGTREETECH%20EBB42%20CAN%20V1.1-SIZE.pdf
- src: https://global.bttwiki.com/EBB%2042%20CAN.html

### KNOMI  ·  `btt_knomi`

- **Category:** accessory  ·  **Confidence:** high
- **PCB:** 37.86 × 34.53 mm, 1.6 mm thick
- **Mounting:** 0×  (Ø), pattern other-describe, pitch × mm
  - notes: ROUND PCB (~34.53 mm dia body) with a small flat tab at the bottom (two 10.97 mm edge segments flanking a connector notch). NO mounting holes on the PCB. The board SNAP-FITS into a printed "Mounting Plate" that clips onto the StealthBurner (BTT provides STLs). Overall bounding box 34.53 (W) x 37.86 (H) mm per v1.0-SIZE drawing; manual also cites 34.59 mm width and ~39.5 mm assembled depth. Model as a round board that drops into a snap-fit cradle, NOT a screw pattern.

- **Connectors:** USB-C (UART-to-USB, DC 5V in) and a power-in header (DC 5~24V, +/-); BOOT button. 1.28in 240x240 round LCD (non-touch).

- **⚠ Verify:** Outline 34.53 x 37.86 mm read directly from official v1.0-SIZE.pdf. Minor width conflict: SIZE.pdf=34.53 vs manual=34.59 (~0.06 mm rounding). thickness assumed. No standoff/hole data because design is snap-fit (confirmed in manual + assembly drawings).

- src: https://github.com/bigtreetech/KNOMI/blob/master/KNOMI1/Hardware/BIGTREETECH%20KNOMI%20v1.0-SIZE.pdf
- src: https://github.com/bigtreetech/KNOMI/blob/master/KNOMI1/KNOMI%201%20User%20Manual%2020241214.pdf
- src: https://global.bttwiki.com/KNOMI.html

### KNOMI 2  ·  `btt_knomi2`

- **Category:** accessory  ·  **Confidence:** high
- **PCB:** 41.12 × 38.48 mm, 1.6 mm thick
- **Mounting:** 0×  (Ø), pattern other-describe, pitch × mm
  - notes: ROUND PCB; round body diameter ~35.65 mm (~38.42 mm tall round portion), with small bottom tabs extending the overall bounding box to 38.48 (W) x 41.12 (H) mm per the official manual overview drawing. NO mounting holes - SNAP-ON into a printed Mounting Plate (the v1.1 carrier increased the gap). BTT provides StealthBurner Main Body + Mounting Plate STLs.

- **Connectors:** USB-C (UART-to-USB, DC 5V in) and power-in header (DC 5V, +/-); BOOT button. 1.28in round LCD, display area 32.4 x 32.4 mm, 240x240, 5-point capacitive touch.

- **⚠ Verify:** Four dims read directly from the official manual overview drawing: 38.48 mm (max width incl tabs), 35.65 mm (round body dia), 41.12 mm (overall height incl tabs), 38.42 mm (round-portion height). Hardware TOP.pdf has no dimension callouts. thickness assumed. Snap-fit, no PCB holes (confirmed in manual + assembly pages).

- src: https://github.com/bigtreetech/KNOMI/blob/master/KNOMI2/Manual/KNOMI%202%20User%20Manual%2020240109.pdf
- src: https://github.com/bigtreetech/KNOMI/blob/master/KNOMI2/Hardware/BIGTREETECH%20knomi%20v2.0-TOP.pdf
- src: https://global.bttwiki.com/KNOMI2.html

### Kraken (V1.0/V1.1)  ·  `btt_kraken_v1_x`

- **Category:** mainboard  ·  **Confidence:** medium
- **PCB:** 200.0 × 113.0 mm, 1.6 mm thick
- **Mounting:** 4× M3 (Ø3.2), pattern rectangular, pitch 193.0×106.03 mm
  - holes (x,y mm): [[5.0, 4.0], [198.0, 4.0], [5.0, 110.03], [198.0, 110.03]]
  - notes: Larger than Octopus. Overall 200.00 x 113.41 mm (wiki rounds 200 x 113). Mounting pitch X = 193.00, Y = 106.03 mm, 4 corner holes. Insets are slightly ASYMMETRIC (~5 mm left long edge, ~4 mm right). holes_xy are RECONSTRUCTED, not all individually dimensioned. The 52.02/65.20/26.39/ 30.86 mm callouts on the drawing are connector positions, NOT mounting holes. hole_dia 3.2 = M3 convention.

- **Clearance:** standoff 5 mm, top component  mm
- **Connectors:** 8-axis high-current board. Stepper headers (MOTOR0-7) + large bulk caps along one long edge. MOTOR-POWER, POWER, BED-POWER, BED-OUT high-current screw terminals on one short edge. USB-C, RJ45, SD, Vbat and fan/endstop headers on the opposite long edge / right side. Heater outputs (HE0-3) along bottom edge.

- **⚠ Verify:** Overall 200 x 113 and pitch 193.00 x 106.03 read from official SIZE.png (matches wiki). MEDIUM because per-corner insets are asymmetric and not fully dimensioned (holes_xy reconstructed - verify before drilling); drawing height 113.41 vs wiki 113. V1.0/V1.1 share this drawing.

- src: https://github.com/bigtreetech/BIGTREETECH-Kraken/blob/master/Hardware/BIGTREETECH%20Kraken%20V1.0-SIZE.png
- src: https://global.bttwiki.com/Kraken.html

### Manta E3EZ  ·  `btt_manta_e3ez`

- **Category:** mainboard  ·  **Confidence:** medium
- **PCB:** 120.0 × 90.81 mm, 1.6 mm thick
- **Mounting:** 4× M3 (Ø3.2), pattern other-describe, pitch × mm
  - notes: IDENTITY: the task's "E3 EZ" resolves to the Manta E3EZ Klipper mainboard (BTT has no standalone product simply named "E3 EZ"); flag if a different board was meant. Designed to reuse Ender-3 mounting locations, so the hole pattern is IRREGULAR. Official SIZE PDF: overall 120.00 x 90.81 mm, 4 mounting holes. Per-hole [x,y] not reconstructed (partial dimension chains). Hosts a CM4/CB1 module (CM4 uses M2x10 screws, separate from the board's M3 chassis mounting).

- **Connectors:** Motor headers (X/Y/Z1/Z2/E0/E1) across the top; CM4/CB1 SODIMM socket, CPU/RAM and HDMI at center/right; USB, power and bed/hotend terminals bottom-left edge.

- **⚠ Verify:** Overall 120.00 x 90.81 mm HIGH confidence (official SIZE PDF). Hole count (4) and irregular pattern MEDIUM; exact centers not cleanly dimensioned - derive holes_xy from the in-repo STEP/3D model. "E3 EZ" -> "Manta E3EZ" mapping is an assumption.

- src: https://github.com/bigtreetech/Manta-E3EZ/blob/master/Hardware/BIGTREETECH%20Manta%20E3EZ%20V1.0-SIZE.pdf
- src: https://github.com/bigtreetech/Manta-E3EZ

### Manta M4P  ·  `btt_manta_m4p`

- **Category:** mainboard  ·  **Confidence:** medium
- **PCB:** 160.0 × 95.0 mm, 1.6 mm thick
- **Mounting:** 4× M3 (Ø3.2), pattern other-describe, pitch 97.0×84.2 mm
  - notes: 4 holes, roughly rectangular but the top-left hole is inset (NOT on the corner): it sits at X=48 mm, top-right hole 97 mm to its right (X=145). Vertical pitch top->bottom = 84.2 mm. Wiki lists install sizes "146 x 84.2 mm; 97 x 84.2 mm" indicating two hole-column spacings (a stepped layout). CB1/CM4 core board mounts via board-to-board connector + its own standoffs.

- **Clearance:** standoff 5 mm, top component  mm
- **Connectors:** Bottom edge carries power input, USB-C, USB-A, and RJ45/Ethernet. Stepper driver sockets (4x) and motor/endstop headers along the top/right. CB1/CM4 SBC mounts on top via board-to-board connector.

- **⚠ Verify:** PCB size 160 x 95 HIGH (official SIZE.png + wiki). Exact hole XY MEDIUM (stepped/irregular layout; pitch_x/pitch_y read from drawing but holes_xy not enumerated). hole_dia and thickness assumed.

- src: https://github.com/bigtreetech/Manta-M4P/blob/master/Hardware/BIGTREETECH_Manta_M4P_V2.1_220608%20SIZE.png
- src: https://global.bttwiki.com/M4P.html

### Manta M5P  ·  `btt_manta_m5p`

- **Category:** mainboard  ·  **Confidence:** medium
- **PCB:** 137.39 × 95.0 mm, 1.6 mm thick
- **Mounting:** 4× M3 (Ø3.2), pattern rectangular, pitch ×86.5 mm
  - notes: Four corner mounting holes inset ~4.50 mm from left/bottom edges (top-right shows 4.50 X / 4.00 Y). Vertical hole span 86.50 mm. Horizontal span ~= 137.39 - 4.5 - 4.5 ~= 128.4 mm (COMPUTED, not directly labeled). A separate 4-hole cluster near the LAN/SBC region is the CB1/CM4 core-board mount, NOT the main board mounts.

- **Clearance:** standoff 5 mm, top component  mm
- **Connectors:** Bottom edge: power, USB-C, USB-A, RJ45/Ethernet. 5x stepper driver sockets and motor/endstop headers across the right side. CB1/CM4 SBC mounts on top via board-to-board connector.

- **⚠ Verify:** PCB size 137.39 x 95.00 HIGH (official SIZE-top.pdf; wiki rounds to 137.5). 86.50 mm vertical span and 4.50/4.00 mm insets read from drawing. Horizontal pitch is COMPUTED (not labeled) -> hole-center X MEDIUM. hole_dia and thickness assumed.

- src: https://github.com/bigtreetech/Manta-M5P/blob/master/Hardware/BIGTREETECH%20MANTA%20M5P%20V1.0-SIZE-top.pdf
- src: https://global.bttwiki.com/M5P.html

### Manta M8P V1.1  ·  `btt_manta_m8p_v1_1`

- **Category:** mainboard  ·  **Confidence:** medium
- **PCB:** 169.93 × 102.74 mm, 1.6 mm thick
- **Mounting:** 6× M3 (Ø3.2), pattern other-describe, pitch × mm
  - notes: Board is 169.93 x 102.74 mm (NOT ~148x130 - that hint was wrong). V1.0 and V1.1 share one hardware dir and one SIZE drawing (identical mechanicals). Corner holes inset 5.00 mm; bottom dim chain 5.00 / 124.94 / 157.94 / 169.93 mm and top chain to 155.00 mm locate mounting holes along the long edges. hole_count=6 (corners + mid-edge) is a visual read and could be 5.

- **Clearance:** standoff 5 mm, top component  mm
- **Connectors:** Top/left edges carry the 8 stepper driver sockets and motor power screw terminals. Right edge: USB-C, USB-A, RJ45/Ethernet (and HDMI with CM4). CB1/CM4 SBC mounts on top via board-to-board connector.

- **⚠ Verify:** PCB size 169.93 x 102.74 HIGH (official V1.0/V1.1 SIZE-top.pdf; wiki 170 x 102.7). 5.00 mm corner inset confirmed. hole_count MEDIUM (could be 5), individual hole XY LOW (connector-referenced dimension chains). hole_dia and thickness assumed.

- src: https://github.com/bigtreetech/Manta-M8P/blob/master/V1.0_V1.1/Hardware/BIGTREETECH%20MANTA%20M8P%20V1.0-SIZE-top.pdf
- src: https://global.bttwiki.com/M8P.html

### Manta M8P V2.0  ·  `btt_manta_m8p_v2`

- **Category:** mainboard  ·  **Confidence:** medium
- **PCB:** 169.93 × 102.74 mm, 1.6 mm thick
- **Mounting:** 6× M3 (Ø3.2), pattern other-describe, pitch × mm
  - notes: Board outline 169.93 x 102.74 mm. SIZE drawing shows corner insets 5.00 and 4.43 mm. Mounting-hole layout is essentially the same as V1.0/V1.1 (corners + mid-edge); same enclosures generally fit V1.x and V2.0.

- **Clearance:** standoff 5 mm, top component  mm
- **Connectors:** Top edge: 8 stepper driver sockets, motor power screw terminals. Right edge: USB-C, USB-A, RJ45/Ethernet (HDMI with CM4). CB1/CM4 SBC mounts on top via board-to-board connector.

- **⚠ Verify:** PCB size 169.93 x 102.74 HIGH (official V2.0 SIZE.pdf; wiki 170 x 102.7). 5.00 mm corner inset confirmed. Dense connector-referenced drawing -> exact hole XY LOW, hole_count MEDIUM. Mechanically interchangeable footprint with V1.x. hole_dia and thickness assumed.

- src: https://github.com/bigtreetech/Manta-M8P/blob/master/V2.0/Hardware/BIGTREETECH%20MANTA%20M8P%20V2.0-SIZE.pdf
- src: https://global.bttwiki.com/M8P-V2_0.html

### Octopus Pro V1.x (V1.0/V1.1)  ·  `btt_octopus_pro_v1_x`

- **Category:** mainboard  ·  **Confidence:** high
- **PCB:** 160.0 × 100.0 mm, 1.6 mm thick
- **Mounting:** 4× M3 (Ø3.2), pattern rectangular, pitch 150.0×90.0 mm
  - holes (x,y mm): [[5.0, 5.0], [155.0, 5.0], [5.0, 95.0], [155.0, 95.0]]
  - notes: Footprint and mounting pattern VERIFIED IDENTICAL to the non-Pro Octopus from the official Octopus Pro SIZE.pdf (160 x 100 overall, 150 x 90 pitch). Pro adds higher-current drivers; mechanical layout unchanged. hole_dia 3.2 = M3 clearance convention.

- **Clearance:** standoff 5 mm, top component  mm
- **Connectors:** Same layout as standard Octopus: MOTOR0-7 stepper headers + caps along one long edge, power input at corner, heaters/endstops/USB/network on opposite edges.

- **⚠ Verify:** 160 x 100 outline and 150 x 90 pitch read directly from official Pro SIZE.pdf - matches standard Octopus exactly. Single SIZE.pdf covers both V1.0 and V1.1 (no mechanical change). thickness/hole_dia conventions.

- src: https://github.com/bigtreetech/BIGTREETECH-OCTOPUS-Pro/blob/master/Hardware/BIGTREETECH%20Octopus%20Pro%20-%20SIZE.pdf

### Octopus V1.1  ·  `btt_octopus_v1_1`

- **Category:** mainboard  ·  **Confidence:** high
- **PCB:** 160.0 × 100.0 mm, 1.6 mm thick
- **Mounting:** 4× M3 (Ø3.2), pattern rectangular, pitch 150.0×90.0 mm
  - holes (x,y mm): [[5.0, 5.0], [155.0, 5.0], [5.0, 95.0], [155.0, 95.0]]
  - notes: 4 corner holes, symmetric. Pitch (150 x 90) confirmed from official SIZE.pdf; overall PCB 160 x 100. Inset = (160-150)/2 = 5 mm and (100-90)/2 = 5 mm on all sides; holes_xy computed from symmetric inset. hole_dia 3.2 is the M3 clearance assumption (corner 'M12' silkscreen label is a ref-designator, not a diameter). V1.1 vs V1.0 differ only in silkscreen / power-IC package; mechanically identical.

- **Clearance:** standoff 5 mm, top component  mm
- **Connectors:** Stepper connectors (MOTOR0-7) + bulk capacitors along one long edge. Power input (MOTOR_POWER) at one corner. USB-C / network / heater outputs (HE0-3) and endstops along the opposite long edge and short edges.

- **⚠ Verify:** 160 x 100 outline and 150 x 90 pitch read directly from official PDF. thickness and hole_dia are conventions. V1.0 and V1.1 share identical mechanics per BTT readme.

- src: https://github.com/bigtreetech/BIGTREETECH-OCTOPUS-V1.0/blob/master/Hardware/BIGTREETECH%20Octopus%20-%20SIZE.pdf
- src: https://github.com/bigtreetech/BIGTREETECH-OCTOPUS-V1.0/blob/master/Hardware/readme.txt

### SKR 3  ·  `btt_skr_3`

- **Category:** mainboard  ·  **Confidence:** high
- **PCB:** 109.67 × 84.3 mm, 1.6 mm thick
- **Mounting:** 4× M3 (Ø3.2), pattern rectangular, pitch 101.85×76.3 mm
  - notes: 4 corner holes forming a rectangle. Center-to-center pitch 101.85 mm (X) x 76.30 mm (Y), read from official SIZE drawing (overall board 109.67 x 84.30 mm). Screw size M3 and 3.2 mm clearance are family convention, not explicitly labeled.

- **Connectors:** Motor (X/Y/Z/Z1/E)/fan headers along top edge; USB, SD card, WiFi module and SERVO/Probe/TFT/EXP headers bottom edge; power and bed/hotend terminals on left edge.

- **⚠ Verify:** Overall dims and rectangular pitch (101.85 x 76.30) HIGH confidence from official SIZE PDF. Hole diameter and thickness assumed. In-repo STEP file (BIGTREETECH SKR 3.step) has exact hole centers.

- src: https://github.com/bigtreetech/SKR-3/blob/master/Hardware%20(SKR%203)/BIGTREETECH%20SKR%203-SIZE.pdf
- src: https://github.com/bigtreetech/SKR-3

### SKR 3 EZ  ·  `btt_skr_3_ez`

- **Category:** mainboard  ·  **Confidence:** high
- **PCB:** 109.67 × 84.3 mm, 1.6 mm thick
- **Mounting:** 4× M3 (Ø3.2), pattern rectangular, pitch 101.85×76.3 mm
  - notes: Same PCB footprint and mounting pattern as the SKR 3 (the EZ is the EZ-driver variant on the identical board outline). Official SIZE drawing confirms 109.67 x 84.30 mm with the 4-corner-hole rectangle, pitch 101.85 (X) x 76.30 (Y).

- **Connectors:** Motor/fan headers (XM/YM/ZM/Z1M/EOM/E1M) top edge; USB, SD-M, CAN-FD, TFT, PS-ON, EXP1/EXP2 and SERVOS/Probe bottom edge; power & bed/hotend terminals on left edge.

- **⚠ Verify:** Footprint identical to SKR 3, confirmed from the SKR 3 EZ SIZE PDF. Hole diameter and thickness assumed. STEP file in-repo for exact coordinates.

- src: https://github.com/bigtreetech/SKR-3/blob/master/Hardware%20(SKR%203%20EZ)/BIGTREETECH%20SKR%203%20EZ%20V1.0-SIZE.pdf

### SKR Mini E3 V3  ·  `btt_skr_mini_e3_v3`

- **Category:** mainboard  ·  **Confidence:** medium
- **PCB:** 103.75 × 70.25 mm, 1.6 mm thick
- **Mounting:** 6× M3 (Ø3.2), pattern other-describe, pitch × mm
  - notes: Drops into the Ender-3 / Ender-3 Pro/V2 board location and reuses the original Creality mounting bosses, so the hole pattern is IRREGULAR (not a clean rectangle). Official SIZE drawing shows 6 plated mounting holes. Per-hole [x,y] NOT reconstructed (drawing leader lines are partial); pull exact centers from the in-repo STEP file. Two PCB revisions exist in the repo (V3.0 and V3.0.1); these dims are the canonical V3.0.

- **Connectors:** Stepper/endstop/fan headers along top edge (XM/YM/ZM/EM); POWER, heated- bed and hotend screw terminals on bottom-left edge; USB-C, TFT/EXP and thermistor/probe headers clustered bottom and right. Right edge has a tab carrying the I/O / display connector.

- **⚠ Verify:** Overall 103.75 x 70.25 mm and 6-hole count are HIGH confidence (official SIZE PDF). Per-hole coordinates and hole diameter are LOW — derive holes_xy from BTT E3 SKR MINI V3.0.step before cutting. Thickness assumed.

- src: https://github.com/bigtreetech/BIGTREETECH-SKR-mini-E3/blob/master/hardware/BTT%20SKR%20MINI%20E3%20V3.0/Hardware/BTT%20E3%20SKR%20MINI%20V3.0_SIZE_20220301.pdf
- src: https://global.bttwiki.com/SKR%20MINI%20E3.html

### SKR Pico  ·  `btt_skr_pico`

- **Category:** mainboard  ·  **Confidence:** high
- **PCB:** 85.0 × 56.0 mm, 1.6 mm thick
- **Mounting:** 4× M2.5 (Ø2.75), pattern rectangular, pitch 58.0×49.0 mm
  - holes (x,y mm): [[3.5, 3.5], [61.5, 3.5], [3.5, 52.5], [61.5, 52.5]]
  - notes: Deliberately matches the Raspberry Pi Model B / Pi 4 mounting footprint: 58.00 x 49.00 mm hole rectangle, M2.5 screws, 3.50 mm in from two edges. Read from official SIZE PDF (overall 85.00 x 56.00 mm). holes_xy computed from the inset+pitch (origin = bottom-left PCB corner); board outline has castellated/notched edges so corner is nominal. hole_dia 2.75 mm is the RPi-standard M2.5 clearance.

- **Connectors:** Stepper driver sockets (E/X/Y/Z) across the top; USB-C and VBED/I-O on the left edge; motor, endstop (X/Y/Z-STOP), heater/fan and thermistor terminals/headers along the bottom and right edges.

- **⚠ Verify:** Overall dims, 58 x 49 pitch and 3.50 mm inset HIGH confidence from official SIZE PDF (corroborated by RPi-compatible-mount note). M2.5 / 2.75 mm hole dia inferred from RPi standard (not labeled). holes_xy computed, not directly dimensioned.

- src: https://github.com/bigtreetech/SKR-Pico/blob/master/Hardware/BTT%20SKR%20Pico%20V1.0-SIZE.pdf
- src: https://github.com/bigtreetech/SKR-Pico

### U2C V2 (V2.0/V2.1)  ·  `btt_u2c_v2`

- **Category:** usb_can_bridge  ·  **Confidence:** medium
- **PCB:** 85.45 × 25.35 mm, 1.6 mm thick
- **Mounting:** 4× M3 (Ø), pattern rectangular, pitch ×19.23 mm
  - notes: Official BTT dimension drawing: overall 85.45 x 25.35 mm. Four mounting holes, one near each corner. Drawing labels a 2.00 mm inset from the right edge to the hole centers and a 19.23 mm vertical pitch. The horizontal (X) pitch and hole diameter are NOT labeled -> null. M3 is the community-standard screw (not BTT-stated).

- **Clearance:** standoff 5 mm, top component  mm
- **Connectors:** Left short edge: USB Type-C (CAN_IN to host). Right short edge: 4-pin screw terminal (Power + CAN_OUT). Mid-board: additional CAN_OUT JST headers (3 CAN outputs on the '-3' variant). Connectors exit both short ends.

- **⚠ Verify:** Overall L/W (85.45 x 25.35), 19.23 mm vertical hole pitch and 2.00 mm edge inset read directly from the official dimension drawing (HIGH on those). Hole diameter, X-pitch, screw size, thickness NOT published. Overall MEDIUM because hole geometry is incomplete.

- src: https://global.bttwiki.com/U2C.html
- src: https://global.bttwiki.com/img/U2C/U2C_Dimension.webp
- src: https://github.com/bigtreetech/docs/blob/master/docs/U2C.md

### U2C V3  ·  `btt_u2c_v3`

- **Category:** usb_can_bridge  ·  **Confidence:** low
- **PCB:**  ×  mm,  mm thick
- **Mounting:** ×  (Ø), pattern , pitch × mm
  - notes: NO authoritative evidence that a "U2C V3" product exists. BTT's official lineage is V1.0/V1.1 (STM32F072C8) and V2.0/V2.1 (STM32G0B1C8). The "U2C 3" / "V2.1-3" naming seen in listings refers to "3 CAN OUTPUTS", NOT hardware version 3. Treat as nonexistent unless a new revision is confirmed. Use the btt_u2c_v2 entry for all current U2C dimensional data.

- **Connectors:** N/A - product not confirmed to exist.
- **⚠ Verify:** DO NOT generate geometry for this entry. No U2C V3 found in BTT wiki, BTT docs GitHub, or community klipper_canbus docs (as of 2026-06). If a BOM truly needs a V3, confirm the SKU with BTT first - the part likely does not exist or is mislabeled.

- src: https://global.bttwiki.com/U2C.html
- src: https://github.com/bigtreetech/docs/blob/master/docs/U2C.md
- src: https://maz0r.github.io/klipper_canbus/controller/u2c.html

## Duet3D

### Duet 2 WiFi / Ethernet  ·  `duet2_wifi_ethernet`

- **Category:** mainboard  ·  **Confidence:** high
- **PCB:** 123.0 × 100.0 mm, 1.6 mm thick
- **Mounting:** 4× M3 (Ø4.2), pattern rectangular, pitch 92.0×115.0 mm
  - holes (x,y mm): [[4.0, 4.0], [96.0, 4.0], [4.0, 119.0], [96.0, 119.0]]
  - notes: WiFi and Ethernet variants share one PCB. Hole pattern is identical to the Duet 3 Mini 5+ (the Mini uses Ø4.3 mm; Duet 2 uses Ø4.2 mm -- negligible 0.1 mm, both clear M3 and M4). Commonly mounted with M3.
- **Clearance:** standoff 6 mm, top component  mm
- **⚠ Verify:** From KiCad. Thickness 1.6 mm standard, not annotated.
- src: https://github.com/Duet3D/Duet-2-Hardware/blob/master/Duet2/Duet2v1.06/Duet2.kicad_pcb
- src: https://docs.duet3d.com/Duet3D_hardware/Duet_2_family/Duet_2_WiFi_Ethernet_Hardware_Overview

### Duet 3 Mainboard 6HC  ·  `duet3_6hc`

- **Category:** mainboard  ·  **Confidence:** high
- **PCB:** 140.0 × 134.0 mm, 1.6 mm thick
- **Mounting:** 4× M3 (Ø4.3), pattern rectangular, pitch 124.0×130.0 mm
  - holes (x,y mm): [[5.0, 5.0], [129.0, 5.0], [5.0, 135.0], [129.0, 135.0]]
  - notes: Holes are isolated (non-plated) with a ~2.2 mm keep-out ring. Drilled Ø4.3 mm (M4 clearance) but Duet's own guides specify M3 screws. Width is 134 mm, length 140 mm -- the commonly cited "144x96" figure is WRONG.
- **Clearance:** standoff 8 mm, top component  mm
- **Connectors:** USB + RJ45/Ethernet on one short edge; CAN_OUT on a long edge. PT100/ thermocouple daughterboard header (2.54 mm) interior at approx [84,81].
- **⚠ Verify:** Outline + holes confirmed twice (dimension SVG and KiCad). Thickness 1.6 mm is standard but not explicitly annotated in the drawings.
- src: https://github.com/Duet3D/Duet3-Mainboard-6HC/blob/master/Duet3_Mainboard_6HC_v1.0/Duet3_MB_6HC_v0.6%26later_Dimensions.svg
- src: https://github.com/Duet3D/Duet3-Mainboard-6HC/blob/master/Duet3_Mainboard_6HC_v1.02/CAD/Duet3_MB_6HC.kicad_pcb
- src: https://docs.duet3d.com/Duet3D_hardware/Duet_3_family/Duet_3_Mainboard_6HC_Hardware_Overview

### Duet 3 Mainboard 6XD  ·  `duet3_6xd`

- **Category:** mainboard  ·  **Confidence:** high
- **PCB:** 140.0 × 115.0 mm, 1.6 mm thick
- **Mounting:** 4× M3 (Ø4.3), pattern rectangular, pitch 104.5×129.5 mm
  - holes (x,y mm): [[5.5, 5.5], [110.0, 5.0], [5.0, 135.0], [110.0, 135.0]]
  - notes: Narrower than the 6HC (115 mm vs 134 mm) but same 140 mm length. The bottom-left hole sits at [5.5,5.5] in the source file (~0.5 mm offset from the 5 mm grid of the other three) -- treat that corner as medium confidence. Two interior Ø2.5 mm holes are a daughterboard mount, not chassis mounting.
- **Clearance:** standoff 8 mm, top component  mm
- **Connectors:** External-driver mainboard; differential driver outputs.
- **⚠ Verify:** Outline + 3 holes high confidence from KiCad. The [5.5,5.5] corner asymmetry is in the source file; verify sub-mm precision on that hole physically.
- src: https://github.com/Duet3D/Duet3-Mainboard-6XD/blob/master/v1.01/CAD/Duet3_MB_6XD.kicad_pcb
- src: https://docs.duet3d.com/Duet3D_hardware/Duet_3_family/Duet_3_Mainboard_6XD_Hardware_Overview

### Duet 3 Mini 5+  ·  `duet3_mini5plus`

- **Category:** mainboard  ·  **Confidence:** high
- **PCB:** 123.0 × 100.0 mm, 1.6 mm thick
- **Mounting:** 4× M3 (Ø4.3), pattern rectangular, pitch 92.0×115.0 mm
  - holes (x,y mm): [[4.0, 4.0], [96.0, 4.0], [4.0, 119.0], [96.0, 119.0]]
  - notes: Footprint is byte-for-byte identical to the Duet 2 WiFi/Ethernet (same 100x123 outline, 92x115 pitch, 4 mm inset) -- one mount fits both. Drilled Ø4.3 mm (M4 clearance); Duet documents fixing with 4x M3 6mm screws. The commonly cited "117x89" figure is WRONG.
- **Clearance:** standoff 6 mm, top component  mm
- **Connectors:** Stepper-driver connectors mirrored to the opposite side vs Duet 2.
- **⚠ Verify:** Outline + holes from KiCad. Thickness 1.6 mm standard, not annotated.
- src: https://github.com/Duet3D/Duet3-Mini5plus/blob/main/v1.02_wifi/Duet3_5+_Wifi_v1.02_KiCAD/Duet3_5+_Wifi.kicad_pcb
- src: https://docs.duet3d.com/Duet3D_hardware/Duet_3_family/Duet_3_Mini_5+_Hardware_Overview

### Duet 3 Toolboard 1LC  ·  `duet3_toolboard_1lc`

- **Category:** toolhead_can  ·  **Confidence:** high
- **PCB:** 54.0 × 47.0 mm, 1.6 mm thick
- **Mounting:** 4× M3 (Ø3.2), pattern rectangular, pitch 34.0×34.0 mm
  - holes (x,y mm): [[13.0, 4.0], [47.0, 4.0], [13.0, 38.0], [47.0, 38.0]]
  - notes: Square 34x34 mm hole pattern, but offset toward the lower-left of the board (NOT centred): 13 mm from left edge / 7 mm from right; 4 mm from bottom / 9 mm from top.
- **Clearance:** standoff 5 mm, top component  mm
- **Connectors:** Heater/CAN/5V on top edge; VIN top-right; DRIVER bottom-right; IO on left.
- **⚠ Verify:** From official dimension SVG. Thickness 1.6 mm standard, not annotated.
- src: https://github.com/Duet3D/Duet3-Toolboard-1LC/blob/master/ToolBoard_1LC_v1.0/Duet3_TB_1LC_v1.0_Dimensions.svg
- src: https://docs.duet3d.com/Duet3D_hardware/Duet_3_family/Duet_3_Toolboard_1LC

### Duet3D PT100 temperature daughterboard v1.1  ·  `duet3d_pt100_daughterboard`

- **Category:** thermocouple_amp  ·  **Confidence:** high
- **PCB:** 31.74 × 26.16 mm, 1.6 mm thick
- **Mounting:** 2×  (Ø2.54), pattern 2-hole, pitch 38.5×0.0 mm
  - holes (x,y mm): [[13.05, 0.0], [13.05, 38.5]]
  - notes: Secured with a SUPPLIED PLASTIC SNAP-IN PILLAR, not an M-screw. Holes are Ø2.54 mm NPTH from the official KiCad board file. Design around the pillar.
- **Connectors:** 2x5 (10-pin) 2.54 mm header plugs into Duet expansion/SPI header; screw terminals for PT100 wires.
- **⚠ Verify:** Outline 26.16 x 31.74 and Ø2.54 holes from official KiCad source (high). 38.5 mm pitch is medium (derived from connector footprint coords; rotation ambiguous). Mounting is a plastic pillar, not a screw.
- src: https://github.com/Duet3D/TempDaughterboards/tree/master/MAXTempRTD
- src: https://docs.duet3d.com/Duet3D_hardware/Accessories/PT100_Temperature_Daughterboard

## Fotek

### Fotek SSR-25DA solid state relay (SSR-DA series body)  ·  `fotek_ssr_25da`

- **Category:** ssr  ·  **Confidence:** medium
- **PCB:** 57.4 × 44.8 mm, 28.0 mm thick
- **Mounting:** 2× M4 (Ø4.8), pattern 2-hole, pitch 47.6×0.0 mm
  - holes (x,y mm): [[4.9, 22.4], [52.5, 22.4]]
  - notes: Standard Fotek SSR-DA series housing ~57.4 x 44.8 x 28 mm. Two Ø4.8 mm mounting holes (M4) ~47.6 mm apart on the long axis. SSR-40DA shares the SAME housing and hole pattern (only current rating differs).
- **Connectors:** 4 screw terminals: input 3-32 VDC (terminals 3,4), output 24-480 VAC (terminals 1,2).
- **⚠ Verify:** SSR-DA series body ~57.4 x 44.8 x 28 mm and ~47.6 mm hole spacing for M4 are the well-known Fotek standard, but the exact figures were NOT read off the datasheet drawing directly (datasheet sites returned 403/were not fetched). Multiple distributor listings give ~63 x 45 x 23 mm overall incl. terminals; housing footprint vs overall differs. CONFIRM hole spacing on the actual unit before a tight-tolerance bracket. SSR-40DA = same housing.
- src: https://www.fotek.com.tw/en-gb/product-category/143
- src: https://www.alldatasheet.com/datasheet-pdf/pdf/1132522/FOTEK/SSR-25DA.html

## Fysetc

### Catalyst V2.0  ·  `fysetc_catalyst_v2_0`

- **Category:** mainboard  ·  **Confidence:** low
- **PCB:**  ×  mm, 1.6 mm thick
- **Mounting:** 4× M3 (Ø3.2), pattern rectangular, pitch × mm
  - notes: Voron 0 dedicated board (CM68 Cortex-A55 SBC carrier + STM32F401/F446, 4x stepstick). Designed to mount in the Voron 0 electronics location; the product page notes the V0 mount is 15 mm from plate, board adds 6 mm + 1.6 mm so a shim is used. 4 corner mounting holes visible on CATALYST V2.0 PinsOut.png. FYSETC did NOT publish PCB length/width or hole pitch anywhere found; a CAD STEP (CATALYST Board V2.0 STEP.rar) and an interactive 3D PDF exist in the repo but no dimensioned drawing. Left null rather than guessed.

- **Connectors:** CM68 (RK3568) SBC carrier + STM32 motion MCU, 4x driver, 15A bed MOS, multi-voltage fans. Mounts in Voron 0 with a printed mount/shim (community mounts exist on Printables).

- **⚠ Verify:** PCB length/width and hole pitch NOT found in any authoritative source — measure the board or open hardware/CATALYST Board V2.0 STEP.rar. Only confirmed: M3 4-corner holes (from PinsOut.png), Voron 0 mounting context, ~6 mm board stack + 1.6 mm PCB. DO NOT design a mount from this entry without measuring.

- src: https://github.com/FYSETC/Catalyst_Kit_V2.0 (hardware/ STEP + PinsOut.png + PDF3D)
- src: https://www.fysetc.com/products/fysetc-catalyst-motherboard-based-on-arm-a55-m4-support-spi-and-uart-for-tmc2209-voron-v0-high-quality-3d-printer-parts

### Cheetah V2.0  ·  `fysetc_cheetah_v2_0`

- **Category:** mainboard  ·  **Confidence:** medium
- **PCB:** 101.5 × 72.0 mm, 1.6 mm thick
- **Mounting:** 4× M3 (Ø3.2), pattern rectangular, pitch × mm
  - notes: Wiki: "101.5mm x 72mm, Compatible with the Creality ender 3 motherboard size". COPIES the Creality Ender 3 / Ender 5 mounting footprint (4 holes), so Ender 3 board mounts fit. FYSETC does not restate the Ender 3 hole coordinates; use the documented Ender 3 board pattern. STM32F401, 4x onboard TMC2209.

- **Clearance:** standoff 5 mm, top component  mm
- **Connectors:** STM32F401, 4x onboard 2209, EXP display headers, used on Voron 0.1.
- **⚠ Verify:** PCB size high-confidence. Hole pattern = Creality Ender 3 footprint (vendor-stated compatibility) but exact coordinates not given by FYSETC — cross-check against an Ender 3 board template before cutting.

- src: https://wiki.fysetc.com/Cheetah_Board_V20/
- src: https://github.com/FYSETC/FYSETC-Cheetah-v2

### Cheetah V3.0  ·  `fysetc_cheetah_v3_0`

- **Category:** mainboard  ·  **Confidence:** medium
- **PCB:** 101.5 × 72.0 mm, 1.6 mm thick
- **Mounting:** 4× M3 (Ø3.2), pattern rectangular, pitch × mm
  - notes: Wiki: "101.5mm x 72mm, Compatible with the Creality ender 3/ender5 motherboard size". Four-layer TG155 FR4. Same Ender 3/5 mounting footprint as V2.0; pinout differs (not config-compatible with V2). 4 corner holes visible on the V3.0 Position PDF. Exact hole coordinates not published — use the Ender 3 board pattern.

- **Clearance:** standoff 5 mm, top component  mm
- **Connectors:** STM32F446 180MHz, BLTouch + CAN headers, 5V@SBC power, multi-voltage fans, EXP1/EXP2.
- **⚠ Verify:** PCB size high-confidence. Hole pattern = Ender 3/5 footprint (vendor-stated). A Cheetah_V3.0.step file exists in the repo for exact hole extraction; raw point-cloud bbox was noisy here, so coordinates left null rather than reported wrong.

- src: https://wiki.fysetc.com/Cheatah_Board_V30/
- src: https://github.com/FYSETC/Cheetah_V3.0 (Hardware/CHEETAH V3.0 Position.pdf, Cheetah_V3.0.step)

### Mini12864 Panel (RGB) V2.1  ·  `fysetc_mini12864_rgb_v2_1`

- **Category:** accessory  ·  **Confidence:** high
- **PCB:** 104.99 × 47.0 mm, 1.6 mm thick
- **Mounting:** 4× M3 (Ø3.2), pattern rectangular, pitch 41.0×93.0 mm
  - notes: Measured directly from the vendor dimensional drawing 12864mini(RGB)_V2.1_dwg.pdf. PCB = 104.99 mm (long) x 47 mm (wide). Four mounting holes in a rectangular pattern: 41 mm horizontal pitch x 93 mm vertical pitch (callouts read "41", "93", "104,99", "47" on the drawing). This is the standard Mini12864 display footprint — COMPATIBLE with the BTT Mini12864 / Voron-spec Mini12864 mounts and cases. Hole dia assumed M3 clearance (~3.2 mm); drawing did not annotate hole diameter. V2.0 shares the same outline (separate dwg in repo).

- **Connectors:** Sitronix ST7567 128x64 LCD with RGB indicator, SD card slot (side or vertical), SPI to host, 2x EXP ribbon headers. 3D-printable case/mount STLs available.

- **⚠ Verify:** length/width and 41 x 93 mm 4-hole pattern read directly off the vendor dimensioned drawing (high). Standard Mini12864 footprint — interchangeable with BTT/Voron Mini12864 mounts. Hole diameter (3.2) inferred, not annotated.

- src: https://github.com/FYSETC/FYSETC-Mini-12864-Panel (hardware/V2.1/12864mini(RGB)_V2.1_dwg.pdf)
- src: https://wiki.fysetc.com/Mini12864_Panel/

### S6 V1.2  ·  `fysetc_s6_v1_2`

- **Category:** mainboard  ·  **Confidence:** medium
- **PCB:** 117.0 × 87.0 mm, 1.6 mm thick
- **Mounting:** × M3 (Ø3.2), pattern rectangular, pitch × mm
  - notes: Wiki: "Compact size: 117mm x 87mm, Same as F6" — shares the FYSETC F6 PCB outline, so F6 mounts/holders fit. Mounting hole count and spacing not published by FYSETC; many Thingiverse F6 cases work. V1.2 and V2.1 share this outline.

- **Clearance:** standoff 5 mm, top component  mm
- **Connectors:** STM32F446VET6, 6 driver sockets, XH connectors.
- **⚠ Verify:** PCB size high-confidence (wiki). Hole pattern unverified (null). Shares footprint with FYSETC F6.

- src: https://wiki.fysetc.com/FYSETC_S6/
- src: https://github.com/FYSETC/FYSETC-S6

### SB CAN Toolhead (V1.1 / V1.3)  ·  `fysetc_sb_can_toolhead`

- **Category:** toolhead_can  ·  **Confidence:** low
- **PCB:**  ×  mm, 1.6 mm thick
- **Mounting:** 2× M3 (Ø3.2), pattern rectangular, pitch × mm
  - notes: STM32F072 Stealthburner CAN toolhead board (onboard TMC2209 + ADXL345), the FYSETC equivalent of the BTT EBB SB2209/SB2240 class. Wiki install step states "Your Stealthburner should have two holes with heat inserts on" — i.e. it mounts to the standard Voron Stealthburner toolhead with 2x M3 heat-set inserts (the Stealthburner SB-board footprint). FYSETC ships SB CAN TOOLHEAD V1.1.DXF and V1.1/V1.3 STEP files, but no dimensioned drawing; the DXF/STEP geometry was too noisy (cable model included) to extract a reliable PCB outline or exact 2-hole spacing here, so length/width and pitch are null.

- **Connectors:** STM32F072, onboard 2209, ADXL345, Micro-USB (firmware/DFU), HE0 (XH2.54 2P, 4A), CAN. Mounts behind the Stealthburner front; 2.5 m 4-core CAN cable included.

- **⚠ Verify:** Footprint = Voron Stealthburner SB-board (2x M3 heat-set holes) per wiki install text — call out as a copied/standard Stealthburner footprint. Exact PCB size and 2-hole spacing NOT reliably extracted; pull from SB CAN TOOLHEAD V1.1.DXF / V1.3.step or measure before use.

- src: https://github.com/FYSETC/FYSETC_SB_CAN_TOOLHEAD (DXF + STEP, SB CAN TollHead V1.1 Position.pdf)
- src: https://wiki.fysetc.com/SB%20CAN%20ToolHead/

### Spider King V1.0  ·  `fysetc_spider_king_v1`

- **Category:** mainboard  ·  **Confidence:** medium
- **PCB:** 177.0 × 108.0 mm, 1.6 mm thick
- **Mounting:** × M3 (Ø3.2), pattern rectangular, pitch × mm
  - notes: 10-axis industrial mainboard with swappable "King" MCU core (RP2040 / F446 / F407 / H7xx). Wiki states "very small size of 177mm*108mm". Mounting hole count/pattern not published.

- **Clearance:** standoff 5 mm, top component  mm
- **Connectors:** Up to 10 stepper drivers, isolated CAN, ESP32/WiFi, multiple Pi links. Large board.
- **⚠ Verify:** PCB size high-confidence (wiki "177mm*108mm"). Hole pattern entirely unverified — null. thickness_mm assumed 1.6 (typical), not vendor-stated.

- src: https://wiki.fysetc.com/FYSETC-SPIDER-KING/
- src: https://github.com/FYSETC/FYSETC-SPIDER-KING

### Spider Pro V1.2  ·  `fysetc_spider_pro_v1_2`

- **Category:** mainboard  ·  **Confidence:** high
- **PCB:** 179.0 × 109.0 mm, 1.6 mm thick
- **Mounting:** 4× M3 (Ø3.2), pattern rectangular, pitch 92.0×92.0 mm
  - holes (x,y mm): [[33.76, 14.2], [33.76, 106.2], [125.76, 14.2], [125.76, 106.2]]
  - notes: Measured directly from the vendor CAD file SPIDER_PRO_V1.2_CAD.dxf. PCB OUTLINE layer bbox = 179.0 x 109.0 mm. Four mounting holes form a 92 x 92 mm rectangular pattern at the listed centers (origin = DXF coordinate frame, NOT guaranteed to be the bottom-left PCB corner; the outline starts near X=26.8/Y=5.7 in the same frame, so subtract that offset if you need corner-relative coords). The hole circles read r=3.1 mm (copper ring/keepout); actual drill is M3 clearance (~3.2 mm). Two additional r=3.0 holes near the right edge at ~(201.7,18.3)/(201.7,102.1) appear to be secondary fixings. Spider Pro is a LARGER board than the standard Spider (155.3x76.5) — do not interchange mounts.

- **Clearance:** standoff 5 mm, top component  mm
- **Connectors:** Spider Pro is the higher-spec Spider with onboard isolated CAN etc.
- **⚠ Verify:** length/width and the 92x92 mm 4-hole pattern measured from vendor DXF (high). Hole-center origin is the DXF frame, not necessarily PCB corner — re-zero to the OUTLINE bbox before use.

- src: https://github.com/FYSETC/Spider_Pro/blob/main/Hardware/SPIDER_PRO_V1.2_CAD.dxf

### Spider V1.x  ·  `fysetc_spider_v1_x`

- **Category:** mainboard  ·  **Confidence:** medium
- **PCB:** 155.3 × 76.5 mm, 1.6 mm thick
- **Mounting:** 4× M3 (Ø3.2), pattern rectangular, pitch × mm
  - notes: 4 mounting holes, one near each corner (visible on the official Spider V1.0C/V1.1 Designator Diagram PDFs). FYSETC does not publish exact hole coordinates. Hole diameter assumed M3 clearance (~3.2 mm) from community Spider mounts; not vendor-stated. V1.0/V1.1 differ electrically (5V@8A DC-DC) but share the Spider PCB outline.

- **Clearance:** standoff 5 mm, top component  mm
- **Connectors:** STM32F446 mainboard for Voron 2.4 / Trident; 8 driver sockets. Tallest components are the driver heatsinks and electrolytic caps; top clearance not vendor-specified.

- **⚠ Verify:** PCB size high-confidence (wiki). Hole pattern/pitch unverified — measure a board or the V1.x designator diagram before cutting standoffs.

- src: https://wiki.fysetc.com/Spider/
- src: https://github.com/FYSETC/FYSETC-SPIDER (hardware/V1.x designator diagrams)

### Spider V2.2  ·  `fysetc_spider_v2_2`

- **Category:** mainboard  ·  **Confidence:** medium
- **PCB:** 155.3 × 76.5 mm, 1.6 mm thick
- **Mounting:** 4× M3 (Ø3.2), pattern rectangular, pitch × mm
  - notes: 4 corner mounting holes confirmed visually on the official "Spider V2.2 Designator Diagram.pdf". Same PCB outline as V1.x/V2.3/V3.0. Exact hole coordinates not published by FYSETC; pitch left null rather than guessed.

- **Clearance:** standoff 5 mm, top component  mm
- **Connectors:** STM32F446 180MHz. 8 driver sockets. Identical footprint family to other Spider revs.
- **⚠ Verify:** PCB size high-confidence (wiki "155.3mm x 76.5mm"). 4-hole rectangular pattern confirmed from vendor designator PDF; pitch not measurable from that PDF — verify before use.

- src: https://wiki.fysetc.com/Spider/
- src: https://github.com/FYSETC/FYSETC-SPIDER (hardware/V2.2)

### Spider V3 (V3.0)  ·  `fysetc_spider_v3_0`

- **Category:** mainboard  ·  **Confidence:** medium
- **PCB:** 155.3 × 76.5 mm, 1.6 mm thick
- **Mounting:** 4× M3 (Ø3.2), pattern rectangular, pitch × mm
  - notes: Drop-in replacement for earlier Spider revs sharing the 155.3 x 76.5 mm outline and the Voron 2.4 R2 / Trident wiring. STM32F446 (and an H7 variant, see fysetc_spider_v3_h7). 4 corner holes; exact coordinates not vendor-published.

- **Clearance:** standoff 5 mm, top component  mm
- **Connectors:** STM32F446 V3.0. Same mounting footprint as V1.x/V2.x Spider per shared Voron wiring docs.
- **⚠ Verify:** PCB size high-confidence. Pitch unverified. "V3" without H7 suffix = STM32F446; do not confuse with Spider V3.0 H7 (separate repo FYSETC-SPIDER-H7) which shares the outline.

- src: https://wiki.fysetc.com/Spider/
- src: https://github.com/FYSETC/FYSETC-SPIDER (hardware/V3.0)

### Spider V3.0 H7  ·  `fysetc_spider_v3_h7`

- **Category:** mainboard  ·  **Confidence:** medium
- **PCB:** 155.3 × 76.5 mm, 1.6 mm thick
- **Mounting:** 4× M3 (Ø3.2), pattern rectangular, pitch × mm
  - notes: STM32H723 550MHz variant of the Spider, same Spider PCB outline and Voron mounting. Separate hardware repo (FYSETC-SPIDER-H7) but FYSETC markets it as form-factor compatible with the standard Spider. Hole coordinates not published.

- **Clearance:** standoff 5 mm, top component  mm
- **Connectors:** STM32H723VGT6. Same Spider footprint as F446 versions.
- **⚠ Verify:** PCB size inherited from Spider line (high-confidence). Pitch unverified. Included because the task asked for "king/v3" and notable current Spider variants.

- src: https://www.fysetc.com/products/fysetc-spider-v3-0-h7-32-bit-motherboard
- src: https://github.com/FYSETC/FYSETC-SPIDER-H7

### UCAN V1.0  ·  `fysetc_ucan_v1_0`

- **Category:** usb_can_bridge  ·  **Confidence:** low
- **PCB:**  ×  mm, 1.6 mm thick
- **Mounting:** 0×  (Ø), pattern other, pitch × mm
  - notes: Small open-source USB-C-to-CAN bridge dongle (STM32F072CBT6, candleLight firmware). It is a long, thin USB-stick-form board with USB-C on one end and a CAN connector/JST on the other. The Component Position drawing shows NO dedicated screw mounting holes (the large circles on the silk are corner copper/keepout zones, not mounting holes) — this is a free-floating dongle, not a panel-mount board. PCB outline dimensions are not published in any spec line; a UCAN_ V1.0.step CAD file exists in the repo but raw extraction was unreliable.

- **Connectors:** USB-C (PA11/PA12) one end, CAN (PA8/PA9) the other, status LEDs. No mounting hardware.
- **⚠ Verify:** No mounting pattern (dongle) — high-confidence there are no screw holes per the position drawing. PCB length/width NOT published; open CAD/UCAN_ V1.0.step or measure. Typical units of this class are roughly 36 x 12 mm but THIS IS NOT VENDOR-CONFIRMED — left null.

- src: https://wiki.fysetc.com/UCAN/
- src: https://github.com/FYSETC/UCAN (CAD/UCAN_ V1.0.step, Hardware/UCAN V1.0 Component Position.pdf)
- src: https://www.fysetc.com/products/fysetc-ucan-board

## Generic/various

### 3D printer heatbed MOSFET power module (25A)  ·  `heatbed_mosfet_module`

- **Category:** mosfet  ·  **Confidence:** medium
- **PCB:** 60.0 × 50.0 mm, 1.6 mm thick
- **Mounting:** 4× M3 (Ø3.2), pattern rectangular, pitch × mm
  - notes: Common heatbed MOSFET board ~60 x 50 mm (overall incl. heatsink ~30 mm tall), 4 corner holes Ø3.2 mm for M3. Exact hole pitch varies by clone and is NOT consistently published - MEASURE before a tight mount.
- **Clearance:** standoff  mm, top component 30.0 mm
- **Connectors:** Input screw terminal (12/24V + trigger from board heater output), output screw terminal to bed. Switches via power MOSFET (allows PID).
- **⚠ Verify:** ~60 x 50 mm outline and Ø3.2 mm M3 corner holes corroborated across vendor listings (medium). Hole PITCH not authoritatively published and varies between clones - low confidence on exact spacing; measure the actual board.
- src: https://reprap.org/wiki/Heated_Bed_MOSFET_Power_Expansion_Module
- src: https://www.th3dstudio.com/product/high-amp-12v-24v-mosfet-heated-bed-or-hotend/

### GY-291 ADXL345 accelerometer breakout  ·  `gy291_adxl345`

- **Category:** accelerometer  ·  **Confidence:** medium
- **PCB:** 20.4 × 15.8 mm, 1.6 mm thick
- **Mounting:** 2× M3 (Ø3.0), pattern 2-hole, pitch 15.0×0.0 mm
  - notes: The de-facto standard mount: 2 collinear Ø3 mm holes, 15 mm apart, on the edge opposite the pin header. The BTT USB boards copy this at 15.5 mm so they are mount-compatible. NO 4-corner hole pattern exists on this board.
- **Connectors:** 8-pin (or 7-pin) 2.54 mm header: GND/VCC/CS/SDO/SDA/SCL/INT1/INT2. SPI or I2C.
- **⚠ Verify:** 2-hole / Ø3 / 15 mm spacing corroborated by an authoritative vendor and the community-standard layout. Exact outline varies slightly by clone; thickness assumed 1.6 mm. NOT a 4-hole board.
- src: https://www.bastelgarage.ch/acceleration-sensor-adxl345-gy-291

### LM2596 adjustable buck converter module  ·  `lm2596_buck`

- **Category:** buck_converter  ·  **Confidence:** medium
- **PCB:** 43.2 × 21.0 mm, 1.6 mm thick
- **Mounting:** 2× M3 (Ø), pattern 2-hole, pitch × mm
  - notes: ~43.2 x 21 x 14 mm. 2 mounting holes (diagonal corners) for small M3/M2.5 screws. Hole spacing not authoritatively published - measure the unit.
- **Clearance:** standoff  mm, top component 14.0 mm
- **Connectors:** IN+/IN- and OUT+/OUT- solder pads; multiturn trimpot for output voltage.
- **⚠ Verify:** 43.2 x 21 x 14 mm corroborated; 2 holes confirmed. Exact hole spacing and diameter not published - measure before designing a tight mount.
- src: https://components101.com/modules/mini360-dc-dc-buck-converter-module
- src: https://www.theengineeringprojects.com/2020/09/lm2596-buck-converter-datasheet-pinout-features-applications.html

### Mini-360 DC-DC buck converter module  ·  `mini360_buck`

- **Category:** buck_converter  ·  **Confidence:** medium
- **PCB:** 22.0 × 17.0 mm, 1.6 mm thick
- **Mounting:** 0×  (Ø), pattern none, pitch × mm
  - notes: Tiny ~22 x 17 x 4 mm module with NO mounting holes - typically hot-glued or pocketed/zip-tied in place. Design a friction pocket, not a screw mount.
- **Clearance:** standoff  mm, top component 4.0 mm
- **Connectors:** IN+/IN- and OUT+/OUT- solder pads; trimpot for output voltage.
- **⚠ Verify:** ~22 x 17 x 4 mm corroborated; no mounting holes (pocket/glue mount).
- src: https://components101.com/modules/mini360-dc-dc-buck-converter-module

### TMC2208 StepStick driver module  ·  `stepstick_tmc2208`

- **Category:** driver_module  ·  **Confidence:** high
- **PCB:** 20.32 × 15.24 mm, 1.6 mm thick
- **Mounting:** 0×  (Ø), pattern none(header-mounted), pitch 15.24×2.54 mm
  - notes: Identical StepStick footprint to TMC2209; header-mounted, no screws.
- **Connectors:** 2x 1x8 0.1in male pin headers.
- **⚠ Verify:** Same 0.6 x 0.8 in StepStick standard as TMC2209.
- src: https://reprap.org/wiki/StepStick
- src: https://www.pololu.com/product/1182

## Generic/various (FYSETC, BTT plug-in)

### TMC5160 plug-in StepStick driver module  ·  `stepstick_tmc5160`

- **Category:** driver_module  ·  **Confidence:** medium
- **PCB:** 20.32 × 15.24 mm, 1.6 mm thick
- **Mounting:** 0×  (Ø), pattern none(header-mounted), pitch 15.24×2.54 mm
  - notes: The StepStick-form-factor TMC5160 (plug-in) shares the 15.24 x 20.32 mm footprint. NOTE: this is the plug-in module ONLY; the high-power external TMC5160T Plus is a separate entry below.
- **Connectors:** 2x 1x8 0.1in male pin headers; taller components/caps on top.
- **⚠ Verify:** Plug-in TMC5160 modules follow the StepStick footprint, but some vendor variants are slightly wider or taller due to larger caps. Confidence medium on exact outline for a specific vendor part; header pitch is standard.
- src: https://reprap.org/wiki/StepStick

## Generic/various (SONGLE SRD-05VDC-SL-C)

### 1-channel 5V relay module  ·  `relay_module_1ch`

- **Category:** relay  ·  **Confidence:** low
- **PCB:** 50.0 × 26.0 mm, 1.6 mm thick
- **Mounting:** 2× M3 (Ø3.1), pattern 2-hole, pitch × mm
  - notes: Common 1-channel board ~50 x 26 mm with 2 corner holes for M3. Exact outline and hole spacing vary by clone - measure the specific unit.
- **Clearance:** standoff  mm, top component 19.0 mm
- **Connectors:** 3-pin control header (VCC/GND/IN); screw terminal NO/COM/NC; jumper for opto-isolation.
- **⚠ Verify:** 1-channel boards are not standardized; ~50 x 26 mm is typical but outline and hole pitch vary widely between vendors. Treat as low confidence and measure the actual board.
- src: https://components101.com/switches/5v-single-channel-relay-module-pinout-features-applications-working-datasheet
- src: https://www.handsontec.com/dataspecs/relay/SRD-05VDC-SL-C.pdf

### 2-channel 5V relay module  ·  `relay_module_2ch`

- **Category:** relay  ·  **Confidence:** low
- **PCB:** 50.5 × 38.5 mm, 1.6 mm thick
- **Mounting:** 4× M3 (Ø3.1), pattern rectangular, pitch × mm
  - notes: Common 2-channel board ~50.5 x 38.5 mm, 4 corner holes for M3. Outline and hole spacing vary by clone - measure the specific unit.
- **Clearance:** standoff  mm, top component 19.0 mm
- **Connectors:** 4-pin control header (VCC/GND/IN1/IN2) or 6-pin with JD-VCC; 2x screw terminals NO/COM/NC.
- **⚠ Verify:** 2-channel boards not standardized; ~50.5 x 38.5 mm typical. SainSmart/clone variants differ. Low confidence on exact outline and hole pitch - measure.
- src: https://components101.com/switches/5v-dual-channel-relay-module-pinout-features-applications-working-datasheet
- src: https://www.sainsmart.com/products/2-channel-5v-relay-module

### 4-channel 5V relay module  ·  `relay_module_4ch`

- **Category:** relay  ·  **Confidence:** medium
- **PCB:** 71.0 × 45.0 mm, 1.6 mm thick
- **Mounting:** 4× M3 (Ø3.1), pattern rectangular, pitch 66.7×40.0 mm
  - holes (x,y mm): [[2.15, 2.5], [68.85, 2.5], [2.15, 42.5], [68.85, 42.5]]
  - notes: Most standardized of the blue relay boards: 71 x 45 mm, 4 corner holes Ø3.0-3.1 mm, hole rectangle 66.7 x 40 mm. Hole coords derived by centering that rectangle in the outline (verify on actual board).
- **Clearance:** standoff  mm, top component 19.0 mm
- **Connectors:** 6-pin control header (VCC/GND/IN1-IN4) + JD-VCC jumper; 4x screw terminals NO/COM/NC.
- **⚠ Verify:** 71 x 45 mm outline and 66.7 x 40 mm hole spacing corroborated across multiple vendor listings (medium-high). Hole diameter 3.0-3.1 mm. Corner hole coords are derived (centered rectangle) - confirm inset on the unit.
- src: https://components101.com/switches/5v-four-channel-relay-module-pinout-features-applications-working-datasheet
- src: http://wiki.sunfounder.cc/index.php?title=4_Channel_5V_Relay_Module
- src: https://www.circuitbasics.com/wp-content/uploads/2015/11/SRD-05VDC-SL-C-Datasheet.pdf

## Generic/various (Watterott SilentStepStick, BTT, FYSETC, etc.)

### TMC2209 StepStick / SilentStepStick driver module  ·  `stepstick_tmc2209`

- **Category:** driver_module  ·  **Confidence:** high
- **PCB:** 20.32 × 15.24 mm, 1.6 mm thick
- **Mounting:** 0×  (Ø), pattern none(header-mounted), pitch 15.24×2.54 mm
  - notes: Standard Pololu/StepStick footprint 0.6 in x 0.8 in. Mounts via two 1x8 (16-pin total) 0.1 in (2.54 mm) male headers, NOT screws. The two header rows sit 0.6 in (15.24 mm) apart, each row spanning 7 x 2.54 = 17.78 mm. TMC2208 plug-in module is the SAME footprint.
- **Connectors:** 2x 1x8 0.1in male pin headers (plugs into stepper-driver socket).
- **⚠ Verify:** 15.24 x 20.32 mm is the industry-standard StepStick/Pololu carrier size, corroborated by the TMC2209 SilentStepStick datasheet and the BTT MAX31865 manual (which states it copies the stepper-driver footprint at exactly this size). Header-mounted only; no screw holes. Top heatsink height varies.
- src: https://www.mouser.com/pdfDocs/TMC2209_SilentStepStick_Rev110.pdf
- src: https://reprap.org/wiki/TMC2209
- src: https://www.pololu.com/product/1182

## HartK

### HartK Stealthburner Toolhead PCB  ·  `hartk_stealthburner_toolhead_pcb`

- **Category:** toolhead_can  ·  **Confidence:** low
- **PCB:**  ×  mm, 1.6 mm thick
- **Mounting:** × M3 (Ø3.2), pattern other, pitch × mm
  - notes: The reference two-piece Voron Stealthburner toolhead PCB that many toolboards (incl. LDO Nitehawk-SB) clone for their form factor. Mounts into the Stealthburner printed body with M3x8 SHCS + M3x6 BHCS (per Voron hardware docs), NOT a board-edge rectangular pattern. Only Gerbers/STEP are published (no raw KiCad .kicad_pcb), so exact outline/hole XY were not machine-extracted. Included as a flag because it is a de-facto footprint standard worth its own library entry.
- **Clearance:** standoff 5 mm, top component  mm
- **⚠ Verify:** Flagged reference footprint. Outline + hole XY UNVERIFIED -- extract from Gerbers/STEP in CAD if a library entry is wanted. Mounting is body-clip, not a simple hole pattern.
- src: https://github.com/VoronDesign/Voron-Hardware/tree/master/Stealthburner_Toolhead_PCB
- src: https://github.com/hartk1213/MISC/tree/main/PCBs/Stealthburner_Toolhead_PCB

## Huvud

### Huvud (original)  ·  `huvud_original`

- **Category:** toolhead_can  ·  **Confidence:** high
- **PCB:** 48.0 × 45.0 mm, 1.6 mm thick
- **Mounting:** 4× M3 (Ø3.2), pattern rectangular, pitch 37.0×40.0 mm
  - holes (x,y mm): [[4.0, 4.0], [41.0, 4.0], [4.0, 44.0], [41.0, 44.0]]
  - notes: Open-hardware Klipper toolhead board. 37x40 mm rectangular pattern -- does NOT match the NEMA17 31 mm bolt circle; mounts via a printed bracket, not directly on a stepper face. Parsed from KiCad source (small connector notch on top edge). holes_xy derived from outline + pitch (4 mm inset).
- **Clearance:** standoff 5 mm, top component  mm
- **Connectors:** Connector notch on the top edge.
- **⚠ Verify:** Outline + 37x40 pattern from KiCad. holes_xy derived from pitch/inset.
- src: https://github.com/bondus/KlipperToolboard/blob/master/PCB/Huvud/Huvud.kicad_pcb

### HuvudTiny  ·  `huvud_tiny`

- **Category:** toolhead_can  ·  **Confidence:** high
- **PCB:** 42.0 × 42.0 mm, 1.6 mm thick
- **Mounting:** 4× M3 (Ø3.2), pattern rectangular, pitch 31.0×31.0 mm
  - holes (x,y mm): [[5.5, 5.5], [36.5, 5.5], [5.5, 36.5], [36.5, 36.5]]
  - notes: 42x42 mm board; 31x31 mm square pattern = exactly the NEMA17 bolt circle, perfectly centred (5.5 mm inset all sides). Bolts directly onto the back face of a NEMA17 stepper with M3 screws. Plated holes (via). Parsed from KiCad source.
- **Clearance:** standoff 5 mm, top component  mm
- **⚠ Verify:** Outline + centred 31x31 NEMA17 pattern confirmed from KiCad geometry.
- src: https://github.com/bondus/KlipperToolboard/blob/master/PCB/HuvudTiny/Huvud.kicad_pcb

## LDO Motors

### LDO Leviathan (V1.2/V1.3)  ·  `ldo_leviathan`

- **Category:** mainboard  ·  **Confidence:** high
- **PCB:** 170.0 × 100.0 mm, 1.6 mm thick
- **Mounting:** 4× M3 (Ø3.2), pattern rectangular, pitch 160.0×90.0 mm
  - holes (x,y mm): [[5.0, 5.0], [165.0, 5.0], [5.0, 95.0], [165.0, 95.0]]
  - notes: Voron-oriented all-in-one mainboard. Rounded-rect, 5 mm corner radius; holes 5 mm in from all edges, concentric with the corner arcs. Holes are plated top+bottom (grounding). V1.2 and V1.3 share this form factor. Parsed from KiCad source -- all four numbers confirmed from geometry.
- **Clearance:** standoff 6 mm, top component  mm
- **⚠ Verify:** Outline, holes, AND thickness (1.6 mm from board stackup) all confirmed directly from KiCad source.
- src: https://github.com/MotorDynamicsLab/Leviathan/blob/main/KiCad/V1.3/Leviathan_V1.3.kicad_pcb

### LDO Nitehawk-36  ·  `ldo_nitehawk_36`

- **Category:** toolhead_can  ·  **Confidence:** low
- **PCB:**  ×  mm, 1.6 mm thick
- **Mounting:** × M3 (Ø3.2), pattern other, pitch 43.84× mm
  - notes: Toolhead board for the 36 mm NEMA14 standard; commonly mounted via a printed adapter (repo ships Universal/Rigid/Flex, G2SA, WWG2, O2, Orbiter mounts). Two Ø3.2 mm (M3) mounting circles in the source geometry are spaced 43.84 mm in X (same toolhead-PCB hole spacing as the Mellow SHT36 -- a useful cross-check that 43.84 mm is a real standard). PCB 1.6 mm thick (STEP z-layer). Full hole set / outline could not be cleanly extracted because the shipped STEP is a full assembly.
- **Clearance:** standoff 5 mm, top component  mm
- **⚠ Verify:** 43.84 mm X hole spacing and 1.6 mm thickness are firm; PCB outline, full hole count/pattern, and Y pitch UNVERIFIED. Extract from the repo DXF/STEP in CAD before cutting. Often mounted via a printed adapter rather than directly.
- src: https://github.com/MotorDynamicsLab/Nitehawk-36
- src: https://github.com/MotorDynamicsLab/Nitehawk-36/blob/master/CAD/NH36-outline.dxf
- src: https://github.com/MotorDynamicsLab/Nitehawk-36/blob/master/Hardware/Nitehawk-36%20V1.2/Nitehawk-36_V1.2_3D%20Layout.pdf

### LDO Nitehawk-SB  ·  `ldo_nitehawk_sb`

- **Category:** toolhead_can  ·  **Confidence:** low
- **PCB:**  ×  mm, 1.6 mm thick
- **Mounting:** × M3 (Ø3.2), pattern other, pitch × mm
  - notes: Stealthburner toolhead board; form factor "based on HartK's two-piece Stealthburner toolhead PCB" (the de-facto Voron SB toolhead PCB standard). It clips/screws into the Stealthburner printed body (M3 into the SB fan housing), NOT a stepper bolt circle or a simple rectangular pattern. PCB is 1.6 mm thick (confirmed from STEP z-layer). No KiCad source published; the shipped STEP is a full toolhead assembly, so clean outline/hole XY could not be machine-extracted.
- **Clearance:** standoff 5 mm, top component  mm
- **Connectors:** Mounts behind the Stealthburner front; USB adapter is a separate PCB.
- **⚠ Verify:** Mounting is via the Stealthburner body, not a board-edge hole pattern. PCB outline + exact hole XY UNVERIFIED -- extract from the repo STEP / dimensioned Layout.pdf in CAD, or use the HartK Stealthburner_Toolhead_PCB reference footprint. Thickness 1.6 mm is firm.
- src: https://github.com/MotorDynamicsLab/Nitehawk-SB
- src: https://github.com/MotorDynamicsLab/Nitehawk-SB/blob/master/Hardware/Nitehawk-SB_V1.5_3D%20Layout.pdf
- src: https://docs.ldomotors.com/en/Toolboard/nitehawk-sb

## Makerbase

### MKS CANable V2.0  ·  `mks_canable_v2`

- **Category:** usb_can_bridge  ·  **Confidence:** high
- **PCB:** 45.0 × 16.2 mm, 1.6 mm thick
- **Mounting:** 4× M2 (Ø2.2), pattern rectangular, pitch 34.7×12.6 mm
  - holes (x,y mm): [[9.0, 1.8], [43.7, 1.8], [9.0, 14.4], [43.7, 14.4]]
  - notes: USB-CAN adapter. Fully dimensioned drawing. Holes are M2 (Ø2.20), NOT M3. Left holes 9.0 mm in from left edge; right holes 1.3 mm in from right edge (43.7 mm from left); X pitch = 34.7 mm. Y span 12.6 mm, ~1.8 mm inset top/ bottom. CANable V1.0 and Pro-V1.0 are separate boards (not measured here).
- **Clearance:** standoff 4 mm, top component  mm
- **Connectors:** USB on one short edge, CAN terminal/connector on the other.
- **⚠ Verify:** Fully dimensioned drawing, all values annotated. Thickness not annotated.
- src: https://github.com/makerbase-mks/CANable-MKS/blob/main/Hardware/MKS%20CANable%20V2.0/MKS%20CANable%20V2.0_001%20size.pdf

### MKS Monster8 V2.0  ·  `mks_monster8_v2`

- **Category:** mainboard  ·  **Confidence:** medium
- **PCB:** 160.0 × 90.0 mm, 1.6 mm thick
- **Mounting:** 4× M3 (Ø3.2), pattern rectangular, pitch 152.0×82.0 mm
  - holes (x,y mm): [[4.0, 4.0], [156.0, 4.0], [4.0, 86.0], [156.0, 86.0]]
  - notes: Outline and hole positions are high confidence. Hole DIAMETER is NOT numerically annotated in the SIZE.pdf (unlike Robin Nano/SKIPR); 3.2 mm / M3 inferred from pad geometry and board class -- see verify_notes.
- **Clearance:** standoff 5 mm, top component  mm
- **⚠ Verify:** Outline + hole XY high confidence. Hole Ø (3.2 mm) is INFERRED, not annotated -- confirm against a Gerber/STEP before relying on hole diameter. Thickness not annotated.
- src: https://github.com/makerbase-mks/MKS-Monster8/blob/main/hardware/MKS%20Monster8%20V2.0_003/MKS%20Monster8%20V2.0_003%20SIZE.pdf

### MKS Robin Nano V3.x  ·  `mks_robin_nano_v3`

- **Category:** mainboard  ·  **Confidence:** high
- **PCB:** 110.0 × 84.0 mm, 1.6 mm thick
- **Mounting:** 4× M3 (Ø3.4), pattern rectangular, pitch 102.0×76.5 mm
  - holes (x,y mm): [[4.0, 3.75], [106.0, 3.75], [4.0, 80.25], [106.0, 80.25]]
  - notes: V3.0 and V3.1 share this outline. Hole Ø annotated 3.40 mm (M3 clearance).
- **Clearance:** standoff 5 mm, top component  mm
- **⚠ Verify:** Outline + hole Ø annotated in SIZE.pdf. Thickness not annotated (1.6 mm assumed).
- src: https://github.com/makerbase-mks/MKS-Robin-Nano-V3.X/blob/main/hardware/MKS%20Robin%20Nano%20V3.1_001/MKS%20Robin%20Nano%20V3.1_001%20SIZE.pdf

### MKS SKIPR V1.0  ·  `mks_skipr`

- **Category:** mainboard  ·  **Confidence:** high
- **PCB:** 160.0 × 100.0 mm, 1.6 mm thick
- **Mounting:** 4× M3 (Ø3.2), pattern rectangular, pitch 152.0×92.0 mm
  - holes (x,y mm): [[4.0, 4.0], [156.0, 4.0], [4.0, 96.0], [156.0, 96.0]]
  - notes: Klipper SBC+MCU combo board. Hole Ø annotated Ø3.2 (M3).
- **Clearance:** standoff 5 mm, top component  mm
- **Connectors:** SBC-style I/O cluster (USB / HDMI / Ethernet) along one long edge; verify connector-side clearance for cabling.
- **⚠ Verify:** Outline + hole Ø annotated in SIZE.pdf. Thickness not annotated.
- src: https://github.com/makerbase-mks/MKS-SKIPR/blob/main/hardware/MKS%20SKIPR%20V1.0_002/MKS%20SKIPR%20V1.0_002%20SIZE.pdf

### MKS THR42 V1.0  ·  `mks_thr42`

- **Category:** toolhead_can  ·  **Confidence:** high
- **PCB:** 42.0 × 42.0 mm, 1.6 mm thick
- **Mounting:** 4× M3 (Ø3.2), pattern rectangular, pitch 31.0×31.0 mm
  - holes (x,y mm): [[9.0, 8.94], [40.0, 8.94], [9.0, 39.94], [40.0, 39.94]]
  - notes: Square 31x31 mm = NEMA17 face bolt pattern; bolts directly onto a NEMA17 stepper. Hole Ø annotated 3.20 mm (M3). holes_xy derived from annotated 9.0 mm left inset + 8.94 mm bottom inset + 31 mm pitch -- a STEP file ships in the same repo folder for exact coordinates. (Sibling MKS THR36 is a round R=25 mm board with a different pattern.)
- **Clearance:** standoff 5 mm, top component  mm
- **⚠ Verify:** Outline, 31x31 pitch, hole Ø all annotated in SIZE.pdf. holes_xy positions derived from annotated insets; confirm against the repo STEP if exact XY matters. Thickness not annotated.
- src: https://github.com/makerbase-mks/MKS-THR36-THR42-UTC/blob/main/hardware/MKS%20THR42%20V1.0_001/PCB%20%20MKS%20THR42%20V1.0_001%20SIZE.pdf

## Mellow

### Fly Gemini V2/V3 (formerly Fly-CDY)  ·  `mellow_fly_gemini`

- **Category:** mainboard  ·  **Confidence:** low
- **PCB:**  ×  mm, 1.6 mm thick
- **Mounting:** 4× M3 (Ø3.2), pattern rectangular, pitch 143.0×78.0 mm
  - notes: NO official dimensioned drawing is published for any Gemini version. Values derived solely from parsing the Gemini V2 STEP and are UNVERIFIED. Outline roughly 143-150 x 78-82 mm; hole rectangle ~143 x 78 mm but the STEP also contains extra Ø3.2 holes that do not form a clean rectangle, so a trustworthy mounting rectangle could not be established.
- **Clearance:** standoff 6 mm, top component  mm
- **Connectors:** Dual-toolhead / SBC-style mainboard.
- **⚠ Verify:** ALL dimensions UNVERIFIED (no drawing; STEP holes ambiguous). Do not cut to these without measuring a physical board.
- src: https://github.com/Mellow-3D/Fly-Gemini-V2/blob/main/Hardware/gemini_v2.step
- src: https://mellow-3d.github.io/fly-gemini_v3_general.html

### Fly Super8  ·  `mellow_fly_super8`

- **Category:** mainboard  ·  **Confidence:** high
- **PCB:** 155.58 × 109.68 mm, 1.6 mm thick
- **Mounting:** 4× M3 (Ø3.2), pattern rectangular, pitch 149.38×103.45 mm
  - holes (x,y mm): [[3.1, 3.0], [152.48, 3.0], [3.1, 106.45], [152.48, 106.45]]
  - notes: 8-driver mainboard. Hole rectangle 149.38 x 103.45 mm. NOTE: a low-res docs thumbnail can misread the Y pitch as "100.45" -- the correct value is 103.45 mm (confirmed by STEP). holes_xy derived from outline/pitch centring.
- **Clearance:** standoff 6 mm, top component  mm
- **⚠ Verify:** Outline 155.58x109.68 and hole pitch 149.38x103.45 confirmed by drawing AND STEP (<0.1 mm). Thickness 1.6 mm nominal.
- src: https://github.com/Mellow-3D/mellow-3d.github.io/blob/gh-pages/images/fly-super8/fly-super8_dimensions.webp
- src: https://github.com/Mellow-3D/Fly-Super8/blob/main/Hardware/super8.step

### Fly-SHT36 (v1)  ·  `mellow_fly_sht36`

- **Category:** toolhead_can  ·  **Confidence:** high
- **PCB:** 51.27 × 36.26 mm, 1.6 mm thick
- **Mounting:** 2× M3 (Ø3.2), pattern linear, pitch 43.84×0.0 mm
  - notes: ONLY 2 mounting holes, collinear, spaced 43.84 mm (confirmed by both the dimension drawing and STEP). Mounts via two "ear" tabs on a printed bracket. Does NOT use the NEMA17 31 mm pattern (that assumption is false for the SHT36 -- only the SHT42 uses 31x31). Exact hole XY relative to the PCB corner not extracted; use the 43.84 mm spacing.
- **Clearance:** standoff 5 mm, top component  mm
- **⚠ Verify:** Outline + 43.84 mm spacing confirmed by drawing AND STEP. Thickness 1.6 mm nominal.
- src: https://mellow.klipper.cn/en/docs/ProductDoc/ToolBoard/fly-sht36/sht36/
- src: https://github.com/Mellow-3D/Klipper-CAN-Toolboards/blob/main/FLY-SHT36/STEP%20File/36.step

### Fly-SHT36 v2.0  ·  `mellow_fly_sht36_v2`

- **Category:** toolhead_can  ·  **Confidence:** high
- **PCB:** 51.27 × 45.67 mm, 1.6 mm thick
- **Mounting:** 2× M3 (Ø3.2), pattern linear, pitch 43.84×0.0 mm
  - notes: Same 2-hole 43.84 mm pattern as v1; board is taller (45.67 mm vs 36.26 mm) because connectors extend the outline on the connector side.
- **Clearance:** standoff 5 mm, top component  mm
- **⚠ Verify:** Outline + spacing from drawing and STEP. Thickness 1.6 mm nominal.
- src: https://github.com/Mellow-3D/mellow-3d.github.io/blob/gh-pages/images/fly-sht36_v2/sht36v2_dimensions.webp
- src: https://github.com/Mellow-3D/Klipper-CAN-Toolboards/blob/main/Fly-SHT36v2.0/Cad_SHT36v2.0.step

### Fly-SHT42  ·  `mellow_fly_sht42`

- **Category:** toolhead_can  ·  **Confidence:** high
- **PCB:** 42.0 × 42.0 mm, 1.6 mm thick
- **Mounting:** 4× M3 (Ø3.2), pattern rectangular, pitch 31.0×31.0 mm
  - notes: Square (chamfered corners). 31x31 mm = NEMA17 face bolt pattern -- bolts directly onto a NEMA17 stepper. Drawing labels 31.00 mm both directions; STEP confirms to 0.01 mm. Pattern centred -> ~5.5 mm inset each side.
- **Clearance:** standoff 5 mm, top component  mm
- **⚠ Verify:** 31x31 confirmed by drawing AND STEP. Thickness 1.6 mm nominal.
- src: https://github.com/Mellow-3D/mellow-3d.github.io/blob/gh-pages/images/fly-sht36-42/sht_42_size.png
- src: https://github.com/Mellow-3D/Klipper-CAN-Toolboards/blob/main/FLY-SHT42/STEP%20File/42CAN.step

### Fly-UTOC (UTOC-1 / UTOC-3)  ·  `mellow_fly_utoc`

- **Category:** usb_can_bridge  ·  **Confidence:** low
- **PCB:** 85.45 × 19.23 mm, 1.6 mm thick
- **Mounting:** 4× M2 (Ø), pattern rectangular, pitch 79.33× mm
  - notes: USB-CAN bridge. X hole pitch 79.33 mm is dimensioned (high confidence). Y pitch is NOT dimensioned on the official drawing (~13-14 mm estimated, LOW confidence). Hole Ø / screw size not stated; community mounts use M2 self-tapping screws, implying ~Ø2.2 holes -- treat hole Ø and Y pitch as UNVERIFIED. No STEP exists in the Mellow repos to confirm.
- **Clearance:** standoff 4 mm, top component  mm
- **Connectors:** USB one end, CAN the other (DIN-clip-style mount common).
- **⚠ Verify:** Outline + X pitch (79.33) are firm; hole Ø, screw size, and Y pitch are UNVERIFIED -- measure a physical board before cutting these.
- src: https://mellow-3d.github.io/fly-utoc_general.html
- src: https://github.com/Mellow-3D/mellow-3d.github.io/blob/gh-pages/images/fly-utoc/fly-utoc_dimensions.png
- src: https://wiki.kb-3d.com/home/mellow/voron/utoc-3

## Slice Engineering

### Slice Engineering PT1000/PT100 RTD amplifier (does not exist as a PCB)  ·  `slice_pt1000_amplifier`

- **Category:** thermocouple_amp  ·  **Confidence:** low
- **PCB:**  ×  mm,  mm thick
- **Mounting:** 0×  (Ø), pattern other, pitch × mm
  - notes: Slice Engineering does NOT make an amplifier PCB. They sell only the RTD probe and direct users to a MAX31865 amplifier (typically Adafruit's). For a "Slice PT1000 amplifier" entry, map to the Adafruit MAX31865 geometry above.
- **Connectors:** N/A - probe only.
- **⚠ Verify:** No Slice-branded amplifier PCB exists. Entry retained as a cross-reference only.
- src: https://www.sliceengineering.com/products/rtd-pt1000
