import pathlib
import pandas as pd


class UploadFile:
    def __init__(self, file):
        self.file = file
        self.df = pd.DataFrame()

    def get_extension(self):
        return pathlib.Path(self.file).suffix

    def read_csv(self):
        self.df = pd.read_csv(self.file)

    def read_excel(self):
        self.df = pd.read_excel(self.file)

    def read_json(self):
        self.df = pd.read_json(self.file)

    def get_dataframe(self):
        return self.df

    def get_data_from_file(self):
        if self.get_extension() == '.csv':
            self.read_csv()
        elif self.get_extension() in ['.xls', '.xlsx']:
            self.read_excel()
        else:
            self.read_json()

        return self.df

