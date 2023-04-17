import sys
from PyQt5 import QtCore, QtGui, QtWidgets
app = QtWidgets.QApplication(sys.argv)



class Ui_SettingsWindow(object):

    def setupUi(self, SettingsWindow):
        SettingsWindow.setObjectName("SettingsWindow")
        SettingsWindow.setFixedSize(400, 300)
        SettingsWindow.setStyleSheet("background-color: rgb(125, 125, 125);\n"
                           "border-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(SettingsWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        self.fontSizeLabel = QtWidgets.QLabel(self.centralwidget)
        self.fontSizeLabel.setObjectName("fontSizeLabel")
        self.verticalLayout.addWidget(self.fontSizeLabel)

        self.fontSizeSlider = QtWidgets.QSlider(QtCore.Qt.Horizontal, self.centralwidget)
        self.fontSizeSlider.setValue(12)
        self.fontSizeSlider.setObjectName("fontSizeSlider")
        self.verticalLayout.addWidget(self.fontSizeSlider)

        self.darkModeLabel = QtWidgets.QLabel(self.centralwidget)
        self.darkModeLabel.setObjectName("darkModeLabel")
        self.verticalLayout.addWidget(self.darkModeLabel)

        self.darkModeSwitch = QtWidgets.QCheckBox(self.centralwidget)
        self.darkModeSwitch.setObjectName("darkModeSwitch")
        self.verticalLayout.addWidget(self.darkModeSwitch)
        self.fontSizeSlider.valueChanged.connect(self.changeFontSize)
        self.darkModeSwitch.toggled.connect(self.toggleDarkMode)

        SettingsWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SettingsWindow)
        QtCore.QMetaObject.connectSlotsByName(SettingsWindow)
        self.fontSizeSlider.valueChanged.connect(self.changeFontSize)
        self.darkModeSwitch.toggled.connect(self.toggleDarkMode)

    def changeFontSize(self,value):
        font = QtGui.QFont()
        font.setPointSize(value)
        app.setFont(font)

    def toggleDarkMode(self,checked):
        if checked:
            # Aktivace tmavého režimu
            app.setStyleSheet("QMainWindow { background-color: #2b2b2b; color: #ffffff; }")
        else:
            # Deaktivace tmavého režimu
            app.setStyleSheet("")

    def retranslateUi(self, SettingsWindow):
        _translate = QtCore.QCoreApplication.translate
        SettingsWindow.setWindowTitle(_translate("SettingsWindow", "Settings"))
        self.fontSizeLabel.setText(_translate("SettingsWindow", "Font size:"))
        self.darkModeLabel.setText(_translate("SettingsWindow", "Dark mode:"))
