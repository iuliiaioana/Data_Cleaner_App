from uploadFile import f
import pandas as pd
import numpy as np
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

class Data():
    def __init__(self):
        self.data=f.get_dataframe()

class FillNa(Data):
    def __init__(self):
        super().__init__()

    def fillna_spefic_value(self, value,column):
        self.data[column].fillna(value, inplace=True)
        return self.data.head()

    def fillna_average(self,column):
        self.data[column].fillna(self.data[column].mean(),inplace=True)
        return self.data.head()

    def fillna_median(self,column):
        self.data[column].fillna(self.data[column].median(), inplace=True)
        return self.data.head()

    def fillna_forword_fill(self,column):
        self.data[column].ffill( inplace=True)
        return self.data.head(10)

    def fill_backwords_fill(self,column):
        self.data[column].bfill(inplace=True)
        return self.data.head(10)


class Duplicate(Data):
    def __init__(self, data):
        super().__init__(data)


class Drop(Data):
    def __init__(self, data):
        super().__init__(data)

class Outliers(Data):
    def __init__(self, data):
        super().__init__(data)

class Format(Data):
    def __init__(self, data):
        super().__init__(data)



class AlterData():
    def __init__(self):
        super()




if __name__ == '__main__':

    dd = f.get_dataframe()
    # pas3=AlterData(dd)
    # pas3.incercare()
    # with open("fisiereText/AlterData.txt") as a_file:
    #     lines = a_file.readlines()
    #     for line in lines:
    #         print(line)
    test_f1=FillNa()
    print(test_f1.fill_backwords_fill('age'))




