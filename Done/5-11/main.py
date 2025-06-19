# Title: Math Quiz
# Chapter 5, Exercise 11
# Starting Out With Python, 5th Edition
# Date: 2/7/2024
# Author: Ethan Reed
# Class: Python Programming I
# Professor James Smith

from random import *


def main():
    while 1:
        question(randint(0,999),randint(0,999))


def question(num1, num2):
    print(f'  {num1:>3}')
    print(f'+ {num2:>3}')
    answer = num1 + num2
    prompt = input("= ")
    if str(prompt) == str(answer):
        print("Conglaturations!! That is correct!")
    else:
        print(f"Correct answer: {answer}")
        print("I get angrier with every wrong question.")


# Call the main func
if __name__ == '__main__':
    main()
