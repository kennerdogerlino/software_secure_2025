MAX_INPUT_LENGTH = 20


#Get an integer between 1 & 10 input from user
while True:
    try:
        num = int(input('pls enter a number between 1 & 10: '))
        if num < 1 or num >10:
            print('pls enter a number between 1 & 10: ')
        else:
            break
    except ValueError:
        print('Pls input a valid integer')
