# -*- coding: utf-8 -*-
import requests

import bs4
import lxml

from typing import Any, cast, List


class BaseSymbolCrawlerImpl(IWebCrawler):
    """
    """


    def __init__(self, url: str) -> None:
        """
        """

        self.__url = url


    def retrieveSymbols(self) -> List[str]:
        """
        """

        return cast(List[str], self.crawl())


    def crawl(self) -> Any:
        """
        """

        # Get the requested URL.
        request = self.__getRequest()

        soup = bs4.BeautfulSoup(request.text, 'lxml')






    def __getRequest(self) -> None:
        """
        """

        return requests.get(self.__url)
