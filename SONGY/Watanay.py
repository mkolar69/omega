
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Watanay(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(711, 761)
        Form.setStyleSheet("background-color: rgb(125, 125, 125);\n"
                           "border-color: rgb(255, 255, 255);")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 10, 150, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 80, 300, 311))
        self.label_3.setStyleSheet("background-color: rgb(104, 104, 104);\n"
                                   "gridline-color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 50, 91, 31))
        self.label_2.setObjectName("label_2")
        self.treeWidget = QtWidgets.QTreeWidget(Form)
        self.treeWidget.setGeometry(QtCore.QRect(330, 80, 320, 200))
        self.treeWidget.setStyleSheet(
            "background-color: rgb(209, 209, 209);\n""background-image: url(C:\\Users\\matej\\PycharmProjects\\omega\\script\\Main\\pics\\akordy10.png);")
        self.treeWidget.setObjectName("treeWidget")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.treeWidget.headerItem().setFont(0, font)
        self.treeWidget.setIndentation(1)

        header = QtWidgets.QTreeWidgetItem(self.treeWidget)
        self.treeWidget.headerItem().setText(0, "Akordy")
        label = QtWidgets.QLabel()
        pixmap = QtGui.QPixmap('C:\\Users\\matej\\PycharmProjects\\omega\\script\\Main\\pics\\akordy10.png')
        label.setPixmap(pixmap)
        self.treeWidget.setItemWidget(header, 0, label)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "  D\n"
"1. Spinkej můj maličký\n"
"   C           D\n"
"   máš v očích hvězdičky\n"
"             C            G          D\n"
"   dám ti je do vlasů tak usínej tak usínej\n"
"\n"
"   D             C     D\n"
"R: Ho ho Watanay ho ho Watanay\n"
"         C       G       D\n"
"   ho ho Watanay kiokena kiokena\n"
"\n"
"2. Sladkou vůňi nese ti\n"
"   noční motýl z paseky\n"
"   vánek ho políbá už usíná už usíná\n"
"   \n"
"3. V lukách cosi zavoní\n"
"   rád jezdíš na koni\n"
"   má barvu havraní jak uhání jak uhání\n"
"   \n"
"4. V dlani motýl usína\n"
"   hvězdička už zhasíná\n"
"   vánek co ji k tobě nes až do léta ti odlétá\n"
"\n"
"R: Ho ho Watanay..."))
        self.label_2.setText(_translate("Form", "Maxim Turbulec"))
        self.label.setText(_translate("Form", "Ho Ho Watanay"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Watanay()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
