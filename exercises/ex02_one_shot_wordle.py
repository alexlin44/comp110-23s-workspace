"""This is our take on a word guessing game!"""

__author__ = "730465832"

secret_word: str = "python"
word_guess: str = input(f"What is your {len(secret_word)}-letter guess? ")
i: int = 0  # index to move from one digit to the next

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
boxes: str = ""  # This will serve as the string of boxes

while (len(word_guess) != len(secret_word)):  # ensures guess is the correct amount of characters to the secret word
    word_guess = input(f"That was not {len(secret_word)} letters! Try again: ")

exists: bool = False  # boolean variable to check if character exists in the word
idx: int = 0  # alternate index of secret word

while i < len(word_guess):
    if (word_guess[i] == secret_word[i]):
        boxes += GREEN_BOX
    else:
        while exists == (not True) and idx < len(secret_word):
            if (secret_word[idx] == word_guess[i]):
                exists = True  # ends the loop if the index of the secret word matches the guess
            idx += 1
        idx = 0
        if exists == (True):
            boxes += YELLOW_BOX
            exists = False
        else:
            boxes += WHITE_BOX
            exists = False
    i += 1
print(boxes)

if (word_guess == secret_word):
    print("Woo! You got it!")
else:
    print("Not Quite. Play again soon!")