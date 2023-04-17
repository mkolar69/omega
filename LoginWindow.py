import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, \
    QPushButton, QMessageBox
from PyQt5.QtCore import Qt, QTimer
from PyQt5 import QtCore, QtGui, QtWidgets
from RegistrationWIndow import RegistrationWindow
from script.Main.MainWindow import Ui_MainWindow


class LoginWindow(QDialog):
    def __init__(self):
        super().__init__()

        self.init_ui()
        self.users = {
            'pepan': 'pepa',
            'user2': 'password2',
            'user3': 'password3',
        }

        self.login_attempts = 0
        self.login_timer = QTimer()
        self.login_timer.timeout.connect(self.enable_login)
        self.login_timer.setSingleShot(True)

    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def init_ui(self):
        self.setWindowTitle('Přihlášení')
        self.setFixedSize(300, 150)

        layout = QVBoxLayout()

        self.username_label = QLabel('Uživatelské jméno:')
        self.username_input = QLineEdit()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)

        self.password_label = QLabel('Heslo:')
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)

        buttons_layout = QHBoxLayout()

        self.login_button = QPushButton('Přihlásit se')
        self.register_button = QPushButton('Registrovat')
        buttons_layout.addWidget(self.login_button)
        buttons_layout.addWidget(self.register_button)

        layout.addLayout(buttons_layout)

        self.setLayout(layout)

        self.login_button.clicked.connect(self.login)
        self.register_button.clicked.connect(self.register)

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if self.validate_login(username, password):
            self.accept()
        else:
            self.login_attempts += 1
            if self.login_attempts == 3:
                self.login_button.setDisabled(True)
                self.login_timer.start(15000)
            QMessageBox.warning(self, 'Chyba', 'Nesprávné uživatelské jméno nebo heslo.')

    def register(self):
        self.registration_window = RegistrationWindow()
        self.registration_window.exec()

    def validate_login(self, username, password):
        # TODO: Zde zkontrolujte uživatelské jméno a heslo.
        # Můžete vytvořit slovník pro ukládání uživatelů nebo použít databázi.
        if username in self.users and self.users[username] == password:
            return True
        else:
            return False

    def enable_login(self):
        self.login_attempts = 0
        self.login_button.setDisabled(False)


def main():
    app = QApplication(sys.argv)

    login_window = LoginWindow()

    if login_window.exec() == QDialog.Accepted:
        main_window = QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(main_window)
        main_window.show()
        sys.exit(app.exec_())


if __name__ == '__main__':
    main()
