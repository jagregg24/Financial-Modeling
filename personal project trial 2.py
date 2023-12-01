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

def get_user_stock_selection():
    stock_symbols = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA', 'META', 'NFLX', 'NVDA', 'KO', 'JPM']
    print("Available stocks:", ', '.join(stock_symbols))
    
    selected_stocks = []
    while len(selected_stocks) < 4:
        try:
            choice = input(f"Select stock {len(selected_stocks) + 1} of 4: ").upper()
            if choice in stock_symbols and choice not in selected_stocks:
                selected_stocks.append(choice)
            else:
                print("Invalid selection or stock already chosen.")
        except ValueError:
            print("Please enter a valid stock symbol.")

    return selected_stocks

def suggest_stocks(investment, selected_stocks):
    if investment <= 0:
        print("Not enough funds to suggest investments.")
        return

    print(f"You have ${investment} available for investment.")

    # Fetching data for the selected stocks
    data = yf.download(' '.join(selected_stocks), group_by='ticker')

    stock_ev_ebitda_ratios = {}
    for symbol in selected_stocks:
        stock = yf.Ticker(symbol)
        ev_ebitda = stock.info.get('enterpriseToEbitda')
        if ev_ebitda is not None:
            stock_ev_ebitda_ratios[symbol] = ev_ebitda

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
    plt.bar(names, values, color ='blue', width = 0.4)

    plt.xlabel('Stocks')
    plt.ylabel('EV/EBITDA')
    plt.title('EV/EBITDA of Potential Stocks to Invest In')
    plt.show()

def main():
    print("Welcome to the Personal Budget and Investment Calculator!")
    
    income, expenses = get_user_input()
    investment = calculate_investment(income, expenses)
    selected_stocks = get_user_stock_selection()
    suggest_stocks(investment, selected_stocks)

if __name__ == "__main__":
    main()
