import sys; sys.dont_write_bytecode = True
from tkinter import *
from sqlite3 import *
from teacher_ui import teacher_ui_func
from student_ui import student_ui_func

####################

conn = connect("names_for_numbers.db")
c = conn.cursor()

####################

opening_window = Tk()
opening_window.geometry("300x200")
opening_window.configure(bg="#f2efef")
opening_window.resizable(width=False, height=False)
opening_window.title("Names For Numbers")
opening_window.wm_iconbitmap("NFN.ico")


####################

global name
name = StringVar()

instr = Label(opening_window, text="Enter name", bg="#5e5e5e", borderwidth=1, relief="solid")
instr.place(x=97, y=10, width=105, height=25)


name_ent = Entry(opening_window, textvariable = name, borderwidth=1, relief="solid", justify="center")
name_ent.place(x=102, y=45, width=95, height=20)


####################

def name_check():
    name_data = name.get().lower()
    c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    names_list = []
    names_list.append(c.fetchall())
    names_list = str(names_list)
    
    if name_data == "":
        global opening_name_error
        opening_name_error = Label(opening_window, text="Name not found.\nCheck your spelling.\nIf not, contact your\n administrator.", bg="#f2efef")
        opening_name_error.place(x=97, y=105, width=105, height=75)
        
    elif name_data in names_list:
        opening_window.destroy()
        student_ui_func(name_data)
        
    elif name_data == "admin":
        try:
            opening_name_error.place_forget()
        except NameError:
            pass
        opening_name_admin = Label(opening_window, text="Enter Password", bg="#5e5e5e", borderwidth=1, relief="solid")
        opening_name_admin.place(x=97, y=75, width=105, height=25)
        opening_name_admin_entry = Entry(opening_window, show='*', borderwidth=1, relief="solid", justify="center")
        opening_name_admin_entry.place(x=102, y=110, width=95, height=20)
        
        def opening_name_admin_go():
            if opening_name_admin_entry.get() == "admin" and name.get() == "admin":
                opening_window.destroy()
                teacher_ui_func()
            elif opening_name_admin_entry.get() == "":
                incorrect_pass = Label(opening_window, text="Enter A Password", bg="#5e5e5e", justify="center", borderwidth=1, relief="solid")
                incorrect_pass.place(x=97, y=160, width=105, height=20)
            else:
                incorrect_pass = Label(opening_window, text="Incorrect", bg="#5e5e5e", justify="center", borderwidth=1, relief="solid")
                incorrect_pass.place(x=97, y=160, width=105, height=20)
        go_but.grid_remove()
        opening_name_admin_go_button = Button(opening_window, text="Go", command=opening_name_admin_go, bg="#e54747", borderwidth=1, relief="solid")
        opening_name_admin_go_button.place(x=137, y=135, width=25, height=20)
        
    else:
        opening_name_error = Label(opening_window, text="Name not found.\nCheck your spelling.\nIf not, contact your\n administrator.", bg="#f2efef")
        opening_name_error.place(x=97, y=105, width=105, height=75)
    
####################

go_but = Button(opening_window, text="Go", command = name_check, bg="#e54747", borderwidth=1, relief="solid")
go_but.place(x=137, y=75, width=25, height=20)

opening_window.mainloop()
