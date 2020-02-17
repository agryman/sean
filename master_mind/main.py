from random import randint

from re import search

from colorama import init, Back, Style

init()              # initialize colorama for Windows

max_num_pegs = 6            # the maximum number of pegs allowed
default_num_pegs = 4        # the default number of pegs in the secret code

back_colours = (Back.BLACK, Back.RED, Back.GREEN, Back.YELLOW,
                Back.BLUE, Back.WHITE, Back.MAGENTA, Back.CYAN)

max_colours = len(back_colours)
default_num_colours = 6     # the default number of different colours in the secret code

pegs = ['[' + Style.BRIGHT + back_colours[i] + '  ' + Style.RESET_ALL + ']'
        for i in range(len(back_colours))]

legend_items = [str(i) + ' = [' + Style.BRIGHT + back_colours[i] + '  ' + Style.RESET_ALL + ']'
                for i in range(default_num_colours)]

legend = ', '.join(legend_items)

max_guesses = 10            # the maximum numbers of guesses allowed in a game


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

def score_guess(n_pegs, n_colours, secret_code, guess_code):
    secret_spectrum = compute_spectrum(secret_code, n_colours)
    guess_spectrum = compute_spectrum(guess_code, n_colours)
    total_score = sum([min(secret_spectrum[i], guess_spectrum[i]) for i in range(n_colours)])

    black_score = sum([secret_code[i] == guess_code[i] for i in range(n_pegs)])

    white_score = total_score - black_score

    return (black_score, white_score)

def format_score(black_score, white_score):
    return f'{black_score} black and {white_score} white'


def make_legend(n_colours):
    legend_items = generate_legend_items(n_colours)
    legend = ', '.join(legend_items)
    return legend

def make_guess_label(guess_count):
    guess_number = f"[{guess_count}]"
    return f"{guess_number:>4}"

def print_guess_history(guess_history):
    print('-' * 80)
    for i in range(len(guess_history)):
        guess_digits, guess_code, black_score, white_score, n_solutions = guess_history[i]
        formatted_guess_code = format_code(guess_code)
        formatted_guess_score = format_score(black_score, white_score)
        guess_count = i + 1
        guess_label = make_guess_label(guess_count)
        print(f'{guess_label} {guess_digits} = {formatted_guess_code} : {formatted_guess_score} ==> '
              f'{n_solutions:>6} codes match')


def make_all_solutions(n_pegs, n_colours):
    if n_pegs == 1:
        return [[peg] for peg in range(0, n_colours)]

    base = make_all_solutions(n_pegs - 1, n_colours)
    solutions = []
    for b in base:
        for peg in range(0, n_colours):
            c = b.copy();
            c.append(peg)
            solutions.append(c)

    return solutions

def eliminate_solutions(n_pegs, n_colours, solutions, guess_code, black_score, white_score):
    return [code for code in solutions
            if (black_score, white_score) == score_guess(n_pegs, n_colours, code, guess_code)]

def play(n_pegs = default_num_pegs, n_colours = default_num_colours):

    if n_pegs < 2 or n_pegs > max_num_pegs:
        raise Exception(f"Number of pegs, {n_pegs}, must be greater than 1 and at most {max_num_pegs}.")

    if n_colours > max_colours:
        raise Exception(f"Number of colour, {n_colours}, exceeds maximum {max_colours}.")

    print_stars()
    print("Welcome to the Master Mind game!")
    print(f"The object of this game is to guess a secret code composed of {n_pegs} coloured pegs.")
    print(f"Pegs come in these {n_colours} different colours:")
    legend = make_legend(n_colours)
    print(legend)
    print(f"You have {max_guesses} chances to guess the secret code.")
    print("Try to guess it as quickly as possible.")

    # randomly generate the secret code
    secret_code = generate_secret_code(n_pegs, n_colours)
    guess_count = 0
    guess_history = []

    solutions = make_all_solutions(n_pegs, n_colours)
    n_solutions = len(solutions)

    print(f"There are {n_solutions} possible secret codes.")

    while guess_count < max_guesses:
        guess_label = make_guess_label(guess_count + 1)
        guess_digits = input(f"{guess_label} ")
        guess_code = parse_code(guess_digits, n_pegs, n_colours)
        if guess_code is None:
            print(f"Try again. Enter exactly {n_pegs} numeric digits using:")
            print(legend)
        else:
            guess_count = guess_count + 1
            black_score, white_score = score_guess(n_pegs, n_colours, secret_code, guess_code)
            solutions = eliminate_solutions(n_pegs, n_colours, solutions, guess_code, black_score, white_score)
            n_solutions = len(solutions)
            guess_history.append((guess_digits, guess_code, black_score, white_score, n_solutions))
            print_guess_history(guess_history)
            if black_score == n_pegs:
                print(f"Congratulations! You won in {guess_count} tries.")
                break
    else:
        formatted_secret_code = format_code(secret_code)
        print(f"Game over. The secret code is: {formatted_secret_code}")

    print_stars()


if __name__ == '__main__':
    play()
