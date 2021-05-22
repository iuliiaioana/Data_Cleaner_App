from actions.get_data_action.get_data import Data


class Duplicate(Data):
    def __init__(self, data_frame):
        super().__init__(data_frame)

    def duplicate_columns_all(self):
        self.data=self.data[~self.data.duplicated()]
        return self.data.head(10)

    def duplicate_columns_selection(self,columns):
        """
          Default selection keep the first
        """
        self.data=self.data.drop_duplicates(subset=columns)
        return self.data.head(10)

    def duplicate_columns_selection_last(self,columns):
        self.data=self.data.drop_duplicates(subset=columns, keep='last')
        return self.data.head(10)
