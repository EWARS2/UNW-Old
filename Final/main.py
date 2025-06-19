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
        # Create lists for management
        labels = []
        entries = []
        column_list = []
        table_data = []
        self.table_name = ""
        # Normally table_list would be blank, but it's needed for some things
        # that are out of order.
        table_list = get_table_list()

        # Init tkinter
        main_window = Tk()
        main_window.title('Status Board')
        # main_window.geometry('500x500')
        bg_color = '#99FF99'
        main_window['bg'] = bg_color

        # Init frames
        frame_top = Frame(main_window)
        frame_top.pack(pady=20, padx=20)
        frame_table_container = Frame(main_window)
        frame_table_container.pack(pady=20, padx=20)

        # Scrollbars for table frame_entry
        table_scroll = Scrollbar(frame_table_container)
        table_scroll.pack(side=RIGHT, fill=Y)
        table_scroll_horizontal = Scrollbar(frame_table_container, orient='horizontal')
        table_scroll_horizontal.pack(side=BOTTOM, fill=X)
        frame_table = ttk.Treeview(frame_table_container, yscrollcommand=table_scroll.set,
                                   xscrollcommand=table_scroll_horizontal.set)
        frame_table.pack()

        frame_buttons = Frame(main_window)
        frame_buttons.configure(bg=bg_color)
        frame_buttons.pack(pady=10, padx=20)
        frame_entry = Frame(main_window)
        frame_entry.pack(pady=10, padx=20)
        frame_entry_buttons = Frame(main_window)
        frame_entry_buttons.configure(bg=bg_color)
        frame_entry_buttons.pack(pady=10, padx=20)
        # frame_edit_buttons = Frame(main_window)
        # frame_edit_buttons.configure(bg=bg_color)
        # frame_edit_buttons.pack(pady=30, padx=20)

        # Configure scrollbars
        table_scroll.config(command=frame_table.yview)
        table_scroll_horizontal.config(command=frame_table.xview)
        frame_table.column("#0", width=0, stretch=NO)
        frame_table.heading("#0", text="", anchor=CENTER)

        # Create the edit box
        edit_box = Entry(frame_buttons)
        # Pack it later.
        # edit_box.pack()

        # Create the table dropdown variable
        table_dropdown_variable = StringVar(frame_buttons)
        # Set table to last in list
        table_dropdown_variable.set(table_list[(len(table_list) - 1)])
        # Actually create the dropdown thing, but do it later.
        table_dropdown = OptionMenu(frame_buttons, table_dropdown_variable, *table_list)

        # Pack it later.
        # table_dropdown.pack()

        def reload():
            # Get the table list
            for x in get_table_list():
                table_list.append(x)

            # Update table list box
            menu = table_dropdown["menu"]
            menu.delete(0, "end")
            for x in table_list:
                menu.add_command(label=x, command=lambda value=x: table_dropdown_variable.set(value))

            # Grab current table and set it
            # NOT WORKING RN
            self.table_name = table_dropdown_variable.get()

            for x in get_column_list(self.table_name):
                column_list.append(x)

            for x in get_table_data(self.table_name, "*"):
                table_data.append(x)

            # define our column
            frame_table['columns'] = column_list

            # Create table & data entry
            for x in range(len(column_list)):
                # Format Columns - Used in example for centering text entries, not needed
                # frame_table.column(column_list[x], anchor=W)
                # Create Headings
                frame_table.heading(column_list[x], text=column_list[x], anchor=N)

                # Create Entry Labels
                labels.append(Label(frame_entry, text=column_list[x]))
                labels[x].grid(row=0, column=x)
                # Create Data Entry
                entries.append(Entry(frame_entry))
                entries[x].grid(row=1, column=x)

            # Insert data
            for x in table_data:
                frame_table.insert(parent='', index='end', iid=x[0], text='', values=x)

            # Non-working code to make table entries directly editable
            # I cannot figure out how to make this work with the scrollbar code
            # for y in range(len(table_data)):
            #    for x in range(len(column_list)):
            #        text = Text(frame_table, height=1, width=10, pady=20)
            #        text.grid(row=y + 1, column=x)
            #        text.insert(INSERT, table_data[y][x])

        def clear_records():
            for x in table_data:
                frame_table.delete(x[0])
            labels.clear()
            entries.clear()
            column_list.clear()
            table_list.clear()
            table_data.clear()

        def refresh():
            clear_records()
            reload()

        # Select Record function
        def select_record():
            # clear entry boxes
            for x in entries:
                x.delete(0, END)

            # Get row that has focus
            selected = frame_table.focus()
            # grab record values
            values = frame_table.item(selected, 'values')
            # temp_label.config(text=selected)

            # Insert focus row in entry boxes
            for x in range(len(entries)):
                entries[x].insert(0, values[x])

        # Update Record
        def update_record():
            selected = frame_table.focus()

            # Retrieve new data
            new_data = []
            for x in range(len(entries)):
                new_data.append(entries[x].get())

            # Retrieve old data
            # Get row that has focus
            selected = frame_table.focus()
            # grab record values
            old_data = frame_table.item(selected, 'values')

            # save new data
            update_table_entry(self.table_name, new_data, old_data)
            frame_table.item(selected, text="", values=new_data)

            # clear entry boxes
            for x in entries:
                x.delete(0, END)

            # The above code should update things properly.
            # Unless problems are occurring, you shouldn't need to refresh.
            # refresh()

        # Insert New Record
        def insert_new_record():
            # Retrieve new data
            new_data = []
            for x in range(len(entries)):
                new_data.append(entries[x].get())

            # save new data
            create_entry(self.table_name, new_data)
            table_data.append(new_data)
            frame_table.insert(parent='', index='end', iid=new_data[0], text='', values=new_data)

            # clear entry boxes
            for x in entries:
                x.delete(0, END)

        def delete_record():
            # Get row that has focus
            selected = frame_table.focus()
            # grab record values
            values = frame_table.item(selected, 'values')

            # Find & Delete record
            delete_table_entry(self.table_name, values)
            # Then delete the record from the table
            # {{{CODE HERE.}}}

            # But I'm lazy & just refresh anyway
            refresh()

        def new_column():
            create_column(self.table_name, edit_box.get())
            edit_box.delete(0, END)
            refresh()

        def new_table():
            create_table(edit_box.get())
            edit_box.delete(0, END)
            refresh()

        def delete_column():
            remove_column(self.table_name, edit_box.get())
            edit_box.delete(0, END)
            refresh()

        def delete_table():
            remove_table(edit_box.get())
            edit_box.delete(0, END)
            refresh()

        def export_to_csv():
            export_data = [column_list, []]
            refresh()
            for x in table_data:
                export_data.append(x)
            list2csv(export_data, "output.csv")

        # Placeholder function for buttons that do nothing
        def do_nothing():
            pass

        # Buttons, first row
        button_grab = Button(frame_entry_buttons, text="Grab Selected Record", command=select_record)
        button_grab.pack(padx=10, side='left')
        button_delete = Button(frame_entry_buttons, text='Delete Selected Record', command=delete_record)
        button_delete.pack(padx=10, side='left')
        button_replace = Button(frame_entry_buttons, text="Replace Selected Record", command=update_record)
        button_replace.pack(padx=10, side='left')
        button_new_entry = Button(frame_entry_buttons, text='Insert As New Record', command=insert_new_record)
        button_new_entry.pack(padx=10, side='left')

        # Buttons, second row
        # button_save = Button(frame_buttons, text='Save', command=cool_save)
        # button_save.pack(padx=10, side='left')
        button_refresh = Button(frame_buttons, text='Refresh', command=refresh)
        button_refresh.pack(padx=10, side='left')
        export_button = Button(frame_buttons, text='Export', command=export_to_csv)
        export_button.pack(padx=10, side='left')
        button_new_column = Button(frame_buttons, text='New Column', command=new_column)
        button_new_column.pack(padx=10, side='left')
        button_new_table = Button(frame_buttons, text='New Table', command=new_table)
        button_new_table.pack(padx=10, side='left')
        button_new_table = Button(frame_buttons, text='Delete Column', command=delete_column)
        button_new_table.pack(padx=10, side='left')
        button_new_table = Button(frame_buttons, text='Delete Table', command=delete_table)
        button_new_table.pack(padx=10, side='left')

        # Pack the remaining things
        edit_box.pack(padx=10, side='left')
        table_dropdown.pack(padx=10, side='left')

        frame_table.pack()
        refresh()
        main_window.mainloop()


# TODO:
# Re-organize for easier & consistent referencing
# Figure out how to have a separate editing
# "Rename" functionality
# "Search" functionality
# Edit Create Table function for "ID" column to have correct properties
# Column Bug - Longer column lists are not entirely refreshed when a smaller list is created.


# Create an instance of the MyGUI class.
if __name__ == '__main__':
    my_gui = MyGUI()
    cool_kill()
