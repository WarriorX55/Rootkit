#! /usr/bin/python3

import pyfiglet, termcolor
import signal, os, sys

banner = "WarriorX - RAT"
print(termcolor.colored(pyfiglet.figlet_format(banner), color="red", attrs=["bold"]))

# Import the color class library
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Function to handle when the user enters Ctrl+C
def signal_handler(signal, frame):
    print(termcolor.colored('\n=============================', color="white", attrs=["bold"]))
    print(termcolor.colored('[!] Execution aborted by user', color="red", attrs=["bold"]))
    print(termcolor.colored('=============================', color="white", attrs=["bold"]))
    os.system("kill -9 " + str(os.getpid()))
    sys.exit(1)

def list_options():
    print(termcolor.colored('=============================', color="white", attrs=["bold"]))
    print(termcolor.colored("[*] Please Select Choice:", color="blue", attrs=["bold"]))
    print(termcolor.colored('=============================', color="white", attrs=["bold"]))
    print(termcolor.colored("[01]", color="red", attrs=["bold"]), end=" ")
    print(termcolor.colored("Change Configurations", color="yellow", attrs=["bold"]))
    print(termcolor.colored("[02]", color="red", attrs=["bold"]), end=" ")
    print(termcolor.colored("ARP Scan", color="yellow", attrs=["bold"]))
    print(termcolor.colored("[03]", color="red", attrs=["bold"]), end=" ")
    print(termcolor.colored("Spoof ARP", color="yellow", attrs=["bold"]))
    print(termcolor.colored("[04]", color="red", attrs=["bold"]), end=" ")
    print(termcolor.colored("Introduction To Scapy", color="yellow", attrs=["bold"]))
    print(termcolor.colored("[05]", color="red", attrs=["bold"]), end=" ")
    print(termcolor.colored("Socket Server", color="yellow", attrs=["bold"]))
    print(termcolor.colored("[06]", color="red", attrs=["bold"]), end=" ")
    print(termcolor.colored("Socket Cient", color="yellow", attrs=["bold"]))
    print(termcolor.colored("[07]", color="red", attrs=["bold"]), end=" ")
    print(termcolor.colored("Hacker Malware", color="yellow", attrs=["bold"]))
    print(termcolor.colored("[08]", color="red", attrs=["bold"]), end=" ")
    print(termcolor.colored("Victim Malware", color="yellow", attrs=["bold"]))
    print(termcolor.colored("[09]", color="red", attrs=["bold"]), end=" ")
    print(termcolor.colored("Keylogger", color="yellow", attrs=["bold"]))
    print(termcolor.colored("[10]", color="red", attrs=["bold"]), end=" ")
    print(termcolor.colored("Password Cracker", color="yellow", attrs=["bold"]))
    print(termcolor.colored("[11]", color="red", attrs=["bold"]), end=" ")
    print(termcolor.colored("Advanced Hacker Malware", color="yellow", attrs=["bold"]))
    print(termcolor.colored("[12]", color="red", attrs=["bold"]), end=" ")
    print(termcolor.colored("Advanced Victim Malware", color="yellow", attrs=["bold"]))
    print(termcolor.colored("[13]", color="red", attrs=["bold"]), end=" ")
    print(termcolor.colored("Privilege Escalation", color="yellow", attrs=["bold"]))
    print(termcolor.colored("[14]", color="red", attrs=["bold"]), end=" ")
    print(termcolor.colored("Command & Control Center", color="yellow", attrs=["bold"]))
    print(termcolor.colored("[15]", color="red", attrs=["bold"]), end=" ")
    print(termcolor.colored("Persistence", color="yellow", attrs=["bold"]))
    print(termcolor.colored('=============================', color="white", attrs=["bold"]))
    choice = input(termcolor.colored("[+] Choose option: ", color="green", attrs=["bold"]))
    print(termcolor.colored('=============================', color="white", attrs=["bold"]))

    if choice in ['1', '2', '3', '4', '5', '6', '7', '8', '9'] \
    or choice in ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15']:

        if choice == '1' or choice == '01':
            print(termcolor.colored('=============================', color="white", attrs=["bold"]))
            print(termcolor.colored("[01]", color="red", attrs=["bold"]), end=" ")
            print(termcolor.colored("IP Changer", color="yellow", attrs=["bold"]))
            print(termcolor.colored("[02]", color="red", attrs=["bold"]), end=" ")
            print(termcolor.colored("MAC Changer", color="yellow", attrs=["bold"]))
            print(termcolor.colored('=============================', color="white", attrs=["bold"]))
            choice = input(termcolor.colored("[*] Select your choice: ", color="blue", attrs=["bold"]))
            print(termcolor.colored('=============================', color="white", attrs=["bold"]))
            if choice == '1' or choice == '01':
                return os.system("sudo ./Tools/Configurations/ip-changer.py")
            elif choice == '2' or choice == '02':
                return os.system("sudo ./Tools/Configurations/mac-changer.py")

            else:
                print(termcolor.colored("[!] Wrong input, exiting...", color="red", attrs=["bold"]))
                print(termcolor.colored('=============================', color="white", attrs=["bold"]))

        elif choice == '2' or choice == '02':
            return os.system("sudo ./Tools/ARP-Scanner/arp-scanner.py")
        elif choice == '3' or choice == '03':
            return os.system("sudo ./Tools/ARP-Spoof/arpspoof.py")
        elif choice == '4' or choice == '04':
            print(termcolor.colored('=============================', color="white", attrs=["bold"]))
            print(termcolor.colored("[01]", color="red", attrs=["bold"]), end=" ")
            print(termcolor.colored("Intro To Scapy", color="yellow", attrs=["bold"]))
            print(termcolor.colored("[02]", color="red", attrs=["bold"]), end=" ")
            print(termcolor.colored("ICMP Request", color="yellow", attrs=["bold"]))
            print(termcolor.colored('=============================', color="white", attrs=["bold"]))
            choice = input(termcolor.colored("[+] Select your choice: ", color="blue", attrs=["bold"]))
            print(termcolor.colored('=============================', color="white", attrs=["bold"]))
            if choice == '1' or choice == '01':
                return os.system("sudo ./Tools/Scapy-Introduction/scapy-function.py")
            elif choice == '2' or choice == '02':
                return os.system("sudo ./Tools/Scapy-Introduction/icmp-request.py")

            else:
                print(termcolor.colored("[!] Wrong input, exiting...", color="red", attrs=["bold"]))
                print(termcolor.colored('=============================', color="white", attrs=["bold"]))

        elif choice == '5' or choice == '05':
            return os.system("sudo ./Tools/Socket-Server/server.py")
        elif choice == '6' or choice == '06':
            print(termcolor.colored("[!] Try execute this script on your windows machine or in another terminal.", color="red", attrs=["bold"]))
            return os.system("sudo ./Tools/Socket-Client/victim.py")
        elif choice == '7' or choice == '07':
            return os.system("sudo ./Tools/Hacker-Malware/hacker.py")
        elif choice == '8' or choice == '08':
            print(termcolor.colored("[!] Try execute this script on the target machine using windows powershell after running the Hacker-Malware.", color="red", attrs=["bold"]))
            return os.system("sudo ./Tools/Victim-Malware/victim.py")
        elif choice == '9' or choice == '09':
            return os.system("sudo ./Tools/Keylogger/keylogger.py")
        elif choice == '10':
            return os.system("sudo ./Tools/Password-Cracker/cracker.py")
        elif choice == '11':
            return os.system("sudo ./Tools/Hacker-Advanced/advanced-hacker.py")
        elif choice == '12':
            return os.system("sudo ./Tools/Advanced-Victim/advanced-victim.py")
        elif choice == '13':
            print(termcolor.colored('=============================', color="white", attrs=["bold"]))
            print(termcolor.colored("[01]", color="red", attrs=["bold"]), end=" ")
            print(termcolor.colored("Get Privilege", color="yellow", attrs=["bold"]))
            print(termcolor.colored("[02]", color="red", attrs=["bold"]), end=" ")
            print(termcolor.colored("Escalation Privileges", color="yellow", attrs=["bold"]))
            print(termcolor.colored('=============================', color="white", attrs=["bold"]))
            choice = input(termcolor.colored("[+] Select your choice: ", color="blue", attrs=["bold"]))
            print(termcolor.colored('=============================', color="white", attrs=["bold"]))
            if choice == '1' or choice == '01':
                return os.system("sudo ./Tools/Priv-Escalation/priv.py")
            elif choice == '2' or choice == '02':
                return os.system("sudo ./Tools/Priv-Escalation/escalation.py")

            else:
                print(termcolor.colored("[!] Wrong input, exiting...", color="red", attrs=["bold"]))
                print(termcolor.colored('=============================', color="white", attrs=["bold"]))

        elif choice == '14':
            print(termcolor.colored('=============================', color="white", attrs=["bold"]))
            print(termcolor.colored("[01]", color="red", attrs=["bold"]), end=" ")
            print(termcolor.colored("BotNet", color="yellow", attrs=["bold"]))
            print(termcolor.colored("[02]", color="red", attrs=["bold"]), end=" ")
            print(termcolor.colored("Command & Control Center", color="yellow", attrs=["bold"]))
            print(termcolor.colored('=============================', color="white", attrs=["bold"]))
            choice = input(termcolor.colored("[+] Select your choice: ", color="blue", attrs=["bold"]))
            print(termcolor.colored('=============================', color="white", attrs=["bold"]))
            if choice == '1' or choice == '01':
                return os.system("sudo ./Tools/CNC/botnet.py")
            elif choice == '2' or choice == '02':
                return os.system("sudo ./Tools/CNC/CnC.py")

            else:
                print(termcolor.colored("[!] Wrong input, exiting...", color="red", attrs=["bold"]))
                print(termcolor.colored('=============================', color="white", attrs=["bold"]))

        elif choice == '15':
            return os.system("sudo ./Tools/Persistence/persistence.py")

    else:
        print(termcolor.colored("[!] Wrong input, exiting...", color="red", attrs=["bold"]))
        print(termcolor.colored('=============================', color="white", attrs=["bold"]))


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    list_options()

