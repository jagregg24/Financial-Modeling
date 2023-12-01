#task 1
# Importing necessary libraries
import yfinance as yf
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Step 1: Download stock price data for the stocks you're interested in
# For this example, we'll use Apple (AAPL), Microsoft (MSFT), and Google (GOOGL)
stocks = ['AAPL', 'MSFT', 'GOOGL']

# You can adjust the period, start, and end parameters according to your specific needs
data = yf.download(stocks, start="2019-01-01", end="2022-01-01")['Close']

# Step 2: Calculate daily returns of the stocks
returns = data.pct_change()

# Step 3: Calculate the correlation matrix
correlation_matrix = returns.corr()

# Step 4: Creating a heatmap of the correlation matrix
# Setting up figure and axis
plt.figure(figsize=(10, 8))

# Creating a heatmap
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.05)

# Extra configurations for the heatmap
plt.title('Correlation matrix of stock returns', fontsize=15)
plt.xticks(rotation=45)  # Rotating x-axis labels for better readability
plt.yticks(rotation=0)  # Keeping y-axis labels as is

# Display the plot
plt.show()

#task 2
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Download stock price data
stocks = ['AAPL', 'MSFT', 'GOOGL']
data = yf.download(stocks, start="2019-01-01", end="2022-01-01")['Close']

# Step 2: Calculate daily returns
returns = data.pct_change()

# Step 3: Calculate average returns and standard deviation (annualized)
avg_returns = returns.mean() * 252  # There are typically 252 trading days in a year
std_dev = returns.std() * np.sqrt(252)  # Annualizing the standard deviation

# Creating a DataFrame to hold the results
results = pd.DataFrame({'Return': avg_returns, 'Risk': std_dev})

# Step 4: Plotting the risk and return
plt.figure(figsize=(10, 6))

for label, x, y in zip(results.index, results['Risk'], results['Return']):
    plt.scatter(x, y, label=label)

plt.title('Risk vs Return')
plt.xlabel('Risk (Standard Deviation of Annual Returns)')
plt.ylabel('Expected Return')
plt.legend(loc='upper left')
plt.grid(True)
plt.show()

#task 3
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Define the stocks in our sector - for illustration, we're using big tech companies.
tech_stocks = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'FB']

# Fetch data for these stocks
data = yf.download(tech_stocks, start="2022-01-01")['Close']

# Calculate YTD return
latest = data.iloc[-1]  # the latest closing prices
initial = data.iloc[0]  # the first closing prices of the year
ytd_return = (latest - initial) / initial

# For real scenarios, fetch real P/E ratios from a reliable financial data service.
# Here, we will use fictional P/E ratios for the sake of illustration.
pe_ratios = {
    'AAPL': 25.4,  # Fictional data
    'MSFT': 30.2,  # Fictional data
    'GOOGL': 28.1,  # Fictional data
    'AMZN': 60.5,  # Fictional data
    'FB': 24.6,  # Fictional data
}

# Create DataFrame for visualization
sector_performance = pd.DataFrame({
    'YTD Return': ytd_return,
    'P/E Ratio': pe_ratios,
})

# Plotting
sector_performance.plot(kind='bar', figsize=(10, 6))

plt.title('2022 YTD Return and P/E Ratio for Tech Stocks')
plt.ylabel('Performance Metrics')
plt.xlabel('Stocks')
plt.xticks(rotation=45)
plt.grid(axis='y')

# Show the plot
plt.tight_layout()
plt.show()

#task 4
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
# Define stock tickers
tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'META']  # Example stocks

# Download stock data
data = yf.download(tickers, start="2018-01-01", end="2023-01-01")['Close']

# Calculate logarithmic returns
log_returns = np.log(data / data.shift(1))
np.random.seed(42)
num_portfolios = 10000
all_weights = np.zeros((num_portfolios, len(data.columns)))
ret_arr = np.zeros(num_portfolios)
vol_arr = np.zeros(num_portfolios)
sharpe_arr = np.zeros(num_portfolios)

# Simulate random portfolio weights
for x in range(num_portfolios):
    # Weights
    weights = np.array(np.random.random(len(tickers)))
    weights = weights / np.sum(weights)
    
    # Save weights
    all_weights[x, :] = weights
    
    # Expected return
    ret_arr[x] = np.sum((log_returns.mean() * weights * 252))
    
    # Expected volatility
    vol_arr[x] = np.sqrt(np.dot(weights.T, np.dot(log_returns.cov() * 252, weights)))
    
    # Sharpe Ratio
    sharpe_arr[x] = ret_arr[x] / vol_arr[x]
plt.figure(figsize=(12,8))
plt.scatter(vol_arr, ret_arr, c=sharpe_arr, cmap='viridis')
plt.colorbar(label='Sharpe Ratio')
plt.xlabel('Volatility')
plt.ylabel('Return')

# Highlight the portfolio with the best Sharpe Ratio
best_idx = sharpe_arr.argmax()
plt.scatter(vol_arr[best_idx], ret_arr[best_idx], c='red', s=50, edgecolors='black')

plt.title('Efficient Frontier with Random Portfolios')
plt.show()
