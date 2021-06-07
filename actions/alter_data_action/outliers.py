import sys
import pandas as pd
from scipy.stats import stats
from actions.get_data_action.get_data import Data
import numpy as np

np.set_printoptions(threshold=sys.maxsize)


class Outliers(Data):
    def __init__(self, data_frame):
        super().__init__(data_frame)

    def replace_outliers_zscore(self):
        """Replace outliers with median/mean in order to keep
        data for further analysis.
        Returns:
            Pandas DataFrame.
        """
        new_data = self.data
        for column in new_data.columns:
            try:
                if new_data[column].dtype in ['int64', 'float64']:
                    new_data = new_data[np.abs(stats.zscore(new_data[column])) < 3]
                for column in self.data.columns:
                    if self.data[column].dtype in ['int64', 'float64']:
                        z_scores = np.abs(stats.zscore(self.data[column]))
                        for i, item in enumerate(z_scores):
                            if np.abs(item) > 3:
                                self.data.loc[i, column] = new_data[column].mean()
            except:
                print('No able to Replace')

            return self.data


    def delete_outliers_zscore(self):
        """Delete all outliers from every column in the data set.
        
        Returns:
            Pandas DataFrame.

        """
        for column in self.data.columns:
            if self.data[column].dtype in ['int64', 'float64']:
                try:
                    self.data = self.data[np.abs(stats.zscore(self.data[column])) < 3]
                except:
                    print('Invalid DELETE')
        return self.data

    def replace_ouliers_interquartile(self):
        """Replaces the outliers with the mean of remaining values.
        
        Returns:
            Pandas DataFrame.
        """
        for column in self.data.columns:
            if self.data[column].dtype in ['int64', 'float64']:
                try:
                    q_low = self.data[column].quantile(0.05)
                    q_hi = self.data[column].quantile(0.95)
                    iqr = q_hi - q_low
                    df_without_outlier = self.data[
                        (self.data[column] < (q_hi + 1.5 * iqr)) &
                        (self.data[column] > (q_low - 1.5 * iqr))
                    ]
                    mean_of_non_outliers = df_without_outlier.mean()
                    index = self.data.columns.get_loc(column)
                    for d in range(len(self.data[column])):
                        if not (self.data.iloc[d, index] < (q_hi + 1.5 * iqr)) and\
                                (self.data.iloc[d, index] > (q_low - 1.5 * iqr)) or pd.isna(self.data.iloc[d, index]):
                            self.data.loc[d, column] = mean_of_non_outliers[column]
                except:
                    print('No outliers for Replace')
        return self.data

    def delete_outliers_interquartile(self):
        """
        Delete the rows from the dataframe where outliers appears.

        Returns:
            Pandas DataFrame.
        """
        for column in self.data.columns:
            if self.data[column].dtype in ['int64', 'float64']:
                q_low = self.data[column].quantile(0.05)
                q_hi = self.data[column].quantile(0.95)
                iqr = q_hi - q_low
                self.data = self.data[(self.data[column] < q_hi + 1.5 * iqr) & (self.data[column] > q_low - 1.5 * iqr)]
        return self.data


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
                print(switcher[i]())
            elif i != 'o':
                print('Please, give a valid action')
        return
