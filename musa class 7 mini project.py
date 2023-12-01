import yfinance as yf
import numpy as np
from datetime import datetime, timedelta

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

