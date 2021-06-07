from actions.get_data_action.get_data import Data


class DropNA(Data):
    def __init__(self, data_frame):
        super().__init__(data_frame)

    def drop_na(self):
        """Drop the rows where NA values exists.

        Returns:
            Pandas Dataframe
        """        
        self.data.dropna(inplace=True)
        return self.data

    def process(self):
        self.drop_na()
        return
