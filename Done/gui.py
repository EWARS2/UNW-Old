# Title: Display Empty Window
# In-class program
# Starting Out With Python, 5th Edition
# Date: 4/5/2024
# Author: Ethan Reed
# Class: Python Programming I
# Professor James Smith

import tkinter


class MyGUI:
    def __init__(self):
        # Create main windows widget
        self.main_window = tkinter.Tk()

        # Create two label widgets with solid borders.
        self.main_window.title('My first GUI')

        # Create label widget
        self.label1 = tkinter.Label(self.main_window, text='Henlo, World.', borderwidth=4, relief='solid')
        self.label2 = tkinter.Label(self.main_window, text='This is my GUI program.')
        self.label1.pack(ipadx=20, ipady=20, padx=20, pady=20)
        self.label2.pack(ipadx=20, ipady=20, padx=20, pady=20)

        # Enter tkinter main loop
        tkinter.mainloop()


# Call the main func
if __name__ == '__main__':
    myGUI = MyGUI()
