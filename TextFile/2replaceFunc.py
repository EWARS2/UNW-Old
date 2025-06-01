# Title: Program #2 -- File Replacement
# Author: Ethan Reed
# Class: Programming I: Java
# Professor Jonathan Zderad

def main():
    # file_path = "sample.txt"
    file_path = input("Enter file path: ")
    with open(file_path, 'r') as myFile:
        print("Strings are case sensitive")
        String1 = input("Find: ")
        String2 = input("Replace: ")

        file_data = myFile.read()
        file_data = file_data.replace(String1, String2)

        myFile.close()

    new_file_path = file_path + ".new"
    with open(new_file_path, 'w') as myFile:
        myFile.write(file_data)
        myFile.close()

# Call the main func
if __name__ == '__main__':
    main()
