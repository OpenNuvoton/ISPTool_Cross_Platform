import ctypes
import os
from ctypes import byref, c_char, c_int, c_uint, c_void_p, c_ulong, Structure, windll, CFUNCTYPE, WINFUNCTYPE, POINTER

(
    ECE_NO_ERROR,
    ECE_NO_CHIP_CFG_DATA,
    ECE_NO_MATCH_CHIP,
    ECE_NO_MATCH_SERIES,
    ECE_EXPORT_FAILED,
    ECE_CFG_NO_CFG,
    ECE_CFG_DATAFLASH_ADDRESS_ERROR,
    ECE_USE_DEFAULT_CHIP,
    ECE_XLSLIB_NOT_EXIST,
    ECE_FILE_NOT_EXIST
) = map(ctypes.c_int, range(10))

class I_ChipInfoManager(Structure):
    _fields_ = [
        ("ReleaseDLL", CFUNCTYPE(c_void_p)),
        ("GetChipInfo", CFUNCTYPE(c_uint)),
        ("GetChipInfoByFindInfo", CFUNCTYPE(c_uint)),
        ("ExportChipInfo", CFUNCTYPE(c_uint)),
        ("CheckChipFromXLS", CFUNCTYPE(c_uint)),
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
