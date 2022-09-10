from Menu.UI import *
from Menu.UiSDK import *

from Module.Game import *
from Module.Struct import *

from Util.GameAddress import *
from Util.Optimizer import *
from Util.Setting import *
from Util.MessageBox import *

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

import sys, os, signal, threading

if __name__ == "__main__":
   app = QtWidgets.QApplication(sys.argv)
   ui = Widget()
   ui.show()

   def Start():
        print("Search csgo.exe")

        if (Game.Connect("csgo.exe")):
          print("Getting offsets...")
          GameAddress.Update()

          print("Starting services...")
          threading.Thread(target = Optimizer.Scan.Low).start()
          threading.Thread(target = Optimizer.Scan.Average).start()

          Load(ui) 
          Skinchanger_SetSkin()

          print("Maze ready to use :)")

        
        else:
          MessageBox("csgo.exe not found")
          os.kill(os.getpid(), signal.SIGTERM)




   def GlowESP_Start():
        GlowESP.Status = ui.checkBox.isChecked()
        threading.Thread(target = GlowESP.Start).start() if GlowESP.Status else pow(0, 0)

   def GlowESP_ColorEdit():  GlowESP.Color = ColorEdit(ui.colorEdit, GlowESP.Color)
   def GlowESP_Team():       GlowESP.TeamCheck = ui.checkBox_2.isChecked()
   def GlowESP_Slider():     GlowESP.Line = Slider(ui.slider, ui.counter, 0.1, 1)



   def GlowESPHealth_Start():
        GlowESPHealth.Status = ui.checkBox_3.isChecked()
        threading.Thread(target = GlowESPHealth.Start).start() if GlowESPHealth.Status else pow(0, 0)

   def GlowESPHealth_Team():    GlowESPHealth.TeamCheck = ui.checkBox_4.isChecked()
   def GlowESPHealth_Slider():  GlowESPHealth.Line = Slider(ui.slider_2, ui.counter_2, 0.1, 1)



   def Chams_Start():
        Chams.Status = ui.checkBox_5.isChecked()
        threading.Thread(target = Chams.Start).start() if Chams.Status else threading.Thread(target = Chams.Reset).start()

   def Chams_Team():       Chams.TeamCheck = ui.checkBox_6.isChecked()
   def Chams_ColorEdit():  Chams.Color = ColorEdit(ui.colorEdit_2, Chams.Color)



   def NightMod_Start():
        NightMod.Status = ui.checkBox_7.isChecked()
        threading.Thread(target = NightMod.Start).start() if NightMod.Status else threading.Thread(target = NightMod.Reset).start()

   def NightMod_Slider(): NightMod.Value = Slider(ui.slider_3, ui.counter_3, 0.01, 2)



   def FOVChanger_Start():
        FovChanger.Status = ui.checkBox_8.isChecked()
        threading.Thread(target = FovChanger.Start).start() if FovChanger.Status else threading.Thread(target = FovChanger.Reset).start()

   def FOVChanger_Slider(): FovChanger.Fov = Slider(ui.slider_4, ui.counter_4, 1, 0)



   def AimBot_Start():
    AimBot.Status = ui.checkBox_10.isChecked()
    threading.Thread(target = AimBot.Start).start() if AimBot.Status else pow(0, 0)

   def AimBot_Team():         AimBot.TeamCheck = ui.checkBox_11.isChecked()
   def AimBot_Visible():      AimBot.Visible = ui.checkBox_12.isChecked()
   def AimBot_BestBone():     AimBot.Neares = ui.checkBox_13.isChecked()
   def AimBot_FOVSlider():    AimBot.Fov = Slider(ui.slider_5, ui.counter_5, 1, 0)
   def AimBot_SmoothSlider(): AimBot.Smooth = Slider(ui.slider_6, ui.counter_6, 1, 0)

   def AimBot_Bone():
     Bone = ui.comboBox.currentText()

     if (Bone == "Head"): AimBot.Bone = 9
     if (Bone == "Neck"): AimBot.Bone = 8
     if (Bone == "Chest"): AimBot.Bone = 6
     if (Bone == "Stomach"): AimBot.Bone = 3
     if (Bone == "Pelvis"): AimBot.Bone = 0

   def AimBot_Mouse():
     Key = ui.comboBox_4.currentText()

     if (Key == "M1"): AimBot.Key = 1
     if (Key == "M2"): AimBot.Key = 2
     if (Key == "M3"): AimBot.Key = 3
     if (Key == "M4"): AimBot.Key = 4
     if (Key == "M5"): AimBot.Key = 5
     if (Key == "M6"): AimBot.Key = 6
     if (Key == "None"): AimBot.Key = 0



   def TriggerBot_Start():
    TriggerBot.Status = ui.checkBox_14.isChecked()
    threading.Thread(target = TriggerBot.Start).start() if TriggerBot.Status else pow(0, 0)


   def TriggerBot_Team():         TriggerBot.TeamCheck = ui.checkBox_15.isChecked()
   def TriggerBot_Slider():       TriggerBot.Delay = Slider(ui.slider_7, ui.counter_7, 0.01, 2)

   def TriggerBot_Mouse():
     Key = ui.comboBox_5.currentText()

     if (Key == "M1"): TriggerBot.Key = 1
     if (Key == "M2"): TriggerBot.Key = 2
     if (Key == "M3"): TriggerBot.Key = 3
     if (Key == "M4"): TriggerBot.Key = 4
     if (Key == "M5"): TriggerBot.Key = 5
     if (Key == "M6"): TriggerBot.Key = 6
     if (Key == "None"): TriggerBot.Key = 0


   def AutoPistol_Start():
    AutoPistol.Status = ui.checkBox_16.isChecked()
    threading.Thread(target = AutoPistol.Start).start() if AutoPistol.Status else pow(0, 0)


   def Brightness_Start():
    Brightness.Status = ui.checkBox_17.isChecked()
    threading.Thread(target = Brightness.Start).start() if Brightness.Status else threading.Thread(target = Brightness.Reset).start()


   def BunnyHop_Start():
    BunnyHop.Status = ui.checkBox_18.isChecked()
    threading.Thread(target = BunnyHop.Start).start() if BunnyHop.Status else pow(0, 0)


   def NoFlash_Start():
    NoFlash.Status = ui.checkBox_20.isChecked()
    threading.Thread(target = NoFlash.Start).start() if NoFlash.Status else threading.Thread(target = NoFlash.Reset).start()

   def NoFlash_Slider():  NoFlash.Value = Slider(ui.slider_8, ui.counter_8, 1, 0)



   def Skinchanger_Start():
    SkinChanger.Status = ui.checkBox_21.isChecked()
    threading.Thread(target = SkinChanger.Start).start() if SkinChanger.Status else pow(0, 0)

   def Skinchanger_SetSkin():
     Gun = ui.comboBox_2.currentText()
     ui.comboBox_3.clear()
     ui.comboBox_3.addItems(list(GetSkinList(Gun)))
     ui.comboBox_3.setCurrentText(GetSkinName(SkinChanger.GunList[ui.comboBox_2.currentText()]["Skin"], ui.comboBox_2.currentText()))


   def Skinchanger_Id():
     Gun = ui.comboBox_2.currentText()
     Skin = ui.comboBox_3.currentText()

     if (Gun and Skin):
          SkinChanger.GunList[Gun]["Skin"] = GetSkinId(Gun, Skin)

     ui.comboBox_3.setCurrentText(GetSkinName(SkinChanger.GunList[Gun]["Skin"], ui.comboBox_2.currentText()))


   ui.checkBox.stateChanged.connect(GlowESP_Start)
   ui.colorEdit.clicked.connect(GlowESP_ColorEdit)
   ui.checkBox_2.stateChanged.connect(GlowESP_Team)
   ui.slider.valueChanged.connect(GlowESP_Slider)


   ui.checkBox_3.stateChanged.connect(GlowESPHealth_Start)
   ui.checkBox_4.stateChanged.connect(GlowESPHealth_Team)
   ui.slider_2.valueChanged.connect(GlowESPHealth_Slider)


   ui.checkBox_5.stateChanged.connect(Chams_Start)
   ui.colorEdit_2.clicked.connect(Chams_ColorEdit)
   ui.checkBox_6.clicked.connect(Chams_Team)


   ui.checkBox_7.stateChanged.connect(NightMod_Start)
   ui.slider_3.valueChanged.connect(NightMod_Slider)


   ui.checkBox_8.stateChanged.connect(FOVChanger_Start)
   ui.slider_4.valueChanged.connect(FOVChanger_Slider)

   ui.checkBox_8.stateChanged.connect(FOVChanger_Start)

   ui.checkBox_10.stateChanged.connect(AimBot_Start)
   ui.checkBox_11.stateChanged.connect(AimBot_Team)
   ui.checkBox_12.stateChanged.connect(AimBot_Visible)
   ui.checkBox_13.stateChanged.connect(AimBot_BestBone)
   ui.slider_5.valueChanged.connect(AimBot_FOVSlider)
   ui.slider_6.valueChanged.connect(AimBot_SmoothSlider)
   ui.comboBox.currentTextChanged.connect(AimBot_Bone)
   ui.comboBox_4.currentTextChanged.connect(AimBot_Mouse)

   ui.checkBox_14.stateChanged.connect(TriggerBot_Start)
   ui.checkBox_15.stateChanged.connect(TriggerBot_Team)
   ui.slider_7.valueChanged.connect(TriggerBot_Slider)
   ui.comboBox_5.currentTextChanged.connect(TriggerBot_Mouse)

   ui.checkBox_16.stateChanged.connect(AutoPistol_Start)
   ui.checkBox_17.stateChanged.connect(Brightness_Start)
   ui.checkBox_18.stateChanged.connect(BunnyHop_Start)
   ui.checkBox_19.stateChanged.connect(lambda: threading.Thread(target = ShowMoney.Start).start())
   ui.checkBox_22.stateChanged.connect(lambda: threading.Thread(target = GlobalWallHack.Start).start())

   ui.checkBox_20.stateChanged.connect(NoFlash_Start)
   ui.slider_8.valueChanged.connect(NoFlash_Slider)

   ui.checkBox_21.stateChanged.connect(Skinchanger_Start)
   ui.comboBox_2.currentTextChanged.connect(Skinchanger_SetSkin)
   ui.comboBox_3.textActivated.connect(Skinchanger_Id)
   
   ui.Close.clicked.connect(lambda: exec("Save()\nos.kill(os.getpid(), signal.SIGTERM)"))
   ui.Minimize.clicked.connect(lambda: ui.showMinimized())

   threading.Thread(target = Start).start()

   sys.exit(app.exec_())
