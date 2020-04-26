import copy
import datetime

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import yfinance as yf

from concurrent.futures import ThreadPoolExecutor

from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from typing import List


class Launcher:
    """
    """

    symbols: List[str] = ['AAPL', 'AMZN', 'DIS', 'FB', 'MSFT', 'NFLX']    

    # TODO: Make Enums out of this list.
    PERIODS: List[str] = ['1d', '5d' , '1mo' , '3mo' ,' 6mo' ,' 1y' , '2y' ,' 5y' , '10y', 'ytd', 'max']

    # TODO: Make Enums out of this list.
    INTERVALS: List[str] = ['1m', '2m', '5m', '15m', '30m', '60m', '90m', '1h', '1d', '5d', '1wk', '1mo', '3mo']

    # TODO: Make Enums out of this list.
    STOCK_DATA_TYPE: List[str] = ['Adj Close', 'Close', 'High', 'Low', 'Open', 'Volume']


    def __init__(self) -> None:
        """
        Constructs a new 'Launcher' object.
        """

        # Set the plot style.
        plt.style.use('bmh')

        # Suppress 'Pandas' warnings.
        pd.set_option('mode.chained_assignment', None)

        with pd.option_context('mode.chained_assignment', None):
            self.start()


    def start(self) -> None:
        """
        Starts the actual application.
        """

        # Download the market data.
        downloadedData: pd.core.frame.DataFrame = self.__downloadMarkets()

        # Perform the market prediction.
        self.__predictMarkets(downloadedData)
        
        
    def __downloadMarkets(self, period: str = '1mo', interval: str = '1d') -> pd.core.frame.DataFrame:
        """
        Downloads all specified markets for a given period and interval.

        Arguments: 
            period (str): The stock data period to download.
            interval (str): The stock data intervals to download.

        Returns:
            pd.core.frame.DataFrame: The downloaded data from 'Yahoo Finance'.
        """

        # Check if the period is valid, otherwise use the default period instead.
        if period not in self.PERIODS:
            period = '1mo'

        # Check if the interval is valid, otherwise use the default interval instead.
        if interval not in self.INTERVALS:
            interval = '1d'

        return yf.download(tickers = ' '.join(self.symbols), period = period, interval = interval, threads = True)


    def __predictMarkets(self, downloadedData: pd.core.frame.DataFrame, stockDataType: str = 'Close') -> None:
        """
        """

        # Check if the type of the stock data is valid, otherwise use the default type of the stock data.
        if stockDataType not in self.STOCK_DATA_TYPE:
            stockDataType = 'Close'

        # Filter the market data by the relevant column.
        filteredData = downloadedData[[stockDataType]]

        # Get the amount of downloaded markets.
        marketCount = len(filteredData.columns)
        
        with ThreadPoolExecutor(marketCount) as executor:
            results = executor.map(self.__forcast, filteredData)
            
        for value in results:
            print (value)


    def __forcast(self, data):
        """
        """

        return data * 3



    def __forecastMarket(self, symbol: str, futureDaysToPredict: int = 25) -> None:
        """
        """

        # Download the data for the given ticker.
        data = yf.download(tickers = symbol, period = 'max', threads = True, )


        # Get the ticker from 'Yahoo Finance'.
        symbol: yf.ticker.Ticker = yf.Ticker(symbol)

        # Get the data for the given ticker.
        data: pd.core.frame.DataFrame = symbol.history(period = '40000d')

        # Get the 'Closing' prices.
        closingData: pd.core.frame.DataFrame = data[['Close']]                        

        # Create a new column (Target) shifted 'x' days up.
        closingData['Prediction'] = copy.deepcopy(closingData[['Close']].shift(-futureDays))

        # Create the future dataset and convert it to a numpy array and remove the last 'x' days to
        # predict.
        forecastX = np.array(closingData.drop(['Prediction'], 1))[:-futureDays]
        forecastY = np.array(closingData['Prediction'])[:-futureDays]

        errors = {}

        for n in range(5, 95):            

            # Create train and test datasets.
            xTrain, xTest, yTrain, yTest = train_test_split(forecastX, forecastY, test_size = n / 100)
            
            # Create a decision tree regressor and create decision tree model.
            regressor = DecisionTreeRegressor().fit(xTrain, yTrain)

            # Get the last 'x' days of the future dataset.
            xFuture = closingData.drop(['Prediction'], 1)[:-futureDays]
            xFuture = xFuture.tail(futureDays)
            xFuture = np.array(xFuture)

            # Predict the closing prices.
            predictions = regressor.predict(xFuture)

            validation = closingData[forecastX.shape[0]:]
            validation['Predictions'] = predictions
                
            mse = mean_squared_error(validation['Predictions'], validation['Close'])

            errors.update({n : mse})
    
        x = ''
        for k, v in errors.items():
            x += str(int(v)) + ' '
            if k % 94 == 0:
                self.showPlot(closingData, validation, symbol)

        print (symbol, ':', x, '\n')


    def showPlot(self, df, valid, symbol):
        plt.figure(figsize = (16, 8))
        plt.title('Model ' + str(symbol))
        plt.xlabel('Days')
        plt.ylabel('Close Price USD ($)')
        plt.plot(df['Close'][-80:])
        plt.plot(valid[['Close']], color='orange')
        plt.plot(valid[['Predictions']], color='green', linestyle='dashed', linewidth=1)
        plt.legend(['Original', 'Validation', 'Predicted'])
        plt.show()

if __name__ == '__main__':
    Launcher()
