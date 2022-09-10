import Util.SkinList as SkinList

from Module.Struct import *

from Menu.UI import *
from Menu.UiSDK import *

from Tool.GlowESP import *
from Tool.GlowESPHealth import *
from Tool.Chams import *
from Tool.NightMod import *
from Tool.FovChanger import *
from Tool.AimBot import *
from Tool.TriggerBot import *
from Tool.AutoPistol import *
from Tool.Brightness import *
from Tool.BunnyHop import *
from Tool.ShowMoney import *
from Tool.GlobalWallHack import *
from Tool.NoFlash import *
from Tool.SkinChanger import *

import json


def GetSkinList(Gun):
    return SkinList.List[Gun].keys()

def GetSkinId(Gun, Skin):
    return SkinList.List[Gun][Skin]

def GetSkinName(SkinId, Gun):
    Name = {value: key for key, value in SkinList.List[Gun].items()}
    return Name[SkinId]



def Save():
    Config = {
        "GlowESP":
        {
            "Status": GlowESP.Status,
            "Team": GlowESP.TeamCheck,
            "Color": 
            {
                "R": GlowESP.Color.R,
                "G": GlowESP.Color.G,
                "B": GlowESP.Color.B
            },

            "Thickness": GlowESP.Line
        },

        "GlowESPHealth":
        {
            "Status": GlowESPHealth.Status,
            "Team": GlowESPHealth.TeamCheck,
            "Thickness": GlowESPHealth.Line
        },

        "Chams":
        {
            "Status": Chams.Status,
            "Team": Chams.TeamCheck,
            "Color": 
            {
                "R": Chams.Color.R,
                "G": Chams.Color.G,
                "B": Chams.Color.B
            }
        },

        "NightMod":
        {
            "Status": NightMod.Status,
            "Light": NightMod.Value
        },

        "PlayerFOV":
        {
            "Status": FovChanger.Status,
            "FOV": FovChanger.Fov
        },

        "AimBot":
        {
            "Status": AimBot.Status,
            "Team": AimBot.TeamCheck,
            "OnliVisible": AimBot.Visible,
            "BestBone": AimBot.Neares,
            "Smooth": AimBot.Smooth,
            "FOV": AimBot.Fov,
            "Bone": AimBot.Bone,
            "Mouse": AimBot.Key
        },

        "TriggerBot":
        {
            "Status": TriggerBot.Status,
            "Team": TriggerBot.TeamCheck,
            "Delay": TriggerBot.Delay,
            "Key": TriggerBot.Key
        },

        "Misc":
        {
            "AutoPistol": AutoPistol.Status,
            "Brightness": Brightness.Status,
            "BunnyHop": BunnyHop.Status,
            "NoFlash": NoFlash.Status,
            "Flashing": NoFlash.Value
        },

        "Skinchanger":
        {
            "Status": SkinChanger.Status,
            "Skins": SkinChanger.GunList
        }

    }

    File = open("Setting\Setting.json", "w")
    File.write(json.dumps(Config))
    File.close()


def Load(ui):
    File = open("Setting\Setting.json", "r")
    Config = json.loads(File.read())
    File.close()

    GlowESP.Status = Config["GlowESP"]["Status"]
    GlowESP.TeamCheck = Config["GlowESP"]["Team"]
    GlowESP.Line = Config["GlowESP"]["Thickness"]
    GlowESP.Color = ColorRGB(Config["GlowESP"]["Color"]["R"], Config["GlowESP"]["Color"]["G"], Config["GlowESP"]["Color"]["B"])

    ui.checkBox.setChecked(GlowESP.Status)
    ui.checkBox_2.setChecked(GlowESP.TeamCheck)

    GlowESP.Color = SetColorForColorEdit(ui.colorEdit, GlowESP.Color)

    ui.slider.setValue(int(GlowESP.Line * 10))
    GlowESP.Line = Slider(ui.slider, ui.counter, 0.1, 1)


    GlowESPHealth.Status = Config["GlowESPHealth"]["Status"]
    GlowESPHealth.TeamCheck = Config["GlowESPHealth"]["Team"]
    GlowESPHealth.Line = Config["GlowESPHealth"]["Thickness"]

    ui.checkBox_3.setChecked(GlowESPHealth.Status)
    ui.checkBox_4.setChecked(GlowESPHealth.TeamCheck)

    ui.slider_2.setValue(int(GlowESPHealth.Line * 10))
    GlowESPHealth.Line = Slider(ui.slider_2, ui.counter_2, 0.1, 1)

    
    Chams.Status = Config["Chams"]["Status"]
    Chams.TeamCheck = Config["Chams"]["Team"]
    Chams.Color = ColorRGB(Config["Chams"]["Color"]["R"], Config["Chams"]["Color"]["G"], Config["Chams"]["Color"]["B"])

    ui.checkBox_5.setChecked(Chams.Status)
    ui.checkBox_6.setChecked(Chams.TeamCheck)

    Chams.Color = SetColorForColorEdit(ui.colorEdit_2, Chams.Color)


    NightMod.Status = Config["NightMod"]["Status"]
    NightMod.Value = Config["NightMod"]["Light"]

    ui.checkBox_7.setChecked(NightMod.Status)

    ui.slider_3.setValue(int(NightMod.Value * 100))
    NightMod.Value = Slider(ui.slider_3, ui.counter_3, 0.01, 2)



    FovChanger.Status = Config["PlayerFOV"]["Status"]
    FovChanger.Fov = Config["PlayerFOV"]["FOV"]

    ui.checkBox_8.setChecked(FovChanger.Status)

    ui.slider_4.setValue(FovChanger.Fov)
    Slider(ui.slider_4, ui.counter_4, 1, 0)



    AimBot.Status = Config["AimBot"]["Status"]
    AimBot.TeamCheck = Config["AimBot"]["Team"]
    AimBot.Visible = Config["AimBot"]["OnliVisible"]
    AimBot.Neares = Config["AimBot"]["BestBone"]

    AimBot.Smooth = Config["AimBot"]["Smooth"]
    AimBot.Fov = Config["AimBot"]["FOV"]

    AimBot.Bone = Config["AimBot"]["Bone"]
    AimBot.Key = Config["AimBot"]["Mouse"]

    ui.checkBox_10.setChecked(AimBot.Status)
    ui.checkBox_11.setChecked(AimBot.TeamCheck)
    ui.checkBox_12.setChecked(AimBot.Visible)
    ui.checkBox_13.setChecked(AimBot.Neares)

    ui.slider_5.setValue(AimBot.Fov)
    Slider(ui.slider_5, ui.counter_5, 1, 0)

    ui.slider_6.setValue(AimBot.Smooth)
    Slider(ui.slider_6, ui.counter_6, 1, 0)

    Bone = ""

    if (AimBot.Bone == 8): Bone = "Head"
    if (AimBot.Bone == 9): Bone = "Neck"
    if (AimBot.Bone == 6): Bone = "Chest"
    if (AimBot.Bone == 3): Bone = "Stomach"
    if (AimBot.Bone == 0): Bone = "Pelvis"

    ui.comboBox.setCurrentText(Bone)

    Key = ""

    if (AimBot.Key == 1): Key = "M1"
    if (AimBot.Key == 2): Key = "M2"
    if (AimBot.Key == 3): Key = "M3"
    if (AimBot.Key == 4): Key = "M4"
    if (AimBot.Key == 5): Key = "M5"
    if (AimBot.Key == 6): Key = "M6"
    if (AimBot.Key == 0): Key = "None"

    ui.comboBox_4.setCurrentText(Key)


    TriggerBot.Status = Config["TriggerBot"]["Status"]
    TriggerBot.TeamCheck = Config["TriggerBot"]["Team"]
    TriggerBot.Delay = Config["TriggerBot"]["Delay"]
    TriggerBot.Key = Config["TriggerBot"]["Key"]

    ui.slider_7.setValue(int(TriggerBot.Delay * 100))
    Slider(ui.slider_7, ui.counter_7, 0.1, 2)

    if (TriggerBot.Key == 1): Key = "M1"
    if (TriggerBot.Key == 2): Key = "M2"
    if (TriggerBot.Key == 3): Key = "M3"
    if (TriggerBot.Key == 4): Key = "M4"
    if (TriggerBot.Key == 5): Key = "M5"
    if (TriggerBot.Key == 6): Key = "M6"
    if (TriggerBot.Key == 0): Key = "None"

    ui.comboBox_5.setCurrentText(Key)


    AutoPistol.Status = Config["Misc"]["AutoPistol"]
    ui.checkBox_16.setChecked(AutoPistol.Status)

    Brightness.Status = Config["Misc"]["Brightness"]
    ui.checkBox_17.setChecked(Brightness.Status)

    BunnyHop.Status = Config["Misc"]["BunnyHop"]
    ui.checkBox_18.setChecked(BunnyHop.Status)

    NoFlash.Status = Config["Misc"]["NoFlash"]
    NoFlash.Value = Config["Misc"]["Flashing"]
    ui.checkBox_20.setChecked(NoFlash.Status)

    ui.slider_8.setValue(NoFlash.Value)
    Slider(ui.slider_8, ui.counter_8, 1, 0)

    SkinChanger.Status = Config["Skinchanger"]["Status"]
    SkinChanger.GunList = Config["Skinchanger"]["Skins"]

    ui.checkBox_21.setChecked(SkinChanger.Status)