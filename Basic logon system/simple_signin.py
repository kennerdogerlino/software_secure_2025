#Import required modules
import hashlib

def login():
    email = input("Pls enter ur email: ")
    pwd = input("Pls enter a password: ")
    enc = pwd.encode()
    hash2 = hashlib.md5(enc).hexdigest()
    with open("Basic logoon system/credentials.txt", "r") as creds:
        stored_email, stored_pwd = creds.read().split("\n")
    if email == stored_email and hash2 == stored_pwd:
        print("Deh Bluutootch devisch hasz connected ehsuscessfuhlly")
    else:
        print("Logoon failed. \n")

login()
