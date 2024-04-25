# Adventure Game
beginning = input("You are living your normal life and suddenly a pandemic happens! You have two options: MASKS or HOME. Which one do you pick? ")
# Option 1
if beginning.lower() == 'masks':
    vaccine = input("You chose to wear a mask and be safe. Good job! However, just a mask is not enough. The pfizer vaccine was created. What do you do: TAKE or REFUSE? ")
    if vaccine.lower() == 'take':
        symptoms = input("Yay! You took the COVID vaccine! However, there are some symptoms, choose which one you have: FEVER or SORENESS? ")
        if symptoms.lower() == 'fever':
                print("This is terrible! But your fever should go away in a week! I hope you feel better soon!")
        elif symptoms.lower() == 'soreness':
                print("I'm sorry! Your soreness should be gone in 4 days! I hope you feel better!")
        else:
            print("I'm sorry. I didn't understand that.")            
    elif vaccine.lower() == 'refuse': 
        print('You are refusing to take the COVID-19 vaccine. That is okay! everyone has an option, and I hope you do not get sick.')
    else: 
        print("I'm sorry. I didn't understand that.")        

elif beginning.lower() == 'home':
    #use if/elif/else
    print('You chose home')

else:
    print("I'm sorry. I didn't understand that.")
    