"""Checks light, if green, says go."""

light: str = input("What color is the light? ").lower()

if(light == "green"):
    print("Go!")
else:
    if(light != "red"):
        if (light == "yellow"):
            print("Slow down!")
        else:
            print("WHAT?!? ")
    else:
        print("Stop!")
print("Don't look look at your phone!")