# Introduction
print("Welcome to the Dark Forest Adventure Game!")
print("You find yourself in a dark forest. You have a few options...")

# First Scenario: Choose a Path
print("\nYou come across a fork in the road.")
print("Do you want to go LEFT or RIGHT?")

# Get user's choice for the first scenario
choice1 = input("Enter your choice (LEFT/RIGHT): ").upper()

# Check user's choice for the first scenario
if choice1 == "LEFT":
    # Second Scenario: Encounter a Creature
    print("\nYou encounter a mysterious creature.")
    print("Do you want to TALK to the creature or FLEE?")

    # Get user's choice for the second scenario
    choice2 = input("Enter your choice (TALK/FLEE): ").upper()

    # Check user's choice for the second scenario
    if choice2 == "TALK":
        # Third Scenario: Discover a Hidden Path
        print("\nThe creature leads you to a hidden path.")
        print("Do you want to FOLLOW the path or RETURN?")
        
        # Get user's choice for the third scenario
        choice3 = input("Enter your choice (FOLLOW/RETURN): ").upper()

        # Check user's choice for the third scenario
        if choice3 == "FOLLOW":
            print("\nYou find a treasure at the end of the path. Congratulations!")
        elif choice3 == "RETURN":
            print("\nYou decide to return. The creature disappears into the forest.")
        else:
            print("\nSorry, that's not a valid choice.")
    elif choice2 == "FLEE":
        print("\nYou run away from the creature and find yourself lost in the forest.")
    else:
        print("\nSorry, that's not a valid choice.")
elif choice1 == "RIGHT":
    # Second Scenario: Discover an Old Hut
    print("\nYou discover an old hut.")
    print("Do you want to ENTER the hut or IGNORE it?")
    
    # Get user's choice for the second scenario
    choice2 = input("Enter your choice (ENTER/IGNORE): ").upper()

    # Check user's choice for the second scenario
    if choice2 == "ENTER":
        # Third Scenario: Meet a Wise Wizard
        print("\nYou meet a wise wizard inside the hut.")
        print("Do you want to LISTEN to the wizard or LEAVE?")
        
        # Get user's choice for the third scenario
        choice3 = input("Enter your choice (LISTEN/LEAVE): ").upper()

        # Check user's choice for the third scenario
        if choice3 == "LISTEN":
            print("\nThe wizard shares valuable wisdom with you. You feel enlightened.")
        elif choice3 == "LEAVE":
            print("\nYou decide to leave the hut. The wizard bids you farewell.")
        else:
            print("\nSorry, that's not a valid choice.")
    elif choice2 == "IGNORE":
        print("\nYou ignore the hut and continue exploring the forest.")
    else:
        print("\nSorry, that's not a valid choice.")
else:
    print("\nSorry, that's not a valid choice.")