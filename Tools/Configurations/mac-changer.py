#! /usr/bin/python

import subprocess
import pyfiglet
import termcolor

if __name__ == "__main__":
    interface = input(termcolor.colored("[+] Select Network Interface: ", color="green", attrs=["bold"]))
    new_mac = input(termcolor.colored("[+] Enter New Mac Address: ", color="green", attrs=["bold"]))

    print(termcolor.colored(pyfiglet.figlet_format("MAC - Changer"), color="red", attrs=["bold"]))
    print(termcolor.colored("=" * 50, color="white", attrs=["bold"]))

    print(termcolor.colored("[!] Shutting down the interface", color="red", attrs=["bold"]))
    subprocess.run(["ifconfig", "eth0", "down"])

    print(termcolor.colored("=" * 50, color="white", attrs=["bold"]))

    print(termcolor.colored(f"[*] Changing MAC address to : ", color="yellow", attrs=["bold"]), end="")
    print(termcolor.colored(new_mac, color="white", attrs=["bold"]))
    subprocess.run(["ifconfig", interface, "hw", "ether", new_mac])

    print(termcolor.colored("=" * 50, color="white", attrs=["bold"]))

    print(termcolor.colored("[*] MAC address changed to : ", color="yellow", attrs=["bold"]), end="")
    print(termcolor.colored(new_mac, color="white", attrs=["bold"]))
    subprocess.run(["ifconfig", interface, "up"])

    print(termcolor.colored("=" * 50, color="white", attrs=["bold"]))

    print(termcolor.colored("[+] Network interfaced turned on", color="green", attrs=["bold"]))
    print(termcolor.colored("=" * 50, color="white", attrs=["bold"]))


