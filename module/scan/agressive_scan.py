from module.interface import work_iface
from datetime import datetime
from module.mac_vendor import mac_vendor
from module.ip_ttl import icmp_res
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
        ttl = icmp_res(ip)
        print(f"[{i}] IP: {ip} MAC: {mac} TTL: {ttl} MV: {m_vendor}")


