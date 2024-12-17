from PartNumID import *
from PySide6 import QtCore, QtGui, QtWidgets

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

def config_setting_str(chip_type):
    if (chip_type == 0x0):
        return ""
    elif (chip_type in config_type_M051D):
        return "M051D"
    elif (chip_type in config_type_M251):
        return "M251"
    elif (chip_type in config_type_M258):
        return "M258"
    elif (chip_type in config_type_M051A):
        return "M051A"
    elif (chip_type in config_type_M051B):
        return "M051B"
    elif (chip_type in config_type_M058):
        return "M058"
    elif (chip_type in config_type_NUC100):
        return "NUC100"
    elif (chip_type in config_type_NUC122):
        return "NUC122"
    elif (chip_type in config_type_NUC123AN):
        return "NUC123AN"
    elif (chip_type in config_type_NUC123AE):
        return "NUC123AE"
    elif (chip_type in config_type_NUC200):
        return "NUC200"
    elif (chip_type in config_type_MINI51):
        return "MINI51"
    elif (chip_type in config_type_MINI51CN):
        return "MINI51CN"
    elif (chip_type in config_type_M0564):
        return "M0564"
    elif (chip_type in config_type_NANO112):
        return "NANO112"
    elif (chip_type in config_type_NANO103):
        return "NANO103"
    elif (chip_type in config_type_NANO100):
        return "NANO100"
    elif (chip_type in config_type_MINI55):
        return "MINI55"
    elif (chip_type in config_type_NM1120):
        return "NM1120"
    elif (chip_type in config_type_NM1500):
        return "NM1500"
    elif (chip_type in config_type_NUC1262):
        return "NUC1262"
    elif (chip_type in config_type_NUC400):
        return "NUC400"
    elif (chip_type in config_type_M451):
        return "M451"
    elif (chip_type in config_type_M031):
        return "M031"
    elif (chip_type in config_type_M030G):
        return "M030G"
    elif (chip_type in config_type_M0A21):
        return "M0A21"
    elif (chip_type in config_type_M480):
        return "M480"
    elif (chip_type in config_type_M480LD):
        return "M480LD"
    elif (chip_type in config_type_M460):
        return "M460"
    elif (chip_type in config_type_M2351):
        return "M2351"
    elif (chip_type in config_type_M2354):
        return "M2354"
    elif (chip_type in config_type_M471):
        return "M471"
    elif (chip_type in config_type_M2L31):
        return "M2L31"
    elif (chip_type in config_type_M2003):
        return "M2003"
    elif (chip_type in config_type_M55M1):
        return "M55M1"
        
    return ""

