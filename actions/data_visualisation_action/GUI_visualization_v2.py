from tkinter import *
import tkinter as tk
from tkinter import messagebox

import matplotlib.pyplot as plt
import seaborn as sns
from actions.get_data_action.get_data import Data
from actions.upload_file_action.upload_file import UploadFile
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

f = UploadFile(r'C:\Users\burag\AppData\Roaming\JetBrains\PyCharm2020.3\scratches\heart.csv')
data = Data(data_frame=f.get_data_from_file())
data_frame = data.get_data()
types = []
# for col in data_frame.columns:
#     if data_frame[col].dtype == 'object':
#         types.append('string')
#     else:
#         types.append(data_frame[col].dtype)
# OPTIONS = list(zip(data_frame.columns, types))
OPTIONS = data_frame.columns
OPTIONS2 = OPTIONS.copy()
OPTIONS3 = [
    'barplot',
    'scatterplot',
    'lineplot'
]
master = tk.Tk()
master.geometry('600x750')
variable1 = StringVar(master)
variable1.set('X axis')  # default value
w = OptionMenu(master, variable1, *OPTIONS, )
variable2 = StringVar(master)
variable2.set('Y axis')  # default value
w2 = OptionMenu(master, variable2, *OPTIONS2)

variable3 = StringVar(master)
variable3.set(OPTIONS3[0])  # default value
w3 = OptionMenu(master, variable3, *OPTIONS3)

w.pack()
w2.pack()
w3.pack()

frame = tk.Frame(master)
frame.pack()


def ok():
    ox = variable1.get()
    oy = variable2.get()
    type_plot = variable3.get()
    for widgets in frame.winfo_children():
        widgets.destroy()
    figure = plt.Figure(figsize=(6, 5), dpi=100)
    ax = figure.add_subplot(111)
    if type_plot == 'barplot':
        try:
            bar4 = FigureCanvasTkAgg(figure, master)
            bar4.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
            df4 = data_frame[[ox, oy]].groupby([ox]).size()
            df4.plot(kind='bar', x=ox, y=oy, legend=True, ax=ax)
            ax.set_title(' {} vs  {}'.format(ox, oy))
            ax.set_xlabel(ox, fontsize=10)
            ax.set_ylabel(oy, fontsize=10)
        except:
            messagebox.showinfo("Invalid action", "Can not plot")

    elif type_plot == 'scatterplot':

        try:
            scatter3 = FigureCanvasTkAgg(figure, frame)
            scatter3.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
            ax.scatter(data_frame[ox], data_frame[oy], color='g')
            ax.set_xlabel(ox, fontsize=10)
            ax.set_ylabel(oy, fontsize=10)
            ax.set_title(' {} vs  {}'.format(ox, oy))
        except:
            messagebox.showinfo("Invalid action", "Can not plot")

    elif type_plot == 'lineplot':
        try:
            line2 = FigureCanvasTkAgg(figure, master)
            line2.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
            df2 = data_frame[[ox, oy]]
            df2.plot(kind='line', legend=True, ax=ax, color='r', marker='o', fontsize=10)
            ax.set_title(' {} vs  {}'.format(ox, oy))
            ax.set_xlabel(ox, fontsize=10)
            ax.set_ylabel(oy, fontsize=10)

        except:
            messagebox.showinfo("Invalid action", "Can not plot")


button = Button(master, text="Generate plot", command=ok,
                height=5,
                width=20)
button.pack()


def _quit():
    master.quit()  # stops mainloop
    master.destroy()  # this is necessary on Windows to prevent
    # Fatal Python Error: PyEval_RestoreThread: NULL tstate


buttonq = tk.Button(master=master, text="Quit", command=_quit, bg='red',
                    height=5,
                    width=20)
buttonq.pack(side=tk.BOTTOM)

master.mainloop()
