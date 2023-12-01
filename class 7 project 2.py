import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta

# Fetching stock price data for MUSA
musa = yf.download('MUSA', start="2020-01-01", end="2023-01-01")
musa['MUSA Returns'] = musa['Close'].pct_change()

# Calculate date 3 years ago from today
end_date = datetime.today()
start_date = end_date - timedelta(days=3*365)

# Fetch data for Murphy USA (MUSA) for the last 3 years
musa_stock = yf.download('MUSA', start=start_date, end=end_date)

# Display the data
print(musa_stock)

#missing data and outliers
print(musa_stock.isnull().sum())

# Fill missing values using interpolation
musa_stock.interpolate(method='linear', inplace=True)
# Compute IQR for 'Close' prices
Q1 = musa_stock['Close'].quantile(0.25)
Q3 = musa_stock['Close'].quantile(0.75)
IQR = Q3 - Q1

# Define bounds for the outliers
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
# Filter out outliers and create a mask
outliers = musa_stock[(musa_stock['Close'] < lower_bound) | (musa_stock['Close'] > upper_bound)]
print(outliers)
musa_stock = musa_stock[(musa_stock['Close'] >= lower_bound) & (musa_stock['Close'] <= upper_bound)]
musa_stock['Close'] = np.where(musa_stock['Close'] < lower_bound, lower_bound, musa_stock['Close'])
musa_stock['Close'] = np.where(musa_stock['Close'] > upper_bound, upper_bound, musa_stock['Close'])

# Simulating financial metrics for visualization
dates = pd.date_range(start="2020-01-01", end="2022-12-31", freq='M')
financial_data = pd.DataFrame({
    'Date': dates,
    'Stock': 'MUSA',
    'P/E Ratio': np.random.uniform(10, 30, len(dates)),
    'PEG Ratio': np.random.uniform(0.5, 2, len(dates)),
    'YoY Revenue Growth': np.random.uniform(0, 0.2, len(dates))  # assuming growth is between 0% to 20%
})

# Visualization of MUSA Historical Stock Returns
plt.figure(figsize=(15, 7))
plt.plot(musa.index, musa['MUSA Returns'], label='MUSA', color='green')
plt.title('Historical Stock Returns for MUSA')
plt.xlabel('Date')
plt.ylabel('Returns')
plt.legend()
plt.grid(True)
plt.show()

# Visualization for P/E Ratios
plt.figure(figsize=(15, 7))
sns.barplot(x='Date', y='P/E Ratio', data=financial_data, color='lightblue')
plt.title('P/E Ratios for MUSA')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Visualization for PEG Ratios
plt.figure(figsize=(15, 7))
sns.barplot(x='Date', y='PEG Ratio', data=financial_data, color='lightgreen')
plt.title('PEG Ratios for MUSA')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Visualization for YoY Revenue Growth
plt.figure(figsize=(15, 7))
sns.barplot(x='Date', y='YoY Revenue Growth', data=financial_data, color='lightcoral')
plt.title('Year-over-Year Revenue Growth for MUSA')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
