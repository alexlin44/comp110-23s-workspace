"""The tests we are using for the dictionary utilities."""


__author__ = "730465832"


from exercises.ex07.dictionary import invert, favorite_color, count
import pytest


def test_invert_nonunique():
    """Tests if invert correctly asserts a key value when the values are not unique."""
    with pytest.raises(KeyError):
        my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
        invert(my_dictionary)


def test_invert_numbers():
    """Tests if invert works properly for numbers and strings."""
    input_dict = {"one": "1", "two": "2", "three": "3"}
    assert invert(input_dict) == {"1": "one", "2": "two", "3": "three"}


def test_invert_strings():
    """Tests if invert works properly for a two string values."""
    input_dict = {"apple": "red", "banana": "yellow", "orange": "orange"}
    assert invert(input_dict) == {"red": "apple", "yellow": "banana", "orange": "orange"}


def test_favorite_equal():
    """Edge case: tests what happens when there is a tie for favorite color."""
    input_dict = {"Alex": "red", "Jackson": "red", "Caden": "pink", "Arnav": "green", "Kyle": "green"}
    assert favorite_color(input_dict) == "red"


def test_favorite_red():
    """Use case that checks that the function does return the most frequent color."""
    input_dict = {"Alex": "red", "Bob": "blue", "Charlie": "red", "David": "green", "Eddie": "red"}
    assert favorite_color(input_dict) == "red"


def test_favorite_green():
    """Use case that checks that order does not matter."""
    input_dict = {"David": "green", "Alex": "red", "Bob": "blue", "Eddie": "red"}
    assert favorite_color(input_dict) == "red"


def test_count_empty_list():
    """Edge case that tests an empty list returns an empty dict."""
    input_list = []
    assert count(input_list) == {}


def test_count_same_fruit():
    """Tests some items appearing more than once."""
    input_list = ["apple", "banana", "orange", "banana", "apple", "apple"]
    assert count(input_list) == {"apple": 3, "banana": 2, "orange": 1}


def test_count_equal_fruit():
    """Tests what returns when each fruit appears once."""
    input_list = ["apple", "banana", "orange"]
    assert count(input_list) == {"apple": 1, "banana": 1, "orange": 1}