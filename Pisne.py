
from script.Main.SONGY.VedMe import Ui_VedDal
from script.Main.SONGY.SeverniVitr import Ui_Severni
from script.Main.SONGY.KdeDomov import Ui_Kdedomov
from script.Main.SONGY.Montgomery import Ui_Montgomery
from script.Main.SONGY.BajZen import Ui_BajZen
from script.Main.SONGY.Purpura import Ui_Purpura
from script.Main.SONGY.Ukol1 import Ui_Form
from script.Main.SONGY.Klobouk import Ui_Klobouk
from script.Main.SONGY.Kralove import Ui_Kralove
from script.Main.SONGY.Watanay import Ui_Watanay
from script.Main.SONGY.trsvatba import Ui_TrpSv
from script.Main.Db.AddSong import AddSongWindow
import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Pisne(object):
    def openWindow1(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_VedDal()
        self.ui.setupUi(self.window)
        self.window.show()

    def openWindow2(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Severni()
        self.ui.setupUi(self.window)
        self.window.show()

    def openWindow3(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Kdedomov()
        self.ui.setupUi(self.window)
        self.window.show()

    def openAddSongWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.add_song_window = AddSongWindow()
        self.add_song_window.exec_()
        self.add_song_window.setupUi(self.window)
        self.window.show()

    def openWindow7(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()

    def openWindow4(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Montgomery()
        self.ui.setupUi(self.window)
        self.window.show()

    def openWindow5(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_BajZen()
        self.ui.setupUi(self.window)
        self.window.show()

    def openWindow6(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Purpura()
        self.ui.setupUi(self.window)
        self.window.show()

    def openWindow8(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Klobouk()
        self.ui.setupUi(self.window)
        self.window.show()

    def openWindow9(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Kralove()
        self.ui.setupUi(self.window)
        self.window.show()

    def openWindow10(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Watanay()
        self.ui.setupUi(self.window)
        self.window.show()

    def openWindow11(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_TrpSv()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setObjectName("Form")
        Form.setFixedSize(965, 658)
        Form.setStyleSheet("background-color: rgb(125, 125, 125);\n"
                           "border-color: rgb(255, 255, 255);")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollArea.setMinimumSize(QtCore.QSize(950, 658))
        self.scrollArea.setMaximumSize(QtCore.QSize(1677799, 1677729))
        self.scrollArea.setWidgetResizable(True)

        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_11 = QtWidgets.QPushButton(self.scrollAreaWidgetContents,clicked=lambda:self.openWindow1())
        self.pushButton_11.setObjectName("pushButton_11")
        self.verticalLayout.addWidget(self.pushButton_11)
        self.pushButton_12 = QtWidgets.QPushButton(self.scrollAreaWidgetContents,clicked=lambda:self.openWindow2())
        self.pushButton_12.setObjectName("pushButton_12")
        self.verticalLayout.addWidget(self.pushButton_12)
        self.pushButton_13 = QtWidgets.QPushButton(self.scrollAreaWidgetContents,clicked=lambda:self.openWindow3())
        self.pushButton_13.setObjectName("pushButton_13")
        self.verticalLayout.addWidget(self.pushButton_13)
        self.pushButton_14 = QtWidgets.QPushButton(self.scrollAreaWidgetContents,clicked=lambda:self.openWindow4())
        self.pushButton_14.setObjectName("pushButton_14")
        self.verticalLayout.addWidget(self.pushButton_14)
        self.pushButton_15 = QtWidgets.QPushButton(self.scrollAreaWidgetContents,clicked=lambda:self.openWindow5())
        self.pushButton_15.setObjectName("pushButton_15")
        self.verticalLayout.addWidget(self.pushButton_15)
        self.pushButton_16 = QtWidgets.QPushButton(self.scrollAreaWidgetContents,clicked=lambda:self.openWindow6())
        self.pushButton_16.setObjectName("pushButton_16")
        self.verticalLayout.addWidget(self.pushButton_16)
        self.pushButton_17 = QtWidgets.QPushButton(self.scrollAreaWidgetContents,clicked=lambda:self.openWindow7())
        self.pushButton_17.setObjectName("pushButton_17")
        self.verticalLayout.addWidget(self.pushButton_17)
        self.pushButton_18 = QtWidgets.QPushButton(self.scrollAreaWidgetContents,clicked=lambda:self.openWindow8())
        self.pushButton_18.setObjectName("pushButton_18")
        self.verticalLayout.addWidget(self.pushButton_18)
        self.pushButton_19 = QtWidgets.QPushButton(self.scrollAreaWidgetContents,clicked=lambda:self.openWindow9())
        self.pushButton_19.setObjectName("pushButton_19")
        self.verticalLayout.addWidget(self.pushButton_19)
        self.pushButton_20 = QtWidgets.QPushButton(self.scrollAreaWidgetContents,clicked=lambda:self.openWindow10())
        self.pushButton_20.setObjectName("pushButton_20")
        self.verticalLayout.addWidget(self.pushButton_20)
        self.pushButton_21 = QtWidgets.QPushButton(self.scrollAreaWidgetContents,clicked=lambda:self.openWindow11())
        self.pushButton_21.setObjectName("pushButton_21")
        self.verticalLayout.addWidget(self.pushButton_21)
        self.pushButton_22 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_22.setObjectName("pushButton_22")
        self.verticalLayout.addWidget(self.pushButton_22)
        self.pushButton_23 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_23.setObjectName("pushButton_23")
        self.verticalLayout.addWidget(self.pushButton_23)
        self.pushButton_24 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_24.setObjectName("pushButton_24")
        self.verticalLayout.addWidget(self.pushButton_24)
        self.pushButton_25 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_25.setObjectName("pushButton_25")
        self.verticalLayout.addWidget(self.pushButton_25)
        self.pushButton_26 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_26.setObjectName("pushButton_26")
        self.verticalLayout.addWidget(self.pushButton_26)
        self.pushButton_27 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_27.setObjectName("pushButton_27")
        self.verticalLayout.addWidget(self.pushButton_27)
        self.pushButton_28 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_28.setObjectName("pushButton_28")
        self.verticalLayout.addWidget(self.pushButton_28)
        self.pushButton_29 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_29.setObjectName("pushButton_29")
        self.verticalLayout.addWidget(self.pushButton_29)
        self.pushButton_30 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_30.setObjectName("pushButton_30")
        self.verticalLayout.addWidget(self.pushButton_30)
        self.pushButton_31 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_31.setObjectName("pushButton_31")
        self.verticalLayout.addWidget(self.pushButton_31)
        self.pushButton_6 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout.addWidget(self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout.addWidget(self.pushButton_7)
        self.pushButton_8 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout.addWidget(self.pushButton_8)
        self.pushButton_9 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_9.setObjectName("pushButton_9")
        self.verticalLayout.addWidget(self.pushButton_9)
        self.pushButton_10 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_10.setObjectName("pushButton_10")
        self.verticalLayout.addWidget(self.pushButton_10)
        self.pushButton_5 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout.addWidget(self.pushButton_5)
        self.pushButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.addWidget(self.scrollArea)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.add_song_button = QtWidgets.QPushButton(Form)
        self.add_song_button.setGeometry(QtCore.QRect(13, 1, 75, 23))
        self.add_song_button.setObjectName("add_song_button")
        self.add_song_button.setText(_translate("Form", "Přidat píseň"))
        self.add_song_button.clicked.connect(self.openAddSongWindow)
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Písně"))
        self.pushButton_11.setText(_translate("Form", "Ved me dal cesto ma"))
        self.pushButton_12.setText(_translate("Form", "Severni vitr"))
        self.pushButton_13.setText(_translate("Form", "Kde domov muj"))
        self.pushButton_14.setText(_translate("Form", "Montgomery"))
        self.pushButton_15.setText(_translate("Form", "Báječná ženská"))
        self.pushButton_16.setText(_translate("Form", "Purpura"))
        self.pushButton_17.setText(_translate("Form", "Bláznova ukolébavka"))
        self.pushButton_18.setText(_translate("Form", "Klobouk ve křoví"))
        self.pushButton_19.setText(_translate("Form", "My tři králové"))
        self.pushButton_20.setText(_translate("Form", "Ho Ho Watanay"))
        self.pushButton_21.setText(_translate("Form", "Trpasličí svatba"))
        self.pushButton_22.setText(_translate("Form", "PushButton"))
        self.pushButton_23.setText(_translate("Form", "PushButton"))
        self.pushButton_24.setText(_translate("Form", "PushButton"))
        self.pushButton_25.setText(_translate("Form", "PushButton"))
        self.pushButton_26.setText(_translate("Form", "PushButton"))
        self.pushButton_27.setText(_translate("Form", "PushButton"))
        self.pushButton_28.setText(_translate("Form", "PushButton"))
        self.pushButton_29.setText(_translate("Form", "PushButton"))
        self.pushButton_30.setText(_translate("Form", "PushButton"))
        self.pushButton_31.setText(_translate("Form", "PushButton"))
        self.pushButton_6.setText(_translate("Form", "PushButton"))
        self.pushButton_7.setText(_translate("Form", "PushButton"))
        self.pushButton_8.setText(_translate("Form", "PushButton"))
        self.pushButton_9.setText(_translate("Form", "PushButton"))
        self.pushButton_10.setText(_translate("Form", "PushButton"))
        self.pushButton_5.setText(_translate("Form", "PushButton"))
        self.pushButton.setText(_translate("Form", "PushButton"))
        self.pushButton_2.setText(_translate("Form", "PushButton"))
        self.pushButton_3.setText(_translate("Form", "PushButton"))
        self.pushButton_4.setText(_translate("Form", "PushButton"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Pisne()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
