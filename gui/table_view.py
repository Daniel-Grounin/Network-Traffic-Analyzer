from PyQt6.QtWidgets import QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget

class PacketTable(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.table = QTableWidget(0, 5)  # Create table with 5 columns
        self.table.setHorizontalHeaderLabels(["Timestamp", "Source IP", "Destination IP", "Protocol", "Length"])
        self.layout.addWidget(self.table)

    def add_packet(self, timestamp, src_ip, dst_ip, protocol, length):
        row = self.table.rowCount()
        self.table.insertRow(row)
        self.table.setItem(row, 0, QTableWidgetItem(str(timestamp)))
        self.table.setItem(row, 1, QTableWidgetItem(src_ip))
        self.table.setItem(row, 2, QTableWidgetItem(dst_ip))
        self.table.setItem(row, 3, QTableWidgetItem(protocol))
        self.table.setItem(row, 4, QTableWidgetItem(str(length)))
