import abc

import pandas.core

class IDownloader(abc.ABC):
    """
    """

    @abc.abstractmethod
    def download(self) -> pandas.core.frame.DataFrame:
        """
        """

        raise NotImplementError
