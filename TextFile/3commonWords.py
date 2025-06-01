# Title: Program #3 -- Common Words APP
# Author: Ethan Reed
# Class: Programming I: Java
# Professor Jonathan Zderad

def main():
    sentence_ends = '.!?'

    # file_path = "sample.txt"
    file_path = input("Enter file path: ")
    with (open(file_path, 'r') as myFile):
        # Create a dictionary titled dictionary for a bank for words
        dictionary = {}

        for line in myFile:
            for word in line.split():
                # Format words consistently
                word = word.lower().rstrip(sentence_ends)

                # Update count
                if word not in dictionary:
                    dictionary[word] = 0
                dictionary[word] += 1

        myFile.close()

    sorted_words = sorted(dictionary, key=dictionary.get, reverse=True)

    n = abs(int(input("Print how many places of common words? :")))
    print("Most used: ")
    for i in range(n):
        print(str(i+1) + ". " + sorted_words[i])

# Call the main func
if __name__ == '__main__':
    main()
