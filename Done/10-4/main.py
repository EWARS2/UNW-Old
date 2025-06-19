# Title: Employee Class - Main
# Chapter 10, Exercise 4 
# Starting Out With Python, 5th Edition
# Date: 2/15/2024
# Author: Ethan Reed
# Class: Python Programming I
# Professor James Smith

from employees import Employee


def main():
    # Store info
    # There's a better way of implementing this I think
    entries = [Employee("Susan Meyers", 47899, "Accounting", "Vice President"),
               Employee("Mark Jones", 39119, "IT", "Programmer"),
               Employee("Joy Rogers", 81774, "Manufacturing", "Engineer")]

    # Disp info
    print(f"{'Name':<15}{'ID Number':<15}{'Department':<17}Job Title")
    for i in range(len(entries)):
        print(f"{entries[i].get_name():<15}{entries[i].get_id():<15}{entries[i].get_dept():<17}{entries[i].get_job_title()}")


# Call the main func
if __name__ == '__main__':
    main()
