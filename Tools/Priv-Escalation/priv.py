#! /usr/bin/python3

import ctypes
import platform

def is_root():
	if platform.system == "Windows":
		return ctypes.windll.shell32.ISUserAnAdmin()
	else:
		return 1

print(is_root)
elevate()
print(is_root)
