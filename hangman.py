""" hangman.py
The game of hangman on the command line for one player
preciouschicken.com
"""

import random
import sys
from enum import Enum, auto


# Default number of lives player starts with
PLYR_LIVES = 7


class Result(Enum):
    """Winning or losing game end condition"""
    UNDECIDED = auto()
    WIN = auto()
    LOSE = auto()


def select_tgt_wrd() -> str:
    """Returns word from word list text file

    Opens word list file, selects a word at random, converts to lower case.
    Exits with error message if file not found.
    """
    try:
        with open("word_list.txt", "r", encoding="latin-1") as wrd_list:
            return random.choice(list(line.strip() for line in wrd_list)).lower()
    except IOError:
        sys.exit("Error: File 'word_list.txt' not found.")


def find_char(wrd: str, user_char: str) -> bool:
    """Returns true if user character in target word"""
    for char in wrd:
        if char == user_char:
            return True
    return False


def reveal_wrd(wrd: str, correct_chars: list) -> None:
    """Prints position of correct chars e.g. '*a**' """
    reveal = ""
    for char in wrd:
        if char in correct_chars:
            reveal += char
        else:
            reveal += "*"
    print(reveal)


def validate_input() -> str:
    """Ensures user has entered one character only

    Asks user for input, validates is string and one char
    Converts to lower-case
    """
    char = None
    valid_input = False
    while not valid_input:
        char = input("Please enter your next guess: ")
        if char.isalpha() and len(char) == 1:
            valid_input = True
        else:
            print("You must enter one character e.g. 't'.")
    return char.lower()


def commence_turn(tgt_wrd: str) -> Result:
    """Loop inputting user characters until win or lose situation

    Keeps count of user lives, minuses each wrong attempt.
    Records all guessed character, if user repeats then prints.
    """
    # Ensures unique characters only counted in length
    tgt_wrd_len = len(''.join(set(tgt_wrd)))
    correct_chars, incorrect_chars = [], []
    count_plyr_lives = PLYR_LIVES
    game_result = Result.UNDECIDED
    while game_result is Result.UNDECIDED:
        reveal_wrd(tgt_wrd, correct_chars)
        user_char = validate_input()
        if user_char in correct_chars + incorrect_chars:
            print("Character '" + user_char + "' already guessed.")
        elif find_char(tgt_wrd, user_char):
            correct_chars.append(user_char)
            if len(correct_chars) == tgt_wrd_len:
                game_result = Result.WIN
        else:
            # Wrong guess removes life
            count_plyr_lives -= 1
            incorrect_chars.append(user_char)
            if count_plyr_lives > 0:
                print("Incorrect guess, lives remaining: " + str(count_plyr_lives))
            else:
                game_result = Result.LOSE
    return game_result


def main():
    """Calls functions to select word, commence turn and prints result"""
    tgt_wrd = select_tgt_wrd()
    if commence_turn(tgt_wrd) == Result.WIN:
        print("congratulations you win")
    else:
        print("you lose")


if __name__== "__main__" :
    main()
