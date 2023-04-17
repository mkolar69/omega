
from PyQt5 import QtCore, QtWidgets

from script.Main.SONGY.Purpura import Ui_Purpura
from script.Main.SONGY.Kralove import Ui_Kralove
class Ui_Koledy(object):
    def openWindow(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_Purpura()
        self.ui.setupUi( self.window)
        self.window.show()

    def openWindow1(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_Kralove()
        self.ui.setupUi( self.window)
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
        self.commandLinkButton_3 = QtWidgets.QCommandLinkButton(Form)
        self.commandLinkButton_3.setGeometry(QtCore.QRect(20, 110, 185, 41))
        self.commandLinkButton_3.setObjectName("commandLinkButton_3")
        self.commandLinkButton_4 = QtWidgets.QCommandLinkButton(Form)
        self.commandLinkButton_4.setGeometry(QtCore.QRect(20, 150, 185, 41))
        self.commandLinkButton_4.setObjectName("commandLinkButton_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Koledy"))
        self.commandLinkButton.setText(_translate("Form", "Purpura"))
        self.commandLinkButton_2.setText(_translate("Form", "My tři králové"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Koledy()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
