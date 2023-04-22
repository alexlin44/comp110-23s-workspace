"""File to define Bear class."""

__author__ = "730465832"


class Bear:
    """Attributes of age and hunger."""
    age: int
    hunger_score: int

    def __init__(self):
        """Initializes age and hunger_score to 0."""
        self.age = 0
        self.hunger_score = 0
    
    def one_day(self):
        """Adds one to age and hunger_score for each day."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int):
        """Updates hunger score based on how much eaten."""
        self.hunger_score += num_fish