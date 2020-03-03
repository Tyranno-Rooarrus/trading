from typing import Dict, List

import pandas

class DownloaderHelper:
    """
    """

    API_AUTHENTICATION_KEY : str = "1yfXc81wERPmS5zpxZHq"


    @staticmethod
    def formatData(dataFrame: pandas.core.frame.DataFrame, keysToGet: List[str] = ['Open', 'High', 'Low', 'Last']):
        """        
        """

        dataFrame.fillna(method='ffill')

        formattedData = {
            'Date' : dataFrame.index.strftime("%d-%m-%Y").tolist()
        }
        

        for key in keysToGet:
            formattedData.update({
                key : dataFrame[key].tolist()
            })


        
        return formattedData
