import socket

def sniff_packets():
    """Captures and displays raw network packets."""
    try:
        # Create a raw socket to capture packets
        sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
        
        # Bind to the localhost interface (change as needed)
        host = socket.gethostbyname(socket.gethostname())
        sniffer.bind((host, 0))

        # Capture IP headers
        sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

        # Enable promiscuous mode (Windows only)
        try:
            sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
        except AttributeError:
            pass  # Not needed on Linux/Mac

        print(f"Listening for packets on {host}...\nPress Ctrl+C to stop.\n")

        while True:
            raw_packet = sniffer.recvfrom(65565)[0]  # Receive packets
            print(f"Captured Packet: {raw_packet[:20]}...")  # Print first 20 bytes for preview

    except KeyboardInterrupt:
        print("\nStopping packet sniffer.")
        try:
            # Disable promiscuous mode (Windows only)
            sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
        except AttributeError:
            pass

if __name__ == "__main__":
    sniff_packets()
