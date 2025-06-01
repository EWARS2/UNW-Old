# Title: Display Empty Window II: the sequel
# In-class program
# Starting Out With Python, 5th Edition
# Date: 4/5/2024
# Author: Ethan Reed
# Class: Python Programming I
# Professor James Smith

import tkinter


class MyGUI2:
    def __init__(self):
        # Create main windows widget
        self.main_window = tkinter.Tk()

        # Create 2 frames, 1 @ top of window & 1 @ bottom
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Create three label widgets for top frame
        self.label1 = tkinter.Label(self.top_frame, text='Minnesota')
        self.label2 = tkinter.Label(self.top_frame, text='Iowa')
        self.label3 = tkinter.Label(self.top_frame, text='Wisconsin')

        # Pack the top_frame labels
        self.label1.pack(side='top')
        self.label2.pack(side='top')
        self.label3.pack(side='top')

        # Create 3 label widgets 4 the bottom frame
        self.label4 = tkinter.Label(self.bottom_frame, text='St Paul')
        self.label5 = tkinter.Label(self.bottom_frame, text='Des Moines')
        self.label6 = tkinter.Label(self.bottom_frame, text='Madison')

        # Pack the bottom_frame labels
        self.label4.pack(side='left')
        self.label5.pack(side='left')
        self.label6.pack(side='left')

        # Pack the frames
        self.top_frame.pack()
        self.bottom_frame.pack()

        # Enter tkinter main loop
        tkinter.mainloop()


# Create an instance of the MyGui2 class
if __name__ == '__main__':
    my_gui2 = MyGUI2()
