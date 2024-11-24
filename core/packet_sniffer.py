from scapy.all import sniff

class PacketSniffer:
    def __init__(self, interface="wlan0"):
        self.interface = interface
        self.packets = []

    def start_sniffing(self, packet_callback):
        sniff(iface=self.interface, prn=packet_callback, store=False)

    def stop_sniffing(self):
        # No explicit stop method; use CTRL+C to interrupt in CLI mode
        print("Stopping sniffing...")
