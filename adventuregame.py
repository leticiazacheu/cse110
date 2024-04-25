# Adventure Game
beginning = input("You are living your normal life and suddenly a pandemic happens! You have two options: MASKS or HOME. Which one do you pick? ")

# Initialize a boolean variable for vaccination status
vaccinated = False

# Option 1
if beginning.lower() == 'masks':
    vaccine = input("You chose to wear a mask and be safe. Good job! However, just a mask is not enough. The pfizer vaccine was created. What do you do: TAKE or REFUSE? ")
    if vaccine.lower() == 'take':
        vaccinated = True  # Update the vaccination status
        symptoms = input("Yay! You took the COVID vaccine! However, there are some symptoms, choose which one you have: FEVER or SORENESS? ")
        if symptoms.lower() == 'fever':
            print("This is terrible! But your fever should go away in a week! I hope you feel better soon!")
        elif symptoms.lower() == 'soreness':
            print("I'm sorry! Your soreness should be gone in 4 days! I hope you feel better!")
        else:
            print("I'm sorry. I didn't understand that.")            
    elif vaccine.lower() == 'refuse': 
        print('You are refusing to take the COVID-19 vaccine. That is okay! Everyone has an option, and I hope you do not get sick.')
    else: 
        print("I'm sorry. I didn't understand that.")        

# Option 2
elif beginning.lower() == 'home':
    print('You chose to stay at home. Remember to practice social distancing and wash your hands regularly.')

# Invalid input
else:
    print("I'm sorry. I didn't understand that.")

# Check if the player is vaccinated and at home
if vaccinated and beginning.lower() == 'home':
    print("You are vaccinated and staying at home. You're doing a great job protecting yourself and others!")

# Check if the player is not vaccinated and at home
elif not vaccinated and beginning.lower() == 'home':
    print("You are not vaccinated and staying at home. Please consider getting vaccinated when you have the chance.")

# Check if the player is vaccinated and chose masks
elif vaccinated and beginning.lower() == 'masks':
    print("You are vaccinated and wearing a mask. You're taking excellent precautions against the pandemic!")

# Check if the player is not vaccinated and chose masks
elif not vaccinated and beginning.lower() == 'masks':
    print("You are not vaccinated and wearing a mask. It's a good start, but please consider getting vaccinated for added protection.")

# Invalid input for the second time (outside of the initial choice)
else:
    print("I'm sorry. I didn't understand that. Please try again.")
    