from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_C(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(725, 633)
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setGeometry(QtCore.QRect(0, 60, 731, 571))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 729, 569))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setGeometry(QtCore.QRect(20, 60, 681, 291))
        self.label_3.setStyleSheet(
            "background-image: url(C:\\Users\\matej\\PycharmProjects\\omega\\script\\Main\\pics\\akordy11.png);")
        self.label_3.setText("")
        self.label_3.setPixmap(
            QtGui.QPixmap("C:\\Users\\matej\\PycharmProjects\\omega\\script\\Main\\pics\\akordy11.png"))
        self.label_3.setObjectName("label_3")

        self.line_3 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_3.setGeometry(QtCore.QRect(20, 350, 91, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(260, 0, 191, 71))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(260, 10, 151, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(260, 50, 151, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_4.setGeometry(QtCore.QRect(30, 380, 681, 291))
        self.label_4.setStyleSheet(
            "background-image: url(C:\\Users\\matej\\PycharmProjects\\omega\\script\\Main\\pics\\akordy12.png);")
        self.label_4.setText("")
        self.label_4.setPixmap(
            QtGui.QPixmap("C:\\Users\\matej\\PycharmProjects\\omega\\script\\Main\\pics\\akordy12.png"))
        self.label_4.setObjectName("label_3")

        self.line_4 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_4.setGeometry(QtCore.QRect(30, 680, 91, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Základní akordy"))
        self.label.setText(_translate("Form", "Akordy C"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_C()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
