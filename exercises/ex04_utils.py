"""Functions that test different aspects of lists of integers."""

__author__ = "730465832"


def all(list_1: list[int], y: int) -> bool:
    """Returns whether or not an integer matches every index of a list."""
    list_index: int = 0
    check: bool = False
    while list_index < len(list_1):
        if y == list_1[list_index]:
            check = True
        else:
            return False
        list_index += 1
    return check


def max(list_int: list[int]) -> int:
    """Returns highest integer value in a list."""
    if len(list_int) == 0:
        raise ValueError("max() arg is an empty List")
    highest: int = list_int[0]
    max_index: int = 1
    while max_index < len(list_int):
        if list_int[max_index] > highest:
            highest = list_int[max_index]
        max_index += 1
    return highest
        

def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Returns whether or not every element of two lists is identical."""
    equal_idx = 0
    check: bool
    if list_1 == [] and list_2 == []:
        check = True
    if len(list_1) == len(list_2):
        while equal_idx < len(list_1):
            if list_1[equal_idx] == list_2[equal_idx]:
                check = True
            else:
                return False
            equal_idx += 1
        return check
    else:
        return False