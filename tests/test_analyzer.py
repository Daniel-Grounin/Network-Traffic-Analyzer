import unittest
from core.packet_analyzer import PacketAnalyzer

class TestPacketAnalyzer(unittest.TestCase):
    def test_analyze_packet(self):
        analyzer = PacketAnalyzer()
        result = analyzer.analyze_packet("Dummy Packet")
        self.assertIn("Dummy Packet", analyzer.captured_packets)
