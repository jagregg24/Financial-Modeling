import numpy as np
import pandas as pd
import yfinance as yf
from scipy.optimize import minimize
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox

def calculate_investment(income, expenses):
    excess = income - expenses
    if excess <= 0:
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

def suggest_stocks(investment, selected_stocks, result_text, result_window):
    if investment <= 0:
        result_text.insert(tk.END, "Not enough funds to suggest investments.\n")
        return

    # Fetch historical data
    data = get_stock_data(selected_stocks, '2020-01-01', '2022-01-01')

    # Calculate mean returns and covariance
    mean_returns = data.pct_change().mean()
    cov_matrix = data.pct_change().cov()

    # Optimize portfolio for minimum risk
    min_risk_allocation = minimize_risk(mean_returns, cov_matrix, (0, 1))

    # Prepare data for pie chart
    investment_amounts = [min_risk_allocation.x[i] * investment for i in range(len(selected_stocks))]
    labels = [f"{stock} (${amount:.2f})" for stock, amount in zip(selected_stocks, investment_amounts)]

    # Define a threshold for the minimum investment amount to be displayed on the pie chart
    investment_threshold = investment * 0.01  # 1% of the total investment

    # Filter out investments below the threshold
    filtered_amounts_labels = [(amount, label) for amount, label in zip(investment_amounts, labels) if amount > investment_threshold]
    if not filtered_amounts_labels:  # In case all are filtered out
        result_text.insert(tk.END, "All investments are below the threshold.\n")
        return

    filtered_amounts, filtered_labels = zip(*filtered_amounts_labels)

    # Display investment suggestions
    for label, amount in zip(filtered_labels, filtered_amounts):
        result_text.insert(tk.END, f"{label}: ${amount:.2f}\n")

    # Show pie chart in a separate Matplotlib window
    plt.figure(figsize=(8, 8))
    plt.pie(filtered_amounts, labels=filtered_labels, autopct='%1.1f%%')
    plt.title('Investment Distribution Among Selected Stocks')
    plt.show()

def submit_form(income_str, expenses_str, root):
    try:
        income = float(income_str.get())
        expenses = float(expenses_str.get())
        investment = calculate_investment(income, expenses)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for income and expenses.")
        return

    selected_stocks = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA', 'META', 'NFLX', 'NVDA', 'BABA', 'JPM']

    # Create a new window to display the results
    result_window = tk.Toplevel(root)
    result_window.title("Investment Suggestions")

    # Text widget to show the results
    result_text = tk.Text(result_window, height=15, width=50)
    result_text.pack()

    suggest_stocks(investment, selected_stocks, result_text, result_window)

def create_ui():
    root = tk.Tk()
    root.title("Investment Calculator")

    root.geometry("700x500")

    tk.Label(root, text="Monthly Income:").pack()
    income_str = tk.StringVar()
    income_entry = tk.Entry(root, textvariable=income_str)
    income_entry.pack()

    tk.Label(root, text="Monthly Expenses:").pack()
    expenses_str = tk.StringVar()
    expenses_entry = tk.Entry(root, textvariable=expenses_str)
    expenses_entry.pack()

    submit_button = tk.Button(root, text="Calculate Investment", command=lambda: submit_form(income_str, expenses_str, root))
    submit_button.pack()

    root.mainloop()

if __name__ == "__main__":
    create_ui()
