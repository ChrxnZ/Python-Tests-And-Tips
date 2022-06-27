import os
import time
from cryptography.fernet import Fernet

#  Made By Pulsed#0001 (I AM NOT RESPONSIBLE FOR ANY DAMAGE BY ANY MEANS)

def encrypt():
    files = []
    for file in os.listdir():
        if file == "Fernet-TestScript1.py" or file == "dec_key.key":
            continue
        if os.path.isfile(file):
            files.append(file)
    print("Found Files:")
    print(files)
    time.sleep(3)
    
    key = Fernet.generate_key()
    
    with open("dec_key.key", "wb") as thekey:
        thekey.write(key)
    print("Decryption Key Created.")
    time.sleep(3)
    
    for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        contents_encrypted = Fernet(key).encrypt(contents)
        time.sleep(2)
        with open(file, "wb") as thefile:
            thefile.write(contents_encrypted)
    print("All Of The Files Found In The Script's Directory Have Been Encrypted! Check dec_key.key For The Fernet Decryption Key!")
    print("Made By Pulsed#0001 (I AM NOT RESPONSIBLE FOR ANY DAMAGE BY ANY MEANS)")


def decrypt():
    files = []
    for file in os.listdir():
        if file == "Fernet-TestScript1.py" or file == "dec_key.key":
            continue
        if os.path.isfile(file):
            files.append(file)
    print("Found Files:")
    print(files)
    time.sleep(3)
    
    with open("dec_key.key", "rb") as key:
        decrypt_key = key.read()
    print("Decryption Key Read.")
    time.sleep(3)
    
    for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        contents_decrypted = Fernet(decrypt_key).decrypt(contents)
        time.sleep(2)
        with open(file, "wb") as thefile:
            thefile.write(contents_decrypted)
        print("File(s) Have Been Decrypted!")
        print("Made By Pulsed#0001 (I AM NOT RESPONSIBLE FOR ANY DAMAGE BY ANY MEANS)")


print("E or Encryption To Encrypt Files")
print("D or Decryption To Decrypt Files")
choice = str(input("Choose An Option From Above: "))

if choice == "E" or choice == "e" or choice == "Encryption" or choice == "encryption":
    encrypt()

elif choice == "D" or choice == "d" or choice == "Decryption" or choice == "decryption":
    decrypt()
