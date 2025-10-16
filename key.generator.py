'''this one generates an encryption key'''
#imports the required modules
from cryptography.fernet import Fernet

#generate a key
key = Fernet.generate_key()

#write the key to a file
with open('filekey.key', 'wb') as filekey:
    filekey.write(key)
