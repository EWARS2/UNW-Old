# Title: Program #1 -- File Statistics
# Author: Ethan Reed
# Class: Programming I: Java
# Professor Jonathan Zderad

def main():
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    sentence_ends = '.!?'

    #file_path = "sample.txt"
    file_path = input("Enter file path: ")
    with open(file_path, 'r') as myFile:
        letters = 0
        words = 0
        sentences = 0
        char = ' '
        for line in myFile:
            words += len(line.split())
            for char_num in range(len(line)):
                char_previous = char
                char = line[char_num]

                if char in sentence_ends and char_previous not in sentence_ends:
                    sentences += 1

                if char in alphabet:
                    letters += 1

        avgLetterPerWord = letters / words
        avgWordsPerSentence = words / sentences

        myFile.seek(0)
        print("First Line: " + myFile.readline())
        print("Last Line:  " + line)
        print()
        print("Letters:    " + str(letters))
        print("Words:      " + str(words))
        print("Sentences:  " + str(sentences))
        print()
        print(f"Avg Letter Count Per Word: {avgLetterPerWord:.1f}")
        print(f"Avg Words Per Sentence: {avgWordsPerSentence:.1f}")
        myFile.close()


# Call the main func
if __name__ == '__main__':
    main()
