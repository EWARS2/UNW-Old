# Final Project
# Starting Out With Python, 5th Edition
# Date: 2/15/2024
# Author: Ethan Reed
# Class: Python Programming I
# Professor James Smith

from tkinter import *
from tkinter import ttk
from coollibsqlite import *
from coollibexport import *


class MyGUI:
    def __init__(self):
        # Sets current table - Please Change
        table_name = "Clients"

        # Init tkinter
        ws = Tk()
        ws.title('Status Board')
        # ws.geometry('500x500')
        ws['bg'] = '#99FF99'
        # Init frame
        status_frame = Frame(ws)
        status_frame.pack()

        # scrollbars
        status_scroll = Scrollbar(status_frame)
        status_scroll.pack(side=RIGHT, fill=Y)
        status_scroll = Scrollbar(status_frame, orient='horizontal')
        status_scroll.pack(side=BOTTOM, fill=X)

        # Create table frame
        my_status = ttk.Treeview(status_frame, yscrollcommand=status_scroll.set, xscrollcommand=status_scroll.set)
        my_status.pack()
        status_scroll.config(command=my_status.yview)
        status_scroll.config(command=my_status.xview)

        # define our column
        column_list = tuple(get_column_list(table_name))
        my_status['columns'] = column_list

        # Create table & data entry
        my_status.column("#0", width=0, stretch=NO)
        my_status.heading("#0", text="", anchor=CENTER)
        frame = Frame(ws)
        frame.pack(pady=20)
        labels = []
        entries = []
        for x in range(len(column_list)):
            # Format Columns
            my_status.column(column_list[x], anchor=W)
            # Create Headings
            my_status.heading(column_list[x], text=column_list[x], anchor=CENTER)

            # Create Labels
            labels.append(Label(frame, text=column_list[x]))
            labels[x].grid(row=0, column=x)
            # Create Data Entry
            entries.append(Entry(frame))
            entries[x].grid(row=1, column=x)

        # Insert data
        table_data = get_table_data("Clients", "*")
        for x in table_data:
            my_status.insert(parent='', index='end', iid=x[1], text='', values=x)

        # Placeholder function
        def do_nothing():
            pass

        # Select Record function
        def select_record():
            # clear entry boxes
            for x in entries:
                x.delete(0, END)

            # Get row that has focus
            selected = my_status.focus()
            # grab record values
            values = my_status.item(selected, 'values')
            # temp_label.config(text=selected)

            # Insert focus row in entry boxes
            for x in range(len(entries)):
                entries[x].insert(0, values[x])

        # Update Record
        def update_record():
            selected = my_status.focus()

            # Retrieve new data
            new_data = []
            for x in range(len(entries)):
                new_data.append(entries[x].get())
            # save new data
            my_status.item(selected, text="", values=new_data)

            # clear entry boxes
            for x in entries:
                x.delete(0, END)

        def export_to_csv():
            list2csv(get_table_data("Clients", "*"), "test.csv")

        # Buttons
        buttons = Frame()
        buttons.pack(pady=20)
        export_button = Button(buttons, text='Export', command=export_to_csv)
        export_button.pack(padx=10, side='left')
        button_grab = Button(buttons, text="Grab Selected Record", command=select_record)
        button_grab.pack(padx=10, side='left')
        button_replace = Button(buttons, text="Replace Selected Record", command=update_record)
        button_replace.pack(padx=10, side='left')
        button_new_entry = Button(buttons, text='Insert As New Record', command=do_nothing)
        button_new_entry.pack(padx=10, side='left')
        #button_new_column = Button(buttons, text='New Column', command=do_nothing)
        #button_new_column.pack(padx=10, side='left')
        #button_new_table = Button(buttons, text='New Table', command=do_nothing)
        #button_new_table.pack(padx=10, side='left')

        my_status.pack()
        ws.mainloop()


# Create an instance of the MyGUI class.
if __name__ == '__main__':
    my_gui = MyGUI()
