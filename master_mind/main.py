import random
from colorama import init

init()              # initialize colorama for Windows

from colorama import Back, Style

num_pegs = 4        # the number of pegs in the secret code

num_colours = 6     # the number of different colours in the secret code

back_colours = (Back.BLACK, Back.RED, Back.GREEN, Back.YELLOW, Back.BLUE, Back.WHITE)

legend_items = [str(i) + ' = ' + Style.BRIGHT + back_colours[i] + '  ' + Style.RESET_ALL
                for i in range(num_colours)]

legend = ', '.join(legend_items)

def print_stars(n = 40):
    print("*" * n)

def play(n = 64):

    # randomly generate the answer
    answer = random.randint(1, n)

    print_stars()
    print("Welcome to the Master Mind game!")
    print(f"I randomly generated a secret code consisting of {num_pegs} coloured pegs.")
    print(f"There are {num_colours} different colours: {legend}")
    print("Try to guess the secret code as quickly as possible.")

    guess_count = 0

    # TO DO: change this code to handle the rules of Master Mind
    while True:
        guess_count = guess_count + 1
        guess_str = input(f"[{guess_count}] Guess the secret code: ")
        try:
            guess = int(guess_str)
            if guess > answer:
                print("Lower!")
            elif guess < answer:
                print("Higher!")
            else:
                print(f"Correct! You guessed {answer} in {guess_count} tries!")
                break

        except:
            print(f"ERROR: {guess_str} is not a valid integer.")

    print_stars()

play(8)