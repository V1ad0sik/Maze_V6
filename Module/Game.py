import psutil, ctypes
from Module.Module import *

class Game():
    ProcessID, Client, Engine = 0, 0, 0
    Handle = 0


    def GetProcessID(Name):
        for Process in psutil.process_iter():
            if Process.name() == Name:
                return Process.pid


    def Connect(Name):
        Game.ProcessID   = Game.GetProcessID(Name)

        if (Game.ProcessID):
            Game.Client  = Module.GetModuleAddress(Game.ProcessID, "client.dll")
            Game.Engine  = Module.GetModuleAddress(Game.ProcessID, "engine.dll")
            Game.Handle  = ctypes.windll.kernel32.OpenProcess(0x1F0FFF, False, Game.ProcessID)

        return Game.ProcessID