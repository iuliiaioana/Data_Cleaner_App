from actions.alter_data_action.drop import Drop
from actions.alter_data_action.dropNA import DropNA
from actions.alter_data_action.duplicate import Duplicate
from actions.alter_data_action.fill_na import FillNa
from actions.alter_data_action.format import Format
from actions.alter_data_action.outliers import Outliers
from actions.data_visualisation_action.data_visualisation import *
from actions.get_data_action.get_data import Data


class AlterData(Data):
    def __init__(self, data_frame):
        super().__init__(data_frame)

    def procesor(self, actiontype):
        if actiontype == '1':
            return FillNa(self.data)
        elif actiontype == '2':
            return Duplicate(self.data)
        elif actiontype == '3':
            return Drop(self.data)
        elif actiontype == '4':
            return DropNA(self.data)
        elif actiontype == '5':
            return Outliers(self.data)
        elif actiontype == '6':
            return Format(self.data)

    def start(self):
        i = ''
        while i != 'o':
            with open("menu_templates/alter_data.txt") as a_file:
                lines = a_file.readlines()
                for line in lines:
                    print(line)
            i = input('Select operation: ')
            if i in ['1', '2', '3', '4', '5', '6']:
                self.procesor(i).process()
            elif i == '8':
                from actions.data_visualisation_action.data_visualisation import DataVisualisation
                new = DataVisualisation(self.data)
                new.start_visualisation()
            elif i == '7':
                from actions.download_file_action.download import DownloadFile
                test_download = DownloadFile(self.data)
                test_download.start()
            elif i != 'o':
                print('Please, give a valid process')
        return
