from Util.GameData import *
from Util.EntityClass import *
from Module.Memory import *
from Module.Struct import *

import time

class Brightness():
    Status = False


    def Start():
        while (Brightness.Status):
            if (GameData.LocalPlayer):
                Memory.Write.int(Game.Engine + Offsets.Signatures.model_ambient_min, 1)
            
            time.sleep(0.5)


    def Reset():
        if (GameData.LocalPlayer):
            Memory.Write.int(Game.Engine + Offsets.Signatures.model_ambient_min, -1)

