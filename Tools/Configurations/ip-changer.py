#! /usr/bin/python

import subprocess
import pyfiglet
import termcolor

if __name__ == "__main__":
    interface = input(termcolor.colored("[+] Select Network Interface: ", color="green", attrs=["bold"]))
    new_ip = input(termcolor.colored("[+] Enter New IP Address: ", color="green", attrs=["bold"]))

    print(termcolor.colored(pyfiglet.figlet_format("IP - Changer"), color="red", attrs=["bold"]))
    print(termcolor.colored("=" * 50, color="white", attrs=["bold"]))

    print(termcolor.colored(f"[*] Changing The IP Address To : ", color="yellow", attrs=["bold"]), end="")
    print(termcolor.colored(new_ip, color="white", attrs=["bold"]))
    subprocess.run(["ifconfig", interface, new_ip])

    print(termcolor.colored("=" * 50, color="white", attrs=["bold"]))

    print(termcolor.colored("[*] IP Address Has Changed To : ", color="yellow", attrs=["bold"]), end="")
    print(termcolor.colored(new_ip, color="white", attrs=["bold"]))
    subprocess.run(["ifconfig", interface, "up"])

    print(termcolor.colored("=" * 50, color="white", attrs=["bold"]))

    print(termcolor.colored("[+] Network Interfaced Turned on", color="green", attrs=["bold"]))
    print(termcolor.colored("=" * 50, color="white", attrs=["bold"]))

