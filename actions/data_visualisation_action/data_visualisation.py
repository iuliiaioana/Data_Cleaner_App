import pandas as pd
from tkinter import *
import tkinter as tk
from tkinter import messagebox

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from actions.alter_data_action.alter_data import *
from actions.get_data_action.get_data import Data
from actions.upload_file_action.upload_file import UploadFile
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure


class DataVisualisation:
    def __init__(self, data):
        self.data = pd.DataFrame(data)

    def get_head(self):
        return self.data.head()

    def get_info(self):
        return self.data.info()

    def get_describe(self):
        return self.data.describe()

    def get_unique_col(self, col):
        print(', '.join(map(str, self.data[col].unique())))

    def get_unique_all(self):
        for col in self.data.columns:
            unique_vals = self.data[col].unique()
            print(
                "{}: {}".format(
                    col,
                    ', '.join(map(str, unique_vals))
                )
            )

    def get_nunique(self):
        return self.data.nunique()

    def get_confirmation(self):
        from actions.alter_data_action.alter_data import AlterData
        new = AlterData(self.data)
        new.start()
        return

    def get_gui(self):
        lista_coloane = []
        for i in self.data.columns:
            lista_coloane.append(i)

        # print(lista_coloane)
        OPTIONS = lista_coloane

        OPTIONS2 = lista_coloane

        OPTIONS3 = [
            'barplot',
            'scatterplot',
            'lineplot'
        ]
        master = tk.Tk()
        # master.geometry("750x250")
        variable1 = StringVar(master)
        variable1.set(OPTIONS[1])  # default value
        w = OptionMenu(master, variable1, *OPTIONS)

        variable2 = StringVar(master)
        variable2.set(OPTIONS2[2])  # default value
        w2 = OptionMenu(master, variable2, *OPTIONS2)

        variable3 = StringVar(master)
        variable3.set(OPTIONS3[0])  # default value
        w3 = OptionMenu(master, variable3, *OPTIONS3)

        w.pack()
        w2.pack()
        w3.pack()

        def ok():
            # print("value1 is:" + variable1.get())
            ox = variable1.get()
            # print("value2 is:" + variable2.get())
            oy = variable2.get()
            type_plot = variable3.get()
            figure = plt.Figure(figsize=(6, 5), dpi=100)
            if type_plot == 'barplot':
                try:
                    # figure = plt.Figure(figsize=(6, 5), dpi=100)
                    ax = figure.add_subplot(111)
                    bar4 = FigureCanvasTkAgg(figure, master)
                    bar4.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
                    df4 = self.data[[ox, oy]].groupby(ox).sum()
                    df4.plot(kind='bar', legend=True, ax=ax)
                    ax.set_title(' {} vs  {}'.format(ox, oy))
                    ax.set_xlabel(ox, fontsize=10)
                    ax.set_ylabel(oy, fontsize=10)
                    # #
                    # canvas = FigureCanvasTkAgg(figure, master)  # A tk.DrawingArea.
                    # canvas.draw()
                    # canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
                    #
                    # toolbar = NavigationToolbar2Tk(canvas, master)
                    # toolbar.update()
                    # canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
                    #
                    # def on_key_press(event):
                    #     print("you pressed {}".format(event.key))
                    #     key_press_handler(event)
                    #
                    # bar4.mpl_connect("key_press_event", on_key_press)
                    #
                    # def _quit2():
                    #     # master.quit()  # stops mainloop
                    #     master.detele(bar4)  # this is necessary on Windows to prevent
                    #     # Fatal Python Error: PyEval_RestoreThread: NULL tstate
                    #
                    # buttonqq = tk.Button(master=master, text="Delete plot", command=_quit2, bg='red')
                    # buttonqq.pack(side=tk.BOTTOM)



                except:
                    messagebox.showinfo("Invalid action", "Can not plot")

            elif type_plot == 'scatterplot':

                try:
                    # figure = plt.Figure(figsize=(6, 5), dpi=100)
                    ax = figure.add_subplot(111)
                    ax.scatter(self.data[ox], self.data[oy], color='g')
                    scatter3 = FigureCanvasTkAgg(figure, master)
                    scatter3.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
                    # ax3.legend(['Stock_Index_Price'])
                    ax.set_xlabel(ox, fontsize=10)
                    ax.set_ylabel(oy, fontsize=10)
                    ax.set_title(' {} vs  {}'.format(ox, oy))

                except:
                    messagebox.showinfo("Invalid action", "Can not plot")

            elif type_plot == 'lineplot':
                try:
                    # figure = plt.Figure(figsize=(6, 5), dpi=100)
                    ax = figure.add_subplot(111)
                    line2 = FigureCanvasTkAgg(figure, master)
                    line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
                    df2 = self.data[[ox, oy]].groupby(ox).sum()
                    df2.plot(kind='line', legend=True, ax=ax, color='r', marker='o', fontsize=10)
                    ax.set_title(' {} vs  {}'.format(ox, oy))
                    ax.set_xlabel(ox, fontsize=10)
                    ax.set_ylabel(oy, fontsize=10)

                    # canvas = FigureCanvasTkAgg(figure, master)  # A tk.DrawingArea.
                    # canvas.draw()
                    # canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
                    #
                    # toolbar = NavigationToolbar2Tk(canvas, master)
                    # toolbar.update()
                    # canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

                except:
                    messagebox.showinfo("Invalid action", "Can not plot")

        button = Button(master, text="Generate plot", command=ok)
        button.pack()

        def _quit():
            master.quit()  # stops mainloop
            master.destroy()  # this is necessary on Windows to prevent
            # Fatal Python Error: PyEval_RestoreThread: NULL tstate

        buttonq = tk.Button(master=master, text="Quit", command=_quit, bg='red')
        buttonq.pack(side=tk.BOTTOM)

        master.mainloop()

    def start_visualisation(self):
        i = ''
        switcher = {
            '1': self.get_head,
            '2': self.get_info,
            '3': self.get_describe,
            '4': self.get_unique_all,
            '5': self.get_unique_col,
            '6': self.get_nunique,
            '7': self.get_confirmation,
            '8': self.get_gui
        }
        while i != '7':
            with open("menu_templates/validation.txt") as a_file:
                lines = a_file.readlines()
                for line in lines:
                    print(line)
            i = input('Select operation: ')
            if i == '5':
                column = input('Select column name: ')
                for v in column.split(','):
                    print(f'Column {v} with unique values: {switcher[i](v)}')
            elif i in '1234678':
                print(switcher[i]())
            elif i != '7':
                print('Please, give a valid action')

        return
