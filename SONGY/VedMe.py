

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VedDal(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(712, 710)
        Form.setStyleSheet("background-color: rgb(125, 125, 125);\n"
                           "border-color: rgb(255, 255, 255);")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 80, 275, 611))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 20, 451, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(40, 60, 60, 13))
        self.label.setStyleSheet("background-color: rgb(104, 104, 104);\n"
                                   "gridline-color: rgb(255, 255, 255);")
        self.label.setObjectName("label_1")
        self.treeWidget = QtWidgets.QTreeWidget(Form)
        self.treeWidget.setGeometry(QtCore.QRect(330, 80, 310, 601))
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
        Form.setWindowTitle(_translate("Form", "Veď mě dál, cesto má"))
        self.label.setText(_translate("Form", "G              Emi\n"
"1. Někde v dálce cesty končí,\n"
"   D              C          G\n"
"   každá prý však cíl svůj skrývá, \n"
"   G             Emi\n"
"   někde v dálce každá má svůj cíl,\n"
"   D                     C          G\n"
"   ať je pár mil dlouhá, nebo tisíc mil.\n"
"\n"
"           G          D        Emi           C\n"
"R: Veď mě dál, cesto má, veď mě dál, vždyť i já\n"
"               G                 D            C         G\n"
"   tam, kde končíš, chtěl bych dojít, veď mě dál, cesto má.\n"
"   \n"
"   G             Emi\n"
"2. Chodím dlouho po všech cestách,\n"
"   D                 C            G\n"
"   všechny znám je, jen ta má mi zbývá,\n"
"   G                Emi\n"
"   je jak dívky, co jsem měl tak rád,\n"
"   D                C              G\n"
"   plná žáru bývá, hned zas samý chlad.\n"
"\n"
"   G                 D          Emi          C\n"
"R: Veď mě dál, cesto má, veď mě dál, vždyť i já\n"
"               G                  D            C         G\n"
"   tam, kde končíš, chtěl bych dojít, veď mě dál, cesto má.\n"
"\n"
"   Emi        D        G\n"
"*: Pak na patník poslední napíšu křídou\n"
"    C           G                 D\n"
"   jméno své, a pod něj, že jsem žil hrozně rád,\n"
"   Emi                F\n"
"   písně své, co mi v kapsách zbydou,\n"
"   C             G             D                 D7\n"
"   dám si bandou cvrčků hrát a půjdu spát, půjdu spát.\n"
"\n"
"   G                 D          Emi          C\n"
"R Veď mě dál, cesto má, veď mě dál, vždyť i já\n"
"               G                  D            C         G\n"
"   tam, kde končíš, chtěl bych dojít, veď mě dál, cesto má.\n"
"\n"
"          E         A\n"
"|: Veď mě dál cesto má. :|"))
        self.label_2.setText(_translate("Form", "Veď mě dál, cesto má "))
        self.label_3.setText(_translate("Form", "Pavel Bobek"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_VedDal()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
