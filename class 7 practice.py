import numpy as np
import pandas as pd

# Sample data
df = pd.DataFrame({
    'A': [1, 2, np.nan, 4],
    'B': [5, np.nan, 7, 8],
    'C': [9, 10, 11, 12]
})

# Check for missing values
print(df.isna())
print(df.isna().sum())

#standardizing
import pandas as pd
data = {
    'A': [10, 20, 30, 40, 50,],
    'B': [5, 15, 25, 35, 45]
}
df = pd.DataFrame(data)
standardized_df = (df - df.mean()) / df.std()
print("\nStandardized DataFrame:")
print(standardized_df)

#daily and monthly returns w/standardization
import pandas
data = {
    'Date': ['2022-01-01', '2022-01-02', '2022-01-03', '2022-02-01', '2022-02-02'],
    'Close Price': [100, 101, 103, 104, 105]
}
stock_df = pd.DataFrame(data)
stock_df['Date'] = pd.to_datetime(stock_df['Date'])
stock_df.set_index('Date', inplace=True)
stock_df['Daily Returns'] = stock_df['Close Price'].pct_change()
stock_df['Monthly Returns'] = stock_df['Close Price'].resample('M').last().pct_change()
stock_df['Standardized Daily Returns'] = (stock_df['Daily Returns'] - stock_df['Daily Returns'].mean()) / stock_df['Daily Returns'].std()
stock_df['Standardized Monthly Returns'] = (stock_df['Monthly Returns'] - stock_df['Monthly Returns'].mean()) / stock_df['Monthly Returns'].std()
print(stock_df)

#MUSA stock assignment
import yfinance as yf
from datetime import datetime, timedelta

# Calculate date 3 years ago from today
end_date = datetime.today()
start_date = end_date - timedelta(days=3*365)

# Fetch data for Murphy USA (MUSA) for the last 3 years
musa_stock = yf.download('MUSA', start=start_date, end=end_date)

# Display the data
print(musa_stock)


