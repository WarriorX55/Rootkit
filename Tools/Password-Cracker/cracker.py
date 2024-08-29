#! /usr/bin/python3

import zipfile, time
import pyfiglet, termcolor

banner = "> Zip - Cracker <"
print(termcolor.colored(pyfiglet.figlet_format(banner), color="red", attrs=["bold"]))

encrypted_filename= "secret_file.zip"
zFile = zipfile.ZipFile(encrypted_filename, "r")

passFile = open("passwords.txt", "r")

for line in passFile.readlines():
    test_password = line.strip("\r\n").encode('utf-8')

    try:
        print(test_password)
        zFile.extractall(pwd=test_password)
        print(termcolor.colored("[+] Match Found!", color="green", attrs=["bold"]))
        break
        
    except Exception as err:
        pass
