def mimic(my_words: str, letter_idx: str) -> str:
    """Outputs the character of my_words at index letter_idx."""
    if letter_idx < len(my_words):
        return my_words[letter_idx]
    else:
        print("Too high of an index")

print(mimic("Hello", 0))