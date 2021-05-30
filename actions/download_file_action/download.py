import pathlib
import pandas as pd
import os


class DownloadFile:
    def __init__(self, data):
        self.filepath = ''
        self.df = data

    def write_csv(self):
        self.df = self.df.to_csv(self.filepath, index=False, sep=',', encoding='utf-8')

    def write_excel(self):
        self.df = self.df.to_excel(self.filepath, index=False, header=True)

    def write_json(self):
        self.df = self.df.to_json(self.filepath, orient='split')

    def start(self):
        filename = input('Give name of the proceed file:')
        path = os.path.abspath(os.getcwd())
        path += "\\fisiereDownload\\"
        print(path)
        extension = input('Choose from 1)csv 2)excel 3)json')
        if extension == '1':
            self.filepath = path + filename + '.csv'
            self.write_csv()
        elif extension == '2':
            self.filepath = path + filename + '.xlsx'
            self.write_excel()
        elif extension == '3':
            self.filepath = path + filename + '.json'
            self.write_json()
        else:
            print('Please give a valid option')
