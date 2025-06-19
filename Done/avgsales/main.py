# Title: avgSales
# Date: 2/7/2024
# Author: Ethan Reed
# Class: Python Programming I
# Professor James Smith

# Innit vars
sum = count = avg = 0

# Display operation
print("Enter the value of a sale... type 0 to stop.")

# Forever loop with inline break
while True:

    # Get sale from user
    amount = float(input("Sale amount: "))
    
    # As noted in operation, list is 0 terminated.
    # If 0, break.
    if amount == 0:
        break
    
    #If we don't need to break,
    else:
    
        # Add to the sum
        sum = sum + amount
        
        # Inc the counter
        count = count + 1

# Div by 0 check
if count > 0:
    
    #Calc average
    avg = (sum / count)

# Disp results with formatting
print(f"Total sales: "f"${sum:,.2f}")
print(f"Number of sales: {count}")
print("Average sale: "f"${avg:,.2f}")




# Congrats Dr. Smith on the effecient code!
# Was originally trying to contain every entry in a list,
# and get the average from that.
# But this just uses fewer variables and progressively obtains the results.
# Reminds me of how often I've seen this in 6502 assembly...

