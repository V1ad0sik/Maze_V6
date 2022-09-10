from Util.GameData import *
from Util.EntityClass import *
from Util.SDK import *
from Module.Memory import *
from Module.Struct import *

import time, win32api

class BunnyHop():
    Status = False


    def Start():
        while (BunnyHop.Status):
            if (GameData.GameIsActive):
                if (GameData.LocalPlayer and win32api.GetAsyncKeyState(0x20)):
                    if (GameData.MouseState == Offsets.Signatures.dwMouseIndexNoActive):

                        PlayerFlag = Memory.Read.int(GameData.LocalPlayer + Offsets.Netvars.m_fFlags)

                        if (PlayerFlag == 257 or PlayerFlag == 263):
                            Memory.Write.int(Game.Client + Offsets.Signatures.dwForceJump, 6)

            time.sleep(0.002)