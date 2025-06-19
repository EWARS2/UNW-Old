# Title: 
# Chapter 13, Exercise 3
# Starting Out With Python, 5th Edition
# Date: 2/15/2024
# Author: Ethan Reed
# Class: Python Programming I
# Professor James Smith

import tkinter


class MyGUI:
    def __init__(self):
        # Create the main window.
        self.main_window = tkinter.Tk()
        
        # Set window title
        self.main_window.title("C00l 'n Gr00vy C@lcul@tor")
        
        # Set window size
        self.main_window.minsize(450,150)
        
        # Create frames to group Fidgits
        self.frame_in1 = tkinter.Frame()
        self.frame_in2 = tkinter.Frame()
        self.frame_out = tkinter.Frame()
        self.frame_bottom = tkinter.Frame()

        # Create the widgets for in1
        self.in1_label = tkinter.Label(self.frame_in1, text='Enter the number of miles your vehicle can be driven on a full tank:')
        self.in1_entry = tkinter.Entry(self.frame_in1, width=10)
        # Pack in1
        self.in1_label.pack(side='left')
        self.in1_entry.pack(side='left')
        
        # Create the widgets for in2
        self.in2_label = tkinter.Label(self.frame_in2, text='Enter the number of gallons of gas the car holds:')
        self.in2_entry = tkinter.Entry(self.frame_in2, width=10)
        # Pack in2
        self.in2_label.pack(side='left')
        self.in2_entry.pack(side='left')


        # Create the widgets out
        self.out_label = tkinter.Label(self.frame_out, text='miles / gallons = MPG:')

        # We need a StringVar object to associate with
        # an output label. Use the object's set method
        # to store a string of blank characters.
        self.value = tkinter.StringVar()

        # Create a label and associate it with the
        # StringVar object. Any value stored in the
        # StringVar object will automatically be displayed
        # in the label.
        self.out_entry = tkinter.Label(self.frame_out, textvariable=self.value)

        # Pack out
        self.out_label.pack(side='left')
        self.out_entry.pack(side='left')


        # Create the button widgets for the bottom frame.
        self.button_calc = tkinter.Button(self.frame_bottom, text='Calculate', command=self.calc)
        self.button_quit = tkinter.Button(self.frame_bottom, text='Quit', command=self.main_window.destroy)
        # Pack the buttons.
        self.button_calc.pack(side='left')
        self.button_quit.pack(side='left')

        # Pack the frames.
        self.frame_in1.pack()
        self.frame_in2.pack()
        self.frame_out.pack()
        self.frame_bottom.pack()

        # Enter the tkinter main loop.
        tkinter.mainloop()

    # The convert method is a callback function for
    # the Calculate button.
    def calc(self):
        # Get input
        in1 = float(self.in1_entry.get())
        in2 = float(self.in2_entry.get())

        # Calc
        out = in1 / in2

        # Convert miles to a string and store it
        # in the StringVar object. This will automatically
        # update the miles_label widget.
        self.value.set(out)


# Create an instance of the MyGui2 class
if __name__ == '__main__':
    my_gui2 = MyGUI()
