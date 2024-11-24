class Alerts:
    @staticmethod
    def alert_on_unusual_traffic(packet):
        """Analyze packet for anomalies and generate alerts."""
        if packet.haslayer("TCP") and packet["TCP"].dport == 23:  # Example: Telnet port
            return f"Unusual activity detected: {packet.summary()}"
        return None
