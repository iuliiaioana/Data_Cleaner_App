import pathlib
import pandas as pd

class UploadFile:
    def __init__(self,file):
        self.file=file
        self.df=pd.DataFrame()

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


f=UploadFile('upload_files/shootings.csv')
# file_name=input('Give the file name:')

if f.get_extension() == '.csv':
    f.read_csv()
elif f.get_extension() in ['.xls','.xlsx']:
    f.read_excel()
else:
    f.read_json()



