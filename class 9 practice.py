import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.stattools import adfuller

# Downloading stock prices data
symbols = ['AAPL', 'MSFT', 'GOOGL', 'AMZN']
start_date = '2010-01-01'
end_date = '2022-01-01'

# We will store the closing prices of each stock in this dictionary
stock_data = {}

# Fetch the data for each stock and store it in the dictionary
for symbol in symbols:
    data = yf.download(symbol, start=start_date, end=end_date)
    stock_data[symbol] = data['Close']

# Function to test and ensure the time series data is stationary
def test_stationarity(timeseries):
    print('Results of Dickey-Fuller Test:')
    dftest = adfuller(timeseries.dropna(), autolag='AIC')
    dfoutput = pd.Series(dftest[0:4], index=['Test Statistic', 'p-value', '#Lags Used', 'Number of Observations Used'])
    for key, value in dftest[4].items():
        dfoutput['Critical Value (%s)' % key] = value
    print(dfoutput)

# Iterate over each stock symbol and perform analysis
for symbol, close_prices in stock_data.items():
    print(f"\nPerforming Time Series Analysis for {symbol}")

    # Step 1: Test for stationarity
    print("\nTesting for Stationarity")
    test_stationarity(close_prices)

    # If not stationary, perform differencing (we assume first-order differencing makes it stationary)
    # In a real analysis, you might need to do this multiple times or perform other transformations based on the Dickey-Fuller test results.
    diff = close_prices.diff().dropna()
    
    # Test for stationarity again
    print("\nTesting for Stationarity after differencing")
    test_stationarity(diff)

    # Step 2: Fit the ARIMA model
    # Note: The parameters (1, 1, 1) here are example values. In a thorough analysis, you'd use the ACF and PACF plots to determine these.
    model = ARIMA(close_prices, order=(1, 1, 1))
    results = model.fit()

    # Step 3: Plot the original time series and the forecasted series
    plt.figure(figsize=(12, 6))
    plt.plot(close_prices, label='Original')
    plt.plot(results.fittedvalues, color='red', label='Fitted Values')
    plt.title(f'ARIMA Model Results for {symbol}')
    plt.legend()
    plt.show()

    # Step 4: Predicting future values (We predict for the next 30 days here)
    forecast = results.get_forecast(steps=30)
    predicted_mean = forecast.predicted_mean
    confidence_intervals = forecast.conf_int()

    # Plotting the forecast along with confidence intervals
    plt.figure(figsize=(12, 6))
    plt.plot(close_prices.index, close_prices, label='Original')
    plt.plot(predicted_mean.index, predicted_mean, color='red', label='Forecast')
    plt.fill_between(confidence_intervals.index,
                     confidence_intervals.iloc[:, 0],
                     confidence_intervals.iloc[:, 1], color='pink')
    plt.title(f'Forecasted Stock Prices for {symbol}')
    plt.legend()
    plt.show()

    print("\n-----------------------------------------------\n")

