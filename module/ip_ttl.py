from scapy.all import IP, ICMP, sr1


def icmp_res(ip_target):
    ip_p = IP(dst=ip_target)
    icmp_p = ICMP()
    icmp_packet = ip_p / icmp_p

    icmp_reply = sr1(icmp_packet, timeout=1, verbose=0)

    try:
        return icmp_reply.ttl
    except Exception:
        return "No answer or Filtered"
