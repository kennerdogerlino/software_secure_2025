import re
MAX_INPUT_LENGTH = 20

def sanitise_input(name):
    return re.sub(r'[^a-zA-Z0-9_]', '', name)

#Get an integer between 1 & 10 input from user
while True:
    try:
        num = int(input('pls enter a number between 1 & 10: '))
        if num < 1 or num >10:
            print('bro. Enter one thats valid: ')
        else:
            break
    except ValueError:
        print('Pls input a valid integer')

while True:
    try:
        user_name = input('Pls enter your username: ')
        if len(user_name) > MAX_INPUT_LENGTH:
            print(f'Username tuu long. Exceeds the max length of {MAX_INPUT_LENGTH} characters.')
        elif not user_name.strip():
            print('Username cannot be blank or whitespace')
        break
    except ValueError:
        print('Pls input a valid string.')

print(f'Valid number {num}')
print(f'Valid user_name {user_name}')
