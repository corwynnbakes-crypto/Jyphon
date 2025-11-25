from scapy.all import sniff, ARP, IP, TCP
from collections import defaultdict
import time

arp_table = {}
scan_detect = defaultdict(list)
last_alert = {}

def detect_arp_spoof(pkt):
    if pkt.haslayer(ARP) and pkt[ARP].op == 2:  # is-at (response)
        real_mac = arp_table.get(pkt[ARP].psrc)
        current_mac = pkt[ARP].hwsrc
        if real_mac and real_mac != current_mac:
            print(f"[ALERT] Possible ARP spoof: {pkt[ARP].psrc} changed from {real_mac} to {current_mac}")
        arp_table[pkt[ARP].psrc] = current_mac

def detect_port_scan(pkt):
    if pkt.haslayer(IP) and pkt.haslayer(TCP):
        src = pkt[IP].src
        dst_port = pkt[TCP].dport
        now = time.time()

        scan_detect[src].append(now)

        # Only keep last 10 seconds
        scan_detect[src] = [t for t in scan_detect[src] if now - t < 10]

        if len(set(scan_detect[src])) > 10 and (now - last_alert.get(src, 0) > 30):
            print(f"[ALERT] Port scan detected from {src}")
            last_alert[src] = now

def packet_handler(pkt):
    detect_arp_spoof(pkt)
    detect_port_scan(pkt)

print("🛡️ Mr. Robot WiFi Defense Active (connected mode)...")
sniff(prn=packet_handler, store=0)
