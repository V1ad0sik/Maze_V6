from Util.GameData import *
from Util.EntityClass import *
from Module.Memory import *
from Module.Struct import *

import time

class GlowESPHealth():
    Status = False
    TeamCheck = True

    Line = 0.6

    def Start():
        while (GlowESPHealth.Status):
            if (GameData.LocalPlayer):

                for i in range (len(GameData.EntityList)):
                    Entity = EntityClass(GameData.EntityList[i])

                    if (Entity.Valid()):
                        if (GlowESPHealth.TeamCheck and Entity.Teammate()): continue

                        Health = Entity.Health()

                        if (Health >= 60):                   Color = ColorRGB(0, 255, 0)
                        if (Health < 60 and Health >= 25):   Color = ColorRGB(255, 255, 0)
                        if (Health < 25):                    Color = ColorRGB(255, 0, 0)

                        Memory.Write.float(GameData.GlowManager + Entity.GlowIndex() * 0x38 + 0x8, Color.R / 255)
                        Memory.Write.float(GameData.GlowManager + Entity.GlowIndex() * 0x38 + 0xC, Color.G / 255)
                        Memory.Write.float(GameData.GlowManager + Entity.GlowIndex() * 0x38 + 0x10, Color.B / 255)
                        Memory.Write.float(GameData.GlowManager + Entity.GlowIndex() * 0x38 + 0x14, GlowESPHealth.Line)

                        Memory.Write.bool(GameData.GlowManager + Entity.GlowIndex() * 0x38 + 0x28, True)

            time.sleep(0.05)