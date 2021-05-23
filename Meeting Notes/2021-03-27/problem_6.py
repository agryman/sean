def ask():
    while True:
        name = input('Enter your name: ')
        print(f'Your name is {name}')
        while True:
            number_str = input('Enter a number: ')
            try:
                number = float(number_str)
                break
            except:
                print(f'You did not enter a valid number: {number_str}')
        print(f'Your number is: {number}')
        if number < 0:
            break

ask()