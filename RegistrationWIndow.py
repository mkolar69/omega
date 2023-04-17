import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtCore import Qt

class RegistrationWindow(QDialog):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Registrace')
        self.setFixedSize(300, 250)

        layout = QVBoxLayout()

        self.first_name_label = QLabel('Jméno:')
        self.first_name_input = QLineEdit()
        layout.addWidget(self.first_name_label)
        layout.addWidget(self.first_name_input)

        self.last_name_label = QLabel('Příjmení:')
        self.last_name_input = QLineEdit()
        layout.addWidget(self.last_name_label)
        layout.addWidget(self.last_name_input)

        self.birth_date_label = QLabel('Datum narození:')
        self.birth_date_input = QLineEdit()
        layout.addWidget(self.birth_date_label)
        layout.addWidget(self.birth_date_input)

        self.username_label = QLabel('Uživatelské jméno:')
        self.username_input = QLineEdit()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)

        self.password_label = QLabel('Heslo:')
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)

        self.register_button = QPushButton('Registrovat')
        layout.addWidget(self.register_button)

        self.setLayout(layout)

        self.register_button.clicked.connect(self.register)

    def register(self):
        first_name = self.first_name_input.text()
        last_name = self.last_name_input.text()
        birth_date = self.birth_date_input.text()
        username = self.username_input.text()
        password = self.password_input.text()

        if self.validate_registration(first_name, last_name, birth_date, username, password):
            # TODO: Uložte nového uživatele do slovníku nebo databáze.
            QMessageBox.information(self, 'Registrace úspěšná', 'Účet byl úspěšně založen.')
            self.accept()
        else:
            QMessageBox.warning(self, 'Chyba', 'Nepodařilo se založit účet.')

    def validate_registration(self, first_name, last_name, birth_date, username, password):
        # TODO: Zkontrolujte zda jsou všechny informace platné.
        # Můžete použít regulární výrazy nebo jiné metody.
        return True
def main():
    app = QApplication(sys.argv)

    registration_window=RegistrationWindow()

    registration_window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()