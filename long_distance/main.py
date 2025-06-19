# Title: Long Distance Call
# In-class program
# Starting Out With Python, 5th Edition
# Date: 4/12/2024
# Author: Ethan Reed
# Class: Python Programming I
# Professor James Smith

import tkinter
import tkinter.messagebox


class MyGUI:
    def __init__(self):
        # Create the main window.
        self.main_window = tkinter.Tk()
        self.main_window.title('Long Distance Call')
        self.main_window.minsize(275, 120)
        # Create frames
        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Create an IntVar object to use
        self.radio_var = tkinter.IntVar()
        # Set the intVar object to 0 for default option
        self.radio_var.set(0)

        # Create the Radiobutton widgets in the top_frame.
        self.rb1 = tkinter.Radiobutton(self.top_frame, text='Daytime  (6:00AM - 5:59PM)', variable=self.radio_var, value=0)
        self.rb2 = tkinter.Radiobutton(self.top_frame, text='Evening  (6:00PM - 11:59PM)', variable=self.radio_var, value=1)
        self.rb3 = tkinter.Radiobutton(self.top_frame, text='Off-peak (Midnight - 5:59AM)', variable=self.radio_var, value=2)
        # Pack the Radiobuttons.
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()

        # Create the minutes entry
        self.min_label = tkinter.Label(self.mid_frame, text='Enter the number of minutes: ')
        self.min_entry = tkinter.Entry(self.mid_frame, width=10)
        # Pack minutes
        self.min_label.pack(side='left')
        self.min_entry.pack(side='left')

        # Create an OK button and a Quit button.
        self.ok_button = tkinter.Button(self.bottom_frame, text='OK', command=self.show_choice)
        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)
        # Pack the Buttons.
        self.ok_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Pack the frames.
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()
        # Start the mainloop.
        tkinter.mainloop()

    # The show_choice method is the callback function for the
    # OK button.
    def show_choice(self):
        rates = [0.10, 0.15, 0.05]
        time = float(self.min_entry.get())
        charge = rates[int(self.radio_var.get())] * time
        if time < 360:
            tkinter.messagebox.showinfo('Total Charges', f'Your total charges: ${charge:,.2f}')
        else:
            tkinter.messagebox.showinfo('Error: Total Charges', 'Error: Time exceeds 6 hours. '
                                                                f'Your total charges (if your rate remained contant): ${charge:,.2f}')


# Create an instance of the MyGUI class.
if __name__ == '__main__':
    my_gui = MyGUI()
