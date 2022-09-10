from Util.GameData import *
from Util.EntityClass import *
from Module.Memory import *
from Module.Struct import *

import time, win32api

class TriggerBot():
    Status = True
    TeamCheck = True

    Key = 1
    Delay = 0.12


    def GunIsValidForTriggetBot(Player: EntityClass):
        return True if Player.ActiveWeapon() in [1, 2, 3, 4, 7, 8, 9, 10, 11, 13, 14, 16, 17, 19, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40, 60, 61, 63] else False


    def GunIsValidForSniper(Player: EntityClass):
        return Player.Scoped() if Player.ActiveWeapon() in [9, 11, 38, 40] else True

    
    def GetTarger(Player: EntityClass):
        EntityID = Memory.Read.int(Player.EntityObject + Offsets.Netvars.m_iCrosshairId)

        Entity = Memory.Read.int(Game.Client + Offsets.Signatures.dwEntityList + (EntityID - 1) * 0x10)
        Entity = EntityClass(Entity)

        if (Entity.Valid()):
            if (TriggerBot.TeamCheck and Entity.Teammate()):
                return False

            return EntityID > 0 and EntityID <= 64

        return False


    def Start():
        while (TriggerBot.Status):
            Player = EntityClass(GameData.LocalPlayer)

            if (Player.EntityObject and TriggerBot.GunIsValidForTriggetBot(Player) and TriggerBot.GunIsValidForSniper(Player)):
                if TriggerBot.Key != 0 and (not (win32api.GetAsyncKeyState(TriggerBot.Key))):
                    continue

                if (GameData.GameIsActive and TriggerBot.GetTarger(Player)):
                    time.sleep(TriggerBot.Delay)

                    if (TriggerBot.GetTarger(Player)):
                        Memory.Write.int(Game.Client + Offsets.Signatures.dwForceAttack, 6)

            time.sleep(0.05)