"""This is our take on a word guessing game!"""

__author__ = "730465832"

secret_word: str = "python"
word_guess: str = input("What is your 6-letter guess? ")
i: int = 0
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
boxes: str = ""

while (len(word_guess) != 6):
    word_guess = input("That was not 6 letters! Try again: ")

while i < len(word_guess):
    if (word_guess[i] == secret_word[i]):
        boxes += GREEN_BOX + " "
    else:
        boxes += WHITE_BOX + " "
    i += 1
print(boxes)

if (word_guess == secret_word):
    print("Woo! You got it!")
else: print("Not Quite. Play again soon!")