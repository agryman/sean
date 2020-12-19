"""This module implements the hangman game."""

import random
from hangman.hangmanwordbank import HANGMANPICS, words


def load_words():
    """Returns a list of words."""

    return ['words', 'word', 'snake', 'tiger', 'tea'] + words


def display_gallows(wrong_guesses, max_wrong_guesses):
    """Prints the gallows and partially hung person."""

    print(HANGMANPICS[wrong_guesses])
    print(f'You have made {wrong_guesses} wrong guesses. ' +
          f'You have {max_wrong_guesses - wrong_guesses} guesses left.')


def display_word(word, letters_guessed):
    """Prints the word with underscores substituted for letters not guessed."""

    print(''.join([x if x in letters_guessed else '_' for x in word]))


def play_hangman():
    """Play the hangman game."""

    words = load_words()
    word = random.choice(words)

    max_wrong_guesses = 6
    wrong_guesses = 0
    guesses = 0
    letters_guessed = set()
    solved = False

    # run the loop until the player guesses correctly, or guesses wrong too many times
    while not solved and wrong_guesses < max_wrong_guesses:
        display_gallows(wrong_guesses, max_wrong_guesses)
        display_word(word, letters_guessed)

        # ask the player to guess a letter.
        while True:
            letter_guessed = input('Guess a letter: ')
            if len(letter_guessed) != 1:
                print('Error: Input must be a single character.')
                continue
            if not letter_guessed.isalpha():
                print('Error: Input must be a letter.')
                continue
            if letter_guessed in letters_guessed:
                print('Error: You already guessed that letter.')
            break

        guesses += 1
        letters_guessed.add(letter_guessed)

        if letter_guessed not in word:
            wrong_guesses += 1

        solved = all([x in letters_guessed for x in word])

    if solved:
        print(f'Congratulations! You guessed the right word in {guesses} guesses!')
    else:
        print(f'Congratulations! You lost :-(')

    print(f'The secret word is: {word}')
    print(f'You made {wrong_guesses} wrong guesses and {guesses - wrong_guesses} right guesses.')


play_hangman()
