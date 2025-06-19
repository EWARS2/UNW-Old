# Title: Progs & Dogs
# In-class Exercise
# Starting Out With Python, 5th Edition
# Date: 2/15/2024
# Author: Ethan Reed
# Class: Python Programming I
# Professor James Smith

import tkinter
import tkinter.messagebox

class ListBoxSelection:
    def __init__(self):
        # Create the main window.
        self.main_window = tkinter.Tk()
        self.main_window.title("Programming Languages")
        self.main_window.minsize(250,100)

        # Create a Listbox widget.
        self.listbox_progs = tkinter.Listbox(self.main_window, width=0, height=0)
        self.listbox_progs.pack(padx=10, pady=5)

        # Create a list.
        progs = ['C', 'C++', 'Java', 'Python']

        # Populate the Listbox with the list contents.
        for prog in progs:
            self.listbox_progs.insert(tkinter.END, prog)
        
        # Create buttons
        self.button_print = tkinter.Button(self.main_window, text='Print', command=self.__print)
        self.button_delete = tkinter.Button(self.main_window, text='Delete', command=self.__delete)
        self.button_quit = tkinter.Button(self.main_window, text='Quit', command=self.main_window.destroy)
        
        self.button_print.pack(padx=10, pady=5)
        self.button_delete.pack(padx=10, pady=5)
        self.button_quit.pack(padx=10, pady=5)

        # Start the main loop.
        tkinter.mainloop()
    
    def __print(self):
        # Get the index of the selected item.
        indexes = self.listbox_progs.curselection()

        # If an item is selected, display it.
        if (len(indexes) > 0):
            tkinter.messagebox.showinfo(message=self.listbox_progs.get(indexes[0]))
        else:
            tkinter.messagebox.showinfo(message='No item selected.')
    
    def __delete(self):
        # Get the index of the selected item.
        indexes = self.listbox_progs.curselection()

        # If an item is selected, display it.
        if (len(indexes) > 0):
            for i in indexes:
                self.listbox_progs.delete(i)
            tkinter.messagebox.showinfo(message='One item deleted.')
        else:
            tkinter.messagebox.showinfo(message='No item selected.')



# Create an instance of the ListBoxSelection class.
if __name__ == '__main__':
    listbox_selection = ListBoxSelection()