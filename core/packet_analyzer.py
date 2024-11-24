from scapy.all import IP, TCP, UDP, ICMP

class PacketAnalyzer:
    @staticmethod
    def analyze(packet):
        if IP in packet:
            protocol = "TCP" if TCP in packet else "UDP" if UDP in packet else "ICMP" if ICMP in packet else "Other"
            return {
                "time": packet.time,
                "src_ip": packet[IP].src,
                "dst_ip": packet[IP].dst,
                "protocol": protocol,
                "length": len(packet)
            }
        return None
