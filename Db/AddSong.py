from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QPlainTextEdit, QVBoxLayout, QComboBox
from PyQt5 import QtWidgets
from script.Main.Db.database import save_song_to_db

class AddSongWindow(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Přidat píseň")

        layout = QVBoxLayout()

        self.song_title_label = QLabel("Název písně:")
        self.song_title_input = QLineEdit()
        layout.addWidget(self.song_title_label)
        layout.addWidget(self.song_title_input)

        self.author_name_label = QLabel("Jméno autora/autorů:")
        self.author_name_input = QLineEdit()
        layout.addWidget(self.author_name_label)
        layout.addWidget(self.author_name_input)

        self.category_label = QLabel("Kategorie písně:")
        self.category_input = QComboBox()
        self.category_input.addItems(["Klasicke ", "Country", "Koledy","Jezz","Hymny","Pohadky"])
        layout.addWidget(self.category_label)
        layout.addWidget(self.category_input)

        self.song_text_label = QLabel("Text písně:")
        self.song_text_input = QPlainTextEdit()
        layout.addWidget(self.song_text_label)
        layout.addWidget(self.song_text_input)

        self.save_button = QtWidgets.QPushButton("Uložit")
        layout.addWidget(self.save_button)

        # Připojení signálu pro uložení písně
        self.save_button.clicked.connect(self.save_song)

        self.setLayout(layout)

    def save_song(self):
        title = self.song_title_input.text()
        author = self.author_name_input.text()
        category = self.category_input.currentText()
        lyrics = self.song_text_input.toPlainText()

        save_song_to_db(title, author, category, lyrics)

        print("Úspěšně uloženo!")
        self.close()