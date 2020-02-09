from random import randint

from re import search

from colorama import init

init()              # initialize colorama for Windows

from colorama import Back, Style

num_pegs = 4        # the default number of pegs in the secret code

num_colours = 6     # the default number of different colours in the secret code

back_colours = (Back.BLACK, Back.RED, Back.GREEN, Back.YELLOW,
                Back.BLUE, Back.WHITE, Back.MAGENTA, Back.CYAN)

pegs = ['[' + Style.BRIGHT + back_colours[i] + '  ' + Style.RESET_ALL + ']'
        for i in range(len(back_colours))]

legend_items = [str(i) + ' = [' + Style.BRIGHT + back_colours[i] + '  ' + Style.RESET_ALL + ']'
                for i in range(num_colours)]

legend = ', '.join(legend_items)


def digits_code(code):
    digits_in_code = [str(i) for i in code]
    return ''.join(digits_in_code)


def format_code(code):
    pegs_in_code = [pegs[i] for i in code]
    return ' '.join(pegs_in_code)


def parse_code(digits, n_pegs, n_colours):
    if search('^\d+$', digits) is None:
        print('Code must only contain digits. Found one or more non-digits in: ' + digits)
        return None

    if len(digits) != n_pegs:
        print(f'Code must contain exactly {n_pegs} pegs. Found {len(digits)} pegs in: ' + digits)
        return None

    code = [int(d) for d in digits]
    for c in code:
        if c >= n_colours:
            print(f'Maximum colour is {n_colours - 1}. Found higher colour in: ' + digits)
            return None

    return code

def generate_legend_items(n_colours):
    return [str(i) + ' = [' + Style.BRIGHT + back_colours[i] + '  ' + Style.RESET_ALL + ']'
            for i in range(n_colours)]


def generate_secret_code(n_pegs, n_colours):
    return [randint(0, n_colours - 1) for peg in range(n_pegs)]


def print_stars(n = 80):
    print("*" * n)


def compute_spectrum(code, n_colours):
    spectrum = [0 for i in range(n_colours)]
    for c in code:
        spectrum[c] = spectrum[c] + 1

    return spectrum

def score_guess(secret_spectrum, secret_code, guess_code):
    n_colours = len(secret_spectrum)
    guess_spectrum = compute_spectrum(guess_code, n_colours)
    total_score = sum([min(secret_spectrum[i], guess_spectrum[i]) for i in range(n_colours)])

    n_pegs = len(secret_code)
    black_score = sum([secret_code[i] == guess_code[i] for i in range(n_pegs)])

    white_score = total_score - black_score

    return (black_score, white_score)

def play(n_pegs = num_pegs, n_colours = num_colours):

    legend_items = generate_legend_items(n_colours)
    legend = ', '.join(legend_items)

    # randomly generate the secret code
    secret_code = generate_secret_code(n_pegs, n_colours)
    secret_spectrum = compute_spectrum(secret_code, n_colours)
    formatted_secret_code = format_code(secret_code)

    print_stars()
    print("Welcome to the Master Mind game!")
    print(f"I randomly generated a secret code consisting of {n_pegs} coloured pegs. {formatted_secret_code}")
    print(f"There are {n_colours} different colours: {legend}")
    print("Try to guess the secret code as quickly as possible.")

    guess_count = 0

    while True:
        guess_count = guess_count + 1
        guess_digits = input(f"[{guess_count}] Guess the secret code: ")
        guess_code = parse_code(guess_digits, n_pegs, n_colours)
        if guess_code is None:
            print(f"Try again. Enter exactly {n_pegs} numeric digits using: {legend}")
            guess_count = guess_count - 1
        else:
            black_score, white_score = score_guess(secret_spectrum, secret_code, guess_code)
            if black_score == n_pegs:
                print(f"Correct! You guessed {formatted_secret_code} in {guess_count} tries!")
                break
            else:
                print(f"This guess scored {black_score} black and {white_score} white.")

    print_stars()


if __name__ == '__main__':
    play()