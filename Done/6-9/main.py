# Title: Average of Numbers
# Chapter 6, Exercise 9
# Starting Out With Python, 5th Edition
# Date: 2/15/2024
# Author: Ethan Reed
# Class: Python Programming I
# Professor James Smith

def main():
    average('numbers.txt')


def average(filename):
    # Declare vars
    total = 0
    counter = 0
    
    try:
        # Open file for reading
        file_variable = open(str(filename),'r')

        # For every line
        while 1:
            # Get line & clear formatting
            line = file_variable.readline()
            line = line.rstrip()

            # If end of file, break.
            if line=='':
                break
            else:
                # Add value to total
                total += float(line)
                
                # Print current line
                print(f'{counter+1:>3} {line}')

                # Inc counter
                counter+=1
                
    except IOError:
        print(f"Error: Problem opening {filename}")
        print("Please double check the file exists & isn't corrupt.")
        print("Not every value was processed.")
    except ValueError:
        print(f"Error: Line {counter} of {filename} isn't formatted correctly.")
        print(f"It currently reads: {line}")
        print("Not every value was processed.")

    # Calculate average
    if counter == 0:
        average = None
    else:
        average = total / counter
    
    # Display result
    print(f'\nEntry count: {counter}')
    print(f'Entry total: {total}')
    print(f'Entry average: {average}')
    print('Do note that this program treats blank lines as end of file.')


# Call the main func
if __name__ == '__main__':
    main()
