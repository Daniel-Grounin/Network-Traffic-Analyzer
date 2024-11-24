from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QMenuBar, QTextEdit
from PyQt6.QtGui import QAction
from gui.graphs import RealTimeGraphs
from gui.table_view import PacketTable
from core.packet_sniffer import PacketSniffer
import threading

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Network Traffic Analyzer")

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.graphs = RealTimeGraphs()
        self.table = PacketTable()

        self.layout.addWidget(self.graphs)
        self.layout.addWidget(self.table)

        # Menu
        menu = self.menuBar().addMenu("File")
        start_action = QAction("Start Sniffing", self)
        start_action.triggered.connect(self.start_sniffing)
        menu.addAction(start_action)

        self.sniffer = PacketSniffer(self.graphs.update_graphs, self.table.add_packet)

    def start_sniffing(self):
        iface = "WIFICARDNAME" # Replace with your network interface
        threading.Thread(target=self.sniffer.start_sniffing, args=(iface,)).start()

app = QApplication([])
window = MainWindow()
window.show()
app.exec()



