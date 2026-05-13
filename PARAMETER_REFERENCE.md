# BakedBean3D Master Parameters Reference

Complete catalog of all parameter categories in the Fusion 360 master parameter library. Use this as a reference when expanding the parameter set — check here before researching to avoid duplicating existing coverage.

**Total parameters:** 777 (as of 2026-05-13)
**Source of truth:** `BakedBean3D_MasterParams_v4/BakedBean3D_MasterParams_params.csv`
**Legacy XLSX:** `FDM_MasterParams_BakedBean3D_v4.xlsx` (historical only — CSV is canonical)

---

## Original FDM / Engineering Parameters (465 params)

These cover 3D printing tolerances, fasteners, mechanical joints, and component mounting. Source of truth is the XLSX workbook.

### Printer Accuracy — `printer_accuracy_` (9 params)
FDM calibration values: hole shrink compensation (0.15 mm), extrusion line width (0.45 mm), standard layer height (0.20 mm), first layer height, elephant foot compensation, Z-seam protrusion, minimum infill bridging width, solid top layers for mating surfaces.

### Tolerances — `tolerance_` (8 params)
ISO 2768 fine/medium/coarse classes, angular tolerance, FDM fit classes (sliding 0.15 mm/surface, press 0.05 mm, interference -0.05 mm), ISO H7/g6 running clearance reference.

### Hole Geometry — `hole_geometry_` (18 params)
Minimum printable diameter (2.0 mm), teardrop Z offset, FDM compensation, self-tap M3/M4 into plastic, thread engagement length, M2-M6 clearance and close-fit through-holes, boss ODs.

### Heat-Set Inserts — `heatset_insert_` (11 params)
M2-M5 recommended hole IDs, recess depths, boss ODs. Based on Ruthex insert dimensions. M3 follows Voron standard (4.5 mm OD, 4.4 mm hole).

### Counterbore — `counterbore_` (11 params)
Socket cap and button head counterbore diameters/depths for M2-M5 screws.

### Nut Traps — `nut_` (9 params)
Hex nut trap pocket dimensions (across-flats, depth) for M3-M5 nuts. Includes clearance for insertion.

### Hardware (Fasteners) — `hardware_` (54 params)
Comprehensive fastener dimensions for M2-M5: button head, socket cap, flat head screw dimensions (head dia, head height, drive size), nut dimensions, washer OD/ID/thickness, standoff diameters, dowel pins.

### Threaded Features — `thread_` (10 params)
ISO metric thread pitches (M2-M5), FDM thread tolerances, addon profile references, insert thread engagement depths.

### Motion Components — `motion_` (40 params)
3D printer motion system: NEMA 17 motor dimensions (42.3 mm sq, mounting holes), GT2 belt/pulley dimensions, MGN7/MGN9/MGN12 linear rail dimensions (width, height, hole spacing), hotend/toolhead measurements.

### Electronics — `electronics_` (28 params)
PCB/component mounting: Raspberry Pi 4 dimensions and hole spacing, BTT Octopus/SKR board dimensions, JST-XH/Molex connector sizes, DIN rail dimensions, USB-A/C panel cutout sizes, barrel jack dimensions.

### CNC Machining — `cnc_` (17 params)
Aluminum CNC tolerances, tap drill sizes for M3-M6 in aluminum, thread engagement depths for metal, thermal expansion coefficients, minimum wall thickness for machined parts.

### Magnets — `magnet_` (14 params)
Disc magnet dimensions and pocket sizes: 6x2, 6x3, 10x2, 10x3 mm magnets. Pocket IDs account for press-fit tolerance. Recess depths include adhesive allowance.

### Warhammer / Tabletop Gaming — `warhammer_` (14 params)
Miniature base sizes: 25 mm, 32 mm, 40 mm, 50 mm, 60 mm round bases, 25x50 mm cavalry. Magnetization pocket dimensions for each base size.

### Foam Dart Blasters — `foam_` (14 params)
Barrel bore diameters, flywheel gaps, spring guide rod sizes, plunger tube dimensions. Covers standard and half-length dart geometry.

### Wood Screws — `woodscrew_` (80 params)
Imperial wood screw gauges #00 through #20: major diameters, pilot hole sizes for softwood/hardwood, clearance through-hole sizes. Follows ASME/ANSI standards.

### Drill Bits — `drill_` (64 params)
Imperial fractional drill bits from 1/64" to 1" converted to mm equivalents. For reference when specifying hole sizes in metric designs using imperial drill sets.

### Print-in-Place — `print_in_place_` (4 params)
Captive sphere clearance (0.30 mm radial), minimum sphere diameter (8 mm), socket opening ratio (0.65), hinge pin clearance (0.25 mm).

### Twist Lock / Bayonet — `twist_lock_bayonet_` (8 params)
Twist-lock lid mechanism: tab count (3), rotation angle (40 deg), tab/channel dimensions, entry slot width, ramp detent angle, engagement depth, radial clearance.

### Dovetails — `dovetail_` (6 params)
FDM dovetail joints: 60 deg half-angle, base/top widths, depth, clearance per surface, entry chamfer.

### Spring Clips — `spring_clip_` (4 params)
PLA spring clip dimensions: arm thickness (1.6 mm), arm width (6 mm), max deflection (2 mm), hook depth (1.5 mm).

### Containers — `container_` (4 params)
Container design: food-safe wall thickness (2.5 mm), base thickness, corner radius minimum, lid rim width.

### Material Properties — `material_` (9 params)
Shrinkage percentages, chamber temps, thermal expansion, shore hardness for FDM materials.

---

## Everyday Item Reference Dimensions (312 params, added 2026-05-13)

These cover common everyday objects for designing holders, organizers, docks, mounts, and cases. Sources include manufacturer spec sheets, ISO standards, and US Mint specifications. Approximate values are flagged in comments.

### Phones — `phone_` (27 base + 6 derived = 33 params)
**Models covered:** iPhone 16, 16 Pro, 16 Pro Max | iPhone 15, 15 Pro, 15 Pro Max | Samsung Galaxy S24, S24+, S24 Ultra
**Dimensions per model:** height, width, depth (body only, no case)
**Derived:** `phone_universal_max_*` (envelope), `phone_case_allowance` (3 mm), `phone_universal_cased_*` (with case)
**Sources:** Apple 2024/2023 spec sheets, Samsung 2024 spec sheets (exact)

### Tablets — `tablet_` (12 base + 3 derived = 15 params)
**Models covered:** iPad Air 11" (M2), iPad Pro 11" (M4), iPad Pro 13" (M4), iPad Mini 7th gen
**Dimensions per model:** height, width, depth
**Derived:** `tablet_universal_max_*` (envelope across all models)
**Source:** Apple 2024 spec sheets (exact)

### Chargers — `charger_` (6 params)
**Items:** Apple MagSafe 15W puck (56 mm dia), MagSafe 25W puck (55.5 mm dia), Apple Watch charger puck (27.6 mm dia)
**Dimensions:** diameter, thickness
**Source:** Apple spec sheets (exact)

### Drinkware — `drinkware_` (11 base + 2 derived = 13 params)
**Items:** Standard coffee mug (approx 82 mm top dia), Yeti Rambler 20 oz (89 mm lip), Yeti Rambler 30 oz (102 mm lip), Stanley Quencher 40 oz (75 mm base), Hydro Flask 32 oz (91 mm body)
**Derived:** `drinkware_max_body_dia` (102 mm), `drinkware_max_height` (260 mm)
**Sources:** Yeti, Stanley, Hydro Flask spec pages (exact). Coffee mug is approximate/nominal.
**Not yet covered:** Tervis, Contigo, insulated wine tumblers, travel mugs with handles

### EDC (Everyday Carry) — `edc_` (12 base + 1 derived = 13 params)
**Items:** BIC Cristal pen (9 mm hex body, 149 mm length), Sharpie Fine Point (12 mm barrel, 140 mm), chapstick tube (16.5 mm dia, 67 mm), BIC Classic lighter (25x80x12.5 mm), Zippo Classic (38.1x57.2x12.7 mm)
**Derived:** `edc_bic_pen_circular_hole_dia` (10.4 mm, hex across-corners)
**Not yet covered:** Pilot G2, mechanical pencils, pocket knives (Victorinox, Leatherman), hand sanitizer bottles

### Cameras — `camera_` (6 params)
**Items:** GoPro Hero 12/13 Black body (71.8x50.8x33.6 mm), GoPro mount finger gap (3.1 mm), tab thickness (3.0 mm), M5 mount screw
**Sources:** GoPro spec sheet (exact)
**Not yet covered:** DJI Action cameras, Insta360, DSLR/mirrorless body dimensions, lens barrel diameters

### Paint Supplies — `paint_` (8 params)
**Items:** Citadel 12 ml pot (30 mm dia, 35 mm height), Vallejo 17 ml dropper (25 mm dia, 70 mm), Army Painter 12 ml dropper (26 mm dia, 70 mm), 2 oz craft bottle (37 mm dia, 75 mm approx)
**Sources:** Hobby community measurements (Citadel, Vallejo exact per rack standards). Craft bottle approximate.
**Not yet covered:** Tamiya paint jars, Scale75, AK Interactive bottles, Reaper dropper bottles

### Power Tool Batteries — `battery_tool_` (9 params)
**Items:** Milwaukee M18 CP2.0 (118.4x79.2x54.6 mm), Makita 18V LXT 5 Ah (113x75x62 mm), DeWalt 20V MAX 4 Ah (178x76x76 mm)
**Sources:** Milwaukee, Makita, DeWalt spec sheets (exact for Milwaukee/Makita, DeWalt approximate)
**Not yet covered:** Ryobi ONE+ 18V, Bosch 18V, Milwaukee M12, larger capacity variants (XC, HO), battery rail/slide interface dimensions

### Standard Batteries — `battery_` (8 base + 3 derived = 11 params)
**Items:** AA (14.5 mm dia, 50.5 mm), AAA (10.5 mm dia, 44.5 mm), CR2032 (20 mm dia, 3.2 mm), 18650 (18 mm dia, 65 mm)
**Derived:** `battery_aa/aaa/18650_holder_slot_dia` (adds 2x FDM sliding fit tolerance)
**Sources:** IEC 60086 standards (exact)
**Not yet covered:** C cell, D cell, 9V, CR2025, CR123A, 21700 (EV/flashlight cell), LiPo pouch cells

### Connectors & Media — `connector_` (10 params)
**Items:** USB-A plug (12.0x4.5 mm), USB-C plug (8.34x2.56 mm), SD card (24x32x2.1 mm), MicroSD (11x15x1.0 mm)
**Sources:** USB-IF Type-C R2.0 spec (exact), SD Association spec (exact)
**Note:** Complements existing `electronics_usb_a/c_panel_cutout_*` params which are for panel holes, not plug bodies.
**Not yet covered:** Mini-USB, Micro-USB, USB-B, CompactFlash

### Audio Accessories — `audio_` (3 params)
**Items:** AirPods Pro 2 charging case (60.6x45.2x21.7 mm)
**Source:** Apple spec sheet (exact)
**Not yet covered:** AirPods Max, Samsung Galaxy Buds, Pixel Buds, Sony WF/WH series, AirPods 4 case, earbuds charging cases generally

### Cards — `card_` (8 params)
**Items:** Credit/ID card (ISO 7810 ID-1: 85.60x53.98x0.76 mm, corner radius 3.18 mm), US business card (88.9x50.8 mm), poker playing card (63.5x88.9 mm)
**Sources:** ISO/IEC 7810 (exact), USPCC standard (exact)
**Not yet covered:** ID-2 (visa), ID-3 (passport page), bridge-size playing cards, tarot cards, trading cards (MTG/Pokemon: 63x88 mm standard)

### US Coins — `coin_us_` (12 params)
**Items:** Penny (19.05 mm dia), nickel (21.21 mm), dime (17.91 mm), quarter (24.26 mm), half dollar (30.61 mm), dollar coin (26.49 mm) — diameter and thickness each
**Source:** US Mint official specifications (exact)
**Not yet covered:** Euro coins, UK coins, Canadian coins, coin roll wrapper dimensions

### Cables & Plugs — `cable_` (10 params)
**Items:** USB-C cable OD (~3.5 mm), Lightning cable OD (~3.2 mm), HDMI Type A plug (13.9x4.55 mm), DisplayPort plug (16.1x4.76 mm), RJ45 plug (11.68x13.5 mm), 3.5 mm audio jack (3.5 mm dia, 14 mm barrel)
**Sources:** HDMI spec, VESA spec, TIA/EIA-568 (exact for plugs). Cable ODs are approximate/nominal.
**Not yet covered:** HDMI Mini/Micro, USB4/Thunderbolt cable OD, coaxial cable (RG6/RG59), speaker wire gauges, power cord (IEC C13/C14)

### Pegboard — `pegboard_` (7 params)
**Items:** Standard 1/4" hole (7.14 mm actual, 9/32"), 25.4 mm spacing, 6.35 mm board thickness, hook wire 4.72 mm (7 gauge). Small/hobby: 4.76 mm hole, 3.18 mm board, light hook wire 3.76 mm (9 gauge).
**Sources:** Industry standards (exact)
**Not yet covered:** French cleat dimensions, slatwall slot dimensions, Wall Control metal pegboard (different hole pattern)

### Power Tools — `tool_` (18 params)
**Items:** DeWalt DCD771 drill (219x53x191 mm), Milwaukee M18 FUEL drill (175x58x208 mm), DeWalt DCS391 circ saw (305x229x216 mm, 165 mm blade), Milwaukee M18 circ saw (330 mm, 184 mm blade), DeWalt DCW210 orbital sander (180x127x130 mm, 127 mm pad), Milwaukee M18 sander (267x125x146 mm)
**Sources:** DeWalt, Milwaukee spec sheets (exact for most, width approximate on some)
**Not yet covered:** Jigsaws, reciprocating saws, impact drivers, multi-tools, routers, planers, angle grinders, Ryobi/Bosch/Makita tool bodies

### Hand Tools — `handtool_` (21 params)
**Items:** Screwdriver handle (33 mm dia nominal), shaft (6 mm), hammer 16 oz (330 mm, 130 mm head width, 31 mm handle dia), adjustable wrenches 6"/8"/10" (length + jaw capacity), Stanley 25 ft tape measure (76x76x44 mm), Stanley 99E utility knife (152x44x19 mm), 9" torpedo level (229x41x17 mm)
**Sources:** Klein Tools, Crescent, Stanley spec sheets (exact for most). Handle diameters are nominal ranges.
**Not yet covered:** Socket sets/ratchets, Allen key holder dims, wire strippers, crimping tools, tin snips, clamps (bar, spring, C-clamp)

### Keys — `key_` (8 params)
**Items:** KW1 Kwikset blank (54 mm length, 22 mm bow, 2.1 mm thick), SC1 Schlage blank (54 mm, 22 mm bow, 2.3 mm thick), 25 mm split ring (25 mm OD, 1.5 mm wire)
**Sources:** Locksmith specifications (exact for thickness, approximate for bow dimensions)
**Not yet covered:** Medeco, Yale blanks, padlock keys, car key fob envelopes (too variable to standardize), carabiner clips, retractable badge reels

### Game Controllers — `controller_` (12 base + 3 derived = 15 params)
**Items:** Xbox Series X/S (153x102x61 mm), PS5 DualSense (160x106x66 mm), Nintendo Switch Pro (152x106x63 mm), Joy-Con single (35.9x102x13.9 mm)
**Derived:** `controller_universal_max_*` (DualSense envelope at 160x106x66 mm)
**Sources:** Microsoft, Sony, Nintendo spec sheets (exact)
**Not yet covered:** Xbox Elite, PS5 DualSense Edge, 8BitDo controllers, Steam Deck, Switch Lite

### Remotes — `remote_` (9 params)
**Items:** Apple TV Siri Remote 3rd gen (35.6x137.2x9.1 mm), Amazon Fire TV remote (38x148x18 mm), Roku Voice Remote Pro (41x145x20 mm)
**Sources:** Apple (exact). Amazon and Roku approximate — manufacturers don't publish official mm dimensions.
**Not yet covered:** Samsung TV remote, LG Magic Remote, universal remotes (Logitech Harmony), Nvidia Shield remote

### Watches — `watch_` (11 params)
**Items:** Apple Watch Series 10 42 mm (42x36x9.7 mm), Series 10 46 mm (46x39x9.7 mm), Apple Watch Ultra 2 (49x44x14.4 mm), standard band widths 20 mm and 22 mm
**Sources:** Apple spec sheets (exact). Band widths are industry standards.
**Not yet covered:** Samsung Galaxy Watch, Garmin watches, Fitbit, traditional watch case sizes (38-46 mm range), watch stand/dock dimensions

### Smart Home — `smarthome_` (12 params)
**Items:** Echo Dot 5th gen (100 mm dia, 89 mm height), Google Nest Mini 2nd gen (98 mm dia, 42 mm), Echo Show 5 (147x82x91 mm), TP-Link Kasa EP10 smart plug (60x51.5x38 mm), Philips Hue Bridge (88x88x26 mm)
**Sources:** Amazon, Google, TP-Link, Philips spec pages (exact)
**Not yet covered:** Echo Show 8/10/15, Google Nest Hub, HomePod Mini, smart switches (Lutron Caseta), smart thermostats (Nest, Ecobee), smart locks

### Security Cameras — `camera_security_` (17 params)
**Items:** Ring Indoor Cam 2nd gen (49 mm cube), Ring Stick Up Cam (60 mm dia, 97 mm height), Ring Video Doorbell (61.7x126.5x22.1 mm), UniFi G4 Bullet (75 mm dia, 140 mm length), G4 Instant (81.6x50x47.2 mm), G5 Flex (48 mm dia, 107.5 mm height), 1/4"-20 tripod mount (6.35 mm dia, 1.27 mm pitch)
**Sources:** Ring, Ubiquiti datasheets (exact). Tripod mount is ANSI/ASME standard.
**Not yet covered:** Wyze Cam, Blink, Arlo, Reolink, UniFi G4/G5 Pro, PoE injector dimensions, NVR/DVR enclosures, Ring Floodlight mount plate pattern (needs physical verification)

### Bottles — `bottle_` (12 params)
**Items:** Pill bottles 13/20/30 dram (33-46 mm dia, 54-69 mm height), Nalgene 32 oz wide mouth (90 mm dia, 214 mm, 63 mm mouth), eye drop 15 ml (29 mm dia approx, 77 mm), 28/400 spray neck (28 mm OD)
**Sources:** Pharmaceutical industry standards (pill bottles exact per dram size), Nalgene spec (exact), eye drops approximate.
**Not yet covered:** 40/60 dram pill bottles, vitamin bottles, Nalgene narrow mouth, CamelBak, essential oil bottles (5/10/15/30 ml), mason jars (regular/wide mouth), spray bottle trigger body

### Storage Media — `media_` (19 params)
**Items:** Samsung T7 SSD (57.3x85x8 mm), WD My Passport (75x107x11.15 mm), 2.5" SATA (69.85x100.45x7/9.5 mm), 3.5" SATA (101.6x147x25.4 mm), M.2 2280 (22x80x2.23 mm), CFexpress Type B (29.6x38.36x3.8 mm)
**Sources:** Samsung, WD datasheets (exact), SFF-8201/8301 standards (exact), PCI-SIG M.2 spec (exact), CFA CFexpress spec (exact)
**Not yet covered:** Samsung T9, NVMe external enclosures, USB flash drive form factors (too variable), CompactFlash, M.2 2230/2242 variants, 3.5" floppy (retro)

### Glasses / Eyewear — `glasses_` (6 params)
**Items:** Sunglasses hard case (70x42x165 mm nominal), folded eyeglasses envelope (140x48x48 mm nominal)
**All approximate** — these vary enormously by frame style. Comments flag as nominal.
**Not yet covered:** Specific frame brands, contact lens case, lens cloth case

---

## Adding New Parameters

### Format
```
Name,Expression,Unit,Comment
```
- **Name:** lowercase_snake_case, category prefix, regex `^[a-z][a-z0-9_]*$`
- **Expression:** literal value with unit (`147.6 mm`) or formula (`2 * some_param`)
- **Unit:** `mm`, `cm`, `in`, `deg`, `rad`, or empty for dimensionless
- **Comment:** What it is, source/year, confidence flag, design hint

### Confidence flags in comments
- **Exact:** "Apple 2024 spec" / "ISO 7810" / "US Mint specification" / "SFF-8201 standard"
- **Approximate:** "Nominal — verify with calipers for tight-fit designs"

### Workflow
1. Research dimensions from manufacturer spec sheets (prefer official sources)
2. Add rows to `BakedBean3D_MasterParams_params.csv` (source of truth — XLSX is legacy/historical)
3. Validate with `validate_params.py` (name format, duplicates, unit validity, reference resolution)
4. Update this reference file with new category documentation
5. Commit to the `fusion_params` submodule
