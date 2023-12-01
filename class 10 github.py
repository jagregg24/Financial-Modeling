import wrds

# Securely input your credentials without hardcoding them
username = input("Enter your WRDS username: ")
password = input("Enter your WRDS password: ")

# Establish connection
conn = wrds.Connection(wrds_username=username, wrds_password=password)

# Define a function to retrieve Apple's stock data for a given month and year
def fetch_apple_data(year, month):
    sql_query = f"""
        SELECT date, permno, prc, vol, ret
        FROM crsp.dsf
        WHERE permno = 'AAPL_permno' AND date BETWEEN '{year}-{month}-01' AND '{year}-{month}-31'
    """
    return conn.raw_sql(sql_query)

# Define a function to retrieve bond returns for a given month and year
def fetch_bond_data(year, month):
    sql_query = f"""
        SELECT date, bond_id, return
        FROM bond_returns_db.bond_returns
        WHERE date BETWEEN '{year}-{month}-01' AND '{year}-{month}-31'
    """
    return conn.raw_sql(sql_query)

# Fetch data
apple_data = fetch_apple_data(2020, 1)
bond_data = fetch_bond_data(2020, 1)

# Close connection
conn.close()

# Print results (optional)
print(apple_data)
print(bond_data)

#5 stocks and 1 fixed income
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import minimize
import wrds

# Connect to WRDS
conn = wrds.Connection()

# Retrieve data (Replace 'AAPL_permno' etc with actual PERMNO or other identifiers)
stocks = ["AAPL_permno", "MSFT_permno", "GOOGL_permno", "AMZN_permno", "TSLA_permno"]
data = pd.DataFrame()
for stock in stocks:
    query = f"""
        SELECT date, ret 
        FROM crsp.dsf 
        WHERE permno = '{stock}' 
        AND date BETWEEN '2020-01-01' AND '2020-12-31'
    """
    temp = conn.raw_sql(query)
    data = pd.concat([data, temp.set_index('date')], axis=1)
data.columns = stocks

# Optionally retrieve fixed income data
query = """
    SELECT date, return as ret_bond
    FROM bond_returns_db.bond_returns 
    WHERE date BETWEEN '2020-01-01' AND '2020-12-31'
"""
bond_data = conn.raw_sql(query)
data = pd.merge(data, bond_data.set_index('date'), left_index=True, right_index=True, how='left')
conn.close()

# Calculate daily returns
returns = data.pct_change().dropna()

# Expected returns and covariance matrix
expected_returns = returns.mean()
cov_matrix = returns.cov()

# Objective function (Negative Sharpe Ratio)
def objective(weights): 
    portfolio_return = np.sum(expected_returns * weights)
    portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
    return -portfolio_return / portfolio_volatility

# Portfolio optimization
num_assets = len(data.columns)
constraints = ({'type': 'eq', 'fun': lambda weights: np.sum(weights) - 1})
bounds = tuple((0, 1) for asset in range(num_assets))
result = minimize(objective, num_assets*[1./num_assets], bounds=bounds, constraints=constraints)

# Efficient frontier
target_returns = np.linspace(expected_returns.min(), expected_returns.max(), 100)
target_volatilities = []

for tar in target_returns:
    constraints = ({'type': 'eq', 'fun': lambda weights: np.sum(weights) - 1},
                   {'type': 'eq', 'fun': lambda weights: np.sum(expected_returns * weights) - tar})
    result = minimize(objective, num_assets*[1./num_assets], bounds=bounds, constraints=constraints)
    target_volatilities.append(result['fun'])

# Plotting
plt.plot(target_volatilities, target_returns, 'y-', label="Efficient Frontier")
plt.title("Efficient Frontier")
plt.xlabel("Portfolio Volatility")
plt.ylabel("Portfolio Return")
plt.legend()
plt.grid(True)
plt.show()

#optimal portfolio weights
import numpy as np
import pandas as pd
from scipy.optimize import minimize
import wrds

# Connect to WRDS
conn = wrds.Connection()

# Define tickers
stocks = ["AAPL_permno", "MSFT_permno", "GOOGL_permno", "AMZN_permno", "TSLA_permno", "BOND_permno"]

# Retrieve data (replace with actual PERMNO or other identifiers)
data = pd.DataFrame()
for stock in stocks:
    query = f"""
        SELECT date, ret 
        FROM crsp.dsf 
        WHERE permno = '{stock}' 
        AND date BETWEEN '2020-01-01' AND '2020-12-31'
    """
    temp = conn.raw_sql(query)
    data = pd.concat([data, temp.set_index('date')], axis=1)
data.columns = stocks
conn.close()

# Calculate expected returns and covariance matrix
expected_returns = data.mean()
cov_matrix = data.cov()

# Objective Function (Negative Sharpe Ratio)
def objective(weights): 
    portfolio_return = np.dot(expected_returns, weights)
    portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
    return -portfolio_return / portfolio_volatility

# Constraints and boundaries
constraints = ({'type': 'eq', 'fun': lambda weights: np.sum(weights) - 1})
bounds = tuple((0, 1) for asset in range(len(stocks)))

# If setting a minimum fixed income weight, e.g., 20%:
bounds = list(bounds)
bounds[-1] = (0.2, 1)
bounds = tuple(bounds)

# Optimize
initial_weights = [1./len(stocks) for asset in stocks]
solution = minimize(objective, initial_weights, method='SLSQP', bounds=bounds, constraints=constraints)

# Output
optimal_weights = solution.x
print("Optimal weights: ", optimal_weights)

#efficient frontier
import numpy as np
import pandas as pd
from scipy.optimize import minimize
import wrds
import matplotlib.pyplot as plt

# Connect to WRDS
conn = wrds.Connection()

# Retrieve data (replace with actual PERMNO or other identifiers)
stocks = ["AAPL_permno", "MSFT_permno", "GOOGL_permno", "AMZN_permno", "TSLA_permno", "BOND_permno"]
data = pd.DataFrame()
for stock in stocks:
    query = f"""
        SELECT date, ret 
        FROM crsp.dsf 
        WHERE permno = '{stock}' 
        AND date BETWEEN '2020-01-01' AND '2020-12-31'
    """
    temp = conn.raw_sql(query)
    data = pd.concat([data, temp.set_index('date')], axis=1)
data.columns = stocks
conn.close()

# Define objective and helper functions
expected_returns = data.mean()
cov_matrix = data.cov()

def objective(weights): 
    portfolio_return = np.dot(expected_returns, weights)
    portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
    return -portfolio_return / portfolio_volatility

def efficient_frontier(stocks_included):
    target_returns = np.linspace(expected_returns[stocks_included].min(), expected_returns[stocks_included].max(), 100)
    target_volatilities = []
    for tar in target_returns:
        constraints = ({'type': 'eq', 'fun': lambda weights: np.sum(weights) - 1},
                       {'type': 'eq', 'fun': lambda weights: np.dot(expected_returns[stocks_included], weights) - tar})
        bounds = tuple((0, 1) for asset in stocks_included)
        result = minimize(objective, [1./len(stocks_included) for asset in stocks_included], method='SLSQP', bounds=bounds, constraints=constraints)
        target_volatilities.append(np.sqrt(np.dot(result.x.T, np.dot(cov_matrix.loc[stocks_included, stocks_included], result.x))))
    return target_volatilities, target_returns

# Plot Efficient Frontier: Without fixed income
vol_without, ret_without = efficient_frontier(stocks[:-1])
plt.plot(vol_without, ret_without, label='Without Fixed Income')

# Plot Efficient Frontier: With fixed income
vol_with, ret_with = efficient_frontier(stocks)
plt.plot(vol_with, ret_with, label='With Fixed Income', linestyle='--')

# Customize and display plot
plt.title('Efficient Frontier')
plt.xlabel('Volatility')
plt.ylabel('Expected Return')
plt.legend()
plt.grid(True)
plt.show()



