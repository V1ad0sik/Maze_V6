from Module.Offsets import *
from Module.Game import *
from Module.Memory import *
from pymem import *
from re import *

import requests


class GameAddress():
    Game = 0


    def PatternScanner(Module, Pattern, Extra = 0, Offset = 0, Relative = True):
        ModuleObject = pymem.process.module_from_name(Game.Handle, Module)
        Bytes = GameAddress.Game.read_bytes(ModuleObject.lpBaseOfDll, ModuleObject.SizeOfImage)
        Address = search(Pattern, Bytes).start()

        return GameAddress.Game.read_int(ModuleObject.lpBaseOfDll + Address + Offset) + Extra - ModuleObject.lpBaseOfDll if Relative else GameAddress.Game.read_int(ModuleObject.lpBaseOfDll + Address + Offset) + Extra


    def Update():
        GameAddress.Game = Pymem("csgo.exe")

        Offsets.Signatures.dwEntityList = GameAddress.PatternScanner("client.dll", rb"\xBB....\x83\xFF\x01\x0F\x8C....\x3B\xF8", 0, 1)
        Offsets.Signatures.dwLocalPlayer = GameAddress.PatternScanner("client.dll", rb"\x8D\x34\x85....\x89\x15....\x8B\x41\x08\x8B\x48\x04\x83\xF9\xFF", 4, 3)
        Offsets.Signatures.m_bDormant = GameAddress.PatternScanner("client.dll", rb"\x8A\x81....\xC3\x32\xC0", 8, 2, 0)
        Offsets.Signatures.dwMouseEnable = GameAddress.PatternScanner("client.dll", rb"\xB9....\xFF\x50\x34\x85\xC0\x75\x10", 48, 1)
        Offsets.Signatures.dwViewMatrix = GameAddress.PatternScanner("client.dll", rb"\x0F\x10\x05....\x8D\x85....\xB9", 176, 3)
        Offsets.Signatures.dwClientState = GameAddress.PatternScanner("engine.dll", rb"\xA1....\x33\xD2\x6A\x00\x6A\x00\x33\xC9\x89\xB0", 0, 1)
        Offsets.Signatures.dwGlowObjectManager = GameAddress.PatternScanner("client.dll", rb"\xA1....\xA8\x01\x75\x4B", 4, 1)
        Offsets.Signatures.model_ambient_min = GameAddress.PatternScanner("engine.dll", rb"\xF3\x0F\x10\x0D....\xF3\x0F\x11\x4C\x24.\x8B\x44\x24\x20\x35....\x89\x44\x24\x0C", 0, 4)
        Offsets.Signatures.dwClientState_ViewAngles = GameAddress.PatternScanner("engine.dll", rb"\xF3\x0F\x11\x86....\xF3\x0F\x10\x44\x24.\xF3\x0F\x11\x86", 0, 4, 0)
        Offsets.Signatures.dwForceAttack = GameAddress.PatternScanner("client.dll", rb"\x89\x0D....\x8B\x0D....\x8B\xF2\x8B\xC1\x83\xCE\x04", 0, 2)
        Offsets.Signatures.dwForceJump = GameAddress.PatternScanner("client.dll", rb"\x8B\x0D....\x8B\xD6\x8B\xC1\x83\xCA\x02", 0, 2)
        Offsets.Signatures.dwMouseIndexNoActive = Memory.Read.byte(Game.Client + Offsets.Signatures.dwMouseEnable) + 1

        Hazedumper = requests.get("https://raw.githubusercontent.com/frk1/hazedumper/master/csgo.json").json()

        Offsets.Netvars.m_iHealth = Hazedumper["netvars"]["m_iHealth"]
        Offsets.Netvars.m_hActiveWeapon = Hazedumper["netvars"]["m_hActiveWeapon"]
        Offsets.Netvars.m_iItemDefinitionIndex = Hazedumper["netvars"]["m_iItemDefinitionIndex"]
        Offsets.Netvars.m_iGlowIndex = Hazedumper["netvars"]["m_iGlowIndex"]
        Offsets.Netvars.m_dwBoneMatrix = Hazedumper["netvars"]["m_dwBoneMatrix"]
        Offsets.Netvars.m_vecOrigin = Hazedumper["netvars"]["m_vecOrigin"]
        Offsets.Netvars.m_vecViewOffset = Hazedumper["netvars"]["m_vecViewOffset"]
        Offsets.Netvars.m_iTeamNum = Hazedumper["netvars"]["m_iTeamNum"]
        Offsets.Netvars.m_bSpotted = Hazedumper["netvars"]["m_bSpotted"]
        Offsets.Netvars.m_bIsScoped = Hazedumper["netvars"]["m_bIsScoped"]
        Offsets.Netvars.m_clrRender = Hazedumper["netvars"]["m_clrRender"]
        Offsets.Netvars.m_bUseCustomAutoExposureMin = Hazedumper["netvars"]["m_bUseCustomAutoExposureMin"]
        Offsets.Netvars.m_bUseCustomAutoExposureMax = Hazedumper["netvars"]["m_bUseCustomAutoExposureMax"]
        Offsets.Netvars.m_flCustomAutoExposureMin = Hazedumper["netvars"]["m_flCustomAutoExposureMin"]
        Offsets.Netvars.m_flCustomAutoExposureMax = Hazedumper["netvars"]["m_flCustomAutoExposureMax"]
        Offsets.Netvars.m_iDefaultFOV = Hazedumper["netvars"]["m_iDefaultFOV"]
        Offsets.Netvars.m_iCrosshairId = Hazedumper["netvars"]["m_iCrosshairId"]
        Offsets.Netvars.m_hMyWeapons = Hazedumper["netvars"]["m_hMyWeapons"]
        Offsets.Netvars.m_OriginalOwnerXuidLow = Hazedumper["netvars"]["m_OriginalOwnerXuidLow"]
        Offsets.Netvars.m_iItemIDHigh = Hazedumper["netvars"]["m_iItemIDHigh"]
        Offsets.Netvars.m_nFallbackPaintKit = Hazedumper["netvars"]["m_nFallbackPaintKit"]
        Offsets.Netvars.m_iAccountID = Hazedumper["netvars"]["m_iAccountID"]
        Offsets.Netvars.m_nFallbackStatTrak = Hazedumper["netvars"]["m_nFallbackStatTrak"]
        Offsets.Netvars.m_fFlags = Hazedumper["netvars"]["m_fFlags"]
        Offsets.Netvars.m_flFlashMaxAlpha = Hazedumper["netvars"]["m_flFlashMaxAlpha"]