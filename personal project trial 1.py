import yfinance as yf
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
        investment = 0.3 * excess  # 30% of the excess money
        return investment

def suggest_stocks(investment):
    if investment <= 0:
        print("Not enough funds to suggest investments.")
        return

    print(f"You have ${investment} available for investment.")

    stock_symbols = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA']
    
    # Fetching data for these stocks
    data = yf.download(' '.join(stock_symbols), group_by='ticker')

    stock_ev_ebitda_ratios = {}
    for symbol in stock_symbols:
        stock = yf.Ticker(symbol)
        ev_ebitda = stock.info.get('enterpriseToEbitda')
        if ev_ebitda is not None:  # Ensure the data is available
            stock_ev_ebitda_ratios[symbol] = ev_ebitda

    # Check if we have any ratios to compare
    if not stock_ev_ebitda_ratios:
        print("EV/EBITDA data is not available for the selected stocks.")
        return

    # Find the stock with the lowest EV/EBITDA ratio
    suggested_stock = min(stock_ev_ebitda_ratios, key=stock_ev_ebitda_ratios.get)

    print(f"Based on a sophisticated algorithm (lowest EV/EBITDA), we suggest you invest in: {suggested_stock}")

    # Now, let's add a chart
    names = list(stock_ev_ebitda_ratios.keys())
    values = list(stock_ev_ebitda_ratios.values())

    # Create a bar chart
    plt.figure(figsize=(10, 5))

    # Creating the bar plot
    plt.bar(names, values, color ='blue', width = 0.4)

    plt.xlabel('Stocks')
    plt.ylabel('EV/EBITDA')
    plt.title('EV/EBITDA of Potential Stocks to Invest In')
    plt.show()

def main():
    print("Welcome to the Personal Budget and Investment Calculator!")
    
    income, expenses = get_user_input()
    investment = calculate_investment(income, expenses)
    suggest_stocks(investment)

if __name__ == "__main__":
    main()
