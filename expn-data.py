# import yfinance as yf
# import pandas as pd
#
# # Define stock symbols and date range
# stocks = ['EXPN.L','^FTSE']
#
#
# start_date = "2014-1-1"
# end_date = "2023-12-31"
#
# # Fetch the adjusted close prices for the selected stocks
# stock_data = yf.download(stocks, start=start_date, end=end_date, interval="1mo")["Adj Close"]
#
#
# # Check for missing data
# if stock_data.isnull().values.any():
#     print("Missing values detected, filling...")
#
#
#
# # Save the data to a CSV file
# csv_file = "EXPN-including-index.csv"
# stock_data.to_csv(csv_file)
#
# # Display the first few rows of the data
# print(stock_data.head())


import yfinance as yf

# Define the stock ticker and data range
stock_ticker = "EXPN.L"  # Example: Experian's ticker on the LSE
start_date = "2019-01-01"
end_date = "2023-12-31"

# Fetch monthly data for EXPN
stock_data = yf.download(stock_ticker, start=start_date, end=end_date, interval="1mo")

# Calculate the monthly bid-ask spread (approximate)
stock_data['Bid-Ask Spread'] = stock_data['High'] - stock_data['Low']

# Calculate the average bid-ask spread over the period
avg_bid_ask_spread = stock_data['Bid-Ask Spread'].mean()

print(f"Average Bid-Ask Spread: {avg_bid_ask_spread:.2f}")
