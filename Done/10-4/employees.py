# Title: Employee Class - Employee Class
# Chapter 10, Exercise 4 
# Starting Out With Python, 5th Edition
# Date: 2/15/2024
# Author: Ethan Reed
# Class: Python Programming I
# Professor James Smith

def main():
    pass

class Employee:
    def __init__(self, name, id, dept, job_title):
        self.__name = name
        self.__id = id
        self.__dept = dept
        self.__job_title = job_title
    
    def set_name(self, name):
        self.__name = name
    
    def set_id(self, id):
        self.__id = id
    
    def set_dept(self, dept):
        self.__dept = dept
    
    def set_job_title(self, job_title):
        self.__job_title = job_title
    
    def get_name(self):
        return self.__name
    
    def get_id(self):
        return self.__id
    
    def get_dept(self):
        return self.__dept
    
    def get_job_title(self):
        return self.__job_title


# Call the main func
if __name__ == '__main__':
    main()
