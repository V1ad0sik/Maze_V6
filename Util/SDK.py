from Util.GameData import *
from Util.EntityClass import *
from Module.Memory import *
from Module.Struct import *


class SDK():
    class Weapon():
        Item = 0

        def __init__(self, WeaponID):
            self.Item = WeaponID


        def IsGun(self):
            return True if self.Item in [1, 2, 3, 4, 7, 8, 9, 10, 11, 13, 14, 16, 17, 19, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40, 60, 61, 63, 64] else False

        
        def IsKnife(self):
            return True if self.Item in [42, 59] else False

        
        def IsPistol(self):
            return True if self.Item in [1, 2, 3, 4, 30, 32, 36, 61] else False

    

    def WorldToScreen(BonePos: Vec3, ViewMatrix: list):
        Matrix = VecMatrix()
        NDC, BonePosWTS = Vec2(), Vec2()

        Matrix.x = BonePos.x * ViewMatrix[0] + BonePos.y * ViewMatrix[1] + BonePos.z * ViewMatrix[2] + ViewMatrix[3]
        Matrix.y = BonePos.x * ViewMatrix[4] + BonePos.y * ViewMatrix[5] + BonePos.z * ViewMatrix[6] + ViewMatrix[7]
        Matrix.w = BonePos.x * ViewMatrix[12] + BonePos.y * ViewMatrix[13] + BonePos.z * ViewMatrix[14] + ViewMatrix[15]

        if (Matrix.w > 0.001):
            NDC.x = Matrix.x / Matrix.w
            NDC.y = Matrix.y / Matrix.w
            
            BonePosWTS.x = (GameData.WindowScreen.x / 2 * NDC.x) + (NDC.x + GameData.WindowScreen.x / 2)
            BonePosWTS.y = -(GameData.WindowScreen.y / 2 * NDC.y) + (NDC.y + GameData.WindowScreen.y / 2)


        return BonePosWTS
