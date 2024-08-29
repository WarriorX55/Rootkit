#! /usr/bin/python3

from scapy.all import ICMP 
from scapy.all import IP
from scapy.all import sr1
from scapy.all import ls
import pyfiglet, termcolor

if __name__ == "__main__":
    banner = "Scapy - Function"
    print(termcolor.colored(pyfiglet.figlet_format(banner), color="red", attrs=["bold"]))

    src_ip = input(termcolor.colored("[+] Enter Source IP Address: ", color="green", attrs=["bold"]))
    dest_ip = input(termcolor.colored("[+] Enter Destination IP or Domain: ", color="green", attrs=["bold"]))

    ip_layer = IP(src = src_ip, dst = dest_ip)
    print(ls(ip_layer))  # displaying complete layer info

    # accessing the fields
    print(termcolor.colored("=" * 64, color="white", attrs=["bold"]))

    print(termcolor.colored("[+] Source => ", color="yellow", attrs=["bold"]), end="")
    print(termcolor.colored(ip_layer.src, color="green", attrs=["bold"]))

    print(termcolor.colored("[+] Destination => ", color="yellow", attrs=["bold"]), end="")
    print(termcolor.colored(ip_layer.dst, color="green", attrs=["bold"]))

    print(termcolor.colored("=" * 64, color="white", attrs=["bold"]))

    print(termcolor.colored("[!] Summary  = ", color="red", attrs=["bold"]), end="")
    print(termcolor.colored(ip_layer.summary(), color="green", attrs=["bold"]))

    print(termcolor.colored("=" * 64, color="white", attrs=["bold"]))

