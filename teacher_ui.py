import sys; sys.dont_write_bytecode = True
from tkinter import *
from sqlite3 import *
from time import strftime
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

####################

def teacher_ui_func():
    root = Tk()
    root.configure(background="#c9c9c9")
    root.geometry("725x450")
    root.resizable(width=False, height=False)

    ####################

    a12_font = ("Arial", 12)
    a11_font = ("Arial", 11)
    a9_font = ("Arial", 9)
    a7_font = ("Arial", 7)

    root_canvas = Canvas(root, bg="#F2EFEF", width=725, height=450, highlightthickness=0)
    horizontal_line_one = root_canvas.create_line(0, 40, 725, 40)
    vertical_line_one = root_canvas.create_line(110, 40, 110, 450)

    welcome_admin = Label(root, text="Welcome, Admin.", background="#333", font=a12_font, borderwidth=1, relief="solid")
    welcome_admin.place(x=4, y=3, height=35, width=125)

    date = strftime("%a, %d %b %Y")
    date_label = Label(root, text=date, background="#333", font=a12_font, borderwidth=1, relief="solid")
    date_label.place(x=310, y=3, height=35, width=140)

    conn = connect("names_for_numbers.db")
    c = conn.cursor()
    c.execute("SELECT name FROM sqlite_master WHERE type='table'")
    students_tables = c.fetchall()
    list(students_tables)
    list(students_tables[0])
    del students_tables[0]

    students_label = Label(root, text="Students: " + str(len(students_tables)), background="#333", font=a12_font, borderwidth=1, relief="solid")
    students_label.place(x=630, y=3, height=35, width=90)

    ##########

    def home_frame_raise():
        home_frame.tkraise()

    home = Button(root, text="Home", background="#333", font=a12_font, borderwidth=1, relief="solid", command=home_frame_raise)
    home.place(x=4, y=70, width=100, height=50)

    def add_students_frame_raise():
        add_students_frame.tkraise()

    add_student = Button(root, text="Add\nStudent", background="#333", font=a12_font, borderwidth=1, relief="solid", command=add_students_frame_raise)
    add_student.place(x=4, y=179, width=100, height=50)

    def remove_students_frame_raise():
        remove_students_frame.tkraise()

    remove_student = Button(root, text="Remove\nStudent", background="#333", font=a12_font, borderwidth=1, relief="solid", command=remove_students_frame_raise)
    remove_student.place(x=4, y=285, width=100, height=50)

    def sign_out_close_command():
        root.destroy()
        conn.commit()
        conn.close()

    sign_out_close = Button(root, text="Sign Out\nand Close", background="#333", font=a12_font, borderwidth=1, relief="solid", command=sign_out_close_command)
    sign_out_close.place(x=4, y=390, width=100, height=50)

    ############################################################

    home_frame = Frame(root, bg="#F2EFEF")
    home_frame.place(x=111, y=41, width=615, height=409)

    view_students = Label(home_frame, text="View Students", background="#e54747", font=a12_font, borderwidth=1, relief="solid")
    view_students.place(x=440, y=25, width=160, height=30)

    def view_command():
       view_student_command()

    view_button = Button(home_frame, text="View", background="#e54747", font=a12_font, borderwidth=1, relief="solid", command=view_command)
    view_button.place(x=480, y=330, width=86, height=30)

    ####################

    recent_attempts = Label(home_frame, text="Recent Student Attempts Scores", background="#e54747", font=a12_font, borderwidth=1, relief="solid")
    recent_attempts.place(x=79, y=6, width=249, height=30)

    recent_attempts_frame = Frame(home_frame, bg="#F2EFEF")
    recent_attempts_frame.place(x=95, y=42, width=249, height=126)
    recent_attempts_frame.grid_propagate(0)

    recent_records = []
    for stud in students_tables:
        recent_records_query = "SELECT timestamp, _45, _51, _228, _325, _345, _375, _761, _963, _1236, _1240, _1355, _1542, _1965, _2455, _2545, _3247, _3651, _3763, _3876, _4099, _4539, _4654, _4859, _5263, _5379, _5632, _5771, _5852, _6409, _7227, _7426, _7459, _8413, _8868, _9103, _9132, _9137, _9523, _9621, _9864, table_name FROM {} ORDER BY timestamp DESC LIMIT 5".format(stud[0])
        c.execute(recent_records_query)
        recent_records.append(c.fetchall())
    del recent_records[5:]
        
    recent_records.sort(reverse=True)

    recent_one_score = Counter()
    for one_word in recent_records[0][0]:
        recent_one_score[one_word] += 1
        
    recent_two_score = Counter()
    for two_word in recent_records[1][0]:
        recent_two_score[two_word] += 1
        
    recent_three_score = Counter()
    for three_word in recent_records[2][0]:
        recent_three_score[three_word] += 1
        
    recent_four_score = Counter()
    for four_word in recent_records[3][0]:
        recent_four_score[four_word] += 1
        
    recent_five_score = Counter()
    for five_word in recent_records[4][0]:
        recent_five_score[five_word] += 1

    recent_one = [recent_records[0][0][41].title(), recent_one_score['true'], recent_records[0][0][0]]
    recent_two = [recent_records[1][0][41].title(), recent_two_score['true'], recent_records[1][0][0]]
    recent_three = [recent_records[2][0][41].title(), recent_three_score['true'], recent_records[2][0][0]]
    recent_four = [recent_records[3][0][41].title(), recent_four_score['true'], recent_records[3][0][0]]
    recent_five = [recent_records[4][0][41].title(), recent_five_score['true'], recent_records[4][0][0]]

    heading_one = Label(recent_attempts_frame, bg="#6e7376", text="Name", width=12, padx=1, pady=2, borderwidth=1, relief="solid", font=a7_font).grid(row=0, column=0)
    heading_two = Label(recent_attempts_frame, bg="#6e7376", text="Score", width=6, padx=4, pady=2, borderwidth=1, relief="solid", font=a7_font).grid(row=0, column=1)
    heading_three = Label(recent_attempts_frame, bg="#6e7376", text="Date", width=15, pady=2, borderwidth=1, relief="solid", font=a7_font).grid(row=0, column=2)

    row_one_column_one = Label(recent_attempts_frame, bg="#968983", text=recent_one[0], width=12, padx=1, pady=2, borderwidth=1, relief="solid", font=a7_font).grid(row=1, column=0)
    row_one_column_two = Label(recent_attempts_frame, bg="#968983", text=recent_one[1], width=6, padx=4, pady=2, borderwidth=1, relief="solid", font=a7_font).grid(row=1, column=1)
    row_one_column_three = Label(recent_attempts_frame, bg="#968983", text=recent_one[2], width=15, pady=2, borderwidth=1, relief="solid", font=a7_font).grid(row=1, column=2)

    row_two_column_one = Label(recent_attempts_frame, bg="#fffde2", text=recent_two[0], width=12, padx=1, pady=2, borderwidth=1, relief="solid", font=a7_font).grid(row=2, column=0)
    row_two_column_two = Label(recent_attempts_frame, bg="#fffde2", text=recent_two[1], width=6, padx=4, pady=2, borderwidth=1, relief="solid", font=a7_font).grid(row=2, column=1)
    row_two_column_three = Label(recent_attempts_frame, bg="#fffde2", text=recent_two[2], width=15, pady=2, borderwidth=1, relief="solid", font=a7_font).grid(row=2, column=2)

    row_three_column_one = Label(recent_attempts_frame, bg="#968983", text=recent_three[0], width=12, padx=1, pady=2, borderwidth=1, relief="solid", font=a7_font).grid(row=3, column=0)
    row_three_column_two = Label(recent_attempts_frame, bg="#968983", text=recent_three[1], width=6, padx=4, pady=2, borderwidth=1, relief="solid", font=a7_font).grid(row=3, column=1)
    row_three_column_three = Label(recent_attempts_frame, bg="#968983", text=recent_three[2], width=15, pady=2, borderwidth=1, relief="solid", font=a7_font).grid(row=3, column=2)

    row_four_column_one = Label(recent_attempts_frame, bg="#fffde2", text=recent_four[0], width=12, padx=1, pady=2, borderwidth=1, relief="solid", font=a7_font).grid(row=4, column=0)
    row_four_column_two = Label(recent_attempts_frame, bg="#fffde2", text=recent_four[1], width=6, padx=4, pady=2, borderwidth=1, relief="solid", font=a7_font).grid(row=4, column=1)
    row_four_column_three = Label(recent_attempts_frame, bg="#fffde2", text=recent_four[2], width=15, pady=2, borderwidth=1, relief="solid", font=a7_font).grid(row=4, column=2)

    row_five_column_one = Label(recent_attempts_frame, bg="#968983", text=recent_four[0], width=12, padx=1, pady=2, borderwidth=1, relief="solid", font=a7_font).grid(row=5, column=0)
    row_five_column_two = Label(recent_attempts_frame, bg="#968983", text=recent_four[1], width=6, padx=4, pady=2, borderwidth=1, relief="solid", font=a7_font).grid(row=5, column=1)
    row_five_column_three = Label(recent_attempts_frame, bg="#968983", text=recent_four[2], width=15, pady=2, borderwidth=1, relief="solid", font=a7_font).grid(row=5, column=2)

    ####################

    best_scores_records = []
    for best_stud in students_tables:
        best_scores_query = """SELECT _45, _51, _228, _325, _345, _375, _761, _963, _1236, _1240, _1355, _1542, _1965, _2455, _2545, _3247, _3651, _3763, _3876, _4099, _4539, _4654, _4859,
                                                                                                                        _5263, _5379, _5632, _5771, _5852, _6409, _7227, _7426, _7459, _8413, _8868, _9103, _9132,
                                                                                                                        _9137, _9523, _9621, _9864, table_name FROM {} ORDER BY timestamp DESC LIMIT 5""".format(best_stud[0])
        c.execute(best_scores_query)
        best_scores_fetch_all = c.fetchall()
        best_scores_temp = Counter()
        try:
            for best_scores_word_one in best_scores_fetch_all[0]:
                best_scores_temp[best_scores_word_one] += 1
        except IndexError:
            pass
        try:
            for best_scores_word_two in best_scores_fetch_all[1]:
                best_scores_temp[best_scores_word_two] += 1
        except IndexError:
            pass
        try:
            for best_scores_word_three in best_scores_fetch_all[2]:
                best_scores_temp[best_scores_word_three] += 1
        except IndexError:
            pass
        try:
            for best_scores_word_four in best_scores_fetch_all[3]:
                best_scores_temp[best_scores_word_four] += 1
        except IndexError:
            pass
        try:
            for best_scores_word_five in best_scores_fetch_all[4]:
                best_scores_temp[best_scores_word_five] += 1
        except IndexError:
            pass
        
            best_scores_records.append(best_scores_temp)

    best_scores_list = []
    for student_raw_counter in best_scores_records:
        student_raw_name_counter = student_raw_counter.copy()
        del student_raw_name_counter[None]
        del student_raw_name_counter['true']
        del student_raw_name_counter['false']
        student_raw_name = list(student_raw_name_counter)
        student_raw_sum = student_raw_counter['true'] + student_raw_counter['false']
        student_true_percent = 0
        student_false_percent = 0
        if student_raw_counter['true'] > 0:
            student_true_percent = (student_raw_counter['true']/student_raw_sum)*100
        if student_raw_counter['false'] > 0:
            student_false_percent = (student_raw_counter['false']/student_raw_sum)*100
        try:
            student_tuple = (student_true_percent, student_false_percent, student_raw_name[0])
            best_scores_list.append(student_tuple)
        except IndexError:
            pass

    best_scores_list.sort(reverse=True)
    del best_scores_list[5:]

    ##########

    best_scores_frame = Frame(home_frame, borderwidth=1, relief="solid")
    best_scores_frame.place(x=10, y=176)

    best_scores_figure = plt.figure(figsize=(422/96, 225/96), dpi=96)
    best_scores_plot = best_scores_figure.add_subplot(111)

    correct_data = (best_scores_list[0][0], best_scores_list[1][0], best_scores_list[2][0], best_scores_list[3][0], best_scores_list[4][0])
    incorrect_data = (best_scores_list[0][1], best_scores_list[1][1], best_scores_list[2][1], best_scores_list[3][1], best_scores_list[4][1])
    best_names = (best_scores_list[0][2].title(), best_scores_list[1][2].title(), best_scores_list[2][2].title(), best_scores_list[3][2].title(), best_scores_list[4][2].title())
    ind = np.arange(5)    # the x locations for the groups
    bar_width = 0.3       # the width of the bars: can also be len(x) sequence

    correct = best_scores_plot.bar(ind, correct_data, bar_width)
    incorrect = best_scores_plot.bar(ind, incorrect_data, bar_width, bottom=correct_data, color='#d62728')

    plt.ylabel('Average Score %')
    plt.title('Best Scores In The Past 5 Games')
    plt.xticks(ind, best_names)
    plt.yticks(np.arange(0, 101, 10))
    plt.legend((correct[0], incorrect[0]), ('Correct', 'Incorrect'))
    best_scores_canvas = FigureCanvasTkAgg(best_scores_figure, master=best_scores_frame)
    best_scores_canvas.draw()
    best_scores_canvas.get_tk_widget().pack(expand=1)

    ####################

    student_list_scrollbar = Scrollbar(home_frame)
    student_list_scrollbar.place(x=583, y=75, height=225)

    student_list_box = Listbox(home_frame, font=a12_font, borderwidth=1, relief="solid")
    student_list_box.place(x=440, y=75, height=225, width=144)

    student_list_box.config(yscrollcommand=student_list_scrollbar.set)
    student_list_scrollbar.config(command=student_list_box.yview)

    students_tables_sort = students_tables.copy()
    students_tables_sort.sort()

    for student1 in students_tables_sort:
        student_list_box.insert(END, student1[0].title())

    ############################################################

    add_students_frame = Frame(root, bg="#F2EFEF")
    add_students_frame.place(x=111, y=41, width=615, height=409)

    add_students_top_label = Label(add_students_frame, text="Add Students", background="#e54747", font=a12_font, borderwidth=1, relief="solid")
    add_students_top_label.place(x=15, y=25, width=585, height=30)

    add_students_check_exists = Label(add_students_frame, text="Make Sure The Student Name Doesn't Already Exist, If It Does, You Can Add A Number Behind It.", bg="#e54747", font=a9_font, borderwidth=1, relief="solid")
    add_students_check_exists.place(x=25, y=70, width=565, height=20)

    existing_students_label = Label(add_students_frame, text="Existing Students", bg="#e54747", font=a9_font, borderwidth=1, relief="solid")
    existing_students_label.place(x=25, y=130, width=250, height=20)

    existing_students_list_box = Listbox(add_students_frame, font=a12_font, borderwidth=1, relief="solid")
    existing_students_list_box.place(x=25, y=165, width=234, height=219)

    existing_students_scrollbar = Scrollbar(add_students_frame)
    existing_students_scrollbar.place(x=259, y=165, width=16, height=219)

    existing_students_list_box.config(yscrollcommand=existing_students_scrollbar.set)
    existing_students_scrollbar.config(command=existing_students_list_box.yview)

    for existing_student in students_tables_sort:
        existing_students_list_box.insert(END, existing_student[0].title())

    existing_students_list_box.config(state=DISABLED, disabledforeground="#000")

    add_student_right_label = Label(add_students_frame, text="Add Student (Must Be Lowercase)", bg="#e54747", font=a9_font, borderwidth=1, relief="solid")
    add_student_right_label.place(x=340, y=130, width=250, height=20)

    add_student_right_small_label = Label(add_students_frame, text="Enter New\nStudent's Name: ", bg="#e54747", font=a9_font, borderwidth=1, relief="solid")
    add_student_right_small_label.place(x=340, y=165, width=125, height=40)

    add_student_stringvar = StringVar()

    add_student_entry = Entry(add_students_frame, font=a12_font, justify="center", textvariable=add_student_stringvar)
    add_student_entry.place(x=475, y=165, width=115, height=40)

    ##########

    def add_students_check_command():
        try:
            add_student_pre_existing.place_forget()
        except AttributeError:
            pass
        global add_student_data
        add_student_data = add_student_stringvar.get().lower()
        add_student_exists_counter = 0
        for student_check in students_tables:
            if add_student_data in student_check:
                add_student_pre_existing.config(text="That Student Already Exists")
                add_student_pre_existing.place(x=365, y=275, width=200, height=25)
                add_student_entry.delete(0, END)
                add_student_exists_counter = 1
        if add_student_data == "":
            add_student_pre_existing.config(text="Enter A Name")
            add_student_pre_existing.place(x=365, y=275, width=200, height=25)        
        elif add_student_exists_counter==0:
            add_student_confirm_create_label.place(x=340, y=275, width=200, height=40)
            add_student_confirm_create_yes_button.place(x=540, y=275, width=50, height=20)
            add_student_confirm_create_no_button.place(x=540, y=295, width=50, height=20)
        
    add_student_button = Button(add_students_frame, text="Add Student", bg="#e54747", font=a12_font, borderwidth=1, relief="solid", command=add_students_check_command)
    add_student_button.place(x=365, y=220, width=200, height=35)

    add_student_pre_existing = Label(add_students_frame, text="That Student Already Exists", bg="#e54747", font=a12_font, borderwidth=1, relief="solid")

    add_student_confirm_create_label = Label(add_students_frame, text="Are You Sure You Want\nTo Create This Student", bg="#e54747", font=a9_font, borderwidth=1, relief="solid")

    ##########

    def add_student_confirm_yes_command():
        create_query = "CREATE TABLE {} (runid INTEGER PRIMARY KEY AUTOINCREMENT, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP, _45 BLOB, _51 BLOB, _228 BLOB, _325 BLOB, _345 BLOB, _375 BLOB, _761 BLOB, _963 BLOB, _1236 BLOB, _1240 BLOB, _1355 BLOB, _1542 BLOB, _1965 BLOB, _2455 BLOB, _2545 BLOB, _3247 BLOB, _3651 BLOB, _3763 BLOB, _3876 BLOB, _4099 BLOB, _4539 BLOB, _4654 BLOB, _4859 BLOB, _5263 BLOB, _5379 BLOB, _5632 BLOB, _5771 BLOB, _5852 BLOB, _6409 BLOB, _7227 BLOB, _7426 BLOB, _7459 BLOB, _8413 BLOB, _8868 BLOB, _9103 BLOB, _9132 BLOB, _9137 BLOB, _9523 BLOB, _9621 BLOB, _9864 BLOB, table_name TEXT DEFAULT 'ben')".format(add_student_data)
        c.execute(create_query)
        conn.commit()        
        add_student_confirm_no_command()

    add_student_confirm_create_yes_button = Button(add_students_frame, text="YES", bg="#e54747", font=a12_font, borderwidth=1, relief="solid", command=add_student_confirm_yes_command)

    ##########

    def add_student_confirm_no_command():
        add_student_entry.delete(0, END)
        add_student_data = ""
        add_student_confirm_create_label.place_forget()
        add_student_confirm_create_yes_button.place_forget()
        add_student_confirm_create_no_button.place_forget()

    add_student_confirm_create_no_button = Button(add_students_frame, text="NO", bg="#e54747", font=a12_font, borderwidth=1, relief="solid", command=add_student_confirm_no_command)

    ############################################################

    remove_students_frame = Frame(root, bg="#F2EFEF")
    remove_students_frame.place(x=111, y=41, width=615, height=409)

    remove_students_top_label = Label(remove_students_frame, text="Remove Students", background="#e54747", font=a12_font, borderwidth=1, relief="solid")
    remove_students_top_label.place(x=15, y=25, width=585, height=30)

    remove_students_check_exists = Label(remove_students_frame, text="Make Sure The Student Exists.", bg="#e54747", font=a9_font, borderwidth=1, relief="solid")
    remove_students_check_exists.place(x=25, y=70, width=565, height=20)

    existing_students_remove_label = Label(remove_students_frame, text="Existing Students", bg="#e54747", font=a9_font, borderwidth=1, relief="solid")
    existing_students_remove_label.place(x=25, y=130, width=250, height=20)

    existing_students_remove_list_box = Listbox(remove_students_frame, font=a12_font, borderwidth=1, relief="solid")
    existing_students_remove_list_box.place(x=25, y=165, width=234, height=219)

    existing_students_remove_scrollbar = Scrollbar(remove_students_frame)
    existing_students_remove_scrollbar.place(x=259, y=165, width=16, height=219)

    existing_students_remove_list_box.config(yscrollcommand=existing_students_remove_scrollbar.set)
    existing_students_remove_scrollbar.config(command=existing_students_remove_list_box.yview)

    for existing_student_remove in students_tables_sort:
        existing_students_remove_list_box.insert(END, existing_student_remove[0].title())

    existing_students_remove_list_box.config(state=DISABLED, disabledforeground="#000")

    remove_student_right_label = Label(remove_students_frame, text="Remove Student (Must Be Lowercase)", bg="#e54747", font=a9_font, borderwidth=1, relief="solid")
    remove_student_right_label.place(x=340, y=130, width=250, height=20)

    remove_student_right_small_label = Label(remove_students_frame, text="Enter Student's\nName: ", bg="#e54747", font=a9_font, borderwidth=1, relief="solid")
    remove_student_right_small_label.place(x=340, y=165, width=125, height=40)

    remove_student_stringvar = StringVar()

    remove_student_entry = Entry(remove_students_frame, font=a12_font, justify="center", textvariable=remove_student_stringvar)
    remove_student_entry.place(x=475, y=165, width=115, height=40)

    ##########

    def remove_students_check_command():
        try:
            remove_student_pre_existing.place_forget()
        except AttributeError:
            pass
        global remove_student_data
        remove_student_data = remove_student_stringvar.get().lower()
        remove_student_exists_counter = 0
        for student_check in students_tables:
            if remove_student_data in student_check:
                remove_student_confirm_create_label.place(x=340, y=275, width=200, height=40)
                remove_student_confirm_create_yes_button.place(x=540, y=275, width=50, height=20)
                remove_student_confirm_create_no_button.place(x=540, y=295, width=50, height=20)
                remove_student_exists_counter = 1
        if remove_student_data == "":
            remove_student_pre_existing.config(text="Enter A Name")
            remove_student_pre_existing.place(x=365, y=275, width=200, height=25)        
        elif remove_student_exists_counter==0:
            remove_student_pre_existing.config(text="That Student Doesn't Exist")
            remove_student_pre_existing.place(x=365, y=275, width=200, height=25)
            remove_student_entry.delete(0, END)

        
    remove_student_button = Button(remove_students_frame, text="Remove Student", bg="#e54747", font=a12_font, borderwidth=1, relief="solid", command=remove_students_check_command)
    remove_student_button.place(x=365, y=220, width=200, height=35)

    remove_student_pre_existing = Label(remove_students_frame, text="That Student Doesn't Exist", bg="#e54747", font=a12_font, borderwidth=1, relief="solid")

    remove_student_confirm_create_label = Label(remove_students_frame, text="Are You Sure You Want\nTo Remove This Student", bg="#e54747", font=a9_font, borderwidth=1, relief="solid")

    ##########

    def remove_student_confirm_yes_command():
        create_query = "DROP TABLE {}".format(remove_student_data)
        c.execute(create_query)
        conn.commit()
        remove_student_confirm_no_command()

    remove_student_confirm_create_yes_button = Button(remove_students_frame, text="YES", bg="#e54747", font=a12_font, borderwidth=1, relief="solid", command=remove_student_confirm_yes_command)

    ##########

    def remove_student_confirm_no_command():
        remove_student_entry.delete(0, END)
        remove_student_data = ""
        remove_student_confirm_create_label.place_forget()
        remove_student_confirm_create_yes_button.place_forget()
        remove_student_confirm_create_no_button.place_forget()

    remove_student_confirm_create_no_button = Button(remove_students_frame, text="NO", bg="#e54747", font=a12_font, borderwidth=1, relief="solid", command=remove_student_confirm_no_command)

    ############################################################

    def view_student_command():
        student_list_select = student_list_box.get(student_list_box.curselection())
        
        view_frame = Frame(root, bg="#F2EFEF")
        view_frame.place(x=111, y=41, width=615, height=409)

        view_recent_attempts = Label(view_frame, text=student_list_select.title() + "'s Recent Attempts", background="#e54747", font=a12_font, borderwidth=1, relief="solid")
        view_recent_attempts.place(x=15, y=25, width=585, height=30)

        view_recent_attempts_frame = Frame(view_frame, bg="#fff")
        view_recent_attempts_frame.place(x=25, y=70, width=564, height=324)
        view_recent_attempts_frame.grid_propagate(0)

        view_recent_records = []
        view_recent_records_query = "SELECT timestamp, _45, _51, _228, _325, _345, _375, _761, _963, _1236, _1240, _1355, _1542, _1965, _2455, _2545, _3247, _3651, _3763, _3876, _4099, _4539, _4654, _4859, _5263, _5379, _5632, _5771, _5852, _6409, _7227, _7426, _7459, _8413, _8868, _9103, _9132, _9137, _9523, _9621, _9864, table_name FROM {} ORDER BY timestamp DESC LIMIT 5".format(student_list_select)
        c.execute(view_recent_records_query)
        view_recent_records.append(c.fetchall())

        view_recent_records.sort(reverse=True)

        view_recent_one_score = Counter()
        try:
            for view_one_word in view_recent_records[0][0]:
                view_recent_one_score[view_one_word] += 1
        except IndexError:
            pass
        try:
            view_recent_two_score = Counter()
            for view_two_word in view_recent_records[0][1]:
                view_recent_two_score[view_two_word] += 1
        except IndexError:
            pass
        try:
            view_recent_three_score = Counter()
            for view_three_word in view_recent_records[0][2]:
                view_recent_three_score[view_three_word] += 1
        except IndexError:
            pass        
        try:
            view_recent_four_score = Counter()
            for view_four_word in view_recent_records[0][3]:
                view_recent_four_score[view_four_word] += 1
        except IndexError:
            pass        
        try:
            view_recent_five_score = Counter()
            for view_five_word in view_recent_records[0][4]:
                view_recent_five_score[view_five_word] += 1
        except IndexError:
            pass

        try:
            view_recent_one = [view_recent_records[0][0][41].title(), view_recent_one_score['true'], view_recent_records[0][0][0]]
        except IndexError:
            pass
        try:
            view_recent_two = [view_recent_records[0][1][41].title(), view_recent_two_score['true'], view_recent_records[0][1][0]]
        except IndexError:
            pass
        try:
            view_recent_three = [view_recent_records[0][2][41].title(), view_recent_three_score['true'], view_recent_records[0][2][0]]
        except IndexError:
            pass
        try:
            view_recent_four = [view_recent_records[0][3][41].title(), view_recent_four_score['true'], view_recent_records[0][3][0]]
        except IndexError:
            pass
        try:
            view_recent_five = [view_recent_records[0][4][41].title(), view_recent_five_score['true'], view_recent_records[0][4][0]]
        except IndexError:
            pass
        try:
            view_recent_six = [view_recent_records[0][5][41].title(), view_recent_five_score['true'], view_recent_records[0][5][0]]
        except IndexError:
            pass
        try:
            view_recent_seven = [view_recent_records[0][6][41].title(), view_recent_five_score['true'], view_recent_records[0][6][0]]
        except IndexError:
            pass
        try:
            view_recent_eight = [view_recent_records[0][7][41].title(), view_recent_five_score['true'], view_recent_records[0][7][0]]
        except IndexError:
            pass
        try:
            view_recent_nine = [view_recent_records[0][8][41].title(), view_recent_five_score['true'], view_recent_records[0][8][0]]
        except IndexError:
            pass
        try:
            view_recent_ten = [view_recent_records[0][9][41].title(), view_recent_five_score['true'], view_recent_records[0][9][0]]
        except IndexError:
            pass
        try:
            view_recent_eleven = [view_recent_records[0][10][41].title(), view_recent_five_score['true'], view_recent_records[0][10][0]]
        except IndexError:
            pass
        try:
            view_recent_twelve = [view_recent_records[0][11][41].title(), view_recent_five_score['true'], view_recent_records[0][11][0]]
        except IndexError:
            pass
        try:
            view_recent_thirteen = [view_recent_records[0][12][41].title(), view_recent_five_score['true'], view_recent_records[0][12][0]]
        except IndexError:
            pass

        view_heading_one = Label(view_recent_attempts_frame, bg="#6e7376", text="Name", width=20, padx=4, pady=3, borderwidth=1, relief="solid", font=a11_font).grid(row=0, column=0)
        view_heading_two = Label(view_recent_attempts_frame, bg="#6e7376", text="Score", width=20, padx=4, pady=3, borderwidth=1, relief="solid", font=a11_font).grid(row=0, column=1)
        view_heading_three = Label(view_recent_attempts_frame, bg="#6e7376", text="Date", width=20, pady=3, borderwidth=1, relief="solid", font=a11_font).grid(row=0, column=2)

        equals_filler = "====="

        try:
            view_row_one_column_one = Label(view_recent_attempts_frame, bg="#968983", text=view_recent_one[0], width=20, padx=4, pady=2, borderwidth=1, relief="solid", font=a11_font).grid(row=1, column=0)
            view_row_one_column_two = Label(view_recent_attempts_frame, bg="#968983", text=view_recent_one[1], width=20, padx=4, pady=2, borderwidth=1, relief="solid", font=a11_font).grid(row=1, column=1)
            view_row_one_column_three = Label(view_recent_attempts_frame, bg="#968983", text=view_recent_one[2], width=20, pady=2, borderwidth=1, relief="solid", font=a11_font).grid(row=1, column=2)
        except NameError:
            view_row_one_column_one = Label(view_recent_attempts_frame, bg="#968983", text=equals_filler, width=20, padx=4, pady=2, borderwidth=1, relief="solid", font=a11_font).grid(row=1, column=0)
            view_row_one_column_two = Label(view_recent_attempts_frame, bg="#968983", text=equals_filler, width=20, padx=4, pady=2, borderwidth=1, relief="solid", font=a11_font).grid(row=1, column=1)
            view_row_one_column_three = Label(view_recent_attempts_frame, bg="#968983", text=equals_filler, width=20, pady=2, borderwidth=1, relief="solid", font=a11_font).grid(row=1, column=2)
        try:
            view_row_two_column_one = Label(view_recent_attempts_frame, bg="#fffde2", text=view_recent_two[0], width=20, padx=4, pady=2, borderwidth=1, relief="solid", font=a11_font).grid(row=2, column=0)
            view_row_two_column_two = Label(view_recent_attempts_frame, bg="#fffde2", text=view_recent_two[1], width=20, padx=4, pady=2, borderwidth=1, relief="solid", font=a11_font).grid(row=2, column=1)
            view_row_two_column_three = Label(view_recent_attempts_frame, bg="#fffde2", text=view_recent_two[2], width=20, pady=2, borderwidth=1, relief="solid", font=a11_font).grid(row=2, column=2)
        except NameError:
            view_row_two_column_one = Label(view_recent_attempts_frame, bg="#fffde2", text=equals_filler, width=20, padx=4, pady=2, borderwidth=1, relief="solid", font=a11_font).grid(row=2, column=0)
            view_row_two_column_two = Label(view_recent_attempts_frame, bg="#fffde2", text=equals_filler, width=20, padx=4, pady=2, borderwidth=1, relief="solid", font=a11_font).grid(row=2, column=1)
            view_row_two_column_three = Label(view_recent_attempts_frame, bg="#fffde2", text=equals_filler, width=20, pady=2, borderwidth=1, relief="solid", font=a11_font).grid(row=2, column=2)
        try:
            view_row_three_column_one = Label(view_recent_attempts_frame, bg="#968983", text=view_recent_three[0], width=20, padx=4, pady=2, borderwidth=1, relief="solid", font=a11_font).grid(row=3, column=0)
            view_row_three_column_two = Label(view_recent_attempts_frame, bg="#968983", text=view_recent_three[1], width=20, padx=4, pady=2, borderwidth=1, relief="solid", font=a11_font).grid(row=3, column=1)
            view_row_three_column_three = Label(view_recent_attempts_frame, bg="#968983", text=view_recent_three[2], width=20, pady=2, borderwidth=1, relief="solid", font=a11_font).grid(row=3, column=2)
        except NameError:
            view_row_three_column_one = Label(view_recent_attempts_frame, bg="#968983", text=equals_filler, width=20, padx=4, pady=2, borderwidth=1, relief="solid", font=a11_font).grid(row=3, column=0)
            view_row_three_column_two = Label(view_recent_attempts_frame, bg="#968983", text=equals_filler, width=20, padx=4, pady=2, borderwidth=1, relief="solid", font=a11_font).grid(row=3, column=1)
            view_row_three_column_three = Label(view_recent_attempts_frame, bg="#968983", text=equals_filler, width=20, pady=2, borderwidth=1, relief="solid", font=a11_font).grid(row=3, column=2)
        try:
            view_row_four_column_one = Label(view_recent_attempts_frame, bg="#fffde2", text=view_recent_four[0], width=20, padx=4, pady=2, borderwidth=1, relief="solid", font=a11_font).grid(row=4, column=0)
            view_row_four_column_two = Label(view_recent_attempts_frame, bg="#fffde2", text=view_recent_four[1], width=20, padx=4, pady=2, borderwidth=1, relief="solid", font=a11_font).grid(row=4, column=1)
            view_row_four_column_three = Label(view_recent_attempts_frame, bg="#fffde2", text=view_recent_four[2], width=20, pady=2, borderwidth=1, relief="solid", font=a11_font).grid(row=4, column=2)
        except NameError:
            view_row_four_column_one = Label(view_recent_attempts_frame, bg="#fffde2", text=equals_filler, width=20, padx=4, pady=2, borderwidth=1, relief="solid", font=a11_font).grid(row=4, column=0)
            view_row_four_column_two = Label(view_recent_attempts_frame, bg="#fffde2", text=equals_filler, width=20, padx=4, pady=2, borderwidth=1, relief="solid", font=a11_font).grid(row=4, column=1)
            view_row_four_column_three = Label(view_recent_attempts_frame, bg="#fffde2", text=equals_filler, width=20, pady=2, borderwidth=1, relief="solid", font=a11_font).grid(row=4, column=2)
        try:
            view_row_five_column_one = Label(view_recent_attempts_frame, bg="#968983", text=view_recent_four[0], width=20, padx=4, pady=2, borderwidth=1, relief="solid", font=a11_font).grid(row=5, column=0)
            view_row_five_column_two = Label(view_recent_attempts_frame, bg="#968983", text=view_recent_four[1], width=20, padx=4, pady=2, borderwidth=1, relief="solid", font=a11_font).grid(row=5, column=1)
            view_row_five_column_three = Label(view_recent_attempts_frame, bg="#968983", text=view_recent_four[2], width=20, pady=2, borderwidth=1, relief="solid", font=a11_font).grid(row=5, column=2)
        except NameError:
            view_row_five_column_one = Label(view_recent_attempts_frame, bg="#968983", text=equals_filler, width=20, padx=4, pady=2, borderwidth=1, relief="solid", font=a11_font).grid(row=5, column=0)
            view_row_five_column_two = Label(view_recent_attempts_frame, bg="#968983", text=equals_filler, width=20, padx=4, pady=2, borderwidth=1, relief="solid", font=a11_font).grid(row=5, column=1)
            view_row_five_column_three = Label(view_recent_attempts_frame, bg="#968983", text=equals_filler, width=20, pady=2, borderwidth=1, relief="solid", font=a11_font).grid(row=5, column=2)
        try:
            view_row_six_column_one = Label(view_recent_attempts_frame, bg="#fffde2", text=view_recent_six[0], width=20, padx=4, pady=2, borderwidth=1, relief="solid", font=a11_font).grid(row=6, column=0)
            view_row_six_column_two = Label(view_recent_attempts_frame, bg="#fffde2", text=view_recent_six[1], width=20, padx=4, pady=2, borderwidth=1, relief="solid", font=a11_font).grid(row=6, column=1)
            view_row_six_column_three = Label(view_recent_attempts_frame, bg="#fffde2", text=view_recent_six[2], width=20, pady=2, borderwidth=1, relief="solid", font=a11_font).grid(row=6, column=2)
        except NameError:
            view_row_six_column_one = Label(view_recent_attempts_frame, bg="#fffde2", text=equals_filler, width=20, padx=4, pady=2, borderwidth=1, relief="solid", font=a11_font).grid(row=6, column=0)
            view_row_six_column_two = Label(view_recent_attempts_frame, bg="#fffde2", text=equals_filler, width=20, padx=4, pady=2, borderwidth=1, relief="solid", font=a11_font).grid(row=6, column=1)
            view_row_six_column_three = Label(view_recent_attempts_frame, bg="#fffde2", text=equals_filler, width=20, pady=2, borderwidth=1, relief="solid", font=a11_font).grid(row=6, column=2)
        try:
            view_row_seven_column_one = Label(view_recent_attempts_frame, bg="#968983", text=view_recent_seven[0], width=20, padx=4, pady=2, borderwidth=1, relief="solid", font=a11_font).grid(row=7, column=0)
            view_row_seven_column_two = Label(view_recent_attempts_frame, bg="#968983", text=view_recent_seven[1], width=20, padx=4, pady=2, borderwidth=1, relief="solid", font=a11_font).grid(row=7, column=1)
            view_row_seven_column_three = Label(view_recent_attempts_frame, bg="#968983", text=view_recent_seven[2], width=20, pady=2, borderwidth=1, relief="solid", font=a11_font).grid(row=7, column=2)
        except NameError:
            view_row_seven_column_one = Label(view_recent_attempts_frame, bg="#968983", text=equals_filler, width=20, padx=4, pady=2, borderwidth=1, relief="solid", font=a11_font).grid(row=7, column=0)
            view_row_seven_column_two = Label(view_recent_attempts_frame, bg="#968983", text=equals_filler, width=20, padx=4, pady=2, borderwidth=1, relief="solid", font=a11_font).grid(row=7, column=1)
            view_row_seven_column_three = Label(view_recent_attempts_frame, bg="#968983", text=equals_filler, width=20, pady=2, borderwidth=1, relief="solid", font=a11_font).grid(row=7, column=2)
        try:
            view_row_eight_column_one = Label(view_recent_attempts_frame, bg="#fffde2", text=view_recent_eight[0], width=20, padx=4, pady=2, borderwidth=1, relief="solid", font=a11_font).grid(row=8, column=0)
            view_row_eight_column_two = Label(view_recent_attempts_frame, bg="#fffde2", text=view_recent_eight[1], width=20, padx=4, pady=2, borderwidth=1, relief="solid", font=a11_font).grid(row=8, column=1)
            view_row_eight_column_three = Label(view_recent_attempts_frame, bg="#fffde2", text=view_recent_eight[2], width=20, pady=2, borderwidth=1, relief="solid", font=a11_font).grid(row=8, column=2)
        except NameError:
            view_row_eight_column_one = Label(view_recent_attempts_frame, bg="#fffde2", text=equals_filler, width=20, padx=4, pady=2, borderwidth=1, relief="solid", font=a11_font).grid(row=8, column=0)
            view_row_eight_column_two = Label(view_recent_attempts_frame, bg="#fffde2", text=equals_filler, width=20, padx=4, pady=2, borderwidth=1, relief="solid", font=a11_font).grid(row=8, column=1)
            view_row_eight_column_three = Label(view_recent_attempts_frame, bg="#fffde2", text=equals_filler, width=20, pady=2, borderwidth=1, relief="solid", font=a11_font).grid(row=8, column=2)
        try:
            view_row_nine_column_one = Label(view_recent_attempts_frame, bg="#968983", text=view_recent_nine[0], width=20, padx=4, pady=2, borderwidth=1, relief="solid", font=a11_font).grid(row=9, column=0)
            view_row_nine_column_two = Label(view_recent_attempts_frame, bg="#968983", text=view_recent_nine[1], width=20, padx=4, pady=2, borderwidth=1, relief="solid", font=a11_font).grid(row=9, column=1)
            view_row_nine_column_three = Label(view_recent_attempts_frame, bg="#968983", text=view_recent_nine[2], width=20, pady=2, borderwidth=1, relief="solid", font=a11_font).grid(row=9, column=2)
        except NameError:
            view_row_nine_column_one = Label(view_recent_attempts_frame, bg="#968983", text=equals_filler, width=20, padx=4, pady=2, borderwidth=1, relief="solid", font=a11_font).grid(row=9, column=0)
            view_row_nine_column_two = Label(view_recent_attempts_frame, bg="#968983", text=equals_filler, width=20, padx=4, pady=2, borderwidth=1, relief="solid", font=a11_font).grid(row=9, column=1)
            view_row_nine_column_three = Label(view_recent_attempts_frame, bg="#968983", text=equals_filler, width=20, pady=2, borderwidth=1, relief="solid", font=a11_font).grid(row=9, column=2)
        try:
            view_row_ten_column_one = Label(view_recent_attempts_frame, bg="#fffde2", text=view_recent_ten[0], width=20, padx=4, pady=2, borderwidth=1, relief="solid", font=a11_font).grid(row=10, column=0)
            view_row_ten_column_two = Label(view_recent_attempts_frame, bg="#fffde2", text=view_recent_ten[1], width=20, padx=4, pady=2, borderwidth=1, relief="solid", font=a11_font).grid(row=10, column=1)
            view_row_ten_column_three = Label(view_recent_attempts_frame, bg="#fffde2", text=view_recent_ten[2], width=20, pady=2, borderwidth=1, relief="solid", font=a11_font).grid(row=10, column=2)
        except NameError:
            view_row_ten_column_one = Label(view_recent_attempts_frame, bg="#fffde2", text=equals_filler, width=20, padx=4, pady=2, borderwidth=1, relief="solid", font=a11_font).grid(row=10, column=0)
            view_row_ten_column_two = Label(view_recent_attempts_frame, bg="#fffde2", text=equals_filler, width=20, padx=4, pady=2, borderwidth=1, relief="solid", font=a11_font).grid(row=10, column=1)
            view_row_ten_column_three = Label(view_recent_attempts_frame, bg="#fffde2", text=equals_filler, width=20, pady=2, borderwidth=1, relief="solid", font=a11_font).grid(row=10, column=2)
        try:
            view_row_eleven_column_one = Label(view_recent_attempts_frame, bg="#968983", text=view_recent_eleven[0], width=20, padx=4, pady=2, borderwidth=1, relief="solid", font=a11_font).grid(row=11, column=0)
            view_row_eleven_column_two = Label(view_recent_attempts_frame, bg="#968983", text=view_recent_eleven[1], width=20, padx=4, pady=2, borderwidth=1, relief="solid", font=a11_font).grid(row=11, column=1)
            view_row_eleven_column_three = Label(view_recent_attempts_frame, bg="#968983", text=view_recent_eleven[2], width=20, pady=2, borderwidth=1, relief="solid", font=a11_font).grid(row=11, column=2)
        except NameError:
            view_row_eleven_column_one = Label(view_recent_attempts_frame, bg="#968983", text=equals_filler, width=20, padx=4, pady=2, borderwidth=1, relief="solid", font=a11_font).grid(row=11, column=0)
            view_row_eleven_column_two = Label(view_recent_attempts_frame, bg="#968983", text=equals_filler, width=20, padx=4, pady=2, borderwidth=1, relief="solid", font=a11_font).grid(row=11, column=1)
            view_row_eleven_column_three = Label(view_recent_attempts_frame, bg="#968983", text=equals_filler, width=20, pady=2, borderwidth=1, relief="solid", font=a11_font).grid(row=11, column=2)
        try:
            view_row_twelve_column_one = Label(view_recent_attempts_frame, bg="#fffde2", text=view_recent_twelve[0], width=20, padx=4, pady=2, borderwidth=1, relief="solid", font=a11_font).grid(row=12, column=0)
            view_row_twelve_column_two = Label(view_recent_attempts_frame, bg="#fffde2", text=view_recent_twelve[1], width=20, padx=4, pady=2, borderwidth=1, relief="solid", font=a11_font).grid(row=12, column=1)
            view_row_twelve_column_three = Label(view_recent_attempts_frame, bg="#fffde2", text=view_recent_twelve[2], width=20, pady=2, borderwidth=1, relief="solid", font=a11_font).grid(row=12, column=2)
        except NameError:
            view_row_twelve_column_one = Label(view_recent_attempts_frame, bg="#fffde2", text=equals_filler, width=20, padx=4, pady=2, borderwidth=1, relief="solid", font=a11_font).grid(row=12, column=0)
            view_row_twelve_column_two = Label(view_recent_attempts_frame, bg="#fffde2", text=equals_filler, width=20, padx=4, pady=2, borderwidth=1, relief="solid", font=a11_font).grid(row=12, column=1)
            view_row_twelve_column_three = Label(view_recent_attempts_frame, bg="#fffde2", text=equals_filler, width=20, pady=2, borderwidth=1, relief="solid", font=a11_font).grid(row=12, column=2)
        try:
            view_row_thirteen_column_one = Label(view_recent_attempts_frame, bg="#968983", text=view_recent_thirteen[0], width=20, padx=4, pady=2, borderwidth=1, relief="solid", font=a11_font).grid(row=13, column=0)
            view_row_thirteen_column_two = Label(view_recent_attempts_frame, bg="#968983", text=view_recent_thirteen[1], width=20, padx=4, pady=2, borderwidth=1, relief="solid", font=a11_font).grid(row=13, column=1)
            view_row_thirteen_column_three = Label(view_recent_attempts_frame, bg="#968983", text=view_recent_thirteen[2], width=20, pady=2, borderwidth=1, relief="solid", font=a11_font).grid(row=13, column=2)
        except NameError:
            view_row_thirteen_column_one = Label(view_recent_attempts_frame, bg="#968983", text=equals_filler, width=20, padx=4, pady=2, borderwidth=1, relief="solid", font=a11_font).grid(row=13, column=0)
            view_row_thirteen_column_two = Label(view_recent_attempts_frame, bg="#968983", text=equals_filler, width=20, padx=4, pady=2, borderwidth=1, relief="solid", font=a11_font).grid(row=13, column=1)
            view_row_thirteen_column_three = Label(view_recent_attempts_frame, bg="#968983", text=equals_filler, width=20, pady=2, borderwidth=1, relief="solid", font=a11_font).grid(row=13, column=2)

    ############################################################
        
    home_frame.tkraise()
    root_canvas.pack()
    root.mainloop()
