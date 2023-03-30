"""More list utility tests."""

__author__ = "730465832"


def only_evens(list_1: list[int]) -> list[int]:
    """Returns only the even integers of a list."""
    even_list: list[int] = []
    for element in list_1:
        if element % 2 == 0:
            even_list.append(element)
    return even_list


def concat(list_a: list[int], list_b: list[int]) -> list[int]:
    """Returns a new list containing all the elements of both given lists."""
    combined_list: list[int] = []
    for element in list_a:
        combined_list.append(element)
    for element in list_b:
        combined_list.append(element)
    return combined_list


def sub(list_x: list[int], start_index: int, end_index: int) -> list[int]:
    """Returns a subset of a given list."""
    sub_list: list[int] = []
    if start_index == len(list_x):
        return []
    if start_index < 0:
        start_index = 0
    if end_index < 0:
        end_index = 0
    if end_index > len(list_x):
        end_index = len(list_x)
    for i in range(start_index, end_index):
        sub_list.append(list_x[i])
    return sub_list