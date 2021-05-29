from actions.get_data_action.get_data import Data


class Duplicate(Data):
    def __init__(self, data_frame):
        super().__init__(data_frame)

    def duplicate_columns_all(self):
        self.data = self.data[~self.data.duplicated()]
        return self.data.head(10)

    def duplicate_columns_selection(self, columns):
        """
          By default, the first occurrence is kept, the others are dropped.
        """
        self.data = self.data.drop_duplicates(subset=columns)
        return self.data.head(10)

    def duplicate_columns_selection_last(self, columns):
        self.data = self.data.drop_duplicates(subset=columns, keep='last')
        return self.data.head(10)

    def process(self):
        i = ''
        switcher = {
            '1': self.duplicate_columns_all,
            '2': self.duplicate_columns_selection,
            '3': self.duplicate_columns_selection_last
        }
        while i != 'o':
            with open("menu_templates/duplicate.txt") as a_file:
                lines = a_file.readlines()
                for line in lines:
                    print(line)
            i = input('Select operation: ')
            if i == '2' or i == '3':
                column = input('Select columns name: ')
                for v in column.split(','):
                    print(switcher[i](v))
            elif i == '1':
                print(switcher[i]())
            else:
                print('Please, give a valid action')
        return
