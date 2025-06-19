# Title: Product
# In-Class Exercise
# Starting Out With Python, 5th Edition
# Date: 2/7/2024
# Author: Ethan Reed
# Class: Python Programming I
# Professor James Smith


def main():
    in1 = int(round(float(input("First integer: "))))
    in2 = int(round(float(input("Second integer: "))))
    print(f'Product: {product(in1, in2)}')


def product(num1, num2):
    return num1 * num2


# Call the main func
if __name__ == '__main__':
    main()
