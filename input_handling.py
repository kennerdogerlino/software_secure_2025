import re
MAX_INPUT_LENGTH = 20

def sanitise_input(name):
    return re.sub(r'[^a-zA-Z\s-]', '', name).strip()

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
        hand_sanitiser_name = sanitise_input(user_name)
        if len(hand_sanitiser_name) > MAX_INPUT_LENGTH:
            print(f'Username tuu long. Exceeds the max length of {MAX_INPUT_LENGTH} characters.')
        elif not hand_sanitiser_name.strip():
            print('Username cannot be blank or whitespace')
        break
    except ValueError:
        print('Pls input a valid string.')

print(f'Valid number {num}')
print(f'Valid user_name {hand_sanitiser_name}')
