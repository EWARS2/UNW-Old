# Title: friend_book
# In-class program
# Starting Out With Python, 5th Edition
# Date: 3/18/2024
# Author: Ethan Reed
# Class: Python Programming I
# Professor James Smith


def main():

    friend_book = {"John": "Jamestown",
                   "Billy": "Le Ville",
                   "The Person Who Asked": "Sus town",
                   "Taco John": "Somewhere over the rainbow",
                   "Francis Bacon": "Fromage land"
                   }

    print(friend_book)

    friend_book["Tom"] = "Holland"
    friend_book["Fred"] = "Columbia Heights"

    print(friend_book)

    del friend_book['John']
    del friend_book['The Person Who Asked']

    print(friend_book)


# Call the main func
if __name__ == '__main__':
    main()