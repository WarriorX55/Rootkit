#! /usr/bin/python3

from scapy.all import ICMP
from scapy.all import IP
from scapy.all import sr1
import pyfiglet, termcolor

if __name__ == "__main__":
    banner = "ICMP - Request"
    print(termcolor.colored(pyfiglet.figlet_format(banner), color="red", attrs=["bold"]))

    src_ip = input(termcolor.colored("[+] Enter Source IP Address: ", color="green", attrs=["bold"]))
    dest_ip = input(termcolor.colored("[+] Enter Destination IP or Domain: ", color="green", attrs=["bold"]))

    ip_layer = IP(src = src_ip, dst = dest_ip)
    icmp_req = ICMP(id=100)

    packet = ip_layer / icmp_req

    response = sr1(packet, iface="eth0")
    if response:
        print(response.show())


