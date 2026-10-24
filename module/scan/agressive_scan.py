from module.interface import work_iface
from datetime import datetime
from module.scan.mac_vendor import mac_vendor
from scapy.all import ARP, Ether, srp, IP, ICMP, sr1


def run_scan(target):
    i = 0

    packet = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(op=1, pdst=target)
    rec, error = srp(packet, timeout=3, verbose=0)

    for req, res in rec:
        i += 1
        ip = res.psrc
        mac = res.hwsrc
        m_vendor = mac_vendor(mac)
        print(f"[{i}] IP: {ip} MAC: {mac} MV: {m_vendor}")


