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

