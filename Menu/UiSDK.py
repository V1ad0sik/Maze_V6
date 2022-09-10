from Menu.UI import *
from Module.Struct import *

from PyQt5.QtWidgets import QColorDialog, QPushButton, QSlider, QLabel

def ColorEdit(ui: QPushButton, Color: ColorRGB):
    Dialog = QColorDialog.getColor()
    Color = ColorRGB(Dialog.red(), Dialog.green(), Dialog.blue())

    ui.setStyleSheet("QPushButton{" + f"background-color: rgb({Color.R}, {Color.G}, {Color.B}); border: none; border-radius: 3px;" + "}")

    return Color


def Slider(slider: QSlider, label: QLabel, Mul, Round):
    Value = round(slider.value() * Mul, Round)
    label.setText(f"<html><head/><body><p><span style=\" color:#ffffff;\">{Value}</span></p></body></html>")

    return Value


def SetColorForColorEdit(ui: QPushButton, Color: ColorRGB):
    ui.setStyleSheet("QPushButton{" + f"background-color: rgb({Color.R}, {Color.G}, {Color.B}); border: none; border-radius: 3px;" + "}")
    return Color