from Util.GameData import *
from Util.EntityClass import *
from Util.SDK import *
from Module.Memory import *
from Module.Struct import *

import time, win32api

class AutoPistol():
    Status = False


    def Start():
        while (AutoPistol.Status):
            Player = EntityClass(GameData.LocalPlayer)
            Weapon = SDK.Weapon(Player.ActiveWeapon())

            if (win32api.GetAsyncKeyState(1) and GameData.GameIsActive and GameData.MouseState == Offsets.Signatures.dwMouseIndexNoActive and Player.EntityObject and Weapon.IsPistol()):
                Memory.Write.int(Game.Client + Offsets.Signatures.dwForceAttack, 6)

            time.sleep(0.025)