import unittest
from core.packet_sniffer import PacketSniffer

class TestPacketSniffer(unittest.TestCase):
    def test_sniffer_initialization(self):
        sniffer = PacketSniffer("eth0")
        self.assertEqual(sniffer.interface, "eth0")


