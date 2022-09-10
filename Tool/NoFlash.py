from Util.GameData import *
from Util.EntityClass import *
from Util.SDK import *
from Module.Memory import *
from Module.Struct import *

import time

class NoFlash():
    Status = False
    Value = 0


    def Start():
        while (NoFlash.Status):
            if (GameData.LocalPlayer):
                Memory.Write.float(GameData.LocalPlayer + Offsets.Netvars.m_flFlashMaxAlpha, NoFlash.Value)

            time.sleep(0.1)
                

    def Reset():
        if (GameData.LocalPlayer):
            Memory.Write.float(GameData.LocalPlayer + Offsets.Netvars.m_flFlashMaxAlpha, 255)