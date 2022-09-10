from Util.GameData import *
from Util.EntityClass import *
from Module.Memory import *
from Module.Struct import *

import time, win32api


class SkinChanger():
    Status = False

    GunList = {
        "P2000" : { "ID" : 32, "Skin": 894 }, "USP-S" : { "ID" : 61, "Skin": 313 }, "Glock" : { "ID" : 4, "Skin": 38 }, 
        "Dual Berettas" : { "ID" : 2, "Skin": 1126 }, "P250" : { "ID" : 36, "Skin": 813 }, "Tec-9" : { "ID" : 30, "Skin": 684 }, 
        "CZ75-Auto" : { "ID" : 63, "Skin": 543 }, "Desert Eagle" : { "ID" : 1, "Skin": 231 }, "Five-SeveN" : { "ID" : 3, "Skin": 1128 }, 
        "R8" : { "ID" : 64, "Skin": 37 }, "Nova" : { "ID" : 35, "Skin": 62 }, "XM1014" : { "ID" : 25, "Skin": 850 }, 
        "MAG-7" : { "ID" : 27, "Skin": 431 }, "M249" : { "ID" : 14, "Skin": 1148 }, "Negev" : { "ID" : 28, "Skin": 763 }, 
        "Sawed-Off" : { "ID" : 29, "Skin": 720 }, "MAC-10" : { "ID" : 17, "Skin": 1067 }, "MP5-SD" : { "ID" : 23, "Skin": 923 }, 
        "UMP-45" : { "ID" : 24, "Skin": 704 }, "P90" : { "ID" : 19, "Skin": 611 }, "PP-19" : { "ID" : 26, "Skin": 526 }, 
        "MP9" : { "ID" : 34, "Skin": 262 }, "MP7" : { "ID" : 33, "Skin": 536 }, "FAMAS" : { "ID" : 10, "Skin": 194 }, 
        "M4A4" : { "ID" : 16, "Skin": 664 }, "M4A1-S" : { "ID" : 60, "Skin": 1073 }, "SSG 08" : { "ID" : 40, "Skin": 899 }, 
        "AUG" : { "ID" : 8, "Skin": 601 }, "AWP" : { "ID" : 9, "Skin": 446 }, "SCAR-20" : { "ID" : 38, "Skin": 312 }, 
        "Galil" : { "ID" : 13, "Skin": 379 }, "AK-47" : { "ID" : 7, "Skin": 302 }, "SG 553" : { "ID" : 39, "Skin": 897 }, 
        "G3SG1" : { "ID" : 11, "Skin": 511 }
    }


    def GetWeaponSkin(WeaponID):
        for Item in SkinChanger.GunList.items():
            if Item[1]["ID"] == WeaponID:
                return Item[1]["Skin"]

        return 0


    def Start():
        while (SkinChanger.Status):
            if (GameData.LocalPlayer):
                
                for i in range(8):
                    MyWeapon = Memory.Read.int(GameData.LocalPlayer + Offsets.Netvars.m_hMyWeapons + (i - 1) * 0x4) &0xFFF
                    WeaponAddress = Memory.Read.int(Game.Client + Offsets.Signatures.dwEntityList + (MyWeapon - 1) * 0x10)

                    if (WeaponAddress):
                        WeaponID = Memory.Read.short(WeaponAddress + Offsets.Netvars.m_iItemDefinitionIndex)
                        WeaponOwner = Memory.Read.int(WeaponAddress + Offsets.Netvars.m_OriginalOwnerXuidLow)

                        Memory.Write.int(WeaponAddress + Offsets.Netvars.m_iItemIDHigh, -1)
                        Memory.Write.int(WeaponAddress + Offsets.Netvars.m_nFallbackPaintKit, SkinChanger.GetWeaponSkin(WeaponID))
                        Memory.Write.int(WeaponAddress + Offsets.Netvars.m_iAccountID, WeaponOwner)
                        Memory.Write.int(WeaponAddress + Offsets.Netvars.m_nFallbackStatTrak, 1337)


                if (win32api.GetAsyncKeyState(0x75)):
                    Memory.Write.int(GameData.EnginePoint + 0x174, -1)

            time.sleep(0.01)