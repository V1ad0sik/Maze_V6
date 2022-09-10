from Util.GameData import *
from Util.EntityClass import *
from Module.Memory import *
from Module.Struct import *

import time

class NightMod():
    Status = False
    Value = 1.0


    def Start():
        while (NightMod.Status):
            if (GameData.LocalPlayer):


                for i in range (32, 2048):
                    Entity = Memory.Read.int(Game.Client + Offsets.Signatures.dwEntityList + (i * 0x10))
                    Entity = EntityClass(Entity)

                    if (Entity.ClassID() == 69):
                        Memory.Write.int(Entity.EntityObject + Offsets.Netvars.m_bUseCustomAutoExposureMin, 1)
                        Memory.Write.int(Entity.EntityObject + Offsets.Netvars.m_bUseCustomAutoExposureMax, 1)

                        Memory.Write.float(Entity.EntityObject + Offsets.Netvars.m_flCustomAutoExposureMin, NightMod.Value)
                        Memory.Write.float(Entity.EntityObject + Offsets.Netvars.m_flCustomAutoExposureMax, NightMod.Value)
                
            time.sleep(0.5)


    def Reset():
        if (GameData.LocalPlayer):


            for i in range (32, 2048):
                Entity = Memory.Read.int(Game.Client + Offsets.Signatures.dwEntityList + (i * 0x10))
                Entity = EntityClass(Entity)

                if (Entity.ClassID() == 69):
                    Memory.Write.int(Entity.EntityObject + Offsets.Netvars.m_bUseCustomAutoExposureMin, 1)
                    Memory.Write.int(Entity.EntityObject + Offsets.Netvars.m_bUseCustomAutoExposureMax, 1)

                    Memory.Write.float(Entity.EntityObject + Offsets.Netvars.m_flCustomAutoExposureMin, 1)
                    Memory.Write.float(Entity.EntityObject + Offsets.Netvars.m_flCustomAutoExposureMax, 1)
                
