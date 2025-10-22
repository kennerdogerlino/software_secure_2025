'''this one encryptes a file'''
#imports the required modules
from cryptography.fernet import Fernet

#Open the key
with open('filekey.key', 'rb') as filekey:
    key = filekey.read()

#Use the key
fernet = Fernet(key)

#Open file to be encrypted
with open('Unencrypted.docx', 'rb') as file:
    unencrypted = file.read()

#Encrypt the file
encrypted = fernet                                                             .encrypt(unencrypted)

#write the encrypted data
with open('Encrypted.docx', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)
