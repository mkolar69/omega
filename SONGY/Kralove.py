
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Kralove(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(714, 761)
        Form.setStyleSheet("background-color: rgb(125, 125, 125);\n"
                           "border-color: rgb(255, 255, 255);")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 70, 71, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 100, 200, 350))
        self.label_3.setStyleSheet("background-color: rgb(104, 104, 104);\n"
                                   "gridline-color: rgb(2, 200, 2);")
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 30, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.treeWidget = QtWidgets.QTreeWidget(Form)
        self.treeWidget.setGeometry(QtCore.QRect(340, 100, 320, 390))
        self.treeWidget.setStyleSheet(
            "background-color: rgb(209, 209, 209);\n""background-image: url(C:\\Users\\matej\\PycharmProjects\\omega\\script\\Main\\pics\\akordy9.png);")
        self.treeWidget.setObjectName("treeWidget")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.treeWidget.headerItem().setFont(0, font)
        self.treeWidget.setIndentation(1)

        header = QtWidgets.QTreeWidgetItem(self.treeWidget)
        self.treeWidget.headerItem().setText(0, "Akordy")
        label = QtWidgets.QLabel()
        pixmap = QtGui.QPixmap('C:\\Users\\matej\\PycharmProjects\\omega\\script\\Main\\pics\\akordy9.png')
        label.setPixmap(pixmap)
        self.treeWidget.setItemWidget(header, 0, label)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "My tři králové"))
        self.label_2.setText(_translate("Form", "Vánoční koledy"))
        self.label.setText(_translate("Form", "My tři králové"))
        self.label_3.setText(_translate("Form", "   G   f# Em Am D D7 G\n"
"1. My tři králové jdeme k vám,\n"
"   C   Em  Am  D   D  D7    G\n"
"   štěstí, zdraví, vinšujem vám.\n"
"\n"
"2. Štěstí, zdraví, dlouhá léta,\n"
"   my jsme k vám přisli z daleka.\n"
"\n"
"3. Z daleka je cesta naše,\n"
"   do Betléma mysl naše.\n"
"\n"
"4. Co ty, černej, stojíš vzadu,\n"
"   vystrkuješ na nás bradu.\n"
"\n"
"5. A já černej vystupuju,\n"
"   a Nový rok vám vinšuju.\n"
"\n"
"6. A my taky vystupujem\n"
"   a Nový rok vám vinšujem."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Kralove()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
