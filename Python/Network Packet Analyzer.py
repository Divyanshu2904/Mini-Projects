from scapy.all import *


def packet_handler(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        proto = packet[IP].proto

        print(f"Source IP: {src_ip}, Destination IP: {dst_ip}, Protocol: {proto}")

        if TCP in packet:
            payload = packet[TCP].payload
            print("TCP Packet:")
            print(payload)
        elif UDP in packet:
            payload = packet[UDP].payload
            print("UDP Packet:")
            print(payload)
        elif ICMP in packet:
            payload = packet[ICMP].payload
            print("ICMP Packet:")
            print(payload)


def main():
    print("Starting packet sniffer...")
    sniff(prn=packet_handler, store=0)


if __name__ == "__main__":
    main()