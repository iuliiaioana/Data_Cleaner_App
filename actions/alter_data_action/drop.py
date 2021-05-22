from actions.get_data_action.get_data import Data


class Drop(Data):
    def __init__(self, data_frame):
        super().__init__(data_frame)

    def drop_columns(self, columns):
        self.data.drop(columns, axis=1, inplace=True)
        return self.data.head(10)