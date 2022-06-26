import os
import sys
import time
import random
import pyperclip
from colorama import Fore
from cryptography.fernet import Fernet

#  Made By Pulsed#1874 (I AM NOT RESPONSIBLE FOR ANY DAMAGE BY ANY MEANS)

def Clear_Terminal():
    os.system("cls")

def verify_test():
    ver = random.randint(500,5000)
    Clear_Terminal()
    print(f"{Fore.LIGHTMAGENTA_EX}Verification Number Is{Fore.RESET}: {Fore.RED}" +str(ver) + f"{Fore.RESET}")
    verify = int(input(f"{Fore.CYAN}Enter The Number{Fore.RESET}{Fore.LIGHTYELLOW_EX} Above{Fore.RESET}   {Fore.LIGHTRED_EX}^{Fore.RESET}  {Fore.LIGHTBLACK_EX}->{Fore.RESET}  "))
    if verify == ver:
        print(f"{Fore.RED}Verifying...{Fore.RESET}")
        time.sleep(3)
        menuu()
        
def menuu():
    Clear_Terminal()
    menu = input(f"""
                 {Fore.BLUE}Python Fernet Encrypter And Decrypter By{Fore.RESET} {Fore.LIGHTGREEN_EX}Pulsed#1874{Fore.RESET}
                 {Fore.RED}V 1.1.0-A
                 {Fore.LIGHTCYAN_EX}[E]{Fore.RESET} - {Fore.BLUE}Encrypt Files In Script Directory{Fore.RESET} 
                 {Fore.LIGHTCYAN_EX}[D]{Fore.RESET} - {Fore.BLUE}Decrypt Files In Script Directory{Fore.RESET}\n""")
    
    if menu == "E" or menu == "e":
        Encrypt()
        
    if menu == "D" or menu == "d":
        Decrypt()
        
def Encrypt():
    files = []
    for file in os.listdir():
        if file == "Fernet-TestScript2.py" or file == "Decryption_Key.key":
            continue
        if os.path.isfile(file):
            files.append(file)
    print(f"{Fore.LIGHTYELLOW_EX}Found Files:{Fore.RESET}")
    print(f"{Fore.CYAN} " +str(files) + f"{Fore.RESET}")
    time.sleep(3)
    
    key = Fernet.generate_key()
    print(f"{Fore.GREEN} Decryption Key Created. {Fore.RESET}")
    time.sleep(2)
    pyperclip.copy(str(key))
    print(f"{Fore.MAGENTA} Decryption Key Copied To Clipboard. {Fore.RESET}")
    time.sleep(2)
    
    with open("Decryption_Key.key", "wb") as thekey:
        thekey.write(key)
    print(f"{Fore.CYAN} Decryption Key Written In Decryption_Key.key")
    time.sleep(3)
    
    for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        contents_encrypted = Fernet(key).encrypt(contents)
        time.sleep(2)
        with open(file, "wb") as thefile:
            thefile.write(contents_encrypted)
        print(f"{Fore.LIGHTGREEN_EX} File Encrypted. {Fore.RESET}")
    print(f"{Fore.LIGHTYELLOW_EX} All File(s) Found Have Been Encrypted!{Fore.RESET}")
    print(f"{Fore.RED}Made By {Fore.RESET}{Fore.LIGHTGREEN_EX}Pulsed#1874{Fore.RESET}")

def Decrypt():
    files = []
    for file in os.listdir():
        if file == "Fernet-TestScript2.py" or file == "Decryption_Key.key":
            continue
        if os.path.isfile(file):
            files.append(file)
    print(f"{Fore.LIGHTYELLOW_EX}Found Files:{Fore.RESET}")
    print(f"{Fore.CYAN} " +str(files) + f"{Fore.RESET}")
    time.sleep(3)
    
    with open("Decryption_Key.key", "rb") as thekey:
        key = thekey.read()
    print(f"{Fore.RED} Decryption Key In Decryption_Key.key Is Read.")
    time.sleep(3)
    
    for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        contents_decrypted = Fernet(key).decrypt(contents)
        time.sleep(2)
        with open(file, "wb") as thefile:
            thefile.write(contents_decrypted)
        print(f"{Fore.LIGHTGREEN_EX} File Decrypted. {Fore.RESET}")
    print(f"{Fore.LIGHTYELLOW_EX} All File(s) Found Have Been Decrypted!{Fore.RESET}")
    print(f"{Fore.RED}Made By {Fore.RESET}{Fore.LIGHTGREEN_EX}Pulsed#1874{Fore.RESET}")

        
#  The Start Of The Script! 
if 1 == 1:
    verify_test()
