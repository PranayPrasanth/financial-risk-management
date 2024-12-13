import yfinance as yf
import pandas as pd

# Define stock symbols and date range
stocks = ['EXPN.L','^FTSE']


start_date = "2014-1-1"
end_date = "2023-12-31"

# Fetch the adjusted close prices for the selected stocks
stock_data = yf.download(stocks, start=start_date, end=end_date, interval="1mo")["Adj Close"]


# Check for missing data
if stock_data.isnull().values.any():
    print("Missing values detected, filling...")



# Save the data to a CSV file
csv_file = "EXPN-including-index.csv"
stock_data.to_csv(csv_file)

# Display the first few rows of the data
print(stock_data.head())
