"""example of a while loop statement"""

counter: int = 0 
maximum: int = int(input("Count up to what number squared? "))
while counter < maximum:
    counter_squared: int = counter ** 2
    print(f"The square of {str(counter)} is {str(counter_squared)}")
    counter = counter + 1

print(chr(129313))