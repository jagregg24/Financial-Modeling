import yfinance as yf
import matplotlib.pyplot as plt

# Define the ticker symbol and timeframe you want to fetch data for
tickerSymbol = 'MUSA'  # for MUSA, for example
timeframe = "1y"  # 1 year of data

# Fetch the data
tickerData = yf.Ticker(tickerSymbol)
stock_data = tickerData.history(period=timeframe)

# Create a figure and a plot
plt.figure(figsize=(14, 7))  # width:14 inches, height:7 inches

# Plot the close prices, and you can choose to plot other data like open, high, low prices
plt.plot(stock_data.index, stock_data['Close'], label=f"{tickerSymbol} Stock Close Price", color='blue')

# Customize the appearance and annotations
plt.title(f"{tickerSymbol} Stock Price Over the Last Year")
plt.xlabel("Date")
plt.ylabel("Close Price (in USD)")
plt.legend()
plt.grid(True)  # Adding a grid for better readability

# Show the plot
plt.show()

#seaborn
# Import necessary libraries
import yfinance as yf
import seaborn as sns
import matplotlib.pyplot as plt

# Download stock data
data = yf.download('AAPL','2020-01-01','2023-01-01')  # This will download Apple's stock data from Jan 1, 2020, to Jan 1, 2023

# Resetting the index of the DataFrame to make 'Date' a column; this is necessary for Seaborn to recognize the 'Date' field properly.
data.reset_index(inplace=True)

# Creating a Seaborn line plot for the stock's closing price
sns.lineplot(x='Date', y='Close', data=data)

# Enhancing the plot with labels and a title
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.title('Apple Stock Closing Prices Over Time')

# Displaying the plot
plt.show()

#seaborn again
import yfinance as yf
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Step 1: Download stock data
symbols = ['AAPL', 'GOOGL', 'MSFT', 'AMZN']  # You can include more symbols as needed
data = yf.download(symbols, start="2020-01-01", end="2023-01-01")['Close']

# Step 2: Calculate correlation matrix
correlation_matrix = data.corr()

# Step 3: Create a heatmap of the correlation matrix
plt.figure(figsize=(10, 8))  # Specifies the output size
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)

# Step 4: Enhance visualization with labels and a title
plt.title('Correlation Matrix of Stock Prices')
plt.yticks(rotation=0)  # To keep the y-axis labels readable

# Step 5: Display the plot
plt.show()

#candlestick chart
import yfinance as yf
import mplfinance as mpf

# Downloading the data from Yahoo Finance for a specific period
musa_data = yf.download('MUSA', start='2022-01-01', end='2023-01-01')

# We will use the 'Close', 'Open', 'High', 'Low' and 'Volume' data for the candlestick chart
# Ensure we have data before proceeding
if not musa_data.empty:
    # Creating the candlestick chart
    mpf.plot(musa_data, type='candle', style='yahoo', volume=True, title='Murphy USA Candlestick Chart')
else:
    print("No trading data available for the given period.")
