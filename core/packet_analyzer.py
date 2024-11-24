from scapy.all import *

class PacketAnalyzer:
    def __init__(self):
        self.captured_packets = []

    def analyze_packet(self, packet):
        """Analyze and store a packet."""
        packet_summary = packet.summary()
        self.captured_packets.append(packet_summary)
        return packet_summary
