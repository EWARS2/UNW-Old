# Title: Interstates
# In-class program
# Starting Out With Python, 5th Edition
# Date: 3/18/2024
# Author: Ethan Reed
# Class: Python Programming I
# Professor James Smith


def main():
    routes = {"MN": 35, "SF": 80, "SE": 90, "WA": 94, "MI": 95, "TC": 494}

    # Create east_west dictionary based on highway # evenly /by 2
    east_west = {k: v for k, v in routes.items() if v % 2 == 0}
    print("East-West interstate highways")
    for key,value in east_west.items():
        print(f'{key}: {value}')

    print()
    # Determine important routes - divisible by 5
    important = {k: v for k, v in east_west.items() if v % 5 == 0}
    print("Important routes:")
    for key, value in important.items():
        print(f'{key}: {value}')


# Call the main func
if __name__ == '__main__':
    main()