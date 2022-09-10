from Util.GameData import *
from Util.EntityClass import *
from Module.Memory import *
from Module.Struct import *

import time

class Chams():
    Status = False
    TeamCheck = True
    Color = ColorRGB(255, 255, 255)


    def Start():
        while (Chams.Status):
            if (GameData.LocalPlayer):

                for i in range (len(GameData.EntityList)):
                    Entity = EntityClass(GameData.EntityList[i])

                    if (Entity.Valid()):
                        if (Chams.TeamCheck and Entity.Teammate()): continue

                        Memory.Write.int(Entity.EntityObject + Offsets.Netvars.m_clrRender, Chams.Color.R)
                        Memory.Write.int(Entity.EntityObject + Offsets.Netvars.m_clrRender + 0x1, Chams.Color.G)
                        Memory.Write.int(Entity.EntityObject + Offsets.Netvars.m_clrRender + 0x2, Chams.Color.B)


            time.sleep(0.2)


    def Reset():
        if (GameData.LocalPlayer):

            for i in range (len(GameData.EntityList)):
                Entity = EntityClass(GameData.EntityList[i])

                if (Entity.Valid()):
                    Memory.Write.int(Entity.EntityObject + Offsets.Netvars.m_clrRender, 255)
                    Memory.Write.int(Entity.EntityObject + Offsets.Netvars.m_clrRender + 0x1, 255)
                    Memory.Write.int(Entity.EntityObject + Offsets.Netvars.m_clrRender + 0x2, 255)