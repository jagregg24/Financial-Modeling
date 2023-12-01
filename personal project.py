import yfinance as yf
import random

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
        investment = 0.3 * excess  # 30% of the excess money
        return investment

def suggest_stocks(investment):
    if investment <= 0:
        print("Not enough funds to suggest investments.")
        return

    print(f"You have ${investment} available for investment.")

    stock_symbols = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA']
    
    data = yf.download(' '.join(stock_symbols), group_by='ticker')

    stock_pe_ratios = {}
    for symbol in stock_symbols:
        stock = yf.Ticker(symbol)
        pe_ratio = stock.info['trailingPE']
        stock_pe_ratios[symbol] = pe_ratio

    suggested_stock = min(stock_pe_ratios, key=stock_pe_ratios.get)

    print(f"Based on a sophisticated algorithm (lowest P/E ratio), we suggest you invest in: {suggested_stock}")

def main():
    print("Welcome to the Personal Budget and Investment Calculator!")
    
    income, expenses = get_user_input()
    investment = calculate_investment(income, expenses)
    suggest_stocks(investment)

if __name__ == "__main__":
    main()

