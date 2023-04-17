# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Montgomery(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(714, 722)
        Form.setStyleSheet("background-color: rgb(125, 125, 125);\n"
                           "border-color: rgb(255, 255, 255);")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 10, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 50, 71, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(30, 80, 260, 611))
        self.label_3.setStyleSheet("background-color: rgb(104, 104, 104);\n"
                                   "gridline-color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.treeWidget = QtWidgets.QTreeWidget(Form)
        self.treeWidget.setGeometry(QtCore.QRect(330, 100, 310, 400))
        self.treeWidget.setStyleSheet(
            "background-color: rgb(209, 209, 209);\n""background-image: url(C:\\Users\\matej\\PycharmProjects\\omega\\script\\Main\\pics\\akordy3.png);")
        self.treeWidget.setObjectName("treeWidget")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.treeWidget.headerItem().setFont(0, font)
        self.treeWidget.setIndentation(1)

        header = QtWidgets.QTreeWidgetItem(self.treeWidget)
        self.treeWidget.headerItem().setText(0, "Akordy")
        label = QtWidgets.QLabel()
        pixmap = QtGui.QPixmap('C:\\Users\\matej\\PycharmProjects\\omega\\script\\Main\\pics\\akordy3.png')
        label.setPixmap(pixmap)
        self.treeWidget.setItemWidget(header, 0, label)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Montgomery"))
        self.label.setText(_translate("Form", "Montgomery"))
        self.label_2.setText(_translate("Form", "Wabi Daněk"))
        self.label_3.setText(_translate("Form", " Celá sloka mandolína\n"
"   G                          C    Ami\n"
"1. Déšť ti, holka, smáčel vlasy, smáčel vlasy,\n"
"   D7                         G   D7\n"
"   z tvých očí zbyl prázdný kruh,\n"
"   G                        C     Ami\n"
"   kde jsou zbytky tvojí krásy, tvojí krásy,\n"
"   D7                    G   D7\n"
"   to ví dneska snad jen Bůh.\n"
"\n"
"   G                    C      Ami\n"
"R: Z celé jižní eskadrony, eskadrony\n"
"   D7                G   D7\n"
"   nezbyl ani jeden muž (ani kuš!),\n"
"   G                     C    Ami\n"
"   v Montgomery bijou zvony, bijou zvony (blijou sloni),\n"
"   D7                    G   D7\n"
"   déšť ti smejvá ze rtů rúž.\n"
"\n"
"   G                        C       Ami\n"
"2. Na kopečku v prachu cesty, v prachu cesty\n"
"   D7              G    D7\n"
"   leží i tvůj generál,\n"
"   G                    C         Ami\n"
"   v ruce šátek od nevěsty, od nevěsty,\n"
"   D7            G  D7\n"
"   ale ruka leží dál.\n"
"R:\n"
" SOLO MANDOLINA\n"
"    G                       C            Ami\n"
"3. Tvář má zšedivělou strachem, no vážně strachem,\n"
"   D7                         G  D7\n"
"   zbylo v ní pár těžkejch chvil,\n"
"   G                        C       Ami\n"
"   proužek krve stéká prachem, stéká prachem,\n"
"   D7                        G  D7\n"
"   déšť mu slepil vlas jak jíl.\n"
"R:\n"
"   G                      C       Ami \n"
"4. Déšť ti šeptá jeho jméno, jeho jméno,\n"
"   D7               G D7\n"
"   šeptá ho i listoví,\n"
"   G                        C         Ami\n"
"   lásku měl rád víc než život, víc než život,\n"
"   D7               G D7\n"
"   to ti nikdy nepoví.\n"
"R:                                + G  D7  G"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Montgomery()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
