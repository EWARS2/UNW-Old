# Title: clock
# Date: 2/7/2024
# Author: Ethan Reed
# Class: Python Programming I
# Professor James Smith

#Dependencies
from time import sleep

# Get number of minutes to loop from user and convert to integer
minutesResponse = int(round((float(input("How many minutes?")))))

# Loop for 'minutesResponse' minutes
for minutesTemp in range(0,minutesResponse):

    # Loop for 60 seconds
    for secondsTemp in range(0,60):
        
        # Output with formatting minutes:seconds
        # Re-prints on the same line.
        print(f"\r{minutesTemp}:{secondsTemp}", end='')
        
        # Wait 1 second (supposedly). Actual clock part of the clock
        sleep(.1)


