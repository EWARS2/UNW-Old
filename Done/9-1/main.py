# Title: Course Information
# Chapter 9, Exercise 1
# Starting Out With Python, 5th Edition
# Date: 2/15/2024
# Author: Ethan Reed
# Class: Python Programming I
# Professor James Smith

def main():
    course_room = {'CS101': '3004',
                   'CS102': '4501',
                   'CS103': '6755',
                   'NT110': '1244',
                   'CM241': '1411'
                   }
    course_instructor = {'CS101': 'Haynes',
                         'CS102': 'Alvarado',
                         'CS103': 'Rich',
                         'NT110': 'Burke',
                         'CM241': 'Lee'
                         }
    course_meet_time = {'CS101': "8:00 AM",
                        'CS102': "9:00 AM",
                        'CS103': "10:00 AM",
                        'NT110': "11:00 AM",
                        'CM241': "1:00 PM"}
    while 1:
        # Get course to search for
        search = str(input("(Type 'Q' to quit)Enter a Course Key to retrieve details from: "))
        print()

        # Exit if requested
        if search.capitalize() == 'Q':
            break

        # Retrieve & print results
        try:
            print(f'Room Number:   {course_room[search]}')
            print(f'Instructor:    {course_instructor[search]}')
            print(f'Meeting Time:  {course_meet_time[search]}')
        except KeyError:
            print(f'Course Key "{search}" not found in dictionary. '
                  "This could be an error on our end. "
                  "Please try again.")
        print()


# Call the main func
if __name__ == '__main__':
    main()
