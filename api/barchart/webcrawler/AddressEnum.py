# -*- coding: utf-8 -*-
import urllib.parse

from enum import Enum

@unique
class AddressEnum(Enum):
	"""
	"""

    # The base URL of the 'barchart' website.
    BASE_URL : str = 'https://www.barchart.com/'

	# The top 100 ETFS listed.
	ETFS_TOP_100_URL : str = urljoin(BASE_URL 'etfs-funds', 'top-100-etfs')

	# The major futures listed.
	FUTURES_FULL_LIST_URL : str = urljoin(BASE_URL, 'futures', 'major-commodities')
