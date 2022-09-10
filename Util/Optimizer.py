from threading import Lock

from Module.Game import *
from Module.Memory import *
from Module.Offsets import *

from Util.GameData import *
from Util.EntityClass import *

import time, win32api, win32gui 

class Optimizer:
    Mutex = Lock()


    class Scan():

        def Low():
            GameData.EnginePoint = Memory.Read.int(Game.Engine + Offsets.Signatures.dwClientState)

            GameData.WindowScreen.x = win32api.GetSystemMetrics(0)
            GameData.WindowScreen.y = win32api.GetSystemMetrics(1)

            while (True):
                Optimizer.Mutex.acquire()

                GameData.LocalPlayer = Memory.Read.int(Game.Client + Offsets.Signatures.dwLocalPlayer)
                GameData.GlowManager = Memory.Read.int(Game.Client + Offsets.Signatures.dwGlowObjectManager)
                GameData.MyTeamList = Memory.Read.int(GameData.LocalPlayer + Offsets.Netvars.m_iTeamNum)

                GameData.GameIsActive = win32gui.GetWindowText(win32gui.GetForegroundWindow()) == "Counter-Strike: Global Offensive - Direct3D 9"

                Optimizer.Mutex.release()
                time.sleep(0.5)


        def Average():
            while (True):
                Optimizer.Mutex.acquire()

                GameData.MouseState = Memory.Read.byte(Game.Client + Offsets.Signatures.dwMouseEnable)

                if (GameData.LocalPlayer):

                    for i in range(len(GameData.ViewMatrix)):
                        GameData.ViewMatrix[i] = Memory.Read.float(Game.Client + Offsets.Signatures.dwViewMatrix + (i * 4))

                    for i in range(1, 32):
                        Entity = Memory.Read.int(Game.Client + Offsets.Signatures.dwEntityList + (i * 0x10))
                        Entity = EntityClass(Entity)
 
                        GameData.EntityList[i] = Entity.EntityObject if (not Entity.Dormant() and Entity.Health() > 0) else 0


                Optimizer.Mutex.release()
                time.sleep(0.02)