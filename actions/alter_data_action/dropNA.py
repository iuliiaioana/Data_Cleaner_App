from actions.get_data_action.get_data import Data


class DropNA(Data):
    def __init__(self, data_frame):
        super().__init__(data_frame)

    def drop_na(self):
        self.data.dropna(inplace=True)
        return self.data.head(10)

    def process(self):
        self.drop_na()
        return
