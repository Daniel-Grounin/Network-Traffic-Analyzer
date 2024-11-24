import pyqtgraph as pg
from PyQt6.QtWidgets import QVBoxLayout, QWidget

class RealTimeGraphs(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Graphs for packet statistics
        self.packet_rate_graph = pg.PlotWidget(title="Packet Rate (Packets/sec)")
        self.data_throughput_graph = pg.PlotWidget(title="Data Throughput (Bytes/sec)")

        # Setup packet rate graph
        self.packet_rate_graph.showGrid(x=True, y=True)
        self.packet_rate_graph.setLabel('left', 'Packets', units='count')
        self.packet_rate_graph.setLabel('bottom', 'Time', units='sec')
        self.packet_rate_curve = self.packet_rate_graph.plot(pen='g')

        # Setup data throughput graph
        self.data_throughput_graph.showGrid(x=True, y=True)
        self.data_throughput_graph.setLabel('left', 'Bytes', units='B/sec')
        self.data_throughput_graph.setLabel('bottom', 'Time', units='sec')
        self.data_throughput_curve = self.data_throughput_graph.plot(pen='b')

        self.layout.addWidget(self.packet_rate_graph)
        self.layout.addWidget(self.data_throughput_graph)

        self.packet_rate_data = []
        self.data_throughput_data = []
        self.time_data = []

    def update_graphs(self, time, packet_rate, throughput):
        self.time_data.append(time)
        self.packet_rate_data.append(packet_rate)
        self.data_throughput_data.append(throughput)

        self.packet_rate_curve.setData(self.time_data, self.packet_rate_data)
        self.data_throughput_curve.setData(self.time_data, self.data_throughput_data)
