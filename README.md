## cli-hangman

A game of hangman, written in Python, to be played on the command line.  Words to guess are contained in the *word_list.txt* file which must be in the same directory as the Python executable.

You have seven lives, each incorrect guess of a letter removes a life.  Running out of lives or correctly guessing the word exits the program.  Once a letter has been incorrectly guessed once it will not remove additional lives if guessed again (i.e. entering the same incorrect letter repeatedly will only lose one life).

To begin enter at the command line: `python hangman.py`

### Screenshot

Successfully guessing the word "universe":

![Screenshot of cli-hangman](https://github.com/PreciousChicken/cli-hangman/blob/main/hangmain_screenshot.png)
