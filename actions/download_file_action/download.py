import pathlib
import pandas as pd
import os


class DownloadFile:
    def __init__(self, data):
        self.df = data

    def write_csv(self):
        self.df = self.df.to_csv(self.filepath, index=False, sep=',', encoding='utf-8')

    def write_excel(self):
        self.df = self.df.to_excel(self.filepath, index=False, header=True)

    def write_json(self):
        self.df = self.df.to_json(self.filepath, orient='split')

    def start(self):
        filename = input('Give name of the proceed file: ')
        path = os.path.join(os.path.abspath(os.getcwd()), 'download_files')
        extension = input('Choose from 1)csv 2)excel 3)json:\n')
        if extension == '1':
            self.filepath = os.path.join(path, filename + '.csv')
            self.write_csv()
        elif extension == '2':
            self.filepath = os.path.join(path, filename + '.xlsx')
            self.write_excel()
        elif extension == '3':
            self.filepath = os.path.join(path, filename + '.json')
            self.write_json()
        else:
            print('Please give a valid option')

        print('New path of the saved file:',self.filepath)
        return
