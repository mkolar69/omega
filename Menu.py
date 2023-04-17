
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from Kategorie import Ui_Form
from Pisne import Ui_Pisne
from script.Main.akordy.Akordy import Ui_Akordy
app = QtWidgets.QApplication(sys.argv)
from Settings import Ui_SettingsWindow


class Ui_Menu(object):

    def openWindow1(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_Form()
        self.ui.setupUi( self.window)
        self.window.show()

    def openWindow(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_Pisne()
        self.ui.setupUi( self.window)
        self.window.show()

    def openWindow2(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Akordy()
        self.ui.setupUi(self.window)
        self.window.show()
    def openSettingsWindow(self):
        self.settingsWindow = QtWidgets.QMainWindow()
        self.settingsUi = Ui_SettingsWindow()
        self.settingsUi.setupUi(self.settingsWindow)
        self.settingsWindow.show()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(125, 125, 125);\n"
                           "border-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 30, 601, 131))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.openWindow1())
        self.pushButton.setGeometry(QtCore.QRect(100, 190, 200, 91))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.openWindow())
        self.pushButton_2.setGeometry(QtCore.QRect(500, 190, 200, 91))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.openWindow2())
        self.pushButton_4.setGeometry(QtCore.QRect(300, 190, 200, 91))
        self.pushButton_4.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(250, 360, 281, 131))
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.pushButton_3.clicked.connect(QtCore.QCoreApplication.quit)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.menuSettings.addAction(self.actionSettings)
        self.actionSettings.triggered.connect(self.openSettingsWindow)
        self.backButton = QtWidgets.QPushButton(self.centralwidget, text="Back",clicked=lambda: self.goBack(MainWindow))
        self.backButton.setObjectName("backButton")
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Zpěvník"))
        self.label.setText(_translate("MainWindow", "Vitejte v aplikaci SongBook"))
        self.pushButton.setText(_translate("MainWindow", "Kategorie"))
        self.pushButton_2.setText(_translate("MainWindow", "Pisne"))
        self.pushButton_4.setText(_translate("MainWindow", "Akordy"))
        self.pushButton_3.setText(_translate("MainWindow", "Vypnout"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))

    def goBack(self,window):
        window.show()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Menu()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
