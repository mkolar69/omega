import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from Menu import Ui_Menu
app = QtWidgets.QApplication(sys.argv)
from Settings import Ui_SettingsWindow

class Ui_MainWindow(object):

    def openWindow(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_Menu()
        self.ui.setupUi(self.window)
        self.window.show()

    def openSettingsWindow(self):
        self.settingsWindow = QtWidgets.QMainWindow()
        self.settingsUi = Ui_SettingsWindow()
        self.settingsUi.setupUi(self.settingsWindow)
        self.settingsWindow.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(125, 125, 125);\n"
                           "border-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Start = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.openWindow())
        self.Start.setGeometry(QtCore.QRect(280, 230, 271, 171))
        self.Start.setObjectName("Start")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 70, 431, 131))
        font = QtGui.QFont()
        font.setPointSize(72)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuCategories = QtWidgets.QMenu(self.menubar)
        self.menuCategories.setObjectName("menuCategories")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuCategories.addSeparator()
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuCategories.menuAction())

        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.menuSettings.addAction(self.actionSettings)
        self.actionSettings.triggered.connect(self.openSettingsWindow)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Zpěvník"))
        self.Start.setText(_translate("MainWindow", "Click "))
        self.label.setText(_translate("MainWindow", "SongBook"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.menuCategories.setTitle(_translate("MainWindow", "Categories"))




class UI_CategoriesWindow(object):
    def setupUi(self, CategoriesWindow):
        CategoriesWindow.setObjectName("CategoriesWindow")
        CategoriesWindow.resize(800, 600)

        self.centralwidget = QtWidgets.QWidget(CategoriesWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Vytvoření hlavního layoutu
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        # Vytvoření vertikálního layoutu pro nadpis
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        # Nadpis
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        # Vložení vertikálního layoutu s nadpisem do hlavního layoutu
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)

        # Vytvoření layoutu pro tlačítka kategorií
        self.categoriesLayout = QtWidgets.QVBoxLayout()
        self.categoriesLayout.setObjectName("categoriesLayout")

        # Tlačítka kategorií
        self.buttonCategory1 = QtWidgets.QPushButton(self.centralwidget)
        self.buttonCategory1.setObjectName("buttonCategory1")
        self.categoriesLayout.addWidget(self.buttonCategory1)

        self.buttonCategory2 = QtWidgets.QPushButton(self.centralwidget)
        self.buttonCategory2.setObjectName("buttonCategory2")
        self.categoriesLayout.addWidget(self.buttonCategory2)

        self.buttonCategory3 = QtWidgets.QPushButton(self.centralwidget)
        self.buttonCategory3.setObjectName("buttonCategory3")
        self.categoriesLayout.addWidget(self.buttonCategory3)

        # Vložení layoutu s tlačítky kategorií do hlavního layoutu
        self.gridLayout.addLayout(self.categoriesLayout, 2, 0, 1, 1)

        # Propojení tlačítek kategorií s funkcí pro zobrazení kategorií
        self.buttonCategory1.clicked.connect(lambda: self.showSongsWindow('Kategorie 1'))
        self.buttonCategory2.clicked.connect(lambda: self.showSongsWindow('Kategorie 2'))
        self.buttonCategory3.clicked.connect(lambda: self.showSongsWindow('Kategorie 3'))

        CategoriesWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(CategoriesWindow)
        QtCore.QMetaObject.connectSlotsByName(CategoriesWindow)

    def retranslateUi(self, CategoriesWindow):
        _translate = QtCore.QCoreApplication.translate
        CategoriesWindow.setWindowTitle(_translate("CategoriesWindow", "Kategorie"))
        self.label.setText(_translate("CategoriesWindow", "Výběr kategorie"))
        self.buttonCategory1.setText(_translate("CategoriesWindow", "Kategorie 1"))
        self.buttonCategory2.setText(_translate("CategoriesWindow", "Kategorie 2"))
        self.buttonCategory3.setText(_translate("CategoriesWindow", "Kategorie 3"))

    def showSongsWindow(self, category):
        # Zavření okna s kategoriemi
        CategoriesWindow.close()

        # Vytvoření okna s písněmi
        self.SongsWindow = QtWidgets.QMainWindow()
        self.ui = Ui_SongsWindow()
        self.ui.setupUi(self.SongsWindow, category)
        self.SongsWindow.show()


class Ui_SongsWindow(object):
    def setupUi(self, SongsWindow):
        SongsWindow.setObjectName("SongsWindow")
        SongsWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(SongsWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")

        # přidáme 10 tlačítek s kategoriemi
        self.category_buttons = []
        for i in range(10):
            btn = QtWidgets.QPushButton(self.centralwidget)
            btn.setObjectName("categoryButton_" + str(i))
            btn.setText("Category " + str(i + 1))
            self.category_buttons.append(btn)
            self.gridLayout.addWidget(btn, i, 0, 1, 1)

        self.verticalLayout_2.addLayout(self.gridLayout)
        SongsWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SongsWindow)
        QtCore.QMetaObject.connectSlotsByName(SongsWindow)

    def retranslateUi(self, SongsWindow):
        _translate = QtCore.QCoreApplication.translate
        SongsWindow.setWindowTitle(_translate("SongsWindow", "SongBook"))
        self.label.setText(_translate("SongsWindow", "Choose a category"))

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

class CategoriesWindow(QtWidgets.QMainWindow, UI_CategoriesWindow):
    def __init__(self, parent=None):
        super(CategoriesWindow, self).__init__(parent)
        self.setupUi(self)

class SongsWindow(QtWidgets.QMainWindow, Ui_SongsWindow):
    def __init__(self, parent=None):
        super(SongsWindow, self).__init__(parent)
        self.setupUi(self)
if __name__ == "__main__":
    mainWin = MainWindow()
    categoriesWin = CategoriesWindow()

    mainWin.show()
    sys.exit(app.exec_())