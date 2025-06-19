# Title: Favorite Movies
# In-class exercise
# Starting Out With Python, 5th Edition
# Date: 2/14/2024
# Author: Ethan Reed
# Class: Python Programming I
# Professor James Smith


def main():
    # Get four movies
    movie1 = input("Movie 1: ")
    movie2 = input("Movie 2: ")
    movie3 = input("Movie 3: ")
    movie4 = input("Movie 4: ")

    # Open file using Append
    infile = open(r'movies.txt','a')

    # Write contents to file
    infile.write(movie1 + '\n')
    infile.write(movie2 + '\n')
    infile.write(movie3 + '\n')
    infile.write(movie4 + '\n')

    # Close file
    infile.close()

    # Open file for reading
    infile = open(r'movies.txt', 'r')

    # Read file contents to var
    file_contents = infile.read()
    print(file_contents)

    # Close file
    infile.close()


# Call the main func
if __name__ == '__main__':
    main()
