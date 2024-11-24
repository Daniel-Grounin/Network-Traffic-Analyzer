from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QListWidget

class PacketDetails(QWidget):
    def __init__(self, packets):
        super().__init__()
        self.setWindowTitle("Packet Details")
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Captured Packets:"))

        self.packet_list = QListWidget()
        for packet in packets:
            self.packet_list.addItem(packet)

        layout.addWidget(self.packet_list)
        self.setLayout(layout)
