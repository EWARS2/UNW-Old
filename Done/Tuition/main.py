# Title: Tuition
# Mid-term Challenge
# Starting Out With Python, 5th Edition
# Date: 3/4/2024
# Author: Ethan Reed
# Class: Python Programming I
# Professor James Smith

def main():
    # Dec vars
    incoming_cost = current_cost = 20000
    increase_rate = 0.03  # 3 percent
    total = 0

    print("Tuition\n")

    # Calculate and display
    for i in range(5):
        total += current_cost
        print(f'Year {(i+1):.0f}: ${current_cost:>12,.2f}     Total: ${total:>12,.2f}')
        current_cost += increase_rate * current_cost


# Call the main func
if __name__ == '__main__':
    main()