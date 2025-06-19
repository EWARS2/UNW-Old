# Title: Employee Production Worker - create.py
# In-class program
# Starting Out With Python, 5th Edition
# Date: 3/18/2024
# Author: Ethan Reed
# Class: Python Programming I
# Professor James Smith

import emp


def main():
    # Local vars
    worker_name = ''
    worker_id = ''
    worker_shift = 0
    worker_pay = 0.0

    # Get data attributes
    worker_name = input("Enter the Name: ")
    worker_id = input("Enter the ID Number: ")
    worker_shift = input("Enter the Shift Number: ")
    worker_pay = input("Enter the Hourly Pay Rate: $")
    print()

    # Create an instance of ProductionWorker
    worker = emp.ProductionWorker(worker_name, worker_id, worker_shift, worker_pay)

    # Disp info
    print('Production worker information:')
    print(f'Name: {worker.get_name()}')
    print(f'ID Number: {worker.get_id_number()}')
    print(f'Shift: {worker.get_shift_number()}')
    print(f'Hourly Pay Rate: ${worker.get_pay_rate()}')


# Call the main func
if __name__ == '__main__':
    main()
