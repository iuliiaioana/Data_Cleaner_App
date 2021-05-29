from actions.alter_data_action.drop import Drop
from actions.alter_data_action.duplicate import Duplicate
from actions.alter_data_action.fill_na import FillNa
from actions.alter_data_action.outliers import Outliers
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
        elif actiontype == '5':
            return Outliers(self.data)

    def start(self):
        i = ''
        while i != '7':
            with open("menu_templates/alter_data.txt") as a_file:
                lines = a_file.readlines()
                for line in lines:
                    print(line)
            i = input('Select operation: ')
            if i == '1' or i == '2' or i == '3' or i == '5':
                self.procesor(i).process()
            elif i != '7' :
                print('Please, give a valid process')
        return
