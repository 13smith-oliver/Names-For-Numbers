import sys; sys.dont_write_bytecode = True
from tkinter import *
from sqlite3 import *
from time import *
from random import choice

####################

def student_ui_func(name_data):
    conn = connect("names_for_numbers.db")
    c = conn.cursor()

    ####################

    number_words = {
                                "Forty Five" : 45,
                                "Fifty One" : 51,
                                "Two Hundred and Twenty Eight" : 228,
                                "Three Hundred and Twenty Five" : 325,
                                "Three Hundred and Forty Five" : 345,
                                "Three Hundred and Seventy Five" : 375,
                                "Seven Hundred and Sixty One" : 761,
                                "Nine Hundred and Sixty Three" : 963,
                                "One Thousand, Two Hundred and Thirty Six" : 1236,
                                "One Thousand, Two Hundred and Forty" : 1240,
                                "One Thousand, Three Hundred and Fifty Five" : 1355,
                                "One Thousand, Five Hundred and Forty Two" : 1542,
                                "One Thousand, Nine Hundred and Sixty Five" : 1965,
                                "Two Thousand, Four Hundred and Fifty Five" : 2455,
                                "Two Thousand, Five Hundred and Forty Five" : 2545,
                                "Three Thousand, Two Hundred and Forty Seven" : 3247,
                                "Three Thousand, Six Hundred and Fifty One" : 3651,
                                "Three Thousand, Seven Hundred and Sixty Three" : 3763,
                                "Three Thousand, Eight Hundred and Seventy Six" : 3876,
                                "Four Thousand and Ninety Nine" : 4099,
                                "Four Thousand, Five Hundred and Thirty Nine" : 4539,
                                "Four Thousand, Six Hundred and Fifty Four" : 4654,
                                "Four Thousand, Eight Hundred and Fifty Nine" : 4859,
                                "Five Thousand, Two Hundred and Sixty Three" : 5263,
                                "Five Thousand, Three Hundred and Seventy Nine" : 5379,
                                "Five Thousand, Six Hundred and Thirty Two" : 5632,
                                "Five Thousand, Seven Hundred and Seventy One" : 5771,
                                "Five Thousand, Eight Hundred and Fifty Two" : 5852,
                                "Six Thousand, Four Hundred and Nine" : 6409,
                                "Seven Thousand, Two Hundred and Twenty Seven" : 7227,
                                "Seven Thousand, Four Hundred and Twenty Six" : 7426,
                                "Seven Thousand, Four Hundred and Fifty Nine" : 7459,
                                "Eight Thousand, Four Hundred and Thirteen" : 8413,
                                "Eight Thousand, Eight Hundred and Sixty Eight" : 8868,
                                "Nine Thousand, One Hundred and Three" : 9103,
                                "Nine Thousand, One Hundred and Thirty Two" : 9132,
                                "Nine Thousand, One Hundred and Thirty Seven" : 9137,
                                "Nine Thousand, Five Hundred and Twenty Three" : 9523,
                                "Nine Thousand, Six Hundred and Twenty One" : 9621,
                                "Nine Thousand, Eight Hundred and Sixty Four" : 9864
    }

    ####################

    user_table_name = name_data

    query = 'SELECT _45 FROM {} ORDER BY runid DESC LIMIT 3'.format(user_table_name)
    c.execute(query)
    status_1 = c.fetchall()
    if ('true',) in status_1:
        status_1 = True
    else:
        status_1 = False

    query = 'SELECT _51 FROM {} ORDER BY runid DESC LIMIT 3'.format(user_table_name)
    c.execute(query)
    status_2 = c.fetchall()
    if ('true',) in status_2:
        status_2 = True
    else:
        status_2 = False

    query = 'SELECT _228 FROM {} ORDER BY runid DESC LIMIT 3'.format(user_table_name)
    c.execute(query)
    status_3 = c.fetchall()
    if ('true',) in status_3:
        status_3 = True
    else:
        status_3 = False

    query = 'SELECT _325 FROM {} ORDER BY runid DESC LIMIT 3'.format(user_table_name)
    c.execute(query)
    status_4 = c.fetchall()
    if ('true',) in status_4:
        status_4 = True
    else:
        status_4 = False

    query = 'SELECT _345 FROM {} ORDER BY runid DESC LIMIT 3'.format(user_table_name)
    c.execute(query)
    status_5 = c.fetchall()
    if ('true',) in status_5:
        status_5 = True
    else:
        status_5 = False

    query = 'SELECT _375 FROM {} ORDER BY runid DESC LIMIT 3'.format(user_table_name)
    c.execute(query)
    status_6 = c.fetchall()
    if ('true',) in status_6:
        status_6 = True
    else:
        status_6 = False

    query = 'SELECT _761 FROM {} ORDER BY runid DESC LIMIT 3'.format(user_table_name)
    c.execute(query)
    status_7 = c.fetchall()
    if ('true',) in status_7:
        status_7 = True
    else:
        status_7 = False

    query = 'SELECT _963 FROM {} ORDER BY runid DESC LIMIT 3'.format(user_table_name)
    c.execute(query)
    status_8 = c.fetchall()
    if ('true',) in status_8:
        status_8 = True
    else:
        status_8 = False

    query = 'SELECT _1236 FROM {} ORDER BY runid DESC LIMIT 3'.format(user_table_name)
    c.execute(query)
    status_9 = c.fetchall()
    if ('true',) in status_9:
        status_9 = True
    else:
        status_9 = False

    query = 'SELECT _1240 FROM {} ORDER BY runid DESC LIMIT 3'.format(user_table_name)
    c.execute(query)
    status_10 = c.fetchall()
    if ('true',) in status_10:
        status_10 = True
    else:
        status_10 = False

    query = 'SELECT _1355 FROM {} ORDER BY runid DESC LIMIT 3'.format(user_table_name)
    c.execute(query)
    status_11 = c.fetchall()
    if ('true',) in status_11:
        status_11 = True
    else:
        status_11 = False

    query = 'SELECT _1542 FROM {} ORDER BY runid DESC LIMIT 3'.format(user_table_name)
    c.execute(query)
    status_12 = c.fetchall()
    if ('true',) in status_12:
        status_12 = True
    else:
        status_12 = False

    query = 'SELECT _1965 FROM {} ORDER BY runid DESC LIMIT 3'.format(user_table_name)
    c.execute(query)
    status_13 = c.fetchall()
    if ('true',) in status_13:
        status_13 = True
    else:
        status_13 = False

    query = 'SELECT _2455 FROM {} ORDER BY runid DESC LIMIT 3'.format(user_table_name)
    c.execute(query)
    status_14 = c.fetchall()
    if ('true',) in status_14:
        status_14 = True
    else:
        status_14 = False

    query = 'SELECT _2545 FROM {} ORDER BY runid DESC LIMIT 3'.format(user_table_name)
    c.execute(query)
    status_15 = c.fetchall()
    if ('true',) in status_15:
        status_15 = True
    else:
        status_15 = False

    query = 'SELECT _3247 FROM {} ORDER BY runid DESC LIMIT 3'.format(user_table_name)
    c.execute(query)
    status_16 = c.fetchall()
    if ('true',) in status_16:
        status_16 = True
    else:
        status_16 = False
        
    query = 'SELECT _3651 FROM {} ORDER BY runid DESC LIMIT 3'.format(user_table_name)
    c.execute(query)
    status_17 = c.fetchall()
    if ('true',) in status_17:
        status_17 = True
    else:
        status_17 = False
        
    query = 'SELECT _3763 FROM {} ORDER BY runid DESC LIMIT 3'.format(user_table_name)
    c.execute(query)
    status_18 = c.fetchall()
    if ('true',) in status_18:
        status_18 = True
    else:
        status_18 = False


    query = 'SELECT _3876 FROM {} ORDER BY runid DESC LIMIT 3'.format(user_table_name)
    c.execute(query)
    status_19 = c.fetchall()
    if ('true',) in status_19:
        status_19 = True
    else:
        status_19 = False

    query = 'SELECT _4099 FROM {} ORDER BY runid DESC LIMIT 3'.format(user_table_name)
    c.execute(query)
    status_20 = c.fetchall()
    if ('true',) in status_20:
        status_20 = True
    else:
        status_20 = False

    query = 'SELECT _4539 FROM {} ORDER BY runid DESC LIMIT 3'.format(user_table_name)
    c.execute(query)
    status_21 = c.fetchall()
    if ('true',) in status_21:
        status_21 = True
    else:
        status_21 = False

    query = 'SELECT _4654 FROM {} ORDER BY runid DESC LIMIT 3'.format(user_table_name)
    c.execute(query)
    status_22 = c.fetchall()
    if ('true',) in status_22:
        status_22 = True
    else:
        status_22 = False

    query = 'SELECT _4859 FROM {} ORDER BY runid DESC LIMIT 3'.format(user_table_name)
    c.execute(query)
    status_23 = c.fetchall()
    if ('true',) in status_23:
        status_23 = True
    else:
        status_23 = False

    query = 'SELECT _5263 FROM {} ORDER BY runid DESC LIMIT 3'.format(user_table_name)
    c.execute(query)
    status_24 = c.fetchall()
    if ('true',) in status_24:
        status_24 = True
    else:
        status_24 = False

    query = 'SELECT _5379 FROM {} ORDER BY runid DESC LIMIT 3'.format(user_table_name)
    c.execute(query)
    status_25 = c.fetchall()
    if ('true',) in status_25:
        status_25 = True
    else:
        status_25 = False

    query = 'SELECT _5632 FROM {} ORDER BY runid DESC LIMIT 3'.format(user_table_name)
    c.execute(query)
    status_26 = c.fetchall()
    if ('true',) in status_26:
        status_26 = True
    else:
        status_26 = False

    query = 'SELECT _5771 FROM {} ORDER BY runid DESC LIMIT 3'.format(user_table_name)
    c.execute(query)
    status_27 = c.fetchall()
    if ('true',) in status_27:
        status_27 = True
    else:
        status_27 = False

    query = 'SELECT _5852 FROM {} ORDER BY runid DESC LIMIT 3'.format(user_table_name)
    c.execute(query)
    status_28 = c.fetchall()
    if ('true',) in status_28:
        status_28 = True
    else:
        status_28 = False

    query = 'SELECT _6409 FROM {} ORDER BY runid DESC LIMIT 3'.format(user_table_name)
    c.execute(query)
    status_29 = c.fetchall()
    if ('true',) in status_29:
        status_29 = True
    else:
        status_29 = False

    query = 'SELECT _7227 FROM {} ORDER BY runid DESC LIMIT 3'.format(user_table_name)
    c.execute(query)
    status_30 = c.fetchall()
    if ('true',) in status_30:
        status_30 = True
    else:
        status_30 = False

    query = 'SELECT _7426 FROM {} ORDER BY runid DESC LIMIT 3'.format(user_table_name)
    c.execute(query)
    status_31 = c.fetchall()
    if ('true',) in status_31:
        status_31 = True
    else:
        status_31 = False

    query = 'SELECT _7459 FROM {} ORDER BY runid DESC LIMIT 3'.format(user_table_name)
    c.execute(query)
    status_32 = c.fetchall()
    if ('true',) in status_32:
        status_32 = True
    else:
        status_32 = False

    query = 'SELECT _8413 FROM {} ORDER BY runid DESC LIMIT 3'.format(user_table_name)
    c.execute(query)
    status_33 = c.fetchall()
    if ('true',) in status_33:
        status_33 = True
    else:
        status_33 = False

    query = 'SELECT _8868 FROM {} ORDER BY runid DESC LIMIT 3'.format(user_table_name)
    c.execute(query)
    status_34 = c.fetchall()
    if ('true',) in status_34:
        status_34 = True
    else:
        status_34 = False

    query = 'SELECT _9103 FROM {} ORDER BY runid DESC LIMIT 3'.format(user_table_name)
    c.execute(query)
    status_35 = c.fetchall()
    if ('true',) in status_35:
        status_35 = True
    else:
        status_35 = False

    query = 'SELECT _9132 FROM {} ORDER BY runid DESC LIMIT 3'.format(user_table_name)
    c.execute(query)
    status_36 = c.fetchall()
    if ('true',) in status_36:
        status_36 = True
    else:
        status_36 = False

    query = 'SELECT _9137 FROM {} ORDER BY runid DESC LIMIT 3'.format(user_table_name)
    c.execute(query)
    status_37 = c.fetchall()
    if ('true',) in status_37:
        status_37 = True
    else:
        status_37 = False

    query = 'SELECT _9523 FROM {} ORDER BY runid DESC LIMIT 3'.format(user_table_name)
    c.execute(query)
    status_38 = c.fetchall()
    if ('true',) in status_38:
        status_38 = True
    else:
        status_38 = False

    query = 'SELECT _9621 FROM {} ORDER BY runid DESC LIMIT 3'.format(user_table_name)
    c.execute(query)
    status_39 = c.fetchall()
    if ('true',) in status_39:
        status_39 = True
    else:
        status_39 = False

    query = 'SELECT _9864 FROM {} ORDER BY runid DESC LIMIT 3'.format(user_table_name)
    c.execute(query)
    status_40 = c.fetchall()
    if ('true',) in status_40:
        status_40 = True
    else:
        status_40 = False

    ####################

    available_questions = []

    if status_1 == False:
        available_questions.append(45)
    if status_2 == False:
        available_questions.append(51)
    if status_3 == False:
        available_questions.append(228)
    if status_4 == False:
        available_questions.append(325)
    if status_5 == False:
        available_questions.append(345)
    if status_6 == False:
        available_questions.append(375)
    if status_7 == False:
        available_questions.append(761)
    if status_8 == False:
        available_questions.append(963)
    if status_9 == False:
        available_questions.append(1236)
    if status_10 == False:
        available_questions.append(1240)
    if status_11 == False:
        available_questions.append(1355)
    if status_12 == False:
        available_questions.append(1542)
    if status_13 == False:
        available_questions.append(1965)
    if status_14 == False:
        available_questions.append(2455)
    if status_15 == False:
        available_questions.append(2545)
    if status_16 == False:
        available_questions.append(3247)
    if status_17 == False:
        available_questions.append(3651)
    if status_18 == False:
        available_questions.append(3763)
    if status_19 == False:
        available_questions.append(3876)
    if status_20 == False:
        available_questions.append(4099)
    if status_21 == False:
        available_questions.append(4539)
    if status_22 == False:
        available_questions.append(4654)
    if status_23 == False:
        available_questions.append(4859)
    if status_24 == False:
        available_questions.append(5263)
    if status_25 == False:
        available_questions.append(5379)
    if status_26 == False:
        available_questions.append(5632)
    if status_27 == False:
        available_questions.append(5771)
    if status_28 == False:
        available_questions.append(5852)
    if status_29 == False:
        available_questions.append(6409)
    if status_30 == False:
        available_questions.append(7227)
    if status_31 == False:
        available_questions.append(7426)
    if status_32 == False:
        available_questions.append(7459)
    if status_33 == False:
        available_questions.append(8413)
    if status_34 == False:
        available_questions.append(8868)
    if status_35 == False:
        available_questions.append(9103)
    if status_36 == False:
        available_questions.append(9132)
    if status_37 == False:
        available_questions.append(9137)
    if status_38 == False:
        available_questions.append(9523)
    if status_39 == False:
        available_questions.append(9621)
    if status_40 == False:
        available_questions.append(9864)

    ####################

    question_one = choice(available_questions)
    available_questions.remove(question_one)
    for word, number in number_words.items():
        if number == question_one:
            question_one_text = word
    ##########        
    question_two = choice(available_questions)
    available_questions.remove(question_two)
    for word, number in number_words.items():
        if number == question_two:
            question_two_text = word
    ##########       
    question_three = choice(available_questions)
    available_questions.remove(question_three)
    for word, number in number_words.items():
        if number == question_three:
            question_three_text = word
    ##########        
    question_four = choice(available_questions)
    available_questions.remove(question_four)
    for word, number in number_words.items():
        if number == question_four:
            question_four_text = word
    ##########
    question_five = choice(available_questions)
    available_questions.remove(question_five)
    for word, number in number_words.items():
        if number == question_five:
            question_five_text = word
    ##########
    question_six = choice(available_questions)
    available_questions.remove(question_six)
    for word, number in number_words.items():
        if number == question_six:
            question_six_text = word
    ##########
    question_seven = choice(available_questions)
    available_questions.remove(question_seven)
    for word, number in number_words.items():
        if number == question_seven:
            question_seven_text = word
    ##########
    question_eight = choice(available_questions)
    available_questions.remove(question_eight)
    for word, number in number_words.items():
        if number == question_eight:
            question_eight_text = word
    ##########
    question_nine = choice(available_questions)
    available_questions.remove(question_nine)
    for word, number in number_words.items():
        if number == question_nine:
            question_nine_text = word
    ##########
    question_ten = choice(available_questions)
    available_questions.remove(question_ten)
    for word, number in number_words.items():
        if number == question_ten:
            question_ten_text = word

    ####################

    main_window = Tk()
    main_window.geometry("590x360")
    main_window.configure(bg="#F2EFEF")
    main_window.resizable(width=False, height=False)


    ####################

    tick_mark = PhotoImage(file="tick_mark.png")
    cross_mark = PhotoImage(file="cross_mark.png")

    a14_font = ("Arial", 14)
    a9_font = ("Arial", 9)

    ####################

    grey_top_frame = Frame(main_window, bg="#c9c9c9")
    grey_top_frame.place(x=0, y=0, width=590, height=75)
    
    instr_label = Label(main_window, text="In the boxes below,\nwrite the number\nthat goes with\nthe word.", bg="#5e5e5e", pady=2, borderwidth=1, relief="solid", font=a9_font)
    instr_label.place(x=315, y=5, width=125, height=65)

    corner_welcome = Label(main_window, text="Welcome, " + user_table_name.title(), bg="#5e5e5e", pady=2, borderwidth=1, relief="solid", font=a14_font, justify="center")
    corner_welcome.place(x=88, y=20, width=150, height=30)
    
    ####################

    question_one_label = Label(main_window, text=question_one_text, bg="#5e5e5e", borderwidth=1, relief="solid", font=a9_font)
    question_two_label = Label(main_window, text=question_two_text, bg="#5e5e5e", borderwidth=1, relief="solid", font=a9_font)
    question_three_label = Label(main_window, text=question_three_text, bg="#5e5e5e", borderwidth=1, relief="solid", font=a9_font)
    question_four_label = Label(main_window, text=question_four_text, bg="#5e5e5e", borderwidth=1, relief="solid", font=a9_font)
    question_five_label = Label(main_window, text=question_five_text, bg="#5e5e5e", borderwidth=1, relief="solid", font=a9_font)
    question_six_label = Label(main_window, text=question_six_text, bg="#5e5e5e", borderwidth=1, relief="solid", font=a9_font)
    question_seven_label = Label(main_window, text=question_seven_text, bg="#5e5e5e", borderwidth=1, relief="solid", font=a9_font)
    question_eight_label = Label(main_window, text=question_eight_text, bg="#5e5e5e", borderwidth=1, relief="solid", font=a9_font)
    question_nine_label = Label(main_window, text=question_nine_text, bg="#5e5e5e", borderwidth=1, relief="solid", font=a9_font)
    question_ten_label = Label(main_window, text=question_ten_text, bg="#5e5e5e", borderwidth=1, relief="solid", font=a9_font)

    ##########

    question_one_label.place(x=25, y=80, width=275, height=20)
    question_two_label.place(x=25, y=105, width=275, height=20)
    question_three_label.place(x=25, y=130, width=275, height=20)
    question_four_label.place(x=25, y=155, width=275, height=20)
    question_five_label.place(x=25, y=180, width=275, height=20)
    question_six_label.place(x=25, y=205, width=275, height=20)
    question_seven_label.place(x=25, y=230, width=275, height=20)
    question_eight_label.place(x=25, y=255, width=275, height=20)
    question_nine_label.place(x=25, y=280, width=275, height=20)
    question_ten_label.place(x=25, y=305, width=275, height=20)

    ####################

    question_one_save = StringVar()
    question_two_save = StringVar()
    question_three_save = StringVar()
    question_four_save = StringVar()
    question_five_save = StringVar()
    question_six_save = StringVar()
    question_seven_save = StringVar()
    question_eight_save = StringVar()
    question_nine_save = StringVar()
    question_ten_save = StringVar()

    ##########

    question_one_entry = Entry(main_window, textvariable = question_one_save, borderwidth=1, relief="solid", justify="center", font=a9_font)
    question_two_entry = Entry(main_window, textvariable = question_two_save, borderwidth=1, relief="solid", justify="center", font=a9_font)
    question_three_entry = Entry(main_window, textvariable = question_three_save, borderwidth=1, relief="solid", justify="center", font=a9_font)
    question_four_entry = Entry(main_window, textvariable = question_four_save, borderwidth=1, relief="solid", justify="center", font=a9_font)
    question_five_entry = Entry(main_window, textvariable = question_five_save, borderwidth=1, relief="solid", justify="center", font=a9_font)
    question_six_entry = Entry(main_window, textvariable = question_six_save, borderwidth=1, relief="solid", justify="center", font=a9_font)
    question_seven_entry = Entry(main_window, textvariable = question_seven_save, borderwidth=1, relief="solid", justify="center", font=a9_font)
    question_eight_entry = Entry(main_window, textvariable = question_eight_save, borderwidth=1, relief="solid", justify="center", font=a9_font)
    question_nine_entry = Entry(main_window, textvariable = question_nine_save, borderwidth=1, relief="solid", justify="center", font=a9_font)
    question_ten_entry = Entry(main_window, textvariable = question_ten_save, borderwidth=1, relief="solid", justify="center", font=a9_font)

    ##########

    question_one_entry.place(x=450, y=80, width=100, height=20)
    question_two_entry.place(x=450, y=105, width=100, height=20)
    question_three_entry.place(x=450, y=130, width=100, height=20)
    question_four_entry.place(x=450, y=155, width=100, height=20)
    question_five_entry.place(x=450, y=180, width=100, height=20)
    question_six_entry.place(x=450, y=205, width=100, height=20)
    question_seven_entry.place(x=450, y=230, width=100, height=20)
    question_eight_entry.place(x=450, y=255, width=100, height=20)
    question_nine_entry.place(x=450, y=280, width=100, height=20)
    question_ten_entry.place(x=450, y=305, width=100, height=20)

    ####################

    def check_answers():
        question_one_return = question_one_save.get()
        question_two_return = question_two_save.get()
        question_three_return = question_three_save.get()
        question_four_return = question_four_save.get()
        question_five_return = question_five_save.get()
        question_six_return = question_six_save.get()
        question_seven_return = question_seven_save.get()
        question_eight_return = question_eight_save.get()
        question_nine_return = question_nine_save.get()
        question_ten_return = question_ten_save.get()
        ##########
        try:
            question_one_return = int(question_one_return)
        except ValueError:
            pass
        ##########
        try:
            question_two_return = int(question_two_return)
        except ValueError:
            pass
        ##########
        try:
            question_three_return = int(question_three_return)
        except ValueError:
            pass
        ##########
        try:
            question_four_return = int(question_four_return)
        except ValueError:
            pass
        ##########
        try:
            question_five_return = int(question_five_return)
        except ValueError:
            pass
        ##########
        try:
            question_six_return = int(question_six_return)
        except ValueError:
            pass
        ##########
        try:
            question_seven_return = int(question_seven_return)
        except ValueError:
            pass
        ##########
        try:
            question_eight_return = int(question_eight_return)
        except ValueError:
            pass
        ##########
        try:
            question_nine_return = int(question_nine_return)
        except ValueError:
            pass
        ##########
        try:
            question_ten_return = int(question_ten_return)
        except ValueError:
            pass
        ##########
        if question_one_return == number_words[question_one_text]:
            tick_label_one = Label(main_window, image = tick_mark, bg="#F2EFEF")
            tick_label_one.place(x=555, y=80)
            answer_one = "true"
        else:
            cross_label_one = Label(main_window, image = cross_mark, bg="#F2EFEF")
            cross_label_one.place(x=555, y=80)
            answer_one = "false"
        ##########
        if question_two_return == number_words[question_two_text]:
            tick_label_two = Label(main_window, image = tick_mark, bg="#F2EFEF")
            tick_label_two.place(x=555, y=105)
            answer_two = "true"
        else:
            cross_label_two = Label(main_window, image = cross_mark, bg="#F2EFEF")
            cross_label_two.place(x=555, y=105)
            answer_two = "false"
        ##########
        if question_three_return == number_words[question_three_text]:
            tick_label_three = Label(main_window, image = tick_mark, bg="#F2EFEF")
            tick_label_three.place(x=555, y=130)
            answer_three = "true"
        else:
            cross_label_three = Label(main_window, image = cross_mark, bg="#F2EFEF")
            cross_label_three.place(x=555, y=130)
            answer_three = "false"
        ##########
        if question_four_return == number_words[question_four_text]:
            tick_label_four = Label(main_window, image = tick_mark, bg="#F2EFEF")
            tick_label_four.place(x=555, y=155)
            answer_four = "true"
        else:
            cross_label_four = Label(main_window, image = cross_mark, bg="#F2EFEF")
            cross_label_four.place(x=555, y=155)
            answer_four = "false"
        ##########
        if question_five_return == number_words[question_five_text]:
            tick_label_five = Label(main_window, image = tick_mark, bg="#F2EFEF")
            tick_label_five.place(x=555, y=180)
            answer_five = "true"
        else:
            cross_label_five = Label(main_window, image = cross_mark, bg="#F2EFEF")
            cross_label_five.place(x=555, y=180)
            answer_five = "false"
        ##########
        if question_six_return == number_words[question_six_text]:
            tick_label_six = Label(main_window, image = tick_mark, bg="#F2EFEF")
            tick_label_six.place(x=555, y=205)
            answer_six = "true"
        else:
            cross_label_six = Label(main_window, image = cross_mark, bg="#F2EFEF")
            cross_label_six.place(x=555, y=205)
            answer_six = "false"
        ##########
        if question_seven_return == number_words[question_seven_text]:
            tick_label_seven = Label(main_window, image = tick_mark, bg="#F2EFEF")
            tick_label_seven.place(x=555, y=230)
            answer_seven = "true"
        else:
            cross_label_seven = Label(main_window, image = cross_mark, bg="#F2EFEF")
            cross_label_seven.place(x=555, y=230)
            answer_seven = "false"
        ##########
        if question_eight_return == number_words[question_eight_text]:
            tick_label_eight = Label(main_window, image = tick_mark, bg="#F2EFEF")
            tick_label_eight.place(x=555, y=255)
            answer_eight = "true"
        else:
            cross_label_eight = Label(main_window, image = cross_mark, bg="#F2EFEF")
            cross_label_eight.place(x=555, y=255)
            answer_eight = "false"
        ##########
        if question_nine_return == number_words[question_nine_text]:
            tick_label_nine = Label(main_window, image = tick_mark, bg="#F2EFEF")
            tick_label_nine.place(x=555, y=280)
            answer_nine = "true"
        else:
            cross_label_nine = Label(main_window, image = cross_mark, bg="#F2EFEF")
            cross_label_nine.place(x=555, y=280)
            answer_nine = "false"
        ##########
        if question_ten_return == number_words[question_ten_text]:
            tick_label_ten= Label(main_window, image = tick_mark, bg="#F2EFEF")
            tick_label_ten.place(x=555, y=305)
            answer_ten = "true"
        else:
            cross_label_ten = Label(main_window, image = cross_mark, bg="#F2EFEF")
            cross_label_ten.place(x=555, y=305)
            answer_ten = "false"
        ##########    
        question_one_column = "_" + str(number_words[question_one_text])
        question_two_column = "_" + str(number_words[question_two_text])
        question_three_column = "_" +str( number_words[question_three_text])
        question_four_column = "_" + str(number_words[question_four_text])
        question_five_column = "_" + str(number_words[question_five_text])
        question_six_column = "_" + str(number_words[question_six_text])
        question_seven_column = "_" + str(number_words[question_seven_text])
        question_eight_column = "_" + str(number_words[question_eight_text])
        question_nine_column = "_" + str(number_words[question_nine_text])
        question_ten_column = "_" + str(number_words[question_ten_text])
        ##########
        c.execute('INSERT INTO "{}" ({}, {}, {}, {}, {}, {}, {}, {}, {}, {}) VALUES ("{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}")'.format(user_table_name, question_one_column, question_two_column, question_three_column, question_four_column, question_five_column, question_six_column, question_seven_column, question_eight_column,question_nine_column, question_ten_column, answer_one, answer_two, answer_three, answer_four, answer_five, answer_six, answer_seven, answer_eight, answer_nine, answer_ten))
        conn.commit()
        conn.close()

        mark_button.config(text = "Quit!")
        mark_button.config(command = main_window.destroy)
        
    ####################
        
    mark_button = Button(main_window, text="Mark!", command = check_answers, bg="#d3392e", borderwidth=1, relief="solid", font=a9_font)
    mark_button.place(x=355, y=330, width=40, height=25)
                      
    ####################

    main_window.mainloop()
