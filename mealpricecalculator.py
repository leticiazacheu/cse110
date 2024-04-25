# Input from user
child_meal = float(input("What is the price of a child's meal? " ))
adult_meal = float(input("What is the price of an adult's meal? "))
children_count = int(input("How many children are there? "))
adult_count = int(input("How many adults are there? "))
sales_tax = float(input("What is the sales tax rate? "))
print()
# Calculations for subtotal, taxes, and total
subtotal = child_meal * children_count + adult_meal * adult_count
print(f"Subtotal: ${subtotal:.2f}")
taxes = subtotal/100 * sales_tax
print(f"Sales Tax: ${taxes:.2f}")
total = subtotal + taxes
print(f"Total: ${total:.2f}")
print()
# Tip Calculation
tip = float(input("How much would you like to tip your server? "))
new_total = total + tip
print(f"Your total is ${new_total:.2f}")
print()
# Change Calculations
payment_amount = float(input("What is the payment amount? "))
change = payment_amount - new_total
print(f"Change: ${change:.2f}")
print()
print("Thank you for coming in today! I hope you enjoyed it!")