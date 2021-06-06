from actions.get_data_action.get_data import Data


class Format(Data):
    def __init__(self, data_frame):
        super().__init__(data_frame)

    def change_dtype(self):
        for column in self.data.columns:
            if self.data[column].dtype == 'object':
                if self.data[column].nunique() < 10:
                    self.data[column] = self.data[column].astype('category')
                else:
                    self.data[column] = self.data[column].astype('str')

        return self.data

    def change_to_upper(self):
        for column in self.data.columns:
            if self.data[column].dtype == 'object':
                self.data[column] = self.data[column].str.upper()

        return self.data

    def change_to_lower(self):
        for column in self.data.columns:
            if self.data[column].dtype == 'object':
                self.data[column] = self.data[column].str.lower()

        return self.data

    def change_to_proper(self):
        for column in self.data.columns:
            if self.data[column].dtype == 'object':
                self.data[column] = self.data[column].str.capitalize()

        return self.data

    def find_and_replace(self):
        print('Chose one from the columns:', *self.data.columns)
        column = input('Chose in what column you want to replace the value ')
        while column not in self.data.columns:
            column = input('Chose a valid column you want to replace the value ')
        value_to_find = input('What value you want to find ')
        while value_to_find not in self.data[column].unique():
            value_to_find = input('A valid value you want to find ')
        value_to_replace = input('With what value you want to replace ')
        self.data.replace({column:{value_to_find:value_to_replace}},inplace = True)
        return self.data

    def process(self):
        i = ''
        switcher = {
            '1': self.change_dtype,
            '2': self.change_to_upper,
            '3': self.change_to_lower,
            '4': self.change_to_proper,
            '5': self.find_and_replace,
        }
        while i != 'o':
            with open("menu_templates/format.txt") as a_file:
                lines = a_file.readlines()
                for line in lines:
                    print(line)
            i = input('Select operation: ')
            if i == '5':
                print(switcher[i]())
            elif i == '2' or i == '3' or i == '4' or i == '1':
                print(switcher[i]())
            elif i != 'o':
                print('Please, give a valid action')
        return
