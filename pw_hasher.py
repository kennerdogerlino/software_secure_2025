#Import required modules
import bcrypt

#Stored password
password = input('Do not redeem it: ')

#Convert password into an array of bytes
bytes = password.encode('utf-8')

#Generate the salt
salt = bcrypt.gensalt()

#Hash the password with the salt
hash = bcrypt.hashpw(bytes, salt)

#Entered password
entPassword = input('Redeem it: ')

#Convert entpassword into an array of bytes
entBytes = entPassword.encode('utf-8')

#compare the password
result = bcrypt.checkpw(entBytes, hash)
print(result)

#Output the hash
#print(hash)
