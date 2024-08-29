#! /usr/bin/python3

import socket
import pyfiglet
import termcolor

banner = "> Server <"
print(termcolor.colored(pyfiglet.figlet_format(banner), color="red", attrs=["bold"]))

if __name__ == "__main__":
    hacker_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    IP = input(termcolor.colored("[+] Enter your IP address: ", color="green", attrs=["bold"]))
    print(termcolor.colored("=" * 50, color="white", attrs=["bold"]))

    Port = input(termcolor.colored("[+] Select port to listen on: ", color="green", attrs=["bold"]))
    print(termcolor.colored("=" * 50, color="white", attrs=["bold"]))

    message = input(termcolor.colored("[+] Write a message : ", color="blue", attrs=["bold"]))
    print(termcolor.colored("=" * 50, color="white", attrs=["bold"]))

    socket_address = (str(IP), int(Port))
    hacker_socket.bind(socket_address)
    hacker_socket.listen(5)

    print(termcolor.colored("[*] Listening for incoming connection requests", color="yellow", attrs=["bold"]))
    print(termcolor.colored("=" * 50, color="white", attrs=["bold"]))
    hacker_socket, client_address = hacker_socket.accept()

    message_bytes = message.encode()
    hacker_socket.send(message_bytes)

    print(termcolor.colored("[+] Message Sent Successfully!", color="green", attrs=["bold"]))
    hacker_socket.close()

