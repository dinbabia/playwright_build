
import pandas as pd
from pathlib import Path

class ExcelFile:

    def __init__(self, filename) -> None:
        # Read Excel and its specific sheetname
        self._ROOT_DIR = Path(__file__).parent.parent
        self._FILE_PATH = f"{self._ROOT_DIR}\\src\\dataset\\{filename}"
        self._read_xlsx = pd.read_csv(self._FILE_PATH, )
        # Dataframe of the CSV file
        self._df = pd.DataFrame(self._read_xlsx)
        self.data = self._mapData()
     

    def _mapData(self)-> dict:
        '''
        Map the whole dataframe to convert it to a dictionary.

        return: dictionary 
        - Format:
        ------------------------------------
        {
            row_number_0 : {
                item_1 : value_1,
                item_2 : value_2
            },
            row_number_1: {
                item_1 : value_1,
                item_2 : value_2
            }
        }
        '''
        data = {}
        # Iterate each row from 0 to max row number
        for row in range(self._df.shape[0]):
            # Get the data in the row and convert it from DataFrame to Dictionary
            row_data = dict(self._df.iloc[row])
            # Iterate each item in the data
            for key, value in row_data.items():
                # Check if the data contains "|" which denotes that we will convert it to a list
                if "|" in str(value): 
                    row_data[key] = str(value).split(",")
            # Add the data in the data dictionary
            data[row] = row_data
        return data
    
    def get_specific_row(self, row_number: int):
        return self.data[row_number - 2]
   
