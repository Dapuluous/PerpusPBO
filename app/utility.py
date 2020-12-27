import os
import platform
import hashlib

def clear():
	return os.system('cls') if(platform.system() == "Windows") else os.system('clear')

def hashmd5(password):
	return hashlib.md5(password.encode('utf-8')).hexdigest()