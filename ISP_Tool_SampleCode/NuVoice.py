import ctypes
from ctypes import *

class I_ChipInfoManager(Structure):
    _fields_ = [
        ("ReleaseDLL", ReleaseDLL),
        ("GetChipInfo", GetChipInfo),
        ("GetChipInfoByFindInfo", GetChipInfoByFindInfo),
        ("ExportChipInfo", ExportChipInfo),
        ("CheckChipFromXLS", CheckChipFromXLS),
    ] 
                
CHIP_UCID_MAX_LEN = 4  
CHIP_NAME_LEN = 100  

class sChipInfo(Structure):
    _fields_ = [
        ("dwChipID", c_ulong),
        ("dwChipIDMask", c_ulong),
        ("dwChipUCID", c_ulong * CHIP_UCID_MAX_LEN),
        ("sChipName", c_char * CHIP_NAME_LEN),
        ("dwSeriesEnum", c_ulong),
        ("dwAPROMSize", c_ulong),
        ("dwLDROMSize", c_ulong),
        ("dwEmbeedSPIFlashSize", c_ulong),
        ("dwSRAMSize", c_ulong),
        ("dwErasePageSize", c_ulong),
        ("dwDataFlashAddress", c_ulong),
        ("dwDataFlashSize", c_ulong),
    ]
    
gNuVoiceChip = sChipInfo()

def get_NuVoice_info(dwChipID, pConfig):
    ret = False
    hDll = None
    BOOL = ctypes.c_int  
    CreateChipInfoManagerProto = WINFUNCTYPE(BOOL, POINTER(POINTER(I_ChipInfoManager)))

    if os.name == 'nt':  # Windows
        hDll = ctypes.windll.LoadLibrary('./GetChipInformation.dll')
    elif os.name == 'posix':  # Linux/Unix/MacOS
        return None
        
    if hDll is not None:
        pCreateChipInfoManager = CreateChipInfoManagerProto(("CreateChipInfoManager", hDll))
        
        if pCreateChipInfoManager:
            pChipInfoManager = POINTER(I_ChipInfoManager)()
        
            if pCreateChipInfoManager(byref(pChipInfoManager)) == 1:  # Assuming TRUE is 1
                err = pChipInfoManager.contents.GetChipInfo(dwChipID, gNuVoiceChip, pConfig)
                
                if err == ECE_NO_ERROR:
                    ret = True
                
                pChipInfoManager.contents.ReleaseDLL()
                
        windll.kernel32.FreeLibrary(hDll)
    
    return ret






 