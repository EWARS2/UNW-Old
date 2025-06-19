# Title: Buttons & Displaying info - show_courses.py
# In-class program
# Starting Out With Python, 5th Edition
# Date: 3/18/2024
# Author: Ethan Reed
# Class: Python Programming I
# Professor James Smith

import tkinter


class ShowInfoGUI:
    def __init__(self):
        # Create main window
        self.main_window = tkinter.Tk()

        # Create two frames
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Create a blank label in the top frame
        self.value = tkinter.StringVar()
        self.courses_label = tkinter.Label(self.top_frame, textvariable=self.value)

        # Create the two buttons in the bottom frame
        self.courses_button = tkinter.Button(self.bottom_frame, text='Show Info', command=self.show_info)
        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)

        # Pack the label
        self.courses_label.pack()
        # Pack the buttons
        self.courses_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Pack the frames
        self.top_frame.pack()
        self.bottom_frame.pack()

        # Enter the tkinter main loop
        tkinter.mainloop()

    # Define the show_info function
    def show_info(self):
        self.value.set('Data Comm\nDatabase\nPython')


# Create an Instance of ShowInfoGUI
if __name__ == '__main__':
    show_info = ShowInfoGUI()
