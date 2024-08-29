#! /usr/bin/python3

import socket
import pyfiglet
import termcolor

banner = "BotNet - Client"
print(termcolor.colored(pyfiglet.figlet_format(banner), color="red", attrs=["bold"]))

if __name__ == "__main__":

    print(termcolor.colored("[*] Connecting with server", color="yellow", attrs=["bold"]))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("192.168.30.205", 8080))
    run_bot = True

    while run_bot:
        communicate_bot = True
        while  communicate_bot:
            msg = s.recv(1024)
            msg = msg.decode()
            print(termcolor.colored("[+] command center said : ", color="blue", attrs=["bold"]), end="")
            print(termcolor.colored(msg, color="green", attrs=["bold"]))

            if msg == "[!] Exit":
                communicate_bot = False

        ans = input(termcolor.colored("[+] Do you want to remain connected: ", color="green", attrs=["bold"]))
        ans = "connected"

        if ans == "no":
            status = "disconnected"
            s.send(status.encode())
            run_bot = False
        else:
            status = "conntected".encode()
            s.send(status)

    s.close()
