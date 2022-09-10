from Util.GameData import *
from Util.EntityClass import *
from Module.Memory import *
from Module.Struct import *

import time

class FovChanger():
    Status = False
    Fov = 90


    def Start():
        while (FovChanger.Status):
            if (GameData.LocalPlayer):
                Memory.Write.int(GameData.LocalPlayer + Offsets.Netvars.m_iDefaultFOV, FovChanger.Fov)
            
            time.sleep(0.05)


    def Reset():
        if (GameData.LocalPlayer):
            Memory.Write.int(GameData.LocalPlayer + Offsets.Netvars.m_iDefaultFOV, 90)

