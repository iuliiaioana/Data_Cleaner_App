import sys

from scipy.stats import stats
from actions.get_data_action.get_data import Data
import numpy as np

np.set_printoptions(threshold=sys.maxsize)


class Outliers(Data):
    def __init__(self, data_frame):
        super().__init__(data_frame)

    def replace_outliers_zscore(self):
        """
        Replace outliers with median/mean in order to keep date for further analysis
        """
        pass

    def delete_outliers_zscore(self, columns):
        """
        Delete outliers
        """
        # z_scores = stats.zscore(self.data.select_dtypes(include=['int64','float64']))
        # z_scores = stats.zscore(self.data['age'])
        # abs_z_scores = np.abs(z_scores)
        # print(abs_z_scores)
        # filtered_entries = (abs_z_scores < 1).all()
        # print(filtered_entries)
        # self.data = self.data[filtered_entries]
        df = self.data.select_dtypes(include=['float64'])
        self.data = self.data[(np.abs(stats.zscore(df['age'])) < 3).all()]
        return self.data.head(10)

    def replace_ouliers_interquartile(self, columns):
        """
            replace ?
            v1: media de la toate date
            v2: media de la outliere ----------kick
            v3: media de la cele care nu s outliere
              conditie ?
            v4: median datasetului

            TODO: daca vrem sa adaugam la if si nan
        """
        for column in columns:
            q_low = self.data[column].quantile(0.25)
            q_hi = self.data[column].quantile(0.75)
            iqr = q_hi - q_low
            df_without_outlier = self.data[
                (self.data[column] < (q_hi + 1.5 * iqr)) & (self.data[column] > (q_low - 1.5 * iqr))]
            mean_of_non_outliers = df_without_outlier.mean()
            index = self.data.columns.get_loc(column)
            for d in range(len(self.data[column])):
                if not (self.data.iloc[d, index] < (q_hi + 1.5 * iqr)) and (
                        self.data.iloc[d, index] > (q_low - 1.5 * iqr)):
                    self.data.loc[d, column] = mean_of_non_outliers[column]
        return self.data.head(10)

    def delete_outliers_interquartile(self, columns):
        """
        Delete outliers

        """
        for column in columns:
            q_low = self.data[column].quantile(0.25)
            q_hi = self.data[column].quantile(0.75)
            iqr = q_hi - q_low
            self.data = self.data[(self.data[column] < (q_hi + 1.5 * iqr)) & (self.data[column] > (q_low - 1.5 * iqr))]

        return self.data.head(10)

    def process(self):
        i = ''
        switcher = {
            '1': self.delete_outliers_zscore,
            '2': self.replace_outliers_zscore,
            '3': self.delete_outliers_interquartile,
            '4': self.replace_ouliers_interquartile
        }
        while i != 'o':
            with open("menu_templates/outliers.txt") as a_file:
                lines = a_file.readlines()
                for line in lines:
                    print(line)
            i = input('Select operation: ')
            if i == '1' or i == '2' or i == '3' or i == '4':
                columns = input('Select columns name: ')
                print(switcher[i](columns))
            else:
                print('Please, give a valid action')

        return
