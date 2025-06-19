# Title: Total Purchase
# Starting Out With Python 5th Edition
# Chapter 2, Exercise 4
# Date: 2/7/2024
# Author: Ethan Reed
# Class: Python Programming I
# Professor James Smith


# Innit vars
subTotal = count = total = 0
salesTaxPercent = 0.07

# Display operation
print("Enter the value each item... type 0 to stop.")

# Forever loop with inline break
while True:

    # Inc counter
    # Placed here so that first use it =1
    count = count + 1

    # Get item price from user. Convert to float
    amount = float(input(f"Item #{count} Price: $"))

    # As noted above, entries are 0 terminated
    # If 0 is entered, break.
    if amount == 0:
        break

    # If we don't need to break,
    else:

        # Add the current amount to the sum
        subTotal = subTotal + amount

# Calculate sales tax
salesTax = salesTaxPercent * subTotal

# Calculate final total
finalTotal = salesTax + subTotal

# Display results with formatting
print (f"Tax ({salesTaxPercent:.0%}): ${salesTax:,.2f}")
print (f"Subtotal: ${subTotal:,.2f}")
print ("===")
print (f"Total: ${finalTotal:,.2f}")


