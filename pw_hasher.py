#import required modules
import bcrypt

#stored password
password = 'password123'

#Convert password into an array of bytes
bytes = password.encode('utf-8')

#Generate the salt
salt = bcrypt.gensalt()

hash = bcrypt.hashpw(bytes, salt)

print(hash)
