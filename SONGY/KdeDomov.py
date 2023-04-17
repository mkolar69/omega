
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Kdedomov(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(714, 722)
        Form.setStyleSheet("background-color: rgb(125, 125, 125);\n"
                           "border-color: rgb(255, 255, 255);")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 10, 150, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 50, 71, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(30, 100, 240, 400))
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
        Form.setWindowTitle(_translate("Form", "Kde domov můj"))
        self.label.setText(_translate("Form", "Kde domov můj"))
        self.label_2.setText(_translate("Form", "hymny"))
        self.label_3.setText(_translate("Form", "   A         E7             A\n"
"1. Kde domov můj, kde domov můj?\n"
"   A7   D         A\n"
"   Voda hučí po lučinách,\n"
"        D          A\n"
"   bory šumí po skalinách,\n"
"          E7           A\n"
"   v sadě skví se jara květ,\n"
"          E7          A\n"
"   zemský ráj to na pohled.\n"
"        C#           F#mi D\n"
"   A to je ta krásná země,\n"
"        A E7           A  D\n"
"   země česká, domov můj,\n"
"        A E7         A\n"
"   země česká, domov můj!\n"
"\n"
"2. Kde domov můj, kde domov můj?\n"
"   V kraji znáš-li bohumilém\n"
"   duše útlé v těle čilém,\n"
"   mysl jasnou, vznik a zdar,\n"
"   a tu sílu vzdoru zmar!\n"
"   To je Čechů slavné plémě,\n"
"   mezi Čechy domov můj,\n"
"   mezi Čechy domov můj."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Kdedomov()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
