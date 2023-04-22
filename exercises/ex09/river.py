"""File to define River class."""

__author__ = "730465832"


from exercises.ex09.fish import Fish
from exercises.ex09.bear import Bear


class River:
    """Class with attributes days, bears, and fish."""
    days: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Checks the ages of the river wildlife."""
        surviving_fish: list[Fish] = []
        for fish in self.fish:
            if fish.age <= 3:
                surviving_fish.append(fish)
        self.fish = surviving_fish

        surviving_bears: list[Bear] = []
        for bear in self.bears:
            if bear.age <= 5:
                surviving_bears.append(bear)
        self.bears = surviving_bears

        return None

    def remove_fish(self, amount: int):
        """Removes select amount of fish from river."""
        while amount > 0 and self.fish:
            self.fish.pop(0)
            amount -= 1

    def bears_eating(self):
        """Simulates bears eating and removing the fish from the river."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)
        return None
    
    def check_hunger(self):
        """Removes bears with a negative hunger score."""
        surviving_bears: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                surviving_bears.append(bear)
        self.bears = surviving_bears
        return None
        
    def repopulate_fish(self):
        """Algorithm to repopulate fish."""
        num_fish: int = len(self.fish)
        new_fish: int = (num_fish // 2) * 4
        for i in range(new_fish):
            self.fish.append(Fish())
        return None
    
    def repopulate_bears(self):
        """Algorithm to repopulate bears."""
        num_bears: int = len(self.bears)
        new_bears: int = num_bears // 2
        for i in range(new_bears):
            self.bears.append(Bear())
        return None
    
    def view_river(self):
        """Prints the fish and bear populations."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()
            
    def one_river_week(self):
        """Runs the river day 7 times to simulate a week."""
        for i in range(7):
            self.one_river_day()