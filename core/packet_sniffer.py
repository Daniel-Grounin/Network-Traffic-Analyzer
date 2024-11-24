from scapy.all import sniff
import time

class PacketSniffer:
    def __init__(self, graph_callback, table_callback):
        self.graph_callback = graph_callback
        self.table_callback = table_callback
        self.start_time = time.time()

    def process_packet(self, packet):
        timestamp = time.time() - self.start_time
        src_ip = packet[1].src if packet.haslayer("IP") else "Unknown"
        dst_ip = packet[1].dst if packet.haslayer("IP") else "Unknown"
        protocol = packet[1].name if packet.haslayer("IP") else "Other"
        length = len(packet)

        # Update GUI components
        self.graph_callback(timestamp, 1, length)  # 1 packet, `length` bytes
        self.table_callback(timestamp, src_ip, dst_ip, protocol, length)

    def start_sniffing(self, iface):
        sniff(iface=iface, prn=self.process_packet, store=False)
