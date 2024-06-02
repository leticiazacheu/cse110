# Shopping Cart Program

# Start an empty list to store items in the shopping cart
shopping_cart = []

# Function to display the menu
def display_menu():
    print("\nWelcome to the Shopping Cart Program!\n")
    print("Please select one of the following:")
    print("1. Add item")
    print("2. View cart")
    print("3. Quit")

# Function to add an item to the shopping cart
def add_item():
    item = input("What item would you like to add? ")
    shopping_cart.append(item)
    print(f"'{item}' has been added to the cart.")

# Function to view the contents of the shopping cart
def view_cart():
    print("\nThe contents of the shopping cart are:")
    for index, item in enumerate(shopping_cart, start=1):
        print(f"{index}. {item}")

# Main function to run the program
def main():
    while True:
        display_menu()
        choice = input("Please enter an action: ")
        if choice == '1':
            add_item()
        elif choice == '2':
            view_cart()
        elif choice == '3':
            print("Thank you. Goodbye.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()