"""Testing dictionary utilities."""


__author__ = "730465832"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Returns an inverted dictionary based on the inputted one."""
    inverted_dict = {}
    for key in input_dict:
        value = input_dict[key]
        if value in inverted_dict:
            raise KeyError("Values in the input dictionary must be unique.")
        inverted_dict[value] = key
    return inverted_dict


def favorite_color(dict_1: dict[str, str]) -> str:
    """Returns the favorite color that appears the most."""
    color_count = {}
    common_color: str = ""
    counter: int = 0
    for name in dict_1:
        color = dict_1[name]
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1
    
        if color_count[color] > counter or (color_count[color] == counter and color == list(dict_1.values())[0]):
            common_color = color
            counter = color_count[color]

    return common_color


def count(list_1: list[str]) -> dict[str, int]:
    """Returns a dictionary that corresonds each fruit to the number it appears."""
    counter = {}
    for item in list_1:
        if item in counter:
            counter[item] += 1
        else:
            counter[item] = 1
    return counter
