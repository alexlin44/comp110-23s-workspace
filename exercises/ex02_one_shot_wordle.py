"""This is our take on a word guessing game"""

__author__ = "730465832"

secret_word: str = "python"
word_guess: str = input(f"What is your {len(secret_word)}-letter guess? ")
i: int = 0 #index to move from one digit to the next

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

while (len(word_guess) != len(secret_word)):  #ensures guess is the correct amount of characters to the secret word
    word_guess = input(f"That was not {len(secret_word)} letters! Try again: ")

exists: bool = False #boolean variable to check if character exists in the word
idx: int = 0 #alternate index of secret word

while i < len(word_guess):
    if (word_guess[i] == secret_word[i]):
        print(f"{GREEN_BOX}", end = " ")
    else:
        while exists == (not True) and idx < len(secret_word):
            if (secret_word[idx] == word_guess[i]):
                exists: bool = True #ends the loop if the index of the secret word matches the guess
            idx += 1
        idx = 0
        if exists == (True):
            print(f"{YELLOW_BOX}", end = " ")
            exists = False
        else:
            print(f"{WHITE_BOX}", end = " ")
            exists = False
    i += 1

if (word_guess == secret_word):
    print(f"\nWoo! You got it!")
else: print(f"\nNot Quite. Play again soon!")