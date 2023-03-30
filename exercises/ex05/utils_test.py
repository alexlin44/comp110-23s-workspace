"""Testing my functions in utils."""

__author__ = "730465832"


from exercises.ex05.utils import only_evens, sub, concat


def test_empty_evens() -> None:
    """Tests if only_evens works with an empty set."""
    assert only_evens([]) == []


def test_only_odds() -> None:
    """Test if only evens returns an empty set when given a list of all odd integers."""
    assert only_evens([1, 3, 5]) == []


def test_evens_and_odds() -> None:
    """Tests both odd and even numbers."""
    assert only_evens([1, 2, 3, 4, 5, 6]) == [2, 4, 6]


def test_sub_empty() -> None:
    """Test if function works when list is empty."""
    assert sub([], 0, 0) == []


def test_sub_middle_to_end() -> None:
    """Test if function works when starting from the middle and going to the end."""
    assert sub([1, 2, 3, 4, 5], 1, 4) == [2, 3, 4]


def test_sub_first_to_middle() -> None:
    """Test if function works when starting from the beginning and going to the middle."""
    assert sub([1, 2, 3, 4, 5], 0, 3) == [1, 2, 3]


def test_concat_empty() -> None:
    """Tests if concat works with an empty list."""
    assert concat([], []) == []


def test_concat_list_and_list() -> None:
    """Test if concat works with two lists with more than one element."""
    assert concat([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]


def test_concat_list_and_single_element() -> None:
    """Test if concat works with a list and a single element."""
    assert concat([1, 2, 3], [4]) == [1, 2, 3, 4]
