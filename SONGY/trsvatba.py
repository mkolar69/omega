
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TrpSv(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(714, 765)
        Form.setStyleSheet("background-color: rgb(125, 125, 125);")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 30, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 100, 241, 601))
        self.label_3.setStyleSheet("background-color: rgb(104, 104, 104);\n""gridline-color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 70, 151, 31))
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.treeWidget = QtWidgets.QTreeWidget(Form)
        self.treeWidget.setGeometry(QtCore.QRect(330, 100, 310, 601))
        self.treeWidget.setStyleSheet("background-color: rgb(209, 209, 209);\n""background-image: url(C:\\Users\\matej\\PycharmProjects\\omega\\script\\Main\\pics\\akordy4.png);")
        self.treeWidget.setObjectName("treeWidget")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.treeWidget.headerItem().setFont(0, font)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Trpasličí svatba"))
        self.label.setText(_translate("Form", "Trpasličí svatba"))
        self.label_3.setText(_translate("Form", "   G                 C       G\n"
"1. V lese, jó v lese na jehličí,\n"
"                  A      D7\n"
"   koná se svatba trpasličí,\n"
"   G           C        H7\n"
"   žádná divná věc to není,\n"
"   C      C#dim G     Emi  A        D7  (D)\n"
"   Šmudla už má po vojně a tak se žení.\n"
"   Malou má ženu, malinkatou,\n"
"   s malým věnem, malou chatou.\n"
"   Už jim choděj\' telegrámky,\n"
"   už jim hrajou Mendelssohna na varhánky.\n"
"\n"
"           D                            G\n"
"R. Protože láska, láska, láska v každém srdci klíčí,\n"
"           D                      G\n"
"   protože láskou hoří i to srdce trpasličí\n"
"              D                    G\n"
"   a kdo se v téhle věci jednoduše neopičí,\n"
"             D                       G       D    D7\n"
"   ten ať se dívá, co se děje v lese na jehličí.\n"
"\n"
"2. Mají tam lásku, jako trámek,\n"
"   pláče tchyňka, pláče tchánek,\n"
"   štěstíčko přejou mladí, staří,\n"
"   v papinově hrníčku se maso vaří.\n"
"   Pijou tam pivo popovický, (ale jen malý),\n"
"   Šmudla se polil, jako vždycky,\n"
"   Kejchal kejchá na Profouse,\n"
"   jedí hrášek s uzeným a nafouknou se.\n"
"\n"
"R. Protože láska, .....\n"
"\n"
"3. V lese, jó v lese na jehličí,\n"
"   koná se svatba trpasličí,\n"
"   žádná divná věc to není,\n"
"   Šmudla už má po vojně\n"
"   a Šmudla už má po vojně\n"
"   a Šmudla už má po vojně\n"
"   a tak se žení."))
        self.label_2.setText(_translate("Form", "Fešáci"))
        self.treeWidget.setIndentation(1)
        header = QtWidgets.QTreeWidgetItem(self.treeWidget)

        self.treeWidget.headerItem().setText(0, "Akordy")
        label = QtWidgets.QLabel()
        pixmap = QtGui.QPixmap('C:\\Users\\matej\\PycharmProjects\\omega\\script\\Main\\pics\\akordy4.png')
        label.setPixmap(pixmap)
        self.treeWidget.setItemWidget(header, 0, label)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_TrpSv()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
