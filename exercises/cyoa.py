"""A medieval themed choose your own adventure game."""


__author__ = "730465832"


import random

# global variables
points: int = 0
player: str = ""
finished: bool = False

# constants
SWORD_EMOJI: str = "\U0001F5E1"
DRAGON_EMOJI: str = "\U0001F409"
HEART_EMOJI: str = "\U00002764"


def main() -> None:
    """Runs all functions together to structure the game."""
    global points, player, finished
    finished = False
    points = 0
    greet()
    
    while not finished:
        print(f"\nTotal Adventure Points: {points}")
        choice: int = input_choice()
        monster_list: list[str] = ["goblin", "ghoul", "skeleton", "werewolf", "orc"]

        if choice == 1:
            fight_enemy(monster_list[random.randint(0, 4)], random.randint(1, 7))
        elif choice == 2:
            explore_forest(points)
        elif choice == 3:
            visit_village()
        elif choice == 4:
            play_with_dragon()
        else:
            print(f"Goodbye {player}, thanks for playing! I hope to see you again soon {HEART_EMOJI}")
            print(f"\nTotal Adventure Points: {points}")
            finished = True

    return None


def greet() -> None:
    """Introduces player to the game and asks for their name."""
    global player
    player = input("What is your name, swordfighter? ")
    print(f"Welcome {player} to the adventure of a lifetime! You are a brave swordfighter on a quest to defeat the {DRAGON_EMOJI}dragon{DRAGON_EMOJI}.")
    print(f"Your trusty sword {SWORD_EMOJI} is at your side, ready for battle.")
    return None


def input_choice() -> int:
    """Lets the player choose an activity to do."""
    global finished
    while not finished:
        print("\nWhat would you like to do next? (1-5)\n")
        print("1. Fight an enemy")
        print("2. Explore the forest")
        print("3. Visit a village")
        print("4. Play with a dragon")
        print("5. End adventure")
        choice = int(input("\nEnter your choice: "))
        if 1 <= int(choice) <= 5:
            choice = int(choice)
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
    return choice


def fight_enemy(enemy: str, difficulty: int) -> None:
    """Prompt for 'Fight an enemy'."""
    print(f"\nYou encounter a {enemy} in your travels!")
    print(f"The {enemy} has a difficulty rating of {difficulty}.")
    print(f"You draw your sword {SWORD_EMOJI} and prepare to fight!")
    global points
    if random.randint(1, 10) <= difficulty:
        print(f"The {enemy} defeats you! You lose 1 adventure point.")
        points -= 1
    else:
        print(f"You defeat the {enemy} and gain 2 adventure points!")
        points += 2
    
    return None


def explore_forest(points2: int) -> int:
    """Prompt for 'Explore the forest'."""
    global points
    print("\nYou venture deep into the forest, in search of the dragon's lair.")
    print("You hear strange noises in the distance and must decide whether to investigate or not.")
    choice = input("Do you investigate the noises? (y/n) ")
    if choice.lower() == "y":
        print("You find a hidden treasure and gain 3 adventure points!")
        points2 = 3
    else:
        print("You continue your journey through the forest.")
    #  Assign the updated points value to the global variable 'points'
    points += points2

    return points


def visit_village() -> None:
    """Prompt for 'Visit a Village'."""
    print("\nYou come across a small village in your travels.")
    print("You decide to take a break and rest at the local inn.")
    global points

    if random.randint(1, 10) <= 5:
        print("You overhear a group of travelers talking about a secret dragon weakness!")
        print("You gain 4 adventure points for your discovery!")
        points += 4
    
    return None


def play_with_dragon() -> None:
    """Prompt for 'Play with a dragon'."""
    print(f"{player}, you come across the {DRAGON_EMOJI} dragon's lair. You can hear its snarls and feel the heat of its flames grow hotter. What do you do?")
    print("1. Sneak into the lair")
    print("2. Challenge the {DRAGON_EMOJI} dragon to a fight")
    print("3. Flee from the lair")
    
    choice = input("Enter your choice (1-3): ")
    global points
 
    if choice == "1":
        print(f"{player}, you try to sneak into the lair but the {DRAGON_EMOJI} dragon is too alert and catches you. You lose 5 adventure points.")
        points -= 5
    elif choice == "2":
        print(f"{player}, you charge at the dragon with your {SWORD_EMOJI} sword drawn. Roll a dice to see if you hit the {DRAGON_EMOJI} dragon.")
        hit_roll: int = random.randint(1, 6)
        if hit_roll >= 4:
            print(f"You hit the {DRAGON_EMOJI} dragon and deal 10 damage! You gain 10 adventure points.")
            points += 10
        else:
            print(f"You miss the {DRAGON_EMOJI} dragon and it counterattacks. You lose 10 health and 5 adventure points.")
            points -= 5
    elif choice == "3":
        print(f"{player}, you run away from the lair and try to come up with a new plan. You gain 5 adventure points.")
        points += 5
    else:
        print("Invalid choice. Try again.")
        play_with_dragon()

    return None


if __name__ == "__main__":
    main()