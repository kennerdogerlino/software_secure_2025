#Import required modules
import hashlib

def signup():
    email = input("Pls enter ur email: ")
    pwd = input("Pls enter a password: ")
    conf_pwd = input("Pls confirm ur password: ")
    if pwd == conf_pwd:
        enc = pwd.encode()
        hash1 = hashlib.md5(enc).hexdigest()
        with open("credentials.txt", "w") as creds:
            creds.write(email + "\n")
            creds.write(hash1)
        print("You sucksessfully registered")
    else:
        print("The passwords do not match. \n")
        input("Press enter to continue. \n")
        signup()

signup()
