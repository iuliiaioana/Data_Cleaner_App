import pandas as pd


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
        return self.data[col].unique()

    def get_unique_all(self, d=dict()):
        for col in self.data.columns:
            d[col] = list(self.data[col].unique())
        return d

    def get_nunique(self):
        return self.data.nunique()

    def get_confirmation(self):
        print('Go to alter data')
        """
        //TODO: GO TO ALTER DATA MENIU 
        """

    def start_visualisation(self):
        i = ''
        switcher = {
            '1': self.get_head,
            '2': self.get_info,
            '3': self.get_describe,
            '4': self.get_unique_all,
            '5': self.get_unique_col,
            '6': self.get_nunique,
            '7': self.get_confirmation
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
            else:
                print(switcher[i]())
