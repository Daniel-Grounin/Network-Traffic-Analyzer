import logging

logging.basicConfig(
    filename="network_traffic_analyzer.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_packet(packet_summary):
    logging.info(f"Packet Captured: {packet_summary}")

def log_alert(alert_message):
    logging.warning(f"ALERT: {alert_message}")
