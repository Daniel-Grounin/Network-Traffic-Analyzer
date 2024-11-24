from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QTableWidget, QTableWidgetItem, QPushButton, QHBoxLayout
from PyQt6.QtCore import Qt

class Dashboard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Network Traffic Analyzer")
        self.setGeometry(100, 100, 800, 600)

        # Main layout
        layout = QVBoxLayout()

        # Packet table
        self.packet_table = QTableWidget()
        self.packet_table.setColumnCount(5)
        self.packet_table.setHorizontalHeaderLabels(["Time", "Source IP", "Destination IP", "Protocol", "Length"])
        layout.addWidget(self.packet_table)

        # Buttons
        btn_layout = QHBoxLayout()
        self.start_btn = QPushButton("Start Capture")
        self.stop_btn = QPushButton("Stop Capture")
        self.export_btn = QPushButton("Export")
        btn_layout.addWidget(self.start_btn)
        btn_layout.addWidget(self.stop_btn)
        btn_layout.addWidget(self.export_btn)
        layout.addLayout(btn_layout)

        # Set central widget
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Connect buttons to actions
        self.start_btn.clicked.connect(self.start_capture)
        self.stop_btn.clicked.connect(self.stop_capture)
        self.export_btn.clicked.connect(self.export_data)

    def start_capture(self):
        # Placeholder for starting packet capture
        print("Starting packet capture...")

    def stop_capture(self):
        # Placeholder for stopping packet capture
        print("Stopping packet capture...")

    def export_data(self):
        # Placeholder for exporting data
        print("Exporting data...")
