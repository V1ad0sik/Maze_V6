from Util.GameData import *
from Util.EntityClass import *
from Util.SDK import *
from Module.Memory import *
from Module.Struct import *

import time, win32api

class AimBot():
    Status = False
    TeamCheck = True
    Visible = False
    Neares = False

    Fov = 90
    Smooth = 1
    Bone = 8

    Key = 1


    def GetDistanceFromCenter(BonePos: Vec2, WindowScreen: Vec2, Fov):
        Distance = Vec2()

        Distance.x = BonePos.x - (WindowScreen.x / 2)
        Distance.y = BonePos.y - (WindowScreen.y / 2)

        return Fov * Fov - (Distance.x * Distance.x + Distance.y * Distance.y)


    def GetAngle(LocalPlayerPos: Vec3, EntityPos: Vec3):
        BonePos = Vec2()
        Delta = Vec3()

        Delta.x = EntityPos.x - LocalPlayerPos.x
        Delta.y = EntityPos.y - LocalPlayerPos.y
        Delta.z = EntityPos.z - LocalPlayerPos.z

        DeltaVectorLength = sqrt(Delta.x * Delta.x + Delta.y * Delta.y + Delta.z * Delta.z)

        BonePos.x = -asin(Delta.z / DeltaVectorLength) * 57.28
        BonePos.y = atan2(Delta.y, Delta.x) * 57.28

        return BonePos


    def GetBestTarger():
        BestTarger = 0
        BestDistance = 0

        for i in range(len(GameData.EntityList)):
            Entity = EntityClass(GameData.EntityList[i])

            if (Entity.Valid()):
                if ((AimBot.TeamCheck and Entity.Teammate()) or (AimBot.Visible and not(Entity.Visible()))):
                    continue

                EntityWorldToScreen = SDK.WorldToScreen(Entity.BonePos(AimBot.Bone), GameData.ViewMatrix)

                if (EntityWorldToScreen.x > 0 and EntityWorldToScreen.y > 0):
                    Distance = AimBot.GetDistanceFromCenter(EntityWorldToScreen, GameData.WindowScreen, AimBot.Fov)

                    if (BestDistance < Distance and Distance > 0):
                        BestTarger = Entity.EntityObject
                        BestDistance = Distance

        return BestTarger


    def GetBestBone(Entity: EntityClass):
        Bone = [8, 6, 5, 4, 3, 0]
        BestDistance = 0
        BestBone = None

        for i in range(len(Bone)):
            EntityWorldToScreen = SDK.WorldToScreen(Entity.BonePos(Bone[i]), GameData.ViewMatrix)

            if (EntityWorldToScreen.x > 0 and EntityWorldToScreen.y > 0):
                Distance = AimBot.GetDistanceFromCenter(EntityWorldToScreen, GameData.WindowScreen, 180)

                if (BestDistance < Distance and Distance > 0):
                    BestDistance = Distance
                    BestBone = Bone[i]

        return BestBone


    def Start():
        while (AimBot.Status):
            if (GameData.LocalPlayer):
                time.sleep(0.02)

                if (AimBot.Key != 0):
                    if (not(win32api.GetAsyncKeyState(AimBot.Key) and GameData.GameIsActive) and (GameData.MouseState == Offsets.Signatures.dwMouseIndexNoActive)):
                        continue

                Player = EntityClass(GameData.LocalPlayer)
                Weapon = SDK.Weapon(Player.ActiveWeapon())

                if (Player.EntityObject and Weapon.IsGun()):
                    Entity = EntityClass(AimBot.GetBestTarger())

                    if (Entity.Valid()):
                        BonePos, ViewAngle = Vec2(),  Vec2()

                        if (AimBot.Neares):
                            BonePos = AimBot.GetAngle(Player.OriginPos(Aim = True), Entity.BonePos(AimBot.GetBestBone(Entity)))

                        else:
                            BonePos = AimBot.GetAngle(Player.OriginPos(Aim = True), Entity.BonePos(AimBot.Bone))


                        ViewAngle.x = Memory.Read.float(GameData.EnginePoint + Offsets.Signatures.dwClientState_ViewAngles)
                        ViewAngle.y = Memory.Read.float(GameData.EnginePoint + Offsets.Signatures.dwClientState_ViewAngles + 0x4)

                        Memory.Write.float(GameData.EnginePoint + Offsets.Signatures.dwClientState_ViewAngles, ViewAngle.x + ((BonePos.x - ViewAngle.x) / AimBot.Smooth))
                        Memory.Write.float(GameData.EnginePoint + Offsets.Signatures.dwClientState_ViewAngles + 0x4, ViewAngle.y + ((BonePos.y - ViewAngle.y) / AimBot.Smooth))
