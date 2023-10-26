import os

from PartNumID import *
from Flash import *
from NuVoice import *

def GetStaticInfo(self, UID, config):
    chip_name = ""
    chip_type = 0x0
    memory_size = 0
    flash_type = 0
    dataflash_size = 0
    page_size = 0
    table_len = len(PartNumIDs)
    for i in range(table_len):
        if (UID == PartNumIDs[i][1]):
            chip_name = PartNumIDs[i][0]
            chip_type = PartNumIDs[i][2]
            break
            
    if chip_type >= 0x80:
        # type 8051
        DID = UID & 0x0000FFFF
        flash_table_len = len(Flash_8051)
        for i in range(flash_table_len):
            if (DID == Flash_8051[i][3]):
                memory_size = Flash_8051[i][0]
                flash_type = Flash_8051[i][4]
                break
        aprom_size, nvm_size, nvm_addr = GetDynamicInfo_8051(UID, config, memory_size, flash_type)
        
    elif chip_type != 0x0:
        # type Numicro
        flash_table_len = len(Flash_NuMicro)
        for i in range(flash_table_len):
            if (UID == Flash_NuMicro[i][5]):
                memory_size = Flash_NuMicro[i][0]
                dataflash_size = Flash_NuMicro[i][1]
                ldrom_size = Flash_NuMicro[i][4]
                break
        
        config_type_no_flash = {PROJ_M2351, PROJ_M2354ES, PROJ_M2354} 
        if (chip_type in config_type_no_flash):
            aprom_size = memory_size
            nvm_size = 0
            nvm_addr = aprom_size
            return chip_name, chip_type, aprom_size, nvm_size, nvm_addr, page_size
        
        if chip_type == PROJ_NUC123AN or chip_type == PROJ_NUC123AE or chip_type == PROJ_NUC1311 or chip_type == PROJ_M0518:
            flash_type = 2
        else:
            flash_type = 1 if (dataflash_size != 0) else 0
            
        if ((chip_type == PROJ_NUC400AE) or (chip_type == PROJ_M451HD) or (chip_type == PROJ_M471) or (chip_type == PROJ_M0564) 
             or (chip_type == PROJ_NUC1262) or (chip_type == PROJ_NUC1263) or (chip_type == PROJ_M031_512K) or (chip_type == PROJ_M031_256K)):
            flash_type |= 0x200
        elif ((chip_type == PROJ_M480) or (chip_type == PROJ_M480LD) or (chip_type == PROJ_M460HD) or (chip_type == PROJ_M460LD)):
            flash_type |= 0x300
            
        aprom_size, nvm_size, nvm_addr = GetDynamicInfo_NuMicro(UID, config, memory_size, flash_type)
        page_size = 1 << (((flash_type & 0x0000FF00) >>  8) + 9)
    
    elif os.name == 'nt':  # Windows
        pConfig = (c_uint * 4)
        pConfig[0] = config[0]
        pConfig[1] = config[1]
        
        if get_NuVoice_info(UID, pConfig):
            chip_name = gNuVoiceChip.sChipName.split('\0', 1)[0]
            chip_type = None
            aprom_size = gNuVoiceChip.dwAPROMSize
            nvm_size = gNuVoiceChip.dwDataFlashSize
            nvm_addr = gNuVoiceChip.dwDataFlashAddress
            page_size = gNuVoiceChip.dwErasePageSize
            
    return chip_name, chip_type, aprom_size, nvm_size, nvm_addr, page_size
        
def GetDynamicInfo_8051(self, UID, config, memory_size, flash_type):
    flash_mode = flash_type & 0x3
    ldsel = (config[0] >> 8) & 0x07
    ldrom_size = (0x07 - ldsel) * 1024
    ldrom_size = 4096 if (ldrom_size > 4096) else ldrom_size
    nvm_size = 0
    if (flash_mode != 0):
        nvm_size = 0x2800 - ldrom_size
    aprom_size = memory_size - ldrom_size - nvm_size
    nvm_addr = aprom_size
    return aprom_size, nvm_size, nvm_addr
    
def GetDynamicInfo_NuMicro(UID, config, memory_size, flash_type):
    utype = flash_type & 0xFF
    bShare = True if (utype == 0) else False
    
    if (utype == 2) and (config[0] & 0x4 == 0):
        memory_size += 0x1000
        bShare = True
    
    if (bShare):
        if (config[0] & 0x1 == 0):
            page_size = ((flash_type & 0x0000FF00) >>  8) + 9
            addr = config[1] & 0x00FFFFFF
            addr &= ~((1 << page_size) - 1)
            aprom_size = addr if (memory_size > addr) else memory_size
            nvm_size = memory_size - aprom_size
        else:
            aprom_size = memory_size
            nvm_size = 0
        nvm_addr = aprom_size
    else:
        aprom_size = memory_size
        nvm_size = 0x1000
        nvm_addr = 0x1F000
    
    return aprom_size, nvm_size, nvm_addr