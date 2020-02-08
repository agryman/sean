import random

def play(n = 64):

    # randomly generate the answer
    answer = random.randint(1, n)

    print("*" * 30)
    print("Welcome to the guessing game!")
    print(f"I randomly generated an integer between 1 and {n}.")
    print("Try to guess it as quickly as possible.")

    guess_count = 0

    while True:
        guess_count = guess_count + 1
        guess_str = input(f"[{guess_count}] Guess the integer: ")
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

play()