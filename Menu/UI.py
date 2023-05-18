from PyQt5 import QtCore, QtGui, QtWidgets
from Tool.GlowESP import *

_translate = QtCore.QCoreApplication.translate

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(527, 310)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 715, 401))
        self.label.setStyleSheet("background-color: rgb(20, 20, 28);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 527, 23))
        self.label_2.setStyleSheet("background-color: rgb(30, 30, 38);\n"
"font: 63 14pt \"Mayberry Pro\";\n"
"color: #e84118;\n"
"padding-bottom: 2px;\n"
"")
        self.label_2.setObjectName("label_2")
        self.Close = QtWidgets.QPushButton(Form)
        self.Close.setGeometry(QtCore.QRect(502, 0, 23, 23))
        self.Close.setStyleSheet("QPushButton{\n"
"  background-color: rgb(30, 30, 38);\n"
"  border: none;\n"
"  padding-top: 2px;\n"
"  padding-left: 2px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: rgb(33, 33, 41);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: rgb(36, 36, 44);\n"
"}")
        self.Close.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Resource/Image/Close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Close.setIcon(icon)
        self.Close.setIconSize(QtCore.QSize(22, 22))
        self.Close.setObjectName("Close")
        self.Minimize = QtWidgets.QPushButton(Form)
        self.Minimize.setGeometry(QtCore.QRect(477, 0, 23, 23))
        self.Minimize.setStyleSheet("QPushButton{\n"
"  background-color: rgb(30, 30, 38);\n"
"  border: none;\n"
"  padding-top: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: rgb(33, 33, 41);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: rgb(36, 36, 44);\n"
"}")
        self.Minimize.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Resource/Image/Subtract.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Minimize.setIcon(icon1)
        self.Minimize.setIconSize(QtCore.QSize(16, 16))
        self.Minimize.setObjectName("Minimize")
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(5, 30, 86, 20))
        self.checkBox.setStyleSheet("QCheckBox {\n"
"color: white;\n"
"spacing: 5px;\n"
"font: 63 12pt \"Mayberry Pro\";\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"width: 13px;\n"
"height: 13px;\n"
"border: 1px solid #f5f6fa;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"background-color: rgb(40,40,45);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"background-color: rgb(45,45,50);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"background-color: #0652DD;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"background-color: #0652C8;\n"
"}\n"
"")
        self.checkBox.setObjectName("checkBox")
        self.colorEdit = QtWidgets.QPushButton(Form)
        self.colorEdit.setGeometry(QtCore.QRect(140, 30, 31, 20))
        self.colorEdit.setStyleSheet("QPushButton{\n"
f"background-color: rgb({GlowESP.Color.R},{GlowESP.Color.G},{GlowESP.Color.B});\n"
"border: none;\n"
"border-radius: 3px;\n"
"}\n"
"")
        self.colorEdit.setText("")
        self.colorEdit.setObjectName("colorEdit")
        self.checkBox_2 = QtWidgets.QCheckBox(Form)
        self.checkBox_2.setGeometry(QtCore.QRect(4, 50, 57, 20))
        self.checkBox_2.setStyleSheet("QCheckBox {\n"
"color: white;\n"
"spacing: 5px;\n"
"font: 63 12pt \"Mayberry Pro\";\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"width: 13px;\n"
"height: 13px;\n"
"border: 1px solid #f5f6fa;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"background-color: rgb(40,40,45);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"background-color: rgb(45,45,50);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"background-color: #e84118;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"background-color: #D74118;\n"
"}\n"
"")
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_2.setChecked(True)
        self.slider = QtWidgets.QSlider(Form)
        self.slider.setGeometry(QtCore.QRect(5, 70, 121, 22))
        self.slider.setToolTipDuration(-1)
        self.slider.setStatusTip("")
        self.slider.setWhatsThis("")
        self.slider.setAccessibleName("")
        self.slider.setAccessibleDescription("")
        self.slider.setStyleSheet("QSlider::groove:horizontal {\n"
"height: 8px;\n"
"background: #0097e6;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: #1e3799;\n"
"    width: 15px;\n"
"}")
        self.slider.setMinimum(3)
        self.slider.setMaximum(10)
        self.slider.setSingleStep(0)
        self.slider.setPageStep(0)
        self.slider.setProperty("value", 6)
        self.slider.setSliderPosition(6)
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.slider.setInvertedAppearance(False)
        self.slider.setInvertedControls(False)
        self.slider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.slider.setTickInterval(1)
        self.slider.setObjectName("slider")
        self.counter = QtWidgets.QLabel(Form)
        self.counter.setGeometry(QtCore.QRect(140, 70, 31, 20))
        self.counter.setToolTip("")
        self.counter.setStyleSheet("font: 63 12pt \"Mayberry Pro\";")
        self.counter.setAlignment(QtCore.Qt.AlignCenter)
        self.counter.setObjectName("counter")
        self.checkBox_3 = QtWidgets.QCheckBox(Form)
        self.checkBox_3.setGeometry(QtCore.QRect(5, 95, 138, 20))
        self.checkBox_3.setStyleSheet("QCheckBox {\n"
"color: white;\n"
"spacing: 5px;\n"
"font: 63 12pt \"Mayberry Pro\";\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"width: 13px;\n"
"height: 13px;\n"
"border: 1px solid #f5f6fa;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"background-color: rgb(40,40,45);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"background-color: rgb(45,45,50);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"background-color: #0652DD;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"background-color: #0652C8;\n"
"}\n"
"")
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(Form)
        self.checkBox_4.setGeometry(QtCore.QRect(5, 115, 57, 20))
        self.checkBox_4.setStyleSheet("QCheckBox {\n"
"color: white;\n"
"spacing: 5px;\n"
"font: 63 12pt \"Mayberry Pro\";\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"width: 13px;\n"
"height: 13px;\n"
"border: 1px solid #f5f6fa;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"background-color: rgb(40,40,45);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"background-color: rgb(45,45,50);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"background-color: #e84118;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"background-color: #D74118;\n"
"}\n"
"")
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_4.setChecked(True)
        self.slider_2 = QtWidgets.QSlider(Form)
        self.slider_2.setGeometry(QtCore.QRect(5, 135, 121, 22))
        self.slider_2.setToolTipDuration(-1)
        self.slider_2.setStatusTip("")
        self.slider_2.setWhatsThis("")
        self.slider_2.setAccessibleName("")
        self.slider_2.setAccessibleDescription("")
        self.slider_2.setStyleSheet("QSlider::groove:horizontal {\n"
"height: 8px;\n"
"background: #0097e6;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: #1e3799;\n"
"    width: 15px;\n"
"}")
        self.slider_2.setMinimum(3)
        self.slider_2.setMaximum(10)
        self.slider_2.setSingleStep(0)
        self.slider_2.setPageStep(0)
        self.slider_2.setProperty("value", 6)
        self.slider_2.setSliderPosition(6)
        self.slider_2.setOrientation(QtCore.Qt.Horizontal)
        self.slider_2.setInvertedAppearance(False)
        self.slider_2.setInvertedControls(False)
        self.slider_2.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.slider_2.setTickInterval(1)
        self.slider_2.setObjectName("slider_2")
        self.counter_2 = QtWidgets.QLabel(Form)
        self.counter_2.setGeometry(QtCore.QRect(140, 135, 31, 20))
        self.counter_2.setToolTip("")
        self.counter_2.setStyleSheet("font: 63 12pt \"Mayberry Pro\";")
        self.counter_2.setAlignment(QtCore.Qt.AlignCenter)
        self.counter_2.setObjectName("counter_2")
        self.checkBox_5 = QtWidgets.QCheckBox(Form)
        self.checkBox_5.setGeometry(QtCore.QRect(5, 160, 66, 20))
        self.checkBox_5.setStyleSheet("QCheckBox {\n"
"color: white;\n"
"spacing: 5px;\n"
"font: 63 12pt \"Mayberry Pro\";\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"width: 13px;\n"
"height: 13px;\n"
"border: 1px solid #f5f6fa;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"background-color: rgb(40,40,45);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"background-color: rgb(45,45,50);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"background-color: #0652DD;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"background-color: #0652C8;\n"
"}\n"
"")
        self.checkBox_5.setObjectName("checkBox_5")
        self.colorEdit_2 = QtWidgets.QPushButton(Form)
        self.colorEdit_2.setGeometry(QtCore.QRect(140, 160, 31, 20))
        self.colorEdit_2.setStyleSheet("QPushButton{\n"
"background-color: rgb(255,255,255);\n"
"border: none;\n"
"border-radius: 3px;\n"
"}\n"
"")
        self.colorEdit_2.setText("")
        self.colorEdit_2.setObjectName("colorEdit_2")
        self.checkBox_6 = QtWidgets.QCheckBox(Form)
        self.checkBox_6.setGeometry(QtCore.QRect(5, 180, 57, 20))
        self.checkBox_6.setStyleSheet("QCheckBox {\n"
"color: white;\n"
"spacing: 5px;\n"
"font: 63 12pt \"Mayberry Pro\";\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"width: 13px;\n"
"height: 13px;\n"
"border: 1px solid #f5f6fa;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"background-color: rgb(40,40,45);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"background-color: rgb(45,45,50);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"background-color: #e84118;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"background-color: #D74118;\n"
"}\n"
"")
        self.checkBox_6.setObjectName("checkBox_6")
        self.checkBox_6.setChecked(True)
        self.checkBox_7 = QtWidgets.QCheckBox(Form)
        self.checkBox_7.setGeometry(QtCore.QRect(5, 205, 96, 20))
        self.checkBox_7.setStyleSheet("QCheckBox {\n"
"color: white;\n"
"spacing: 5px;\n"
"font: 63 12pt \"Mayberry Pro\";\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"width: 13px;\n"
"height: 13px;\n"
"border: 1px solid #f5f6fa;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"background-color: rgb(40,40,45);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"background-color: rgb(45,45,50);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"background-color: #0652DD;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"background-color: #0652C8;\n"
"}\n"
"")
        self.checkBox_7.setObjectName("checkBox_7")
        self.slider_3 = QtWidgets.QSlider(Form)
        self.slider_3.setGeometry(QtCore.QRect(5, 225, 121, 22))
        self.slider_3.setToolTipDuration(-1)
        self.slider_3.setStatusTip("")
        self.slider_3.setWhatsThis("")
        self.slider_3.setAccessibleName("")
        self.slider_3.setAccessibleDescription("")
        self.slider_3.setStyleSheet("QSlider::groove:horizontal {\n"
"height: 8px;\n"
"background: #0097e6;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: #1e3799;\n"
"    width: 15px;\n"
"}")
        self.slider_3.setMinimum(1)
        self.slider_3.setMaximum(100)
        self.slider_3.setSingleStep(0)
        self.slider_3.setPageStep(0)
        self.slider_3.setProperty("value", 70)
        self.slider_3.setSliderPosition(70)
        self.slider_3.setOrientation(QtCore.Qt.Horizontal)
        self.slider_3.setInvertedAppearance(False)
        self.slider_3.setInvertedControls(False)
        self.slider_3.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.slider_3.setTickInterval(1)
        self.slider_3.setObjectName("slider_3")
        self.counter_3 = QtWidgets.QLabel(Form)
        self.counter_3.setGeometry(QtCore.QRect(140, 225, 34, 20))
        self.counter_3.setToolTip("")
        self.counter_3.setStyleSheet("font: 63 12pt \"Mayberry Pro\";")
        self.counter_3.setAlignment(QtCore.Qt.AlignCenter)
        self.counter_3.setObjectName("counter_3")
        self.checkBox_8 = QtWidgets.QCheckBox(Form)
        self.checkBox_8.setGeometry(QtCore.QRect(5, 250, 98, 20))
        self.checkBox_8.setStyleSheet("QCheckBox {\n"
"color: white;\n"
"spacing: 5px;\n"
"font: 63 12pt \"Mayberry Pro\";\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"width: 13px;\n"
"height: 13px;\n"
"border: 1px solid #f5f6fa;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"background-color: rgb(40,40,45);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"background-color: rgb(45,45,50);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"background-color: #0652DD;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"background-color: #0652C8;\n"
"}\n"
"")
        self.checkBox_8.setObjectName("checkBox_8")
        self.slider_4 = QtWidgets.QSlider(Form)
        self.slider_4.setGeometry(QtCore.QRect(5, 270, 121, 22))
        self.slider_4.setToolTipDuration(-1)
        self.slider_4.setStatusTip("")
        self.slider_4.setWhatsThis("")
        self.slider_4.setAccessibleName("")
        self.slider_4.setAccessibleDescription("")
        self.slider_4.setStyleSheet("QSlider::groove:horizontal {\n"
"height: 8px;\n"
"background: #0097e6;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: #1e3799;\n"
"    width: 15px;\n"
"}")
        self.slider_4.setMinimum(30)
        self.slider_4.setMaximum(170)
        self.slider_4.setSingleStep(0)
        self.slider_4.setPageStep(0)
        self.slider_4.setProperty("value", 90)
        self.slider_4.setSliderPosition(90)
        self.slider_4.setOrientation(QtCore.Qt.Horizontal)
        self.slider_4.setInvertedAppearance(False)
        self.slider_4.setInvertedControls(False)
        self.slider_4.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.slider_4.setTickInterval(1)
        self.slider_4.setObjectName("slider_4")
        self.counter_4 = QtWidgets.QLabel(Form)
        self.counter_4.setGeometry(QtCore.QRect(140, 270, 33, 20))
        self.counter_4.setToolTip("")
        self.counter_4.setStyleSheet("font: 63 12pt \"Mayberry Pro\";")
        self.counter_4.setAlignment(QtCore.Qt.AlignCenter)
        self.counter_4.setObjectName("counter_4")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(180, 30, 2, 275))
        self.label_9.setStyleSheet("background-color: #e84118;")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.checkBox_10 = QtWidgets.QCheckBox(Form)
        self.checkBox_10.setGeometry(QtCore.QRect(190, 30, 78, 20))
        self.checkBox_10.setStyleSheet("QCheckBox {\n"
"color: white;\n"
"spacing: 5px;\n"
"font: 63 12pt \"Mayberry Pro\";\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"width: 13px;\n"
"height: 13px;\n"
"border: 1px solid #f5f6fa;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"background-color: rgb(40,40,45);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"background-color: rgb(45,45,50);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"background-color: #0652DD;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"background-color: #0652C8;\n"
"}\n"
"")
        self.checkBox_10.setObjectName("checkBox_10")
        self.checkBox_11 = QtWidgets.QCheckBox(Form)
        self.checkBox_11.setGeometry(QtCore.QRect(190, 50, 57, 20))
        self.checkBox_11.setStyleSheet("QCheckBox {\n"
"color: white;\n"
"spacing: 5px;\n"
"font: 63 12pt \"Mayberry Pro\";\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"width: 13px;\n"
"height: 13px;\n"
"border: 1px solid #f5f6fa;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"background-color: rgb(40,40,45);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"background-color: rgb(45,45,50);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"background-color: #e84118;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"background-color: #D74118;\n"
"}\n"
"")
        self.checkBox_11.setObjectName("checkBox_11")
        self.checkBox_11.setChecked(True)
        self.checkBox_12 = QtWidgets.QCheckBox(Form)
        self.checkBox_12.setGeometry(QtCore.QRect(190, 70, 103, 20))
        self.checkBox_12.setStyleSheet("QCheckBox {\n"
"color: white;\n"
"spacing: 5px;\n"
"font: 63 12pt \"Mayberry Pro\";\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"width: 13px;\n"
"height: 13px;\n"
"border: 1px solid #f5f6fa;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"background-color: rgb(40,40,45);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"background-color: rgb(45,45,50);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"background-color: #e84118;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"background-color: #D74118;\n"
"}\n"
"")
        self.checkBox_12.setObjectName("checkBox_12")
        self.slider_5 = QtWidgets.QSlider(Form)
        self.slider_5.setGeometry(QtCore.QRect(190, 110, 121, 22))
        self.slider_5.setToolTipDuration(-1)
        self.slider_5.setStatusTip("")
        self.slider_5.setWhatsThis("")
        self.slider_5.setAccessibleName("")
        self.slider_5.setAccessibleDescription("")
        self.slider_5.setStyleSheet("QSlider::groove:horizontal {\n"
"height: 8px;\n"
"background: #0097e6;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: #1e3799;\n"
"    width: 15px;\n"
"}")
        self.slider_5.setMinimum(1)
        self.slider_5.setMaximum(180)
        self.slider_5.setSingleStep(0)
        self.slider_5.setPageStep(0)
        self.slider_5.setProperty("value", 30)
        self.slider_5.setSliderPosition(30)
        self.slider_5.setOrientation(QtCore.Qt.Horizontal)
        self.slider_5.setInvertedAppearance(False)
        self.slider_5.setInvertedControls(False)
        self.slider_5.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.slider_5.setTickInterval(1)
        self.slider_5.setObjectName("slider_5")
        self.counter_5 = QtWidgets.QLabel(Form)
        self.counter_5.setGeometry(QtCore.QRect(320, 110, 33, 20))
        self.counter_5.setToolTip("")
        self.counter_5.setStyleSheet("font: 63 12pt \"Mayberry Pro\";")
        self.counter_5.setAlignment(QtCore.Qt.AlignCenter)
        self.counter_5.setObjectName("counter_5")
        self.slider_6 = QtWidgets.QSlider(Form)
        self.slider_6.setGeometry(QtCore.QRect(190, 130, 121, 22))
        self.slider_6.setToolTipDuration(-1)
        self.slider_6.setStatusTip("")
        self.slider_6.setWhatsThis("")
        self.slider_6.setAccessibleName("")
        self.slider_6.setAccessibleDescription("")
        self.slider_6.setStyleSheet("QSlider::groove:horizontal {\n"
"height: 8px;\n"
"background: #0097e6;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: #1e3799;\n"
"    width: 15px;\n"
"}")
        self.slider_6.setMinimum(0)
        self.slider_6.setMaximum(40)
        self.slider_6.setSingleStep(0)
        self.slider_6.setPageStep(0)
        self.slider_6.setProperty("value", 1)
        self.slider_6.setSliderPosition(1)
        self.slider_6.setOrientation(QtCore.Qt.Horizontal)
        self.slider_6.setInvertedAppearance(False)
        self.slider_6.setInvertedControls(False)
        self.slider_6.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.slider_6.setTickInterval(1)
        self.slider_6.setObjectName("slider_6")
        self.counter_6 = QtWidgets.QLabel(Form)
        self.counter_6.setGeometry(QtCore.QRect(320, 130, 33, 20))
        self.counter_6.setToolTip("")
        self.counter_6.setStyleSheet("font: 63 12pt \"Mayberry Pro\";")
        self.counter_6.setAlignment(QtCore.Qt.AlignCenter)
        self.counter_6.setObjectName("counter_6")
        self.checkBox_13 = QtWidgets.QCheckBox(Form)
        self.checkBox_13.setGeometry(QtCore.QRect(190, 90, 91, 20))
        self.checkBox_13.setStyleSheet("QCheckBox {\n"
"color: white;\n"
"spacing: 5px;\n"
"font: 63 12pt \"Mayberry Pro\";\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"width: 13px;\n"
"height: 13px;\n"
"border: 1px solid #f5f6fa;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"background-color: rgb(40,40,45);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"background-color: rgb(45,45,50);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"background-color: #e84118;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"background-color: #D74118;\n"
"}\n"
"")
        self.checkBox_13.setObjectName("checkBox_13")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(190, 155, 121, 22))
        self.comboBox.setStyleSheet("QComboBox{\n"
"font: 63 10pt \"Mayberry Pro\";\n"
"border: none;\n"
"background-color: rgb(30,30,30);\n"
"color: white;\n"
"font-weight: bold;\n"
"border: 1px solid white;\n"
"}\n"
"\n"
"QComboBox::drop-down{\n"
"    border: none;\n"
"    background-color: rgb(100,100,100);\n"
"    font-weight: bold;\n"
"}")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_4 = QtWidgets.QComboBox(Form)
        self.comboBox_4.setGeometry(QtCore.QRect(190, 180, 121, 22))
        self.comboBox_4.setStyleSheet("QComboBox{\n"
"font: 63 10pt \"Mayberry Pro\";\n"
"border: none;\n"
"background-color: rgb(30,30,30);\n"
"color: white;\n"
"font-weight: bold;\n"
"border: 1px solid white;\n"
"}\n"
"\n"
"QComboBox::drop-down{\n"
"    border: none;\n"
"    background-color: rgb(100,100,100);\n"
"    font-weight: bold;\n"
"}")
        self.comboBox_4.setObjectName("AimBot_Mouse")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.checkBox_14 = QtWidgets.QCheckBox(Form)
        self.checkBox_14.setGeometry(QtCore.QRect(190, 210, 100, 20))
        self.checkBox_14.setStyleSheet("QCheckBox {\n"
"color: white;\n"
"spacing: 5px;\n"
"font: 63 12pt \"Mayberry Pro\";\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"width: 13px;\n"
"height: 13px;\n"
"border: 1px solid #f5f6fa;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"background-color: rgb(40,40,45);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"background-color: rgb(45,45,50);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"background-color: #0652DD;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"background-color: #0652C8;\n"
"}\n"
"")
        self.checkBox_14.setObjectName("checkBox_14")
        self.checkBox_15 = QtWidgets.QCheckBox(Form)
        self.checkBox_15.setGeometry(QtCore.QRect(190, 230, 57, 20))
        self.checkBox_15.setStyleSheet("QCheckBox {\n"
"color: white;\n"
"spacing: 5px;\n"
"font: 63 12pt \"Mayberry Pro\";\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"width: 13px;\n"
"height: 13px;\n"
"border: 1px solid #f5f6fa;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"background-color: rgb(40,40,45);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"background-color: rgb(45,45,50);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"background-color: #e84118;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"background-color: #D74118;\n"
"}\n"
"")
        self.checkBox_15.setObjectName("checkBox_15")
        self.checkBox_15.setChecked(True)
        self.slider_7 = QtWidgets.QSlider(Form)
        self.slider_7.setGeometry(QtCore.QRect(190, 250, 121, 22))
        self.slider_7.setToolTipDuration(-1)
        self.slider_7.setStatusTip("")
        self.slider_7.setWhatsThis("")
        self.slider_7.setAccessibleName("")
        self.slider_7.setAccessibleDescription("")
        self.slider_7.setStyleSheet("QSlider::groove:horizontal {\n"
"height: 8px;\n"
"background: #0097e6;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: #1e3799;\n"
"    width: 15px;\n"
"}")
        self.slider_7.setMinimum(1)
        self.slider_7.setMaximum(100)
        self.slider_7.setSingleStep(0)
        self.slider_7.setPageStep(0)
        self.slider_7.setProperty("value", 12)
        self.slider_7.setSliderPosition(12)
        self.slider_7.setOrientation(QtCore.Qt.Horizontal)
        self.slider_7.setInvertedAppearance(False)
        self.slider_7.setInvertedControls(False)
        self.slider_7.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.slider_7.setTickInterval(1)
        self.slider_7.setObjectName("slider_7")
        self.counter_7 = QtWidgets.QLabel(Form)
        self.counter_7.setGeometry(QtCore.QRect(320, 250, 35, 20))
        self.counter_7.setToolTip("")
        self.counter_7.setStyleSheet("font: 63 12pt \"Mayberry Pro\";")
        self.counter_7.setAlignment(QtCore.Qt.AlignCenter)
        self.counter_7.setObjectName("counter_7")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(360, 30, 2, 275))
        self.label_10.setStyleSheet("background-color: #e84118;")
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.comboBox_5 = QtWidgets.QComboBox(Form)
        self.comboBox_5.setGeometry(QtCore.QRect(190, 275, 121, 22))
        self.comboBox_5.setStyleSheet("QComboBox{\n"
"font: 63 10pt \"Mayberry Pro\";\n"
"border: none;\n"
"background-color: rgb(30,30,30);\n"
"color: white;\n"
"font-weight: bold;\n"
"border: 1px solid white;\n"
"}\n"
"\n"
"QComboBox::drop-down{\n"
"    border: none;\n"
"    background-color: rgb(100,100,100);\n"
"    font-weight: bold;\n"
"}")
        self.comboBox_5.setObjectName("AimBot_Mouse_2")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.checkBox_16 = QtWidgets.QCheckBox(Form)
        self.checkBox_16.setGeometry(QtCore.QRect(370, 30, 99, 20))
        self.checkBox_16.setStyleSheet("QCheckBox {\n"
"color: white;\n"
"spacing: 5px;\n"
"font: 63 12pt \"Mayberry Pro\";\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"width: 13px;\n"
"height: 13px;\n"
"border: 1px solid #f5f6fa;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"background-color: rgb(40,40,45);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"background-color: rgb(45,45,50);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"background-color: #0652DD;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"background-color: #0652C8;\n"
"}\n"
"")
        self.checkBox_16.setObjectName("checkBox_16")
        self.checkBox_17 = QtWidgets.QCheckBox(Form)
        self.checkBox_17.setGeometry(QtCore.QRect(370, 50, 95, 20))
        self.checkBox_17.setStyleSheet("QCheckBox {\n"
"color: white;\n"
"spacing: 5px;\n"
"font: 63 12pt \"Mayberry Pro\";\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"width: 13px;\n"
"height: 13px;\n"
"border: 1px solid #f5f6fa;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"background-color: rgb(40,40,45);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"background-color: rgb(45,45,50);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"background-color: #0652DD;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"background-color: #0652C8;\n"
"}\n"
"")
        self.checkBox_17.setObjectName("checkBox_17")
        self.checkBox_18 = QtWidgets.QCheckBox(Form)
        self.checkBox_18.setGeometry(QtCore.QRect(370, 70, 99, 20))
        self.checkBox_18.setStyleSheet("QCheckBox {\n"
"color: white;\n"
"spacing: 5px;\n"
"font: 63 12pt \"Mayberry Pro\";\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"width: 13px;\n"
"height: 13px;\n"
"border: 1px solid #f5f6fa;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"background-color: rgb(40,40,45);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"background-color: rgb(45,45,50);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"background-color: #0652DD;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"background-color: #0652C8;\n"
"}\n"
"")
        self.checkBox_18.setObjectName("checkBox_18")
        self.checkBox_19 = QtWidgets.QCheckBox(Form)
        self.checkBox_19.setGeometry(QtCore.QRect(370, 90, 110, 20))
        self.checkBox_19.setStyleSheet("QCheckBox {\n"
"color: white;\n"
"spacing: 5px;\n"
"font: 63 12pt \"Mayberry Pro\";\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"width: 13px;\n"
"height: 13px;\n"
"border: 1px solid #f5f6fa;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"background-color: rgb(40,40,45);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"background-color: rgb(45,45,50);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"background-color: #0652DD;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"background-color: #0652C8;\n"
"}\n"
"")
        self.checkBox_19.setObjectName("checkBox_19")
        self.checkBox_20 = QtWidgets.QCheckBox(Form)
        self.checkBox_20.setGeometry(QtCore.QRect(370, 130, 82, 20))
        self.checkBox_20.setStyleSheet("QCheckBox {\n"
"color: white;\n"
"spacing: 5px;\n"
"font: 63 12pt \"Mayberry Pro\";\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"width: 13px;\n"
"height: 13px;\n"
"border: 1px solid #f5f6fa;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"background-color: rgb(40,40,45);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"background-color: rgb(45,45,50);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"background-color: #0652DD;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"background-color: #0652C8;\n"
"}\n"
"")
        self.checkBox_20.setObjectName("checkBox_20")
        self.slider_8 = QtWidgets.QSlider(Form)
        self.slider_8.setGeometry(QtCore.QRect(370, 150, 121, 22))
        self.slider_8.setToolTipDuration(-1)
        self.slider_8.setStatusTip("")
        self.slider_8.setWhatsThis("")
        self.slider_8.setAccessibleName("")
        self.slider_8.setAccessibleDescription("")
        self.slider_8.setStyleSheet("QSlider::groove:horizontal {\n"
"height: 8px;\n"
"background: #0097e6;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: #1e3799;\n"
"    width: 15px;\n"
"}")
        self.slider_8.setMinimum(0)
        self.slider_8.setMaximum(255)
        self.slider_8.setSingleStep(0)
        self.slider_8.setPageStep(0)
        self.slider_8.setProperty("value", 0)
        self.slider_8.setSliderPosition(0)
        self.slider_8.setOrientation(QtCore.Qt.Horizontal)
        self.slider_8.setInvertedAppearance(False)
        self.slider_8.setInvertedControls(False)
        self.slider_8.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.slider_8.setTickInterval(1)
        self.slider_8.setObjectName("slider_8")
        self.counter_8 = QtWidgets.QLabel(Form)
        self.counter_8.setGeometry(QtCore.QRect(495, 150, 33, 20))
        self.counter_8.setToolTip("")
        self.counter_8.setStyleSheet("font: 63 12pt \"Mayberry Pro\";")
        self.counter_8.setAlignment(QtCore.Qt.AlignCenter)
        self.counter_8.setObjectName("counter_8")
        self.checkBox_21 = QtWidgets.QCheckBox(Form)
        self.checkBox_21.setGeometry(QtCore.QRect(370, 170, 106, 20))
        self.checkBox_21.setStyleSheet("QCheckBox {\n"
"color: white;\n"
"spacing: 5px;\n"
"font: 63 12pt \"Mayberry Pro\";\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"width: 13px;\n"
"height: 13px;\n"
"border: 1px solid #f5f6fa;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"background-color: rgb(40,40,45);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"background-color: rgb(45,45,50);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"background-color: #0652DD;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"background-color: #0652C8;\n"
"}\n"
"")
        self.checkBox_21.setObjectName("checkBox_21")
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(370, 195, 151, 22))
        self.comboBox_2.setStyleSheet("QComboBox{\n"
"font: 63 10pt \"Mayberry Pro\";\n"
"border: none;\n"
"background-color: rgb(30,30,30);\n"
"color: white;\n"
"font-weight: bold;\n"
"border: 1px solid white;\n"
"}\n"
"\n"
"QComboBox::drop-down{\n"
"    border: none;\n"
"    background-color: rgb(100,100,100);\n"
"    font-weight: bold;\n"
"}")
        self.comboBox_2.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_3 = QtWidgets.QComboBox(Form)
        self.comboBox_3.setGeometry(QtCore.QRect(370, 220, 151, 22))
        self.comboBox_3.setStyleSheet("QComboBox{\n"
"font: 63 10pt \"Mayberry Pro\";\n"
"border: none;\n"
"background-color: rgb(30,30,30);\n"
"color: white;\n"
"font-weight: bold;\n"
"border: 1px solid white;\n"
"}\n"
"\n"
"QComboBox::drop-down{\n"
"    border: none;\n"
"    background-color: rgb(100,100,100);\n"
"    font-weight: bold;\n"
"}")
        self.comboBox_3.setObjectName("comboBox_3")
        self.checkBox_22 = QtWidgets.QCheckBox(Form)
        self.checkBox_22.setGeometry(QtCore.QRect(370, 110, 136, 20))
        self.checkBox_22.setStyleSheet("QCheckBox {\n"
"color: white;\n"
"spacing: 5px;\n"
"font: 63 12pt \"Mayberry Pro\";\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"width: 13px;\n"
"height: 13px;\n"
"border: 1px solid #f5f6fa;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"background-color: rgb(40,40,45);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"background-color: rgb(45,45,50);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"background-color: #0652DD;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"background-color: #0652C8;\n"
"}\n"
"")
        self.checkBox_22.setObjectName("checkBox_22")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Maze"))
        self.label_2.setText(_translate("Form", "Maze"))
        self.checkBox.setText(_translate("Form", "Glow ESP"))
        self.checkBox_2.setText(_translate("Form", "Team"))
        self.slider.setToolTip(_translate("Form", "<html><head/><body><p>Thickness</p></body></html>"))
        self.counter.setText(_translate("Form", f"<html><head/><body><p><span style=\" color:#ffffff;\">{GlowESP.Line}</span></p></body></html>"))
        self.checkBox_3.setText(_translate("Form", "Glow ESP Health"))
        self.checkBox_4.setText(_translate("Form", "Team"))
        self.slider_2.setToolTip(_translate("Form", "<html><head/><body><p>Thickness</p></body></html>"))
        self.counter_2.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#ffffff;\">0.6</span></p></body></html>"))
        self.checkBox_5.setText(_translate("Form", "Chams"))
        self.checkBox_6.setText(_translate("Form", "Team"))
        self.checkBox_7.setText(_translate("Form", "Night Mod"))
        self.slider_3.setToolTip(_translate("Form", "<html><head/><body><p>Light</p></body></html>"))
        self.counter_3.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#ffffff;\">0.70</span></p></body></html>"))
        self.checkBox_8.setText(_translate("Form", "Player FOV"))
        self.slider_4.setToolTip(_translate("Form", "<html><head/><body><p>Angle view</p></body></html>"))
        self.counter_4.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#ffffff;\">90</span></p></body></html>"))
        self.checkBox_10.setText(_translate("Form", "Aim Bot"))
        self.checkBox_11.setText(_translate("Form", "Team"))
        self.checkBox_12.setText(_translate("Form", "Only visible"))
        self.slider_5.setToolTip(_translate("Form", "<html><head/><body><p>FOV</p></body></html>"))
        self.counter_5.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#ffffff;\">30</span></p></body></html>"))
        self.slider_6.setToolTip(_translate("Form", "<html><head/><body><p>Smooth</p></body></html>"))
        self.counter_6.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#ffffff;\">1</span></p></body></html>"))
        self.checkBox_13.setText(_translate("Form", "Best bone"))
        self.comboBox.setToolTip(_translate("Form", "Bone"))
        self.comboBox.setItemText(0, _translate("Form", "Head"))
        self.comboBox.setItemText(1, _translate("Form", "Neck"))
        self.comboBox.setItemText(2, _translate("Form", "Chest"))
        self.comboBox.setItemText(3, _translate("Form", "Stomach"))
        self.comboBox.setItemText(4, _translate("Form", "Pelvis"))
        self.comboBox_4.setToolTip(_translate("Form", "Mouse"))
        self.comboBox_4.setItemText(0, _translate("Form", "M1"))
        self.comboBox_4.setItemText(1, _translate("Form", "M2"))
        self.comboBox_4.setItemText(2, _translate("Form", "M3"))
        self.comboBox_4.setItemText(3, _translate("Form", "M4"))
        self.comboBox_4.setItemText(4, _translate("Form", "M5"))
        self.comboBox_4.setItemText(5, _translate("Form", "M6"))
        self.comboBox_4.setItemText(6, _translate("Form", "None"))
        self.checkBox_14.setText(_translate("Form", "Trigger Bot"))
        self.checkBox_15.setText(_translate("Form", "Team"))
        self.slider_7.setToolTip(_translate("Form", "<html><head/><body><p>Delay</p></body></html>"))
        self.counter_7.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#ffffff;\">0.12</span></p></body></html>"))
        self.comboBox_5.setToolTip(_translate("Form", "Mouse"))
        self.comboBox_5.setItemText(0, _translate("Form", "M1"))
        self.comboBox_5.setItemText(1, _translate("Form", "M2"))
        self.comboBox_5.setItemText(2, _translate("Form", "M3"))
        self.comboBox_5.setItemText(3, _translate("Form", "M4"))
        self.comboBox_5.setItemText(4, _translate("Form", "M5"))
        self.comboBox_5.setItemText(5, _translate("Form", "M6"))
        self.comboBox_5.setItemText(6, _translate("Form", "None"))
        self.checkBox_16.setText(_translate("Form", "Auto Pistol"))
        self.checkBox_17.setText(_translate("Form", "Brightness"))
        self.checkBox_18.setText(_translate("Form", "Bunny Hop"))
        self.checkBox_19.setText(_translate("Form", "Show Money"))
        self.checkBox_20.setText(_translate("Form", "No Flash"))
        self.slider_8.setToolTip(_translate("Form", "<html><head/><body><p>Flashing</p></body></html>"))
        self.counter_8.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#ffffff;\">0</span></p></body></html>"))
        self.checkBox_21.setText(_translate("Form", "Skinchanger"))
        self.comboBox_2.setToolTip(_translate("Form", "<html><head/><body><p>Gun</p></body></html>"))
        self.comboBox_2.setItemText(0, _translate("Form", "P2000"))
        self.comboBox_2.setItemText(1, _translate("Form", "USP-S"))
        self.comboBox_2.setItemText(2, _translate("Form", "Glock"))
        self.comboBox_2.setItemText(3, _translate("Form", "Dual Berettas"))
        self.comboBox_2.setItemText(4, _translate("Form", "P250"))
        self.comboBox_2.setItemText(5, _translate("Form", "Tec-9"))
        self.comboBox_2.setItemText(6, _translate("Form", "CZ75-Auto"))
        self.comboBox_2.setItemText(7, _translate("Form", "Desert Eagle"))
        self.comboBox_2.setItemText(8, _translate("Form", "Five-SeveN"))
        self.comboBox_2.setItemText(9, _translate("Form", "R8"))
        self.comboBox_2.setItemText(10, _translate("Form", "Nova"))
        self.comboBox_2.setItemText(11, _translate("Form", "XM1014"))
        self.comboBox_2.setItemText(12, _translate("Form", "MAG-7"))
        self.comboBox_2.setItemText(13, _translate("Form", "M249"))
        self.comboBox_2.setItemText(14, _translate("Form", "Negev"))
        self.comboBox_2.setItemText(15, _translate("Form", "Sawed-Off"))
        self.comboBox_2.setItemText(16, _translate("Form", "MAC-10"))
        self.comboBox_2.setItemText(17, _translate("Form", "MP5-SD"))
        self.comboBox_2.setItemText(18, _translate("Form", "UMP-45"))
        self.comboBox_2.setItemText(19, _translate("Form", "P90"))
        self.comboBox_2.setItemText(20, _translate("Form", "PP-19"))
        self.comboBox_2.setItemText(21, _translate("Form", "MP9"))
        self.comboBox_2.setItemText(22, _translate("Form", "MP7"))
        self.comboBox_2.setItemText(23, _translate("Form", "FAMAS"))
        self.comboBox_2.setItemText(24, _translate("Form", "M4A4"))
        self.comboBox_2.setItemText(25, _translate("Form", "M4A1-S"))
        self.comboBox_2.setItemText(26, _translate("Form", "SSG 08"))
        self.comboBox_2.setItemText(27, _translate("Form", "AUG"))
        self.comboBox_2.setItemText(28, _translate("Form", "AWP"))
        self.comboBox_2.setItemText(29, _translate("Form", "SCAR-20"))
        self.comboBox_2.setItemText(30, _translate("Form", "Galil"))
        self.comboBox_2.setItemText(31, _translate("Form", "AK-47"))
        self.comboBox_2.setItemText(32, _translate("Form", "SG 553"))
        self.comboBox_2.setItemText(33, _translate("Form", "G3SG1"))
        self.comboBox_3.setToolTip(_translate("Form", "Skin"))
        self.checkBox_22.setText(_translate("Form", "Global WallHack"))


class Widget(QtWidgets.QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(Widget, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)


    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            x_main, y_main = self.geometry().x(), self.geometry().y()
            cursor_x, cursor_y = QtGui.QCursor.pos().x(), QtGui.QCursor.pos().y()

            if x_main <= cursor_x <= x_main + self.geometry().width():
                if y_main <= cursor_y <= y_main + self.geometry().height():
                    self.old_pos = event.pos()

                else:
                    self.old_pos = None

        elif event.button() == QtCore.Qt.RightButton:
            self.old_pos = None


    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.old_pos = None


    def mouseMoveEvent(self, event):
        try:
            delta = event.pos() - self.old_pos
            self.move(self.pos() + delta)

        except: pass
