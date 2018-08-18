from tkinter import *
from sqlite3 import *
from time import strftime
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

root = Tk()
root.configure(background="#6e7376")
root.geometry("725x450")
root.resizable(width=False, height=False)

####################

a12_font = ("Arial", 12)
a11_font = ("Arial", 11)

root_canvas = Canvas(root, bg="#6e7376", width=725, height=450, highlightthickness=0)
horizontal_line_one = root_canvas.create_line(0, 40, 725, 40)
vertical_line_one = root_canvas.create_line(110, 40, 110, 450)

home_frame = Frame(root, bg="#a1dbcd")
home_frame.place(x=111, y=41, width=615, height=409)
####################



conn = connect("Eduqas_GCSE_SAM_Python_Data.db")
c = conn.cursor()
c.execute("SELECT name FROM sqlite_master WHERE type='table'")
students_tables = c.fetchall()
list(students_tables)
list(students_tables[0])
del students_tables[0]


view_butt = Button(root, command=lambda: view_command())
view_butt.pack()

#####################################################################
def view_command():
    #student_list_select = student_list_box_one.curselection().lower()
    student_list_select = "oliver"
    
    view_frame = Frame(root, bg="#a1dbcd")
    view_frame.place(x=111, y=41, width=615, height=409)

    view_recent_attempts = Label(view_frame, text=student_list_select.title() + "'s Recent Attempts", background="#d3392e", font=a12_font, borderwidth=1, relief="solid")
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

root_canvas.pack()
root.mainloop()
