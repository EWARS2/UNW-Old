# Title: Program #2 -- Full Name App
# Author: Ethan Reed
# Class: Programming I: Java
# Professor Jonathan Zderad

def main():
    my_string = input("Enter string to translate to oppish :")
    print(oppish(my_string))


def oppish(s):
    # 'Y' is considered to be a vowel
    consonants = 'bcdfghjklmnpqrstvwxz'
    word_ends = ' ,.-_~/\\\n\"\''
    return_string = ''
    s_len = len(s)
    for i in range(s_len):
        i_char = s[i]
        return_string += i_char
        if i + 1 < s_len:
            i_char2 = s[i + 1]
            if i_char in consonants and i_char2 not in consonants and i_char2 not in word_ends:
                return_string += 'opp'
    return return_string


# Call the main func
if __name__ == '__main__':
    main()
