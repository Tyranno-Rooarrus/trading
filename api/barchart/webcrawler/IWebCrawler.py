# -*- coding: utf-8 -*-
import abc

from typing import Any


class IWebCrawler(abc.ABC):
    """
    """

    @abc.abstractmethod
    def crawl(self, url: str) -> Any:
        """
        """

        raise NotImplementedError
