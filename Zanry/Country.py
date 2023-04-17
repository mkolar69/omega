from PyQt5 import QtCore, QtWidgets
from script.Main.SONGY.BajZen import Ui_BajZen
class Ui_Country(object):

    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_BajZen()
        self.ui.setupUi(self.window)
        self.window.show()



    def setupUi(self, Form,parent=None):
        self.parent = parent
        self.Form = Form
        Form.setObjectName("Form")
        Form.setFixedSize(581, 407)
        Form.setStyleSheet("background-color: rgb(125, 125, 125);\n"
                           "border-color: rgb(255, 255, 255);")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(Form,clicked=lambda:self.openWindow())
        self.commandLinkButton.setGeometry(QtCore.QRect(20, 30, 185, 41))
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.commandLinkButton_2 = QtWidgets.QCommandLinkButton(Form)
        self.commandLinkButton_2.setGeometry(QtCore.QRect(20, 70, 185, 41))
        self.commandLinkButton_2.setObjectName("commandLinkButton_2")
        self.commandLinkButton_3 = QtWidgets.QCommandLinkButton(Form)
        self.commandLinkButton_3.setGeometry(QtCore.QRect(20, 110, 185, 41))
        self.commandLinkButton_3.setObjectName("commandLinkButton_3")
        self.commandLinkButton_4 = QtWidgets.QCommandLinkButton(Form)
        self.commandLinkButton_4.setGeometry(QtCore.QRect(20, 150, 185, 41))
        self.commandLinkButton_4.setObjectName("commandLinkButton_4")
        self.back_button = QtWidgets.QPushButton(Form, clicked=self.back_to_categories)
        self.back_button.setGeometry(QtCore.QRect(10, 10, 75, 23))
        self.back_button.setObjectName("back_button")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    def back_to_categories(self):
        self.Form.close()
        self.parent.show()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Country"))
        self.commandLinkButton.setText(_translate("Form", "Báječná ženská "))
        self.commandLinkButton_2.setText(_translate("Form", ""))
        self.commandLinkButton_3.setText(_translate("Form", ""))
        self.commandLinkButton_4.setText(_translate("Form", ""))
        self.back_button.setText(_translate("Form", "Zpět"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Country()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
