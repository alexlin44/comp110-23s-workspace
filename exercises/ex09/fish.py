"""File to define Fish class."""

__author__ = "730465832"


class Fish:
    """Attributes of age."""
    age: int

    def __init__(self):
        """Initializes age to 0."""
        self.age = 0
    
    def one_day(self):
        """Adds one to age value for each day."""
        self.age += 1
        return None