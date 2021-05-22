from actions.get_data_action.get_data import Data


class FillNa(Data):
    def __init__(self, data_frame):
        super().__init__(data_frame)

    def fillna_spefic_value(self, value, column):
        self.data[column].fillna(value, inplace=True)
        return self.data.head()

    def fillna_average(self, column):
        self.data[column].fillna(self.data[column].mean(), inplace=True)
        return self.data[column].head(10)

    def fillna_median(self, column):
        self.data[column].fillna(self.data[column].median(), inplace=True)
        return self.data[column].head()

    def fillna_forword_fill(self, column):
        self.data[column].ffill(inplace=True)
        return self.data.head(10)

    def fill_backwords_fill(self, column):
        self.data[column].bfill(inplace=True)
        return self.data.head(10)
