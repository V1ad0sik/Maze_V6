from Util.GameData import *
from Util.EntityClass import *
from Module.Memory import *
from Module.Struct import *

import time

class GlowESP():
    Status = False
    TeamCheck = True

    Color = ColorRGB(255, 255, 255)
    Line = 0.6


    def Start():
        while (GlowESP.Status):
            if (GameData.LocalPlayer):
                for i in range (len(GameData.EntityList)):
                    Entity = EntityClass(GameData.EntityList[i])

                    if (Entity.Valid()):
                        if (GlowESP.TeamCheck and Entity.Teammate()): continue

                        Memory.Write.float(GameData.GlowManager + Entity.GlowIndex() * 0x38 + 0x8, GlowESP.Color.R / 255)
                        Memory.Write.float(GameData.GlowManager + Entity.GlowIndex() * 0x38 + 0xC, GlowESP.Color.G / 255)
                        Memory.Write.float(GameData.GlowManager + Entity.GlowIndex() * 0x38 + 0x10, GlowESP.Color.B / 255)
                        Memory.Write.float(GameData.GlowManager + Entity.GlowIndex() * 0x38 + 0x14, GlowESP.Line)

                        Memory.Write.bool(GameData.GlowManager + Entity.GlowIndex() * 0x38 + 0x28, True)

            time.sleep(0.05)