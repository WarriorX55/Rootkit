#! /usr/bin/python3

import socket
import pyfiglet
import termcolor

banner = "> Client <"
print(termcolor.colored(pyfiglet.figlet_format(banner), color="red", attrs=["bold"]))

if __name__ == "__main__":
    victim_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    hacker_IP = input(termcolor.colored("[+] Enter your IP address: ", color="green", attrs=["bold"]))

    print(termcolor.colored("=" * 50, color="white", attrs=["bold"]))
    hacker_Port = input(termcolor.colored("[+] Select port to conect to: ", color="green", attrs=["bold"]))

    hacker_address = (str(hacker_IP), int(hacker_Port))

    victim_socket.connect((hacker_address))

    data = victim_socket.recv(1024)

    print(termcolor.colored("=" * 50, color="white", attrs=["bold"]))
    print(termcolor.colored(f"Message : ", color="blue", attrs=["bold"]), end="")
    print(termcolor.colored(data.decode(), color="yellow", attrs=["bold"]))
    print(termcolor.colored("=" * 50, color="white", attrs=["bold"]))

    victim_socket.close()

