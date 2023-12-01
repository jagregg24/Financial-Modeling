import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Simulated returns for two assets (just for illustration purposes)
np.random.seed(42)
dates = pd.date_range('20200101', periods=100)
asset1_returns = np.random.randn(100) * 0.001 + 0.0002  # mean 0.0002, std 0.001
asset2_returns = np.random.randn(100) * 0.001 + 0.0003  # mean 0.0003, std 0.001
returns = pd.DataFrame({'Asset1': asset1_returns, 'Asset2': asset2_returns}, index=dates)

# Portfolio weights
weights = np.array([0.5, 0.5])

# Expected portfolio return
exp_return = np.sum(returns.mean() * weights)

# Expected portfolio volatility
exp_volatility = np.sqrt(np.dot(weights.T, np.dot(returns.cov() * 252, weights)))

print(f"Expected Portfolio Return: {exp_return*252:.4f}")
print(f"Expected Portfolio Volatility: {exp_volatility:.4f}")

# Plot Efficient Frontier for two assets
port_returns = []
port_volatilities = []
for w in range(101):
    w /= 100.0
    weights = np.array([w, 1-w])
    port_return = np.sum(returns.mean() * weights) * 252
    port_vol = np.sqrt(np.dot(weights.T, np.dot(returns.cov() * 252, weights)))
    port_returns.append(port_return)
    port_volatilities.append(port_vol)

plt.figure(figsize=(10,6))
plt.scatter(port_volatilities, port_returns, c=(np.array(port_returns)-min(port_returns))/(np.array(port_returns).max()-min(port_returns)), marker='o')
plt.xlabel('Expected Volatility')
plt.ylabel('Expected Return')
plt.colorbar(label='Sharpe ratio')
plt.title('Efficient Frontier')
plt.show()

#sharpe ratio
import numpy as np
import pandas as pd
import yfinance as yf
from scipy.optimize import minimize

# 1. Get the Data

# Define tickers and fetch data
tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN']  # Example tickers
start_date = '2020-01-01'
end_date = '2021-01-01'
prices = yf.download(tickers, start=start_date, end=end_date)['Adj Close']

# Calculate daily returns
returns = prices.pct_change().dropna()

# 2. Define the Optimization Functions

def portfolio_annualized_performance(weights, mean_returns, cov_matrix):
    returns = np.sum(mean_returns * weights) * 252
    std = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights))) * np.sqrt(252)
    return std, returns

def neg_sharpe_ratio(weights, mean_returns, cov_matrix, risk_free_rate):
    p_std, p_return = portfolio_annualized_performance(weights, mean_returns, cov_matrix)
    return -(p_return - risk_free_rate) / p_std

# 3. Run the Optimizer

def max_sharpe_ratio(mean_returns, cov_matrix, risk_free_rate):
    num_assets = len(mean_returns)
    args = (mean_returns, cov_matrix, risk_free_rate)
    constraints = ({'type': 'eq', 'fun': lambda weights: np.sum(weights) - 1})
    bound = (0.0, 1.0)
    bounds = tuple(bound for asset in range(num_assets))
    result = minimize(neg_sharpe_ratio, num_assets*[1./num_assets,], args=args, 
                      bounds=bounds, constraints=constraints)
    return result

mean_returns = returns.mean()
cov_matrix = returns.cov()
risk_free_rate = 0.01  # Example risk-free rate, can be replaced with the rate of your choice

optimal_weights = max_sharpe_ratio(mean_returns, cov_matrix, risk_free_rate).x

print("Optimal weights for maximum Sharpe Ratio:")
for ticker, weight in zip(tickers, optimal_weights):
    print(f"{ticker}: {weight:.4f}")
