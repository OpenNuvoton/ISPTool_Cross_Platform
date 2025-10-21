from PySide6 import QtCore, QtGui, QtWidgets
from PartNumID import *

config_type_M030G = {PROJ_M030G, PROJ_M031GPON}
config_type_M031 = {PROJ_M031_128K, PROJ_M031_64K, PROJ_M031_32K, PROJ_M031_16K, PROJ_M031_512K, PROJ_M031_256K}
config_type_M051A = {PROJ_M051AN}
config_type_M051B = {PROJ_M051BN}
config_type_M051D = {PROJ_M051DN, PROJ_M051DE}
config_type_M0564 = {PROJ_NUC121, PROJ_M0564, PROJ_NUC1261}
config_type_M058 = {PROJ_M058SAN}
config_type_M0A21 = {PROJ_M0A21}
config_type_M2003 = {PROJ_M2003}
config_type_M2351 = {PROJ_M2351}
config_type_M2354 = {PROJ_M2354ES, PROJ_M2354}
config_type_M251 = {PROJ_M252_C, PROJ_M252_D, PROJ_M252_E, PROJ_M252_G}
config_type_M258 = {PROJ_M258, PROJ_M253, PROJ_M256D, PROJ_M258G}
config_type_M2L31 = {PROJ_M2L31}
config_type_M451 = {PROJ_M451HD, PROJ_M451LD, PROJ_M4521}
config_type_M460 = {PROJ_M460HD, PROJ_M460LD}
config_type_M471 = {PROJ_M471}
config_type_M480 = {PROJ_M480}
config_type_M480LD = {PROJ_M480LD}
config_type_M55M1 = {PROJ_M55M1}
config_type_MINI51 = {PROJ_MINI51AN}
config_type_MINI51CN = {PROJ_MINI51DE, PROJ_MINI58}
config_type_MINI55 = {PROJ_MINI55}
config_type_NANO100 = {PROJ_NANO100BN}
config_type_NANO103 = {PROJ_NANO103}
config_type_NANO112 = {PROJ_NANO102AN, PROJ_NANO100AN}
config_type_NM1120 = {PROJ_NM1120, PROJ_NM1230, PROJ_NM1240}
config_type_NM1500 = {PROJ_NM1500AE}
config_type_NUC100 = {PROJ_NUC100AN, PROJ_NUC100CN}
config_type_NUC122 = {PROJ_NUC122AN, PROJ_NUC122DN}
config_type_NUC123AE = {PROJ_NUC123AE}
config_type_NUC123AN = {PROJ_NUC123AN}
config_type_NUC1262 = {PROJ_NUC1262, PROJ_NUC1263}
config_type_NUC131 = {PROJ_NUC1311, PROJ_M0518}
config_type_NUC200 = {PROJ_NUC100DN, PROJ_NUC200AE, PROJ_NUC2201}
config_type_NUC400 = {PROJ_NUC400AE}
config_type_M3331 = {PROJ_M3331IG, PROJ_M3331G}
config_type_M2A23 = {PROJ_M2A23}
config_type_M2U51 = {PROJ_M2U51G, PROJ_M2U51C}
config_type_8051 = {PROJ_N76E885, PROJ_N76E616 ,PROJ_N76E003, PROJ_ML51_32K, PROJ_ML51_16K,
                       PROJ_MS51_16K, PROJ_MS51_8K, PROJ_MS51_32K, PROJ_ML56, PROJ_MUG51,
                       PROJ_MG51, PROJ_MG51D}

category_name_pairs = [
    (config_type_M030G, "M030G"),
    (config_type_M031, "M031"),
    (config_type_M051A, "M051A"),
    (config_type_M051B, "M051B"),
    (config_type_M051D, "M051D"),
    (config_type_M0564, "M0564"),
    (config_type_M058, "M058"),
    (config_type_M0A21, "M0A21"),
    (config_type_M2003, "M2003"),
    (config_type_M2351, "M2351"),
    (config_type_M2354, "M2354"),
    (config_type_M251, "M251"),
    (config_type_M258, "M258"),
    (config_type_M2L31, "M2L31"),
    (config_type_M451, "M451"),
    (config_type_M460, "M460"),
    (config_type_M471, "M471"),
    (config_type_M480, "M480"),
    (config_type_M480LD, "M480LD"),
    (config_type_M55M1, "M55M1"),
    (config_type_MINI51, "MINI51"),
    (config_type_MINI51CN, "MINI51CN"),
    (config_type_MINI55, "MINI55"),
    (config_type_NANO100, "NANO100"),
    (config_type_NANO103, "NANO103"),
    (config_type_NANO112, "NANO112"),
    (config_type_NM1120, "NM1120"),
    (config_type_NM1500, "NM1500"),
    (config_type_NUC100, "NUC100"),
    (config_type_NUC122, "NUC122"),
    (config_type_NUC123AE, "NUC123AE"),
    (config_type_NUC123AN, "NUC123AN"),
    (config_type_NUC1262, "NUC1262"),
    (config_type_NUC131, "NUC131"),
    (config_type_NUC200, "NUC200"),
    (config_type_NUC400, "NUC400"),
    (config_type_M3331, "M3331"),
    (config_type_M2A23, "M2A23"),
    (config_type_M2A23, "M2U51"),
    (config_type_8051, "8051"),
]

CHIP_TYPE_NAME_MAP: dict[int, str] = {}

for config_set, label in category_name_pairs:
    CHIP_TYPE_NAME_MAP.update({identifier: label for identifier in config_set})

def config_setting_str(chip_type: int) -> str:
    if chip_type == 0x0:
        return ""

    return CHIP_TYPE_NAME_MAP.get(chip_type, "")
