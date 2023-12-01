import numpy as np
import pandas as pd
import yfinance as yf
from scipy.optimize import minimize
import matplotlib.pyplot as plt

def get_user_input():
    try:
        income = float(input("Enter your monthly income: "))
        expenses = float(input("Enter your total monthly expenses: "))
    except ValueError:
        print("Please enter a valid number.")
        return get_user_input()
    return income, expenses

def calculate_investment(income, expenses):
    excess = income - expenses
    if excess <= 0:
        print("You don't have excess money for investment.")
        return 0
    else:
        return 0.3 * excess  # 30% of the excess money

def get_stock_data(tickers, start_date, end_date):
    data = yf.download(tickers, start=start_date, end=end_date)['Adj Close']
    return data

def calculate_portfolio_volatility(weights, mean_returns, cov_matrix):
    return np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))

def minimize_risk(mean_returns, cov_matrix, constraint_set):
    num_assets = len(mean_returns)
    args = (mean_returns, cov_matrix)
    constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
    bound = constraint_set
    bounds = tuple(bound for asset in range(num_assets))
    result = minimize(calculate_portfolio_volatility, num_assets*[1./num_assets,], args=args,
                      method='SLSQP', bounds=bounds, constraints=constraints)
    return result

def suggest_stocks(investment, selected_stocks):
    if investment <= 0:
        print("Not enough funds to suggest investments.")
        return

    print(f"You have ${investment:.2f} available for investment.")

    # Define start and end dates for historical data
    start_date = '2020-01-01'
    end_date = '2022-01-01'

    # Fetch historical data
    data = get_stock_data(selected_stocks, start_date, end_date)

    # Calculate mean returns and covariance
    mean_returns = data.pct_change().mean()
    cov_matrix = data.pct_change().cov()

    # Optimize portfolio for minimum risk
    min_risk_allocation = minimize_risk(mean_returns, cov_matrix, (0, 1))

    # Display the optimized portfolio allocation and investment amounts
    print("\nOptimized Portfolio Allocation for Minimum Risk:")
    for i, stock in enumerate(selected_stocks):
        allocation_percentage = min_risk_allocation.x[i]
        amount_to_invest = allocation_percentage * investment
        print(f"{stock}: {allocation_percentage*100:.2f}% (${amount_to_invest:.2f})")




def main():
    print("Welcome to the Personal Budget and Investment Calculator!")
    
    income, expenses = get_user_input()
    investment = calculate_investment(income, expenses)
    selected_stocks = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA', 'META', 'NFLX', 'NVDA', 'BABA', 'JPM']

    suggest_stocks(investment, selected_stocks)

if __name__ == "__main__":
    main()
