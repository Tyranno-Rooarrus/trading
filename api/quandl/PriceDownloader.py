import pandas

import quandl

from api.quandl.base.IDownloader import IDownloader
from api.quandl.helper.DownloaderHelper import DownloaderHelper

class PriceDownloader(IDownloader):
    """
    """

    def __init__(self, tickerName: str, startDate: str = '2008-01-01', frequency: str = "monthly") -> None:
        """
        """        
        
        quandl.ApiConfig.api_key = DownloaderHelper.API_AUTHENTICATION_KEY

        self.__tickerName = tickerName
        self.__startDate = startDate
        self.__frequency = frequency


    # Override
    def download(self) -> pandas.core.frame.DataFrame:
        """
        """

        return quandl.get(self.__tickerName, start_date = self.__startDate, collapse = self.__frequency)
