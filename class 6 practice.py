import yfinance as yf
import pandas as pd

# Fetch data for Apple from Yahoo Finance
apple_data = yf.download('AAPL', start='2020-01-01', end='2023-01-01')

# Display the data
print(apple_data.head())

import yfinance as yf

# Define the ticker symbol
ticker_symbol = "AAPL"

# Get the data
data = yf.Ticker(ticker_symbol)

# Fetch historical market data for Apple from the last 5 years
df = data.history(period="5y")

# Print the data
print(df)
#1
import yfinance as yf

# Define the ticker symbol
ticker_symbol = "AAPL"

# Fetch historical market data for Apple from the last year
data = yf.Ticker(ticker_symbol)
df = data.history(period="1y")
df['Daily Return'] = df['Close'].pct_change()
print(df[['Close', 'Daily Return']])
#moving average
import yfinance as yf

# Define the ticker symbol
ticker_symbol = "AAPL"

# Fetch historical market data for Apple from the last year (or whatever period you're interested in)
data = yf.Ticker(ticker_symbol)
df = data.history(period="1y")
df['30 Day MA'] = df['Close'].rolling(window=30).mean()
print(df[['Close', '30 Day MA']])
#stock portfolio with returns and risks
import yfinance as yf
import pandas as pd

# Define the tickers for our portfolio. Example: Apple, Microsoft, and Google.
tickers = ['AAPL', 'MSFT', 'GOOGL']

# Fetch historical market data for the last year
data = yf.download(tickers, period="1y")['Adj Close']

# Calculate daily returns
daily_returns = data.pct_change().dropna()

# Assign weights to the stocks in our portfolio
# Here, let's assume equal weights for simplicity: 1/3 each
weights = [1./3, 1./3, 1./3]

# Calculate the portfolio returns
portfolio_returns = daily_returns.dot(weights)

# Calculate the mean and standard deviation of the portfolio returns
mean_returns = portfolio_returns.mean()
std_dev = portfolio_returns.std()

print(f"Mean (Expected) Portfolio Return: {mean_returns*100:.2f}%")
print(f"Portfolio Risk (Standard Deviation): {std_dev*100:.2f}%")
#visualization
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Fetching data for the stocks
tickers = ['AAPL', 'MSFT', 'GOOGL']
data = yf.download(tickers, period="1y")['Adj Close']

# Calculate 30-day moving average for each stock
moving_averages = data.rolling(window=30).mean()

# Plotting historical stock prices
data.plot(title="Historical Stock Prices", figsize=(14, 7))

# Plotting moving averages on the same graph
moving_averages.plot(title="30-day Moving Averages", figsize=(14, 7), linestyle='--')

plt.legend([ticker + " Stock Price" for ticker in tickers] + [ticker + " 30-day MA" for ticker in tickers])
plt.show()
#question 1
import pandas as pd


#question 3
import yfinance as yf
import pandas as pd

# Load the data into dataframes
aapl_df = pd.read_csv("AAPL.csv")
msft_df = pd.read_csv("MSFT.csv")
googl_df = pd.read_csv("GOOGL.csv")
import pandas as pd
aapl_df['Daily Return'] = aapl_df['Close Price'].pct_change()
msft_df['Daily Return'] = msft_df['Close Price'].pct_change()
googl_df['Daily Return'] = googl_df['Close Price'].pct_change()
# Merging the dataframes by Date
portfolio = pd.DataFrame({
    'AAPL': aapl_df['Daily Return'],
    'MSFT': msft_df['Daily Return'],
    'GOOGL': googl_df['Daily Return']
})
weights = [0.40, 0.35, 0.25]
portfolio['Portfolio Daily Return'] = portfolio.dot(weights)
overall_return = (portfolio['Portfolio Daily Return'] + 1).prod() - 1
portfolio_risk = portfolio['Portfolio Daily Return'].std()

