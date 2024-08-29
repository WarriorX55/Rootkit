#! /usr/bin/python3

from scapy.all import Ether, ARP, srp
import pyfiglet, termcolor

if __name__ == "__main__":

    banner = "ARP - Scanner"
    print(termcolor.colored(pyfiglet.figlet_format(banner), color="blue", attrs=["bold"]))

    broadcast = "FF:FF:FF:FF:FF:FF"
    ether_layer = Ether(dst = broadcast)

    ip = input(termcolor.colored("[+] Please Enter IP Address: ", color="green", attrs=["bold"]))
    ip_range = "{ip}/24"
    arp_layer = ARP(pdst = ip_range)

    packet = ether_layer / arp_layer
    ans, unans = srp(packet, iface = "eth0", timeout=2)

    for snd, rcv in ans:
        ip = rcv[ARP].psrc
        mac = rcv[Ether].src
        print(termcolor.colored("=" * 56, color="white", attrs=["bold"]))
        print(termcolor.colored(f"[+] IP => {ip}   [+] MAC => {mac}", color="yellow", attrs=["bold"]))
        print(termcolor.colored("=" * 56, color="white", attrs=["bold"]))

