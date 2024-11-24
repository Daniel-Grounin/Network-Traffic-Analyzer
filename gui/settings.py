from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class Settings(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Settings")
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Interface:"))

        self.interface_input = QLineEdit()
        layout.addWidget(self.interface_input)

        self.save_button = QPushButton("Save")
        layout.addWidget(self.save_button)

        self.setLayout(layout)
