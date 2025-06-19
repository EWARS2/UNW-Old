# Title: Employee Production Worker - emp.py
# In-class program
# Starting Out With Python, 5th Edition
# Date: 3/18/2024
# Author: Ethan Reed
# Class: Python Programming I
# Professor James Smith


def main():
    pass


class Employee:
    def __init__(self, name, id_number):
        self.__name = name
        self.__id_number = id_number

    def set_name(self, name):
        self.__name = name

    def set_id_number(self, id_number):
        self.__id_number = id_number

    def get_name(self):
        return self.__name

    def get_id_number(self):
        return self.__id_number


# Subclass
class ProductionWorker(Employee):
    def __init__(self, name, id_number, shift_number, pay_rate):
        # Call superclass __init__ method
        Employee.__init__(self, name, id_number)

        # Init the shift_number & pay_rate attr
        self.__shift_number = shift_number
        self.__pay_rate = pay_rate

    def set_shift_number(self, shift_number):
        self.__shift_number = shift_number

    def set_pay_rate(self, pay_rate):
        self.__pay_rate = pay_rate

    def get_shift_number(self):
        return self.__shift_number

    def get_pay_rate(self):
        return self.__pay_rate


# Call the main func
if __name__ == '__main__':
    main()
