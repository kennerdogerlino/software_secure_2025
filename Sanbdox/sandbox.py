#Create a restricted environmen with limited #
#built-in functions (whitelist)
restricted_env = {'__builtins__': {'print': print}}

#Safe code
safe_code = 'print("Hello World!")'

#Unsafe code
unsafe_code = 'open("credentials.txt", "r")'

exec(safe_code, restricted_env)

#Attempt to run unsafe code
try:
    exec(unsafe_code, restricted_env)
except NameError as e:
    print(f"Error: {e}")
#This will raise an error because 'open' is not in the whitelist