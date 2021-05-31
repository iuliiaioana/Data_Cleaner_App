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

        return self.data.head()

    def change_to_lower(self):
        for column in self.data.columns:
            if self.data[column].dtype == 'object':
                self.data[column] = self.data[column].str.lower()

        return self.data.head()

    def change_to_proper(self):
        for column in self.data.columns:
            if self.data[column].dtype == 'object':
                self.data[column] = self.data[column].str.capitalize()

        return self.data.head()

    def find_and_replace(self):
        pass

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
                find = input('Find: ')
                replace = input('Replace with: ')
                print(switcher[i](find, replace))
            elif i == '2' or i == '3' or i == '4' or i == '1':
                print(switcher[i]())
            elif i != 'o':
                print('Please, give a valid action')
        return
