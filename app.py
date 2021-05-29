import pandas as pd

from actions.alter_data_action.alter_data import AlterData
from actions.alter_data_action.drop import Drop
from actions.alter_data_action.duplicate import Duplicate
from actions.alter_data_action.fill_na import FillNa
from actions.alter_data_action.outliers import Outliers
from actions.data_visualisation_action.data_visualisation import DataVisualisation
from actions.get_data_action.get_data import Data
from actions.upload_file_action.upload_file import UploadFile

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

if __name__ == '__main__':
    f = UploadFile('fisiereDeUpload/shootings.csv')
    data = Data(data_frame=f.get_data_from_file())
    data_frame = data.get_data()

    # data_visualisation = DataVisualisation(data_frame)
    # data_visualisation.start_visualisation()

    # test_f1 = FillNa(data_frame)
    # print(test_f1.fill_backwords_fill('age'))

    # test_duplicate = Duplicate(data_frame)
    # # print(test_duplicate.duplicate_columns_selection('name'))1
    # print(test_duplicate.duplicate_columns_selection_last('name'))

    # test_drop = Drop(data_frame)
    # print(test_drop.drop_columns('age'))

    test_outlier= Outliers(data_frame)
    # print(test_outlier.delete_outliers_zscore(['age']))
    # print(test_outlier.delete_outliers_interquartile(['age']))
    print(test_outlier.replace_ouliers_interquartile(['age']))

    # print()
    # d=DataVisualisation(data_frame)
    # d.get_info()
    test_alterdata=AlterData(data_frame)
    test_alterdata.start()

