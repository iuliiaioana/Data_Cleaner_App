from actions.get_data_action.get_data import Data


class Outliers(Data):
    def __init__(self, data_frame):
        super().__init__(data_frame)