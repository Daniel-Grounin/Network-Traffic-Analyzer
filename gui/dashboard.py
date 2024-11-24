from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLabel

class Dashboard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Network Traffic Analyzer")
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Welcome to the Network Traffic Analyzer!"))

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
