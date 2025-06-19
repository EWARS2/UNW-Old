# Title: nested
# (Volume of multiple 3D boxes using nested for loops)
# Date: 2/7/2024
# Author: Ethan Reed
# Class: Python Programming I
# Professor James Smith

# Define height in feet
# Currently constant.
height = .25

# Displays header showing formatting
print("volume = length * width * height")

# Define length in feet
# Repeat from sizes ranging from 1 to 10 ft
for length in range(1, 11):

    # Define width in feet
    # Repeat from sizes ranging from 1 to 5 ft
    for width in range(1, 6):
    
        # Calculate volume
        volume = length * width * height
        
        # Formatted & aligned print 'volume = length * width * height' 
        print(f"{volume:<6} = {length:^6} * {width:^5} * {height:^6}")


