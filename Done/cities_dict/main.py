# Title: Cities
# In-class program
# Starting Out With Python, 5th Edition
# Date: 3/18/2024
# Author: Ethan Reed
# Class: Python Programming I
# Professor James Smith


def main():
    # Dec
    degrees_latitude = {"Narobi": 1,
                        "Johannesburg": 26,
                        "Cairo": 30,
                        "Abidjan": 5,
                        "Khartoum": 15,
                        "Zanzibar": 6
                        }

    # What on God's green Earth is this code
    print({k: v for k, v in degrees_latitude.items() if v< 23})


# Call the main func
if __name__ == '__main__':
    main()

