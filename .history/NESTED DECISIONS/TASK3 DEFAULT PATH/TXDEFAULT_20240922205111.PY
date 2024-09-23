#If the user makes an invalid choice at any point, 
# incorporate a pass statement to handle it. 
# HINT: How can an else statement be of use here?

#Based on your corrected code from Task 1, expand the game. 
# If the user chooses "cave", ask them if they want to "light a torch" or 
# "proceed in the dark", and provide outcomes for each decision.

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
elif place == "cave":
        action = input("How would you like to proceed? ")
        if action == "light a torch":
            print("Now you can see your path to the hidden treasure")
        elif action == "proceed in the dark":
            print("Tread lightly on your path to the hidden treasure")
            