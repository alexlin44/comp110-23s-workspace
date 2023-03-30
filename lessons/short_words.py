def short_words(word_list: list[str]) -> list[str]:
    """Returns list of words that are shorteer than 5 characters."""
    short_list: list[str] = []
    for word in word_list:
        if len(word) >= 5:
            print(f"{word} is too long!")
        else:
            short_list.append(word)
    return short_list

my_list: list[str] = ["sun", "cloud", "sky"]

print(short_words(my_list))