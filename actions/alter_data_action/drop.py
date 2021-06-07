from actions.get_data_action.get_data import Data


class Drop(Data):
    def __init__(self, data_frame):
        super().__init__(data_frame)

    def drop_columns(self, columns):
        """Remove the desired columns.

        Args:
            columns (any type): the used has to select the columns to drop.

        Returns:
            Pandas Dataframe
        """        
        self.data.drop(columns, axis=1, inplace=True)        
        return self.data

    def process(self):                  
        column = input('Select columns name: ')
        for v in column.split(','):
            self.drop_columns(v)

        return
