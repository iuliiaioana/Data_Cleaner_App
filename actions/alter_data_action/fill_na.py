from actions.get_data_action.get_data import Data


class FillNa(Data):
    def __init__(self, data_frame):
        super().__init__(data_frame)

    def fillna_spefic_value(self, value, column):
        """Replace NA values with the input of the user.

        Args:
            value (int, float,str,bool): the value from the user.
            column (int64,float64, object, category): the column where the fill process occurs.
        """        
        self.data[column].fillna(value, inplace=True)

    def fillna_average(self, column):
        """Replace NA values with the mean of the column.

        Args:
            column (int64,float64, object, category): the column where the fill process occurs.
        """        
        self.data[column].fillna(self.data[column].mean(), inplace=True)

    def fillna_median(self, column):
        """Replace NA values with the median of the column.

        Args:
            column (int64,float64, object, category): the column where the fill process occurs.
        """        
        self.data[column].fillna(self.data[column].median(), inplace=True)

    def fillna_forword_fill(self, column):
        """Replace NA values with the next available value in the column.

        Args:
            column (int64,float64, object, category): the column where the fill process occurs.
        """        
        self.data[column].ffill(inplace=True)

    def fill_backwords_fill(self, column):
        """Replace NA values with the previous value from the column.

        Args:
            column (int64,float64, object, category): the column where the fill process occurs.
        """        
        self.data[column].bfill(inplace=True)

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
            elif i in ['2', '3', '4', '5']:
                column = input('Select column name: ')
                print(switcher[i](column))
            elif i != 'o':
                print('Please, give a valid action')
        return
