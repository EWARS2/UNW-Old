# Title: Prime Numbers
# Chapter 5, Exercise 17
# Starting Out With Python, 5th Edition
# Date: 2/15/2024
# Author: Ethan Reed
# Class: Python Programming I
# Professor James Smith

def main():
    # Repeats for infinite testing!
    while 1:
        # Get number to test from user
        prompt = int(round(float(input("\nEnter an integer to test if it's prime : "))))

        # Test & display result
        if is_prime(prompt):
            print(f"Yep, {prompt} is prime.")
        else:
            print(f"Nope, {prompt} is NOT prime.")


def is_prime(number):
    # Yes, we test every number between 0 & itself.
    # Brute force code works exceptionally well.
    for test in range(number):
        
        # Skip dividing by 0, 1 & itself
        if not (test == 0 or test == 1 or test == number):
            
            # If anything has a remainder of 0, it's not prime.
            if (number % test) == 0:
                return False

    # If all previous tests fail,
    # this number must be prime!
    return True


# Call the main func
if __name__ == '__main__':
    main()
