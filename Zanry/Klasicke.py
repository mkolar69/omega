


from PyQt5 import QtCore, QtWidgets
from script.Main.SONGY.VedMe import Ui_VedDal
from script.Main.SONGY.SeverniVitr import Ui_Severni
from script.Main.SONGY.Montgomery import Ui_Montgomery
from script.Main.SONGY.Watanay import Ui_Watanay
class Ui_Klasik(object):
    def openWindow(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_VedDal()
        self.ui.setupUi( self.window)
        self.window.show()
    def openWindow1(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_Severni()
        self.ui.setupUi( self.window)
        self.window.show()
    def openWindow2(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_Watanay()
        self.ui.setupUi( self.window)
        self.window.show()
    def openWindow3(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Montgomery()
        self.ui.setupUi(self.window)
        self.window.show()


    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(581, 407)
        Form.setStyleSheet("background-color: rgb(125, 125, 125);\n"
                           "border-color: rgb(255, 255, 255);")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(Form,clicked=lambda:self.openWindow())
        self.commandLinkButton.setGeometry(QtCore.QRect(20, 30, 185, 41))
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.commandLinkButton_2 = QtWidgets.QCommandLinkButton(Form,clicked=lambda:self.openWindow1())
        self.commandLinkButton_2.setGeometry(QtCore.QRect(20, 70, 185, 41))
        self.commandLinkButton_2.setObjectName("commandLinkButton_2")
        self.commandLinkButton_3 = QtWidgets.QCommandLinkButton(Form,clicked=lambda:self.openWindow3())
        self.commandLinkButton_3.setGeometry(QtCore.QRect(20, 110, 185, 41))
        self.commandLinkButton_3.setObjectName("commandLinkButton_3")
        self.commandLinkButton_4 = QtWidgets.QCommandLinkButton(Form,clicked=lambda:self.openWindow2())
        self.commandLinkButton_4.setGeometry(QtCore.QRect(20, 150, 185, 41))
        self.commandLinkButton_4.setObjectName("commandLinkButton_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Klasické"))
        self.commandLinkButton.setText(_translate("Form", "Veď mě dál, cesto má "))
        self.commandLinkButton_2.setText(_translate("Form", "Severní vítr"))
        self.commandLinkButton_3.setText(_translate("Form", "Montgomery "))
        self.commandLinkButton_4.setText(_translate("Form", "Ho Ho Watanay "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Klasik()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
