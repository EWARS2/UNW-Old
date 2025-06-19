# Title: sub_cipher
# In-class Exercise
# Starting Out With Python, 5th Edition
# Date: 2/15/2024
# Author: Ethan Reed
# Class: Python Programming I
# Professor James Smith

def main():
    # Get input
    in_msg = str(input("Enter a message to process: "))

    # Process
    result_encrypted = sub_cipher(in_msg, 3)
    result_decrypted = sub_cipher(in_msg, -3)

    # Disp results
    print(f'\nEncrypted: {result_encrypted}')
    print(f'\nDecrypted: {result_decrypted}')


def sub_cipher(msg, offset):
    # Convert input for consistency
    msg = str(msg)
    msg = msg.capitalize()

    # Dec vars
    result = ''

    # Process
    for i in range(len(msg)):
        char = msg[i]
        result += chr(ord(char) + offset)

    return result


# Call the main func
if __name__ == '__main__':
    main()
