from actions.get_data_action.get_data import Data


class FillNa(Data):
    def __init__(self, data_frame):
        super().__init__(data_frame)

    def fillna_spefic_value(self, value, column):
        self.data[column].fillna(value, inplace=True)
        return self.data.head()

    def fillna_average(self, column):
        self.data[column].fillna(self.data[column].mean(), inplace=True)
        return self.data.head(10)

    def fillna_median(self, column):
        self.data[column].fillna(self.data[column].median(), inplace=True)
        return self.data[column].head()

    def fillna_forword_fill(self, column):
        self.data[column].ffill(inplace=True)
        return self.data.head(10)

    def fill_backwords_fill(self, column):
        self.data[column].bfill(inplace=True)
        return self.data.head(10)

    def process(self):
        i = ''
        switcher = {
            '1': self.fillna_spefic_value,
            '2': self.fillna_average,
            '3': self.fillna_median,
            '4': self.fillna_forword_fill,
            '5': self.fill_backwords_fill,
        }
        while i != 'o':
            with open("menu_templates/fill_na.txt") as a_file:
                lines = a_file.readlines()
                for line in lines:
                    print(line)
            i = input('Select operation: ')
            if i == '1':
                value = input('Select value to fill in: ')
                column = input('Select column name: ')
                for v in column.split(','):
                    print(switcher[i](int(value), v))
            elif i != 'o':
                column = input('Select column name: ')
                print(switcher[i](column))
            else:
                print('Please, give a valid action')
        return
