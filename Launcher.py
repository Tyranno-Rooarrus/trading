import pandas

from api.quandl.helper.DownloaderHelper import DownloaderHelper
from api.quandl.PriceDownloader import PriceDownloader


class Launcher:
    """
    """


    def __init__(self) -> None:
        """
        """

        self.start()


    def start(self) -> None:
        """
        """

        gcPrice = PriceDownloader('CHRIS/CME_GC1')

        print (gcPrice)



if __name__ == '__main__':
    Launcher()
