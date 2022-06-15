from cryptography.fernet import Fernet

#  create fernet encryption key
encryption_key = Fernet.generate_key()



#  create a file for the encryption key to be written in
with open("filenameofchoice.txt", 'wb') as keywriter:
    keywriter.write(encryption_key)
