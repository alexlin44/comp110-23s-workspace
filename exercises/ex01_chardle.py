"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730465832"

word: str = input("Enter a 5-character word: ").lower()

if (len(word) != 5):
    print("Error: Word must contain 5 characters")
    exit()

character: str = input("Enter a single character: ").lower()

if (len(character) != 1):
    print("Error: Character must be a single character.")
    exit()

print("Searching for " + character + " in " + word)

match: int = 0

if (word[0] == character):
    print(character + " found at index 0")
    match += 1

elif (word[1] == character):
    print(character + " found at index 1")
    match += 1

elif (word[2] == character):
    print(character + " found at index 2")
    match += 1

elif (word[3] == character):
    print(character + " found at index 3")
    match += 1

elif (word[4] == character):
    print(character + " found at index 4")
    match += 1

if (match == 1):
    print(str(match) + " instance of " + character + " found in " + word)

if (match > 1):
    print(str(match) + " instances of " + character + " found in " + word)

if (match == 0):
    print("No instances of " + character + " found in " + word)