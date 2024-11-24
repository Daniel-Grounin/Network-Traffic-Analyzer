# Raspberry Pi Traffic Analyzer

## Overview

The **Raspberry Pi Traffic Analyzer** is a network traffic monitoring tool designed to capture and analyze network packets on a Raspberry Pi device. This tool leverages **Scapy** for packet sniffing and **PyQt6** for the user interface. It provides real-time packet statistics, network traffic analysis, and supports different network interfaces.

## Features

- **Packet Sniffing**: Capture packets from various network interfaces.
- **Traffic Monitoring**: Real-time visualization of packet rate and data throughput.
- **User Interface**: A graphical interface built with PyQt6 for easy access to network data.
- **Cross-Platform Support**: Works on Kali Linux and other compatible systems like windows (if npcap is cofigured).

## Installation

### Prerequisites
1. **Kali Linux** installed on your Raspberry Pi.
2. **Python 3** and **pip3** installed.
3. **Network interface**: Ethernet or Wi-Fi connection for packet sniffing.

### Setup

1. **Update Raspberry Pi OS**:
    ```bash
    sudo apt update && sudo apt upgrade -y
    ```

2. **Install dependencies**:
    ```bash
    sudo apt install python3 python3-pip libpcap-dev
    pip3 install scapy pyqt6
    ```

3. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/raspberry-pi-traffic-analyzer.git
    cd raspberry-pi-traffic-analyzer
    ```

4. **Run the Analyzer**:
    ```bash
    python3 main.py
    ```

   * Ensure you have the correct network interface name (e.g., `eth0`, `wlan0`) set in the script.

## Usage

Once the tool is running, it will display the following real-time information:

- **Packet Rate (Packets/sec)**: Tracks the rate of incoming and outgoing network packets.
- **Data Throughput (Bytes/sec)**: Displays the data transfer rate of the network.

## Configuration

You can modify the network interface to analyze by changing the `iface` variable in `main.py` to your desired interface (e.g., `wlan0` or `eth0`).

### Example:
```python
iface = "wlan0"  # Replace with your network interface
