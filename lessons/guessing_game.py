"""Ask user for number, give hints about number if wrong"""

SECRET: int = 10  # is in all caps because it is a constant
guess: int = int(input("Guess a number! "))
playing: bool = True

while playing:  # Don't have to put playing == True, playing is the same thing
    if guess == SECRET:
        print("Correct! You did it! Believe in your dreams<3")
        playing = False
    else:
        if guess % 2 == 1:
            print("Your guess is odd. The answer is even. ")
        if guess < SECRET:
            print("Too low! ")
        else:  # guess is greater than SECRET
            print("Too high! ")
        guess = int(input("Wrong guess. Try again! "))  # must be an int value to match the data type

