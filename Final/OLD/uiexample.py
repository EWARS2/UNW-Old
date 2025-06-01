# Final Project
# Starting Out With Python, 5th Edition
# Date: 2/15/2024
# Author: Ethan Reed
# Class: Python Programming I
# Professor James Smith

from tkinter import *
from tkinter import ttk
from coollibsqlite import *


class MyGUI:
    def __init__(self):
        # Init tkinter
        ws = Tk()
        ws.title('Status Board')
        ws.geometry('500x500')
        ws['bg'] = '#AC99F2'
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
        my_status['columns'] = ('student_id', 'student_firstname', 'student_lastname', 'student_gpa')

        # Format columns
        my_status.column("#0", width=0, stretch=NO)
        my_status.column("student_id", anchor=CENTER, width=80)
        my_status.column("student_firstname", anchor=CENTER, width=80)
        my_status.column("student_lastname", anchor=CENTER, width=80)
        my_status.column("student_gpa", anchor=CENTER, width=80)

        # Create Headings
        my_status.heading("#0", text="", anchor=CENTER)
        my_status.heading("student_id", text="Id", anchor=CENTER)
        my_status.heading("student_firstname", text="firstname", anchor=CENTER)
        my_status.heading("student_lastname", text="lastname", anchor=CENTER)
        my_status.heading("student_gpa", text="gpa", anchor=CENTER)

        # Insert data function
        def insert_data(id, firstname, lastname, gpa):
            firstname = str(firstname)
            lastname = str(lastname)
            gpa = str(gpa)
            my_status.insert(parent='', index='end', iid=int(id), text='', values=(str(id), firstname, lastname, gpa))

        # Insert data
        insert_data(1, 'John', 'Johnson', 3.14)
        insert_data(2, 'Rob', 'Robertson', 4.00)
        insert_data(3, 'Mel', 'Nelson', 3.00)
        insert_data(4, 'Neil', 'Tyson', 2.90)
        insert_data(5, 'The Rock', 'Obama', 1.00)
        insert_data(6, 'Quandale', 'Dingle', 3.69)
        insert_data(7, 'Quandarius', 'Pringleton', 3.17)
        insert_data(8, 'Shigeru', 'Miyamoto', 3.09)
        insert_data(9, 'Johnny', 'Johnson', 3.10)
        insert_data(10, 'Carl', 'Wheezer', 3.21)
        insert_data(11, 'Pingus', 'Pingleton', 3.21)
        my_status.pack()

        frame = Frame(ws)
        frame.pack(pady=20)
        # Labels
        studentid = Label(frame, text="Student_id")
        studentid.grid(row=0, column=0)
        studentfirstname = Label(frame, text="Student_firstname")
        studentfirstname.grid(row=0, column=1)
        studentfirstname = Label(frame, text="Student_lastname")
        studentfirstname.grid(row=0, column=2)
        studentgpa = Label(frame, text="Student_gpa")
        studentgpa.grid(row=0, column=3)
        # Entry boxes: ID, firstname, gpa
        studentid_entry = Entry(frame)
        studentid_entry.grid(row=1, column=0)
        studentfirstname_entry = Entry(frame)
        studentfirstname_entry.grid(row=1, column=1)
        studentlastname_entry = Entry(frame)
        studentlastname_entry.grid(row=1, column=2)
        studentgpa_entry = Entry(frame)
        studentgpa_entry.grid(row=1, column=3)

        # Select Record
        def select_record():
            # clear entry boxes
            studentid_entry.delete(0, END)
            studentfirstname_entry.delete(0, END)
            studentlastname_entry.delete(0, END)
            studentgpa_entry.delete(0, END)

            # Get row that has focus
            selected = my_status.focus()
            # grab record values
            values = my_status.item(selected, 'values')
            # temp_label.config(text=selected)

            # Insert focus row in entry boxes
            studentid_entry.insert(0, values[0])
            studentfirstname_entry.insert(0, values[1])
            studentlastname_entry.insert(0, values[2])
            studentgpa_entry.insert(0, values[3])

        # Update Record
        def update_record():
            selected = my_status.focus()
            # save new data
            my_status.item(selected, text="", values=(
                studentid_entry.get(), studentfirstname_entry.get(), studentlastname_entry.get(),
                studentgpa_entry.get()))
            # clear entry boxes
            studentid_entry.delete(0, END)
            studentfirstname_entry.delete(0, END)
            studentlastname_entry.delete(0, END)
            studentgpa_entry.delete(0, END)

        # Buttons
        select_button = Button(ws, text="Select Record", command=select_record)
        select_button.pack(pady=10)
        refresh_button = Button(ws, text="Refresh Record", command=update_record)
        refresh_button.pack(pady=10)

        ws.mainloop()


# Create an instance of the MyGUI class.
if __name__ == '__main__':
    my_gui = MyGUI()
