#!/usr/bin/env python3
"""Generate everyday item reference parameters and append to the master CSV.

Validates naming, units, duplicates, and derived param references before writing.
"""

import csv
import re
import sys
from pathlib import Path

PARAM_NAME_RE = re.compile(r"^[a-z][a-z0-9_]*$")
CSV_PATH = Path("BakedBean3D_MasterParams_v4/BakedBean3D_MasterParams_params.csv")

# fmt: off
NEW_PARAMS = [
    # ── Phones ──────────────────────────────────────────────────────────────
    ("phone_iphone_16_height", "147.6 mm", "mm", "iPhone 16 body height. Apple 2024 spec."),
    ("phone_iphone_16_width", "71.6 mm", "mm", "iPhone 16 body width. Apple 2024 spec."),
    ("phone_iphone_16_depth", "7.80 mm", "mm", "iPhone 16 body depth/thickness. Apple 2024 spec."),
    ("phone_iphone_16_pro_height", "149.6 mm", "mm", "iPhone 16 Pro body height. Apple 2024 spec."),
    ("phone_iphone_16_pro_width", "71.5 mm", "mm", "iPhone 16 Pro body width. Apple 2024 spec."),
    ("phone_iphone_16_pro_depth", "8.25 mm", "mm", "iPhone 16 Pro body depth. Apple 2024 spec."),
    ("phone_iphone_16_pro_max_height", "163.0 mm", "mm", "iPhone 16 Pro Max body height. Apple 2024 spec."),
    ("phone_iphone_16_pro_max_width", "77.6 mm", "mm", "iPhone 16 Pro Max body width. Apple 2024 spec."),
    ("phone_iphone_16_pro_max_depth", "8.25 mm", "mm", "iPhone 16 Pro Max body depth. Apple 2024 spec."),
    ("phone_iphone_15_height", "147.6 mm", "mm", "iPhone 15 body height. Apple 2023 spec."),
    ("phone_iphone_15_width", "71.6 mm", "mm", "iPhone 15 body width. Apple 2023 spec."),
    ("phone_iphone_15_depth", "7.80 mm", "mm", "iPhone 15 body depth. Apple 2023 spec."),
    ("phone_iphone_15_pro_height", "146.6 mm", "mm", "iPhone 15 Pro body height. Apple 2023 spec."),
    ("phone_iphone_15_pro_width", "70.6 mm", "mm", "iPhone 15 Pro body width. Apple 2023 spec."),
    ("phone_iphone_15_pro_depth", "8.25 mm", "mm", "iPhone 15 Pro body depth. Apple 2023 spec."),
    ("phone_iphone_15_pro_max_height", "159.9 mm", "mm", "iPhone 15 Pro Max body height. Apple 2023 spec."),
    ("phone_iphone_15_pro_max_width", "76.7 mm", "mm", "iPhone 15 Pro Max body width. Apple 2023 spec."),
    ("phone_iphone_15_pro_max_depth", "8.25 mm", "mm", "iPhone 15 Pro Max body depth. Apple 2023 spec."),
    ("phone_galaxy_s24_height", "147.0 mm", "mm", "Samsung Galaxy S24 body height. Samsung 2024 spec."),
    ("phone_galaxy_s24_width", "70.6 mm", "mm", "Samsung Galaxy S24 body width. Samsung 2024 spec."),
    ("phone_galaxy_s24_depth", "7.60 mm", "mm", "Samsung Galaxy S24 body depth. Samsung 2024 spec."),
    ("phone_galaxy_s24_plus_height", "158.5 mm", "mm", "Samsung Galaxy S24+ body height. Samsung 2024 spec."),
    ("phone_galaxy_s24_plus_width", "75.9 mm", "mm", "Samsung Galaxy S24+ body width. Samsung 2024 spec."),
    ("phone_galaxy_s24_plus_depth", "7.70 mm", "mm", "Samsung Galaxy S24+ body depth. Samsung 2024 spec."),
    ("phone_galaxy_s24_ultra_height", "162.3 mm", "mm", "Samsung Galaxy S24 Ultra body height. Samsung 2024 spec."),
    ("phone_galaxy_s24_ultra_width", "79.0 mm", "mm", "Samsung Galaxy S24 Ultra body width. Samsung 2024 spec."),
    ("phone_galaxy_s24_ultra_depth", "8.60 mm", "mm", "Samsung Galaxy S24 Ultra body depth. Samsung 2024 spec."),

    # ── Tablets ──────────────────────────────────────────────────────────────
    ("tablet_ipad_air_11_height", "247.6 mm", "mm", "iPad Air 11-inch (M2) body height. Apple 2024 spec."),
    ("tablet_ipad_air_11_width", "178.5 mm", "mm", "iPad Air 11-inch (M2) body width. Apple 2024 spec."),
    ("tablet_ipad_air_11_depth", "6.1 mm", "mm", "iPad Air 11-inch (M2) body depth. Apple 2024 spec."),
    ("tablet_ipad_pro_11_height", "249.7 mm", "mm", "iPad Pro 11-inch (M4) body height. Apple 2024 spec."),
    ("tablet_ipad_pro_11_width", "177.5 mm", "mm", "iPad Pro 11-inch (M4) body width. Apple 2024 spec."),
    ("tablet_ipad_pro_11_depth", "5.3 mm", "mm", "iPad Pro 11-inch (M4) body depth. Apple 2024 spec."),
    ("tablet_ipad_pro_13_height", "281.6 mm", "mm", "iPad Pro 13-inch (M4) body height. Apple 2024 spec."),
    ("tablet_ipad_pro_13_width", "215.5 mm", "mm", "iPad Pro 13-inch (M4) body width. Apple 2024 spec."),
    ("tablet_ipad_pro_13_depth", "5.1 mm", "mm", "iPad Pro 13-inch (M4) body depth. Apple 2024 spec."),
    ("tablet_ipad_mini_7_height", "195.4 mm", "mm", "iPad Mini 7th gen body height. Apple 2024 spec."),
    ("tablet_ipad_mini_7_width", "134.8 mm", "mm", "iPad Mini 7th gen body width. Apple 2024 spec."),
    ("tablet_ipad_mini_7_depth", "6.3 mm", "mm", "iPad Mini 7th gen body depth — thickest current iPad. Apple 2024 spec."),

    # ── Chargers ─────────────────────────────────────────────────────────────
    ("charger_magsafe_15w_dia", "56.0 mm", "mm", "Apple MagSafe 15W charger puck diameter. Apple spec."),
    ("charger_magsafe_15w_thick", "6.0 mm", "mm", "Apple MagSafe 15W charger puck thickness. Apple spec."),
    ("charger_magsafe_25w_dia", "55.5 mm", "mm", "Apple MagSafe 25W charger puck diameter. Apple spec."),
    ("charger_magsafe_25w_thick", "4.5 mm", "mm", "Apple MagSafe 25W charger puck thickness. Apple spec."),
    ("charger_apple_watch_dia", "27.6 mm", "mm", "Apple Watch magnetic charger puck diameter. Apple spec."),
    ("charger_apple_watch_thick", "6.0 mm", "mm", "Apple Watch magnetic charger puck thickness. Apple spec."),

    # ── Drinkware ────────────────────────────────────────────────────────────
    ("drinkware_coffee_mug_std_top_dia", "82.0 mm", "mm", "Standard 8-12 oz coffee mug top/rim diameter. Nominal — verify with calipers. Range 80-89 mm."),
    ("drinkware_coffee_mug_std_base_dia", "70.0 mm", "mm", "Standard coffee mug base diameter. Nominal — verify with calipers. Range 65-75 mm."),
    ("drinkware_coffee_mug_std_height", "95.0 mm", "mm", "Standard coffee mug height. Nominal — verify with calipers. Range 90-100 mm."),
    ("drinkware_yeti_rambler_20oz_lip_dia", "89.0 mm", "mm", "Yeti Rambler 20 oz tumbler lip/rim diameter. Yeti spec."),
    ("drinkware_yeti_rambler_20oz_height", "175.0 mm", "mm", "Yeti Rambler 20 oz tumbler height. Yeti spec."),
    ("drinkware_yeti_rambler_30oz_lip_dia", "102.0 mm", "mm", "Yeti Rambler 30 oz tumbler lip/rim diameter. Yeti spec."),
    ("drinkware_yeti_rambler_30oz_height", "194.0 mm", "mm", "Yeti Rambler 30 oz tumbler height. Yeti spec."),
    ("drinkware_stanley_quencher_40oz_base_dia", "75.0 mm", "mm", "Stanley Quencher H2.0 40 oz base diameter. Stanley spec."),
    ("drinkware_stanley_quencher_40oz_height", "260.0 mm", "mm", "Stanley Quencher H2.0 40 oz height without straw. Stanley spec."),
    ("drinkware_hydro_flask_32oz_body_dia", "91.0 mm", "mm", "Hydro Flask 32 oz wide mouth body diameter. Hydro Flask spec."),
    ("drinkware_hydro_flask_32oz_height", "239.0 mm", "mm", "Hydro Flask 32 oz wide mouth height with cap. Hydro Flask spec."),

    # ── EDC (Everyday Carry) ─────────────────────────────────────────────────
    ("edc_bic_pen_body_width", "9.0 mm", "mm", "BIC Cristal pen hex body across-flats width. For round holder hole use edc_bic_pen_circular_hole_dia."),
    ("edc_bic_pen_length", "149.0 mm", "mm", "BIC Cristal pen overall length with cap."),
    ("edc_sharpie_barrel_dia", "12.0 mm", "mm", "Sharpie Fine Point marker barrel diameter. Approximate — cap is slightly wider at ~14 mm."),
    ("edc_sharpie_length", "140.0 mm", "mm", "Sharpie Fine Point marker length with cap."),
    ("edc_chapstick_dia", "16.5 mm", "mm", "Standard chapstick/lip balm tube diameter."),
    ("edc_chapstick_height", "67.0 mm", "mm", "Standard chapstick/lip balm tube height."),
    ("edc_bic_lighter_width", "25.0 mm", "mm", "BIC Classic lighter body width (wide face)."),
    ("edc_bic_lighter_height", "80.0 mm", "mm", "BIC Classic lighter body height."),
    ("edc_bic_lighter_depth", "12.5 mm", "mm", "BIC Classic lighter body depth (thin face)."),
    ("edc_zippo_width", "38.1 mm", "mm", "Zippo Classic lighter width. Zippo spec."),
    ("edc_zippo_height", "57.2 mm", "mm", "Zippo Classic lighter height. Zippo spec."),
    ("edc_zippo_depth", "12.7 mm", "mm", "Zippo Classic lighter depth. Zippo spec."),

    # ── Cameras ──────────────────────────────────────────────────────────────
    ("camera_gopro_hero_12_width", "71.8 mm", "mm", "GoPro Hero 12/13 Black body width. GoPro spec."),
    ("camera_gopro_hero_12_height", "50.8 mm", "mm", "GoPro Hero 12/13 Black body height. GoPro spec."),
    ("camera_gopro_hero_12_depth", "33.6 mm", "mm", "GoPro Hero 12/13 Black body depth. GoPro spec."),
    ("camera_gopro_mount_finger_gap", "3.1 mm", "mm", "GoPro mounting finger gap between tabs. Standard across all GoPro mounts."),
    ("camera_gopro_mount_tab_thick", "3.0 mm", "mm", "GoPro mounting finger tab thickness."),
    ("camera_gopro_mount_screw_dia", "5.0 mm", "mm", "GoPro mounting screw diameter (M5 thumbscrew)."),

    # ── Paint Supplies ───────────────────────────────────────────────────────
    ("paint_citadel_pot_dia", "30.0 mm", "mm", "Games Workshop Citadel 12 ml paint pot diameter. Many 3D-printed holders use 32 mm holes for clearance."),
    ("paint_citadel_pot_height", "35.0 mm", "mm", "Citadel 12 ml paint pot height with lid."),
    ("paint_vallejo_dropper_dia", "25.0 mm", "mm", "Vallejo 17 ml dropper bottle diameter. Standard 26 mm rack hole accommodates this."),
    ("paint_vallejo_dropper_height", "70.0 mm", "mm", "Vallejo 17 ml dropper bottle height without cap."),
    ("paint_army_painter_dropper_dia", "26.0 mm", "mm", "Army Painter 12 ml dropper bottle diameter. Uses same 26 mm rack standard as Vallejo."),
    ("paint_army_painter_dropper_height", "70.0 mm", "mm", "Army Painter 12 ml dropper bottle height."),
    ("paint_craft_bottle_2oz_dia", "37.0 mm", "mm", "Standard 2 oz acrylic craft paint bottle diameter (FolkArt/Apple Barrel/DecoArt). Nominal — verify with calipers."),
    ("paint_craft_bottle_2oz_height", "75.0 mm", "mm", "Standard 2 oz craft paint bottle height. Nominal — verify with calipers."),

    # ── Tool Batteries ───────────────────────────────────────────────────────
    ("battery_tool_milwaukee_m18_cp2_length", "118.4 mm", "mm", "Milwaukee M18 CP2.0 compact battery length. Milwaukee spec."),
    ("battery_tool_milwaukee_m18_cp2_width", "79.2 mm", "mm", "Milwaukee M18 CP2.0 compact battery width. Milwaukee spec."),
    ("battery_tool_milwaukee_m18_cp2_height", "54.6 mm", "mm", "Milwaukee M18 CP2.0 compact battery height. Milwaukee spec."),
    ("battery_tool_makita_18v_lxt_5ah_length", "113.0 mm", "mm", "Makita 18V LXT BL1850B 5.0 Ah battery length. Makita spec."),
    ("battery_tool_makita_18v_lxt_5ah_width", "75.0 mm", "mm", "Makita 18V LXT BL1850B 5.0 Ah battery width. Makita spec."),
    ("battery_tool_makita_18v_lxt_5ah_height", "62.0 mm", "mm", "Makita 18V LXT BL1850B 5.0 Ah battery height. Makita spec."),
    ("battery_tool_dewalt_20v_max_4ah_length", "178.0 mm", "mm", "DeWalt 20V MAX DCB204 4.0 Ah battery length. DeWalt spec."),
    ("battery_tool_dewalt_20v_max_4ah_width", "76.0 mm", "mm", "DeWalt 20V MAX DCB204 4.0 Ah battery width. DeWalt spec."),
    ("battery_tool_dewalt_20v_max_4ah_height", "76.0 mm", "mm", "DeWalt 20V MAX DCB204 4.0 Ah battery height. DeWalt spec."),

    # ── Standard Batteries ───────────────────────────────────────────────────
    ("battery_aa_dia", "14.5 mm", "mm", "AA cell diameter. IEC 60086 LR6 specification."),
    ("battery_aa_length", "50.5 mm", "mm", "AA cell length. IEC 60086 LR6 specification."),
    ("battery_aaa_dia", "10.5 mm", "mm", "AAA cell diameter. IEC 60086 LR03 specification."),
    ("battery_aaa_length", "44.5 mm", "mm", "AAA cell length. IEC 60086 LR03 specification."),
    ("battery_cr2032_dia", "20.0 mm", "mm", "CR2032 coin cell diameter. IEC standard."),
    ("battery_cr2032_thick", "3.2 mm", "mm", "CR2032 coin cell thickness. IEC standard."),
    ("battery_18650_dia", "18.0 mm", "mm", "18650 lithium cell diameter. Name encodes dimensions: 18 mm dia x 65 mm length."),
    ("battery_18650_length", "65.0 mm", "mm", "18650 lithium cell length. Protected cells may be 67-69 mm with circuit board."),

    # ── Connectors / Media ───────────────────────────────────────────────────
    ("connector_usb_a_plug_width", "12.0 mm", "mm", "USB Type-A plug body width. USB-IF spec. See also electronics_usb_a_panel_cutout_width (14.0 mm) for panel holes."),
    ("connector_usb_a_plug_height", "4.5 mm", "mm", "USB Type-A plug body height. USB-IF spec."),
    ("connector_usb_c_plug_width", "8.34 mm", "mm", "USB Type-C plug body width. USB-IF Type-C R2.0 spec. See also electronics_usb_c_panel_cutout_width (10.0 mm)."),
    ("connector_usb_c_plug_height", "2.56 mm", "mm", "USB Type-C plug body height. USB-IF Type-C R2.0 spec."),
    ("connector_sd_card_width", "24.0 mm", "mm", "Full-size SD card width. SD Association specification."),
    ("connector_sd_card_length", "32.0 mm", "mm", "Full-size SD card length. SD Association specification."),
    ("connector_sd_card_thick", "2.1 mm", "mm", "Full-size SD card thickness. SD Association specification."),
    ("connector_microsd_width", "11.0 mm", "mm", "MicroSD card width. SD Association specification."),
    ("connector_microsd_length", "15.0 mm", "mm", "MicroSD card length. SD Association specification."),
    ("connector_microsd_thick", "1.0 mm", "mm", "MicroSD card thickness. SD Association specification."),

    # ── Audio Accessories ────────────────────────────────────────────────────
    ("audio_airpods_pro_2_case_width", "60.6 mm", "mm", "AirPods Pro 2 charging case width. Apple spec."),
    ("audio_airpods_pro_2_case_height", "45.2 mm", "mm", "AirPods Pro 2 charging case height. Apple spec."),
    ("audio_airpods_pro_2_case_depth", "21.7 mm", "mm", "AirPods Pro 2 charging case depth. Apple spec."),

    # ── Cards ────────────────────────────────────────────────────────────────
    ("card_credit_width", "85.60 mm", "mm", "Standard credit/debit/ID card width. ISO/IEC 7810 ID-1 exact."),
    ("card_credit_height", "53.98 mm", "mm", "Standard credit/debit/ID card height. ISO/IEC 7810 ID-1 exact."),
    ("card_credit_thick", "0.76 mm", "mm", "Standard credit card thickness. ISO/IEC 7810 ID-1 (tolerance 0.68-0.84 mm)."),
    ("card_credit_corner_radius", "3.18 mm", "mm", "Standard credit card corner radius. ISO/IEC 7810 (tolerance 2.88-3.48 mm)."),
    ("card_business_width", "88.9 mm", "mm", "US standard business card width (3.5 inches)."),
    ("card_business_height", "50.8 mm", "mm", "US standard business card height (2 inches)."),
    ("card_playing_poker_width", "63.5 mm", "mm", "Standard poker-size playing card width (2.5 inches). USPCC standard."),
    ("card_playing_poker_height", "88.9 mm", "mm", "Standard poker-size playing card height (3.5 inches). USPCC standard."),

    # ── US Coins ─────────────────────────────────────────────────────────────
    ("coin_us_penny_dia", "19.05 mm", "mm", "US penny diameter. US Mint specification exact."),
    ("coin_us_penny_thick", "1.52 mm", "mm", "US penny thickness. US Mint specification exact."),
    ("coin_us_nickel_dia", "21.21 mm", "mm", "US nickel diameter. US Mint specification exact."),
    ("coin_us_nickel_thick", "1.95 mm", "mm", "US nickel thickness. US Mint specification exact."),
    ("coin_us_dime_dia", "17.91 mm", "mm", "US dime diameter. US Mint specification exact."),
    ("coin_us_dime_thick", "1.35 mm", "mm", "US dime thickness. US Mint specification exact."),
    ("coin_us_quarter_dia", "24.26 mm", "mm", "US quarter diameter. US Mint specification exact."),
    ("coin_us_quarter_thick", "1.75 mm", "mm", "US quarter thickness. US Mint specification exact."),
    ("coin_us_half_dollar_dia", "30.61 mm", "mm", "US half dollar diameter. US Mint specification exact."),
    ("coin_us_half_dollar_thick", "2.15 mm", "mm", "US half dollar thickness. US Mint specification exact."),
    ("coin_us_dollar_dia", "26.49 mm", "mm", "US dollar coin (Sacagawea/Presidential) diameter. US Mint specification exact."),
    ("coin_us_dollar_thick", "2.00 mm", "mm", "US dollar coin thickness. US Mint specification exact."),

    # ── Cables / Plugs ───────────────────────────────────────────────────────
    ("cable_usb_c_cable_od", "3.5 mm", "mm", "USB-C cable outer diameter typical. Nominal — braided cables may be 4.5-5.0 mm."),
    ("cable_lightning_cable_od", "3.2 mm", "mm", "Lightning cable outer diameter typical (Apple original). Third-party may be 3.5-4.5 mm."),
    ("cable_hdmi_plug_width", "13.9 mm", "mm", "HDMI Type A plug width. HDMI specification exact."),
    ("cable_hdmi_plug_height", "4.55 mm", "mm", "HDMI Type A plug height. HDMI specification exact."),
    ("cable_displayport_plug_width", "16.10 mm", "mm", "DisplayPort full-size plug width including latch. VESA spec."),
    ("cable_displayport_plug_height", "4.76 mm", "mm", "DisplayPort full-size plug height. VESA spec."),
    ("cable_rj45_plug_width", "11.68 mm", "mm", "RJ45 Ethernet plug width. TIA/EIA-568 standard exact."),
    ("cable_rj45_plug_height", "13.5 mm", "mm", "RJ45 Ethernet plug height including latch. Without latch ~10.2 mm."),
    ("cable_audio_35mm_plug_dia", "3.5 mm", "mm", "3.5 mm audio jack plug diameter. IEC 60603-11 exact."),
    ("cable_audio_35mm_barrel_length", "14.0 mm", "mm", "3.5 mm audio jack barrel length (TRS/TRRS typical). Varies by manufacturer."),

    # ── Pegboard ─────────────────────────────────────────────────────────────
    ("pegboard_std_hole_dia", "7.14 mm", "mm", "Standard 1/4-inch pegboard hole diameter (actual 9/32 inch). Industry standard."),
    ("pegboard_std_hole_spacing", "25.4 mm", "mm", "Standard pegboard hole center-to-center spacing (1 inch). Industry standard."),
    ("pegboard_std_thickness", "6.35 mm", "mm", "Standard pegboard board thickness (1/4 inch)."),
    ("pegboard_std_hook_wire_dia", "4.72 mm", "mm", "Standard pegboard hook wire diameter (3/16 inch / 7 gauge)."),
    ("pegboard_small_hole_dia", "4.76 mm", "mm", "Small/hobby pegboard hole diameter (3/16 inch / 1/8-inch nominal)."),
    ("pegboard_small_thickness", "3.18 mm", "mm", "Small/hobby pegboard board thickness (1/8 inch)."),
    ("pegboard_light_hook_wire_dia", "3.76 mm", "mm", "Light-duty pegboard hook wire diameter (9 gauge / 0.148 inch)."),

    # ── Power Tools ──────────────────────────────────────────────────────────
    ("tool_dewalt_dcd771_drill_length", "219.0 mm", "mm", "DeWalt DCD771 20V drill length front-to-back. DeWalt spec. Tool only without battery."),
    ("tool_dewalt_dcd771_drill_width", "53.0 mm", "mm", "DeWalt DCD771 20V drill body width. DeWalt spec."),
    ("tool_dewalt_dcd771_drill_height", "191.0 mm", "mm", "DeWalt DCD771 20V drill height handle-to-top. DeWalt spec. Tool only."),
    ("tool_milwaukee_m18_drill_length", "175.0 mm", "mm", "Milwaukee M18 FUEL 2904-20 hammer drill length. Milwaukee spec. Tool only."),
    ("tool_milwaukee_m18_drill_width", "58.0 mm", "mm", "Milwaukee M18 FUEL drill body width. Milwaukee spec."),
    ("tool_milwaukee_m18_drill_height", "208.0 mm", "mm", "Milwaukee M18 FUEL drill height. Milwaukee spec. Tool only."),
    ("tool_dewalt_dcs391_saw_length", "305.0 mm", "mm", "DeWalt DCS391 6.5-inch circular saw length. DeWalt spec."),
    ("tool_dewalt_dcs391_saw_width", "229.0 mm", "mm", "DeWalt DCS391 circular saw base plate width. DeWalt spec."),
    ("tool_dewalt_dcs391_saw_height", "216.0 mm", "mm", "DeWalt DCS391 circular saw height. DeWalt spec."),
    ("tool_dewalt_dcs391_blade_dia", "165.0 mm", "mm", "DeWalt DCS391 circular saw blade diameter (6.5 inch)."),
    ("tool_milwaukee_m18_saw_length", "330.0 mm", "mm", "Milwaukee M18 FUEL 2732-20 7.25-inch circular saw length. Milwaukee spec."),
    ("tool_milwaukee_m18_saw_blade_dia", "184.0 mm", "mm", "Milwaukee M18 FUEL circular saw blade diameter (7.25 inch)."),
    ("tool_dewalt_dcw210_sander_pad_dia", "127.0 mm", "mm", "DeWalt DCW210 orbital sander pad diameter (5 inch). DeWalt spec."),
    ("tool_dewalt_dcw210_sander_length", "180.0 mm", "mm", "DeWalt DCW210 orbital sander body length. DeWalt spec."),
    ("tool_dewalt_dcw210_sander_height", "130.0 mm", "mm", "DeWalt DCW210 orbital sander grip-to-pad height. DeWalt spec."),
    ("tool_milwaukee_m18_sander_pad_dia", "127.0 mm", "mm", "Milwaukee M18 2648-20 orbital sander pad diameter (5 inch)."),
    ("tool_milwaukee_m18_sander_length", "267.0 mm", "mm", "Milwaukee M18 orbital sander body length. Milwaukee spec."),
    ("tool_milwaukee_m18_sander_height", "146.0 mm", "mm", "Milwaukee M18 orbital sander height. Milwaukee spec."),

    # ── Hand Tools ───────────────────────────────────────────────────────────
    ("handtool_screwdriver_handle_dia", "33.0 mm", "mm", "Phillips #2 screwdriver handle diameter typical. Nominal — varies 30-36 mm by brand. Use 38 mm holder hole."),
    ("handtool_screwdriver_shaft_dia", "6.0 mm", "mm", "Standard screwdriver shaft diameter (1/4 inch)."),
    ("handtool_screwdriver_overall_length", "210.0 mm", "mm", "Phillips #2 screwdriver overall length typical (4-inch shaft). Nominal — range 200-220 mm."),
    ("handtool_hammer_16oz_length", "330.0 mm", "mm", "Standard 16 oz claw hammer overall length (13 inch)."),
    ("handtool_hammer_16oz_head_width", "130.0 mm", "mm", "16 oz claw hammer head width (face to claw tip). Klein spec."),
    ("handtool_hammer_16oz_handle_dia", "31.0 mm", "mm", "16 oz hammer handle grip diameter (oval minor axis). Nominal — range 28-35 mm."),
    ("handtool_wrench_adj_6in_length", "152.0 mm", "mm", "6-inch adjustable wrench overall length. Crescent spec."),
    ("handtool_wrench_adj_6in_jaw_width", "24.0 mm", "mm", "6-inch adjustable wrench max jaw capacity (15/16 inch). Crescent spec."),
    ("handtool_wrench_adj_8in_length", "203.0 mm", "mm", "8-inch adjustable wrench overall length. Crescent spec."),
    ("handtool_wrench_adj_8in_jaw_width", "29.0 mm", "mm", "8-inch adjustable wrench max jaw capacity (1-1/8 inch). Crescent spec."),
    ("handtool_wrench_adj_10in_length", "254.0 mm", "mm", "10-inch adjustable wrench overall length. Crescent spec."),
    ("handtool_wrench_adj_10in_jaw_width", "34.0 mm", "mm", "10-inch adjustable wrench max jaw capacity (1-5/16 inch). Crescent spec."),
    ("handtool_tape_measure_25ft_width", "76.0 mm", "mm", "Stanley 25 ft PowerLock tape measure case width. Stanley spec."),
    ("handtool_tape_measure_25ft_height", "76.0 mm", "mm", "Stanley 25 ft tape measure case height. Stanley spec."),
    ("handtool_tape_measure_25ft_depth", "44.0 mm", "mm", "Stanley 25 ft tape measure case depth. Stanley spec."),
    ("handtool_utility_knife_length", "152.0 mm", "mm", "Stanley 99E retractable utility knife body length. Stanley spec."),
    ("handtool_utility_knife_width", "44.0 mm", "mm", "Stanley 99E utility knife body width/height profile. Approximate."),
    ("handtool_utility_knife_depth", "19.0 mm", "mm", "Stanley 99E utility knife body thickness. Approximate."),
    ("handtool_torpedo_level_length", "229.0 mm", "mm", "9-inch torpedo level length. Klein spec."),
    ("handtool_torpedo_level_width", "41.0 mm", "mm", "9-inch torpedo level body width. Klein spec."),
    ("handtool_torpedo_level_height", "17.0 mm", "mm", "9-inch torpedo level body height/profile. Klein spec."),

    # ── Keys ─────────────────────────────────────────────────────────────────
    ("key_kw1_length", "54.0 mm", "mm", "KW1 (Kwikset) house key blank overall length bow to tip. Locksmith spec."),
    ("key_kw1_bow_width", "22.0 mm", "mm", "KW1 key blank bow (head) width. Standard round head."),
    ("key_kw1_blade_thick", "2.1 mm", "mm", "KW1 key blank blade thickness. Locksmith spec exact."),
    ("key_sc1_length", "54.0 mm", "mm", "SC1 (Schlage) house key blank overall length. Locksmith spec."),
    ("key_sc1_bow_width", "22.0 mm", "mm", "SC1 key blank bow (head) width. Standard round head."),
    ("key_sc1_blade_thick", "2.3 mm", "mm", "SC1 key blank blade thickness. Slightly thicker than KW1. Locksmith spec."),
    ("key_split_ring_25mm_od", "25.0 mm", "mm", "Standard 25 mm split ring keychain ring outer diameter."),
    ("key_split_ring_25mm_wire_dia", "1.5 mm", "mm", "Standard 25 mm split ring wire diameter."),

    # ── Game Controllers ─────────────────────────────────────────────────────
    ("controller_xbox_width", "153.0 mm", "mm", "Xbox Series X/S wireless controller width. Microsoft spec."),
    ("controller_xbox_height", "102.0 mm", "mm", "Xbox Series X/S controller height. Microsoft spec."),
    ("controller_xbox_depth", "61.0 mm", "mm", "Xbox Series X/S controller depth. Microsoft spec."),
    ("controller_ps5_dualsense_width", "160.0 mm", "mm", "PS5 DualSense wireless controller width. Sony spec."),
    ("controller_ps5_dualsense_height", "106.0 mm", "mm", "PS5 DualSense controller height. Sony spec."),
    ("controller_ps5_dualsense_depth", "66.0 mm", "mm", "PS5 DualSense controller depth. Sony spec."),
    ("controller_switch_pro_width", "152.0 mm", "mm", "Nintendo Switch Pro Controller width. Nintendo spec."),
    ("controller_switch_pro_height", "106.0 mm", "mm", "Nintendo Switch Pro Controller height. Nintendo spec."),
    ("controller_switch_pro_depth", "63.0 mm", "mm", "Nintendo Switch Pro Controller depth. Nintendo spec."),
    ("controller_joycon_width", "35.9 mm", "mm", "Nintendo Switch Joy-Con single width. Nintendo spec."),
    ("controller_joycon_height", "102.0 mm", "mm", "Nintendo Switch Joy-Con single height. Nintendo spec."),
    ("controller_joycon_depth", "13.9 mm", "mm", "Nintendo Switch Joy-Con body depth (thinnest). Max ~28.4 mm at button protrusion."),

    # ── Remotes ──────────────────────────────────────────────────────────────
    ("remote_apple_tv_siri_width", "35.6 mm", "mm", "Apple TV Siri Remote 3rd gen (USB-C) width. Apple spec."),
    ("remote_apple_tv_siri_height", "137.2 mm", "mm", "Apple TV Siri Remote 3rd gen length/height. Apple spec."),
    ("remote_apple_tv_siri_depth", "9.1 mm", "mm", "Apple TV Siri Remote 3rd gen depth. Apple spec."),
    ("remote_fire_tv_width", "38.0 mm", "mm", "Amazon Fire TV Alexa Voice Remote width. Approximate."),
    ("remote_fire_tv_height", "148.0 mm", "mm", "Amazon Fire TV Alexa Voice Remote length. Approximate."),
    ("remote_fire_tv_depth", "18.0 mm", "mm", "Amazon Fire TV remote depth. Approximate."),
    ("remote_roku_voice_pro_width", "41.0 mm", "mm", "Roku Voice Remote Pro width. Approximate."),
    ("remote_roku_voice_pro_height", "145.0 mm", "mm", "Roku Voice Remote Pro length. Approximate."),
    ("remote_roku_voice_pro_depth", "20.0 mm", "mm", "Roku Voice Remote Pro depth. Approximate."),

    # ── Watches ──────────────────────────────────────────────────────────────
    ("watch_apple_series10_42_height", "42.0 mm", "mm", "Apple Watch Series 10 42 mm case height. Apple spec."),
    ("watch_apple_series10_42_width", "36.0 mm", "mm", "Apple Watch Series 10 42 mm case width. Apple spec."),
    ("watch_apple_series10_42_depth", "9.7 mm", "mm", "Apple Watch Series 10 42 mm case depth. Apple spec."),
    ("watch_apple_series10_46_height", "46.0 mm", "mm", "Apple Watch Series 10 46 mm case height. Apple spec."),
    ("watch_apple_series10_46_width", "39.0 mm", "mm", "Apple Watch Series 10 46 mm case width. Apple spec."),
    ("watch_apple_series10_46_depth", "9.7 mm", "mm", "Apple Watch Series 10 46 mm case depth. Apple spec."),
    ("watch_apple_ultra_2_height", "49.0 mm", "mm", "Apple Watch Ultra 2 case height. Apple spec."),
    ("watch_apple_ultra_2_width", "44.0 mm", "mm", "Apple Watch Ultra 2 case width. Apple spec."),
    ("watch_apple_ultra_2_depth", "14.4 mm", "mm", "Apple Watch Ultra 2 case depth. Apple spec."),
    ("watch_band_width_20mm", "20.0 mm", "mm", "Standard 20 mm watch band/lug width. Common for many smartwatches and men's dress watches."),
    ("watch_band_width_22mm", "22.0 mm", "mm", "Standard 22 mm watch band/lug width. Common for larger men's watches."),

    # ── Smart Home ───────────────────────────────────────────────────────────
    ("smarthome_echo_dot_5_dia", "100.0 mm", "mm", "Amazon Echo Dot 5th gen diameter. Amazon spec."),
    ("smarthome_echo_dot_5_height", "89.0 mm", "mm", "Amazon Echo Dot 5th gen height. Amazon spec."),
    ("smarthome_nest_mini_2_dia", "98.0 mm", "mm", "Google Nest Mini 2nd gen diameter. Google spec."),
    ("smarthome_nest_mini_2_height", "42.0 mm", "mm", "Google Nest Mini 2nd gen height. Google spec."),
    ("smarthome_echo_show_5_width", "147.0 mm", "mm", "Amazon Echo Show 5 3rd gen width. Amazon spec."),
    ("smarthome_echo_show_5_height", "82.0 mm", "mm", "Amazon Echo Show 5 3rd gen height. Amazon spec."),
    ("smarthome_echo_show_5_depth", "91.0 mm", "mm", "Amazon Echo Show 5 3rd gen depth. Amazon spec."),
    ("smarthome_kasa_ep10_width", "60.0 mm", "mm", "TP-Link Kasa EP10 smart plug width. TP-Link spec."),
    ("smarthome_kasa_ep10_height", "51.5 mm", "mm", "TP-Link Kasa EP10 smart plug height. TP-Link spec."),
    ("smarthome_kasa_ep10_depth", "38.0 mm", "mm", "TP-Link Kasa EP10 smart plug depth (excluding prongs). TP-Link spec."),
    ("smarthome_hue_bridge_width", "88.0 mm", "mm", "Philips Hue Bridge width (rounded square shape). Philips spec."),
    ("smarthome_hue_bridge_height", "26.0 mm", "mm", "Philips Hue Bridge height. Philips spec."),

    # ── Security Cameras ─────────────────────────────────────────────────────
    ("camera_security_ring_indoor_width", "49.0 mm", "mm", "Ring Indoor Cam 2nd gen width (cube body). Ring spec."),
    ("camera_security_ring_indoor_height", "49.0 mm", "mm", "Ring Indoor Cam 2nd gen height (camera body only). With stand ~97 mm."),
    ("camera_security_ring_indoor_depth", "49.0 mm", "mm", "Ring Indoor Cam 2nd gen depth (cube body). Ring spec."),
    ("camera_security_ring_stickup_dia", "60.0 mm", "mm", "Ring Stick Up Cam battery body diameter. Ring spec."),
    ("camera_security_ring_stickup_height", "97.0 mm", "mm", "Ring Stick Up Cam height without mount. Ring spec."),
    ("camera_security_ring_doorbell_width", "61.7 mm", "mm", "Ring Video Doorbell current gen width. Ring spec."),
    ("camera_security_ring_doorbell_height", "126.5 mm", "mm", "Ring Video Doorbell current gen height. Ring spec."),
    ("camera_security_ring_doorbell_depth", "22.1 mm", "mm", "Ring Video Doorbell current gen depth. Ring spec."),
    ("camera_security_unifi_g4_bullet_dia", "75.0 mm", "mm", "Ubiquiti UniFi G4 Bullet camera body diameter. Ubiquiti datasheet."),
    ("camera_security_unifi_g4_bullet_length", "140.0 mm", "mm", "Ubiquiti UniFi G4 Bullet camera body length. Ubiquiti datasheet."),
    ("camera_security_unifi_g4_instant_width", "81.6 mm", "mm", "Ubiquiti UniFi G4 Instant camera width. Ubiquiti datasheet."),
    ("camera_security_unifi_g4_instant_height", "50.0 mm", "mm", "Ubiquiti UniFi G4 Instant camera height. Ubiquiti datasheet."),
    ("camera_security_unifi_g4_instant_depth", "47.2 mm", "mm", "Ubiquiti UniFi G4 Instant camera depth. Ubiquiti datasheet."),
    ("camera_security_unifi_g5_flex_dia", "48.0 mm", "mm", "Ubiquiti UniFi G5 Flex turret camera body diameter. Ubiquiti datasheet."),
    ("camera_security_unifi_g5_flex_height", "107.5 mm", "mm", "Ubiquiti UniFi G5 Flex turret camera height. Ubiquiti datasheet."),
    ("camera_security_tripod_mount_thread_dia", "6.35 mm", "mm", "Standard 1/4-20 UNC tripod mount thread outer diameter. ANSI/ASME standard."),
    ("camera_security_tripod_mount_thread_pitch", "1.27 mm", "mm", "Standard 1/4-20 UNC tripod mount thread pitch (20 TPI). ANSI/ASME standard."),

    # ── Bottles ──────────────────────────────────────────────────────────────
    ("bottle_pill_13dram_dia", "33.0 mm", "mm", "13 dram prescription pill bottle body diameter. Pharmaceutical industry standard. Cap dia ~2-4 mm larger."),
    ("bottle_pill_13dram_height", "54.0 mm", "mm", "13 dram pill bottle height. Pharmaceutical standard."),
    ("bottle_pill_20dram_dia", "39.0 mm", "mm", "20 dram prescription pill bottle body diameter. Pharmaceutical standard."),
    ("bottle_pill_20dram_height", "58.0 mm", "mm", "20 dram pill bottle height. Pharmaceutical standard."),
    ("bottle_pill_30dram_dia", "46.0 mm", "mm", "30 dram prescription pill bottle body diameter. Pharmaceutical standard."),
    ("bottle_pill_30dram_height", "69.0 mm", "mm", "30 dram pill bottle height. Pharmaceutical standard."),
    ("bottle_nalgene_32oz_body_dia", "90.0 mm", "mm", "Nalgene 32 oz wide mouth bottle body diameter. Nalgene spec."),
    ("bottle_nalgene_32oz_height", "214.0 mm", "mm", "Nalgene 32 oz wide mouth bottle height. Nalgene spec."),
    ("bottle_nalgene_32oz_mouth_dia", "63.0 mm", "mm", "Nalgene 32 oz wide mouth opening inner diameter. Nalgene spec."),
    ("bottle_eye_drop_15ml_dia", "29.0 mm", "mm", "Standard 15 ml eye drop bottle body diameter. Nominal — varies by brand. Range 22-30 mm."),
    ("bottle_eye_drop_15ml_height", "77.0 mm", "mm", "Standard 15 ml eye drop bottle height with cap. Nominal — range 70-80 mm."),
    ("bottle_spray_28_400_neck_od", "28.0 mm", "mm", "28/400 spray bottle neck finish outer diameter. GPI standard exact."),

    # ── Storage Media ────────────────────────────────────────────────────────
    ("media_samsung_t7_ssd_width", "57.3 mm", "mm", "Samsung T7 portable SSD width. Samsung datasheet."),
    ("media_samsung_t7_ssd_height", "85.0 mm", "mm", "Samsung T7 portable SSD height. Samsung datasheet."),
    ("media_samsung_t7_ssd_depth", "8.0 mm", "mm", "Samsung T7 portable SSD depth. Samsung datasheet."),
    ("media_wd_passport_width", "75.0 mm", "mm", "WD My Passport external HDD width. WD datasheet."),
    ("media_wd_passport_height", "107.0 mm", "mm", "WD My Passport external HDD height. WD datasheet."),
    ("media_wd_passport_depth", "11.15 mm", "mm", "WD My Passport external HDD depth. WD datasheet."),
    ("media_sata_25_width", "69.85 mm", "mm", "2.5-inch SATA drive width. SFF-8201 standard exact."),
    ("media_sata_25_length", "100.45 mm", "mm", "2.5-inch SATA drive length. SFF-8201 standard exact."),
    ("media_sata_25_height_thin", "7.0 mm", "mm", "2.5-inch SATA drive height (thin/SSD). SFF-8201 standard."),
    ("media_sata_25_height_std", "9.5 mm", "mm", "2.5-inch SATA drive height (standard HDD). SFF-8201 standard."),
    ("media_sata_35_width", "101.6 mm", "mm", "3.5-inch SATA drive width. SFF-8301 standard exact."),
    ("media_sata_35_length", "146.99 mm", "mm", "3.5-inch SATA drive length. SFF-8301 standard exact."),
    ("media_sata_35_height", "25.4 mm", "mm", "3.5-inch SATA drive height. SFF-8301 standard. Some newer drives 17.8 mm."),
    ("media_m2_2280_width", "22.0 mm", "mm", "M.2 2280 SSD width. PCI-SIG M.2 specification exact. Name encodes 22 x 80 mm."),
    ("media_m2_2280_length", "80.0 mm", "mm", "M.2 2280 SSD length. PCI-SIG specification exact."),
    ("media_m2_2280_height", "2.23 mm", "mm", "M.2 2280 SSD height (single-sided). Double-sided ~3.73 mm."),
    ("media_cfexpress_type_b_width", "29.6 mm", "mm", "CFexpress Type B card width. CompactFlash Association spec exact."),
    ("media_cfexpress_type_b_height", "38.36 mm", "mm", "CFexpress Type B card height. CFA spec exact."),
    ("media_cfexpress_type_b_thick", "3.8 mm", "mm", "CFexpress Type B card thickness. CFA spec exact."),

    # ── Glasses ──────────────────────────────────────────────────────────────
    ("glasses_hard_case_width", "70.0 mm", "mm", "Sunglasses hard shell case width typical. Nominal — range 65-75 mm. Verify for specific case."),
    ("glasses_hard_case_height", "42.0 mm", "mm", "Sunglasses hard case height typical. Nominal — range 38-45 mm."),
    ("glasses_hard_case_length", "165.0 mm", "mm", "Sunglasses hard case length typical. Nominal — range 155-170 mm."),
    ("glasses_folded_width", "140.0 mm", "mm", "Folded eyeglasses width envelope typical. Nominal — range 130-155 mm."),
    ("glasses_folded_height", "48.0 mm", "mm", "Folded eyeglasses height envelope typical. Nominal — range 40-55 mm."),
    ("glasses_folded_depth", "48.0 mm", "mm", "Folded eyeglasses depth envelope typical. Nominal — range 35-55 mm."),

    # ── Derived Parameters ───────────────────────────────────────────────────
    ("phone_universal_max_height", "phone_iphone_16_pro_max_height", "mm", "Max phone height across all models — iPhone 16 Pro Max at 163.0 mm. For universal holder depth."),
    ("phone_universal_max_width", "phone_galaxy_s24_ultra_width", "mm", "Max phone width across all models — Galaxy S24 Ultra at 79.0 mm."),
    ("phone_universal_max_depth", "phone_galaxy_s24_ultra_depth", "mm", "Max phone depth across all models — Galaxy S24 Ultra at 8.60 mm."),
    ("phone_case_allowance", "3.0 mm", "mm", "Typical rugged phone case adds ~3 mm per side. Adjust per actual case."),
    ("phone_universal_cased_width", "phone_universal_max_width + 2 * phone_case_allowance", "mm", "Universal phone width with case allowance. For holder/dock inner width."),
    ("phone_universal_cased_depth", "phone_universal_max_depth + 2 * phone_case_allowance", "mm", "Universal phone depth with case allowance. For holder/dock slot depth."),
    ("tablet_universal_max_height", "tablet_ipad_pro_13_height", "mm", "Max tablet height — iPad Pro 13 at 281.6 mm."),
    ("tablet_universal_max_width", "tablet_ipad_pro_13_width", "mm", "Max tablet width — iPad Pro 13 at 215.5 mm."),
    ("tablet_universal_max_depth", "tablet_ipad_mini_7_depth", "mm", "Max tablet depth — iPad Mini 7 at 6.3 mm (thickest current iPad)."),
    ("drinkware_max_body_dia", "drinkware_yeti_rambler_30oz_lip_dia", "mm", "Largest drinkware diameter — Yeti 30 oz at 102 mm."),
    ("drinkware_max_height", "drinkware_stanley_quencher_40oz_height", "mm", "Tallest drinkware — Stanley Quencher 40 oz at 260 mm."),
    ("battery_aa_holder_slot_dia", "battery_aa_dia + 2 * tolerance_fit_class_fdm_sliding_per_surface", "mm", "AA battery holder slot diameter with FDM sliding fit clearance."),
    ("battery_aaa_holder_slot_dia", "battery_aaa_dia + 2 * tolerance_fit_class_fdm_sliding_per_surface", "mm", "AAA battery holder slot diameter with FDM sliding fit clearance."),
    ("battery_18650_holder_slot_dia", "battery_18650_dia + 2 * tolerance_fit_class_fdm_sliding_per_surface", "mm", "18650 battery holder slot diameter with FDM sliding fit clearance."),
    ("controller_universal_max_width", "controller_ps5_dualsense_width", "mm", "Max controller width — PS5 DualSense at 160 mm. For universal charging dock/holder."),
    ("controller_universal_max_height", "controller_ps5_dualsense_height", "mm", "Max controller height — DualSense/Switch Pro at 106 mm."),
    ("controller_universal_max_depth", "controller_ps5_dualsense_depth", "mm", "Max controller depth — PS5 DualSense at 66 mm."),
    ("edc_bic_pen_circular_hole_dia", "10.4 mm", "mm", "BIC Cristal hex pen across-corners diameter (9 mm / cos 30). Use for round holder holes."),
]
# fmt: on


def main():
    if not CSV_PATH.exists():
        print(f"ERROR: {CSV_PATH} not found. Run from params/ directory.", file=sys.stderr)
        sys.exit(1)

    # Read existing params
    existing_names = set()
    with open(CSV_PATH, "r", newline="") as f:
        reader = csv.reader(f)
        next(reader)  # skip header
        for row in reader:
            if row:
                existing_names.add(row[0])

    print(f"Existing parameters: {len(existing_names)}")

    # Validate new params
    errors = []
    new_names = set()
    all_names = existing_names.copy()

    for i, (name, expr, unit, comment) in enumerate(NEW_PARAMS):
        if not PARAM_NAME_RE.match(name):
            errors.append(f"  [{i}] invalid name: '{name}'")
        if name in existing_names:
            errors.append(f"  [{i}] duplicate with existing: '{name}'")
        if name in new_names:
            errors.append(f"  [{i}] duplicate within new params: '{name}'")
        if unit not in ("mm", "cm", "in", "deg", "rad", ""):
            errors.append(f"  [{i}] invalid unit: '{unit}'")
        new_names.add(name)
        all_names.add(name)

    # Validate derived param references
    for i, (name, expr, unit, comment) in enumerate(NEW_PARAMS):
        # Check if expression references other params (not just a literal value)
        tokens = set(re.findall(r"[a-z][a-z0-9_]{2,}", expr))
        tokens -= {"mm", "cm", "deg", "rad"}  # remove unit suffixes
        for tok in tokens:
            if tok not in all_names:
                errors.append(f"  [{i}] '{name}' references undefined param: '{tok}'")

    if errors:
        print(f"\nFAILED — {len(errors)} validation error(s):", file=sys.stderr)
        for e in errors:
            print(e, file=sys.stderr)
        sys.exit(1)

    # Append to CSV
    with open(CSV_PATH, "a", newline="") as f:
        writer = csv.writer(f)
        for name, expr, unit, comment in NEW_PARAMS:
            writer.writerow([name, expr, unit, comment])

    total = len(existing_names) + len(NEW_PARAMS)
    print(f"Added {len(NEW_PARAMS)} new parameters")
    print(f"Total parameters: {total}")
    print("Validation passed: all names valid, no duplicates, all references resolve.")


if __name__ == "__main__":
    main()
