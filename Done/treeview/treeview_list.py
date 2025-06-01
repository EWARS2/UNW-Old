from tkinter import *
from  tkinter import ttk
ws = Tk()

ws.title('Contacts')
ws.geometry('500x500')

list = ttk.Treeview(ws)
list.pack()

list['columns']= ('Name','Gender','Title')

# Column declaration
list.column("#0", width=0,  stretch=NO)
list.column("Name",anchor=CENTER, width=80)
list.column("Gender",anchor=CENTER, width=80)
list.column("Title",anchor=CENTER, width=80)

# Column headers
list.heading("#0", text="", anchor=CENTER)
list.heading("Name", text="P_Name", anchor=CENTER)
list.heading("Gender", text="P_Gender", anchor=CENTER)
list.heading("Title", text="P_Title", anchor=CENTER)

# Populate the table
list.insert(parent='',index='end',iid=0,text='',
values=('Andrew','Male','Mr'))
list.insert(parent='',index='end',iid=1,text='',
values=('Ansel','Male','Mr'))
list.insert(parent='',index='end',iid=2,text='',
values=('Ariel','Male','Mr'))
list.insert(parent='',index='end',iid=3,text='',
values=('Alison','Female','Ms'))
list.insert(parent='',index='end',iid=4,text='',
values=('Grace','Female','Ms'))
list.insert(parent='',index='end',iid=5,text='',
values=('Kendra','Female','Ms'))
list.insert(parent='',index='end',iid=6,text='',
values=('Zach','Male','Mr'))
list.insert(parent='',index='end',iid=7,text='',
values=('Zachary','Male','Mr'))
list.insert(parent='',index='end',iid=8,text='',
values=('Morgan','Female','Ms'))
list.insert(parent='',index='end',iid=9,text='',
values=('Shaelyse','Female','Ms'))


ws.mainloop()
