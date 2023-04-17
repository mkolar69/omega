
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BajZen(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(714, 761)
        Form.setStyleSheet("background-color: rgb(125, 125, 125);\n"
                           "border-color: rgb(255, 255, 255);")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 70, 71, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 100, 300, 641))
        self.label_3.setStyleSheet("background-color: rgb(104, 104, 104);\n"
                                   "gridline-color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 30, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.treeWidget = QtWidgets.QTreeWidget(Form)
        self.treeWidget.setGeometry(QtCore.QRect(340, 100, 310, 400))
        self.treeWidget.setStyleSheet(
            "background-color: rgb(209, 209, 209);\n""background-image: url(C:\\Users\\matej\\PycharmProjects\\omega\\script\\Main\\pics\\akordy5.png);")
        self.treeWidget.setObjectName("treeWidget")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.treeWidget.headerItem().setFont(0, font)
        self.treeWidget.setIndentation(1)

        header = QtWidgets.QTreeWidgetItem(self.treeWidget)
        self.treeWidget.headerItem().setText(0, "Akordy")
        label = QtWidgets.QLabel()
        pixmap = QtGui.QPixmap('C:\\Users\\matej\\PycharmProjects\\omega\\script\\Main\\pics\\akordy5.png')
        label.setPixmap(pixmap)
        self.treeWidget.setItemWidget(header, 0, label)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Báječná ženská"))
        self.label.setText(_translate("Form", "Báječná ženská"))
        self.label_2.setText(_translate("Form", "Michal Tučný"))
        self.label_3.setText(_translate("Form", "Začínám já \n"
"\n"
"         G                                          C\n"
"1. Tenhle příběh je pravda, ať visím, jestli vám budu lhát,\n"
"         D7                                           G\n"
"   já jsem potkal jednu dívku a do dnešního dne ji mám rád,\n"
"                                                  C\n"
"   nikdy neměla zlost, když jsem hluboko do kapsy měl,\n"
"           D7                                           G\n"
"   vždycky měla pochopení a já se s ní nikdy hádat nemusel.\n"
"\n"
"           G                                   C\n"
"R: Když si báječnou ženskou vezme báječnej chlap,\n"
"            D7                                        G\n"
"   tak mají báječnej život plnej báječnejch dní bez útrap,\n"
"                                                    C\n"
"   celej den jen tak sedí a popíjejí Châteauneuf-du-Pape,\n"
"           D7                              G\n"
"   když si báječnou ženskou vezme báječnej chlap.\n"
"\n"
"        G                                            C\n"
"2. Nikdy jsem neslyšel: kam jdeš, kdy přijdeš a kde jsi byl,\n"
"        D7                                       G\n"
"   a já nikdy nezapomněl, abych svoje sliby vyplnil,\n"
"                                                       C\n"
"   a když vzpomínala, tak jen na to hezký, co nám život dal,\n"
"         D7                                        G\n"
"   nedala mi příležitost, na co bych si taky stěžoval.\n"
"\n"
"R:\n"
"         G                                                    C\n"
"3. Tenhle příběh je pravda a sním svůj klobouk, jestli jsem vám\n"
"   lhal,\n"
"          D7                                              G\n"
"   že jsem potkal jednu dívku a tu dívku jsem si za ženu vzal,\n"
"                                        C\n"
"   zní to jako pohádka z oříšku královny Máb,\n"
"          D7                                    G\n"
"   že si báječnou ženskou vzal jeden báječnej chlap.\n"
"\n"
"           G                               C\n"
"R: Když si báječnou ženskou vezme báječnej chlap,\n"
"            D7                                  G      \n"
"   tak mají báječnej život plnej báječnejch dní bez útrap,\n"
"                                                    C\n"
"   celej den jen tak sedí a popíjejí Châteauneuf-du-Pape,\n"
"           D7                              G\n"
"   když si báječnou ženskou vezme báječnej chlap. + 4 takty G"))
        self.label.setText(_translate("Form", "Báječná ženská"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_BajZen()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
