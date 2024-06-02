# Shopping Cart Program 

# Additional creativity: 
# This program not only allows users to add, view, and remove items from the shopping cart,
# but also computes and displays the total price of the items in the cart. Prices are shown
# with the currency symbol $ and rounded to two decimals.

# Start empty lists to store items and their prices
items = []
prices = []

# Function to display the menu
def display_menu():
    print("\nWelcome to the Shopping Cart Program!\n")
    print("Please select one of the following:")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")

# Function to add an item to the shopping cart
def add_item():
    item = input("What item would you like to add? ")
    price = float(input(f"What is the price of '{item}'? $"))
    items.append(item)
    prices.append(price)
    print(f"'{item}' has been added to the cart.")

# Function to view the contents of the shopping cart
def view_cart():
    print("\nThe contents of the shopping cart are:")
    for i, item in enumerate(items, start=1):
        print(f"{i}. {item} - ${prices[i-1]:.2f}")

# Function to remove an item from the shopping cart
def remove_item():
    if not items:
        print("The shopping cart is empty.")
        return
    view_cart()
    index = int(input("Which item would you like to remove? ")) - 1
    if 0 <= index < len(items):
        removed_item = items.pop(index)
        removed_price = prices.pop(index)
        print(f"'{removed_item}' has been removed from the cart.")
    else:
        print("Sorry, that is not a valid item number.")

# Function to compute and display the total price of the items in the shopping cart
def compute_total():
    if not items:
        print("The shopping cart is empty.")
        return
    total_price = sum(prices)
    print(f"\nThe total price of the items in the shopping cart is ${total_price:.2f}")

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
            remove_item()
        elif choice == '4':
            compute_total()
        elif choice == '5':
            print("Thank you. Goodbye.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()