import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *

root = Tk()
best_scores_frame = Frame(root)
best_scores_frame.pack()

f = plt.figure(figsize=(249/96, 170/96), dpi=100)
ax = f.add_subplot(111)

correct_data = (80, 60, 52, 39, 35)
incorrect_data = (20, 40, 48, 61, 65)
best_names = ("Oliver", "Ben", "Beth", "Sam", "Olly")
ind = np.arange(5)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence

correct = ax.bar(ind, correct_data, width)
incorrect = ax.bar(ind, incorrect_data, width, bottom=correct_data, color='#d62728')

plt.ylabel('Average Score')
plt.title('Best Average Scores In The Past Five Games')
plt.xticks(ind, best_names)
plt.yticks(np.arange(0, 101, 10))
plt.legend((correct[0], incorrect[0]), ('Correct', 'Incorrect'))

canvas = FigureCanvasTkAgg(f, master=best_scores_frame)
canvas.show()
canvas.get_tk_widget().pack(expand=1)

root.mainloop()
