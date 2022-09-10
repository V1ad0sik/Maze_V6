from Module.Game import *
from Module.Memory import *
from Module.Offsets import *
from Module.Struct import *

from Util.GameData import *

from math import *


class EntityClass():
    EntityObject = 0

    
    def __init__(self, EntityAddres):
        self.EntityObject = EntityAddres


    def Health(self):
        return Memory.Read.int(self.EntityObject + Offsets.Netvars.m_iHealth)


    def ClassID(self):
        EntityClassID = Memory.Read.int(self.EntityObject + 0x8)

        Struct_1 = Memory.Read.int(EntityClassID + 0x8)
        Struct_2 = Memory.Read.int(Struct_1 + 0x1)

        return Memory.Read.int(Struct_2 + 0x14)


    def Distance(self, PlayerPos: Vec3, EntityPos: Vec3):
        return sqrt(pow(PlayerPos.x - EntityPos.x, 2) + pow(PlayerPos.y - EntityPos.y, 2) + pow(PlayerPos.z - EntityPos.z, 2))


    def ActiveWeapon(self):
        ActiveWeapon = Memory.Read.int(self.EntityObject + Offsets.Netvars.m_hActiveWeapon) & 0xFFF
        ActiveWeaponAddress = Memory.Read.int(Game.Client + Offsets.Signatures.dwEntityList + (ActiveWeapon - 1) * 0x10)

        return Memory.Read.short(ActiveWeaponAddress + Offsets.Netvars.m_iItemDefinitionIndex)


    def GlowIndex(self):
        return Memory.Read.int(self.EntityObject + Offsets.Netvars.m_iGlowIndex)


    def BonePos(self, BoneID):
        EntityBonePos = Vec3(0, 0, 0)

        EntityBoneMatrix = Memory.Read.int(self.EntityObject + Offsets.Netvars.m_dwBoneMatrix)

        EntityBonePos.x = Memory.Read.float(EntityBoneMatrix + 0x30 * BoneID + 0xC)
        EntityBonePos.y = Memory.Read.float(EntityBoneMatrix + 0x30 * BoneID + 0x1C)
        EntityBonePos.z = Memory.Read.float(EntityBoneMatrix + 0x30 * BoneID + 0x2C)

        return EntityBonePos


    def OriginPos(self, Aim = False):
        EntityPos = Vec3(0, 0, 0)

        EntityPos.x = Memory.Read.float(self.EntityObject + Offsets.Netvars.m_vecOrigin)
        EntityPos.y = Memory.Read.float(self.EntityObject + Offsets.Netvars.m_vecOrigin + 0x4)
        EntityPos.z = Memory.Read.float(self.EntityObject + Offsets.Netvars.m_vecOrigin + 0x8)

        EntityPos.z += Memory.Read.float(self.EntityObject + Offsets.Netvars.m_vecViewOffset + 0x8) if Aim else 0

        return EntityPos


    def Teammate(self):
        EntityTeamList = Memory.Read.int(self.EntityObject + Offsets.Netvars.m_iTeamNum)

        return GameData.MyTeamList == EntityTeamList


    def Visible(self):
        return Memory.Read.bool(self.EntityObject + Offsets.Netvars.m_bSpotted)


    def LocalPlayer(self):
        return self.EntityObject == GameData.LocalPlayer


    def Scoped(self):
        return Memory.Read.bool(self.EntityObject + Offsets.Netvars.m_bIsScoped)


    def Dormant(self):
        return Memory.Read.bool(self.EntityObject + Offsets.Signatures.m_bDormant)


    def Valid(self):
        return self.EntityObject and not EntityClass.LocalPlayer(self) and EntityClass.Health(self) > 0 and not EntityClass.Dormant(self)