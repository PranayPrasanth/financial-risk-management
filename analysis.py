import yfinance as yf
import numpy as np
import scipy.stats as stats

# Define the stock ticker and data range
stock_ticker = "EXPN.L"  # Experian's ticker on the LSE
start_date = "2019-01-01"
end_date = "2023-12-31"

# Define index ticker
index_ticker = "^FTSE"

# Fetch monthly adjusted closing prices of EXPN
stock_data = yf.download(stock_ticker, start=start_date, end=end_date, interval="1mo")

# Fetch monthly adjusted closing prices of index
index_data = yf.download(index_ticker, start=start_date, end=end_date, interval="1mo")

# Calculate monthly returns of EXPN
stock_returns = stock_data['Adj Close'].pct_change().dropna()

# Calculate monthly returns of index
index_returns = index_data['Adj Close'].pct_change().dropna()

# Ensure that both stock and index have returns data
if len(stock_returns) == 0 or len(index_returns) == 0:
    print("Insufficient data to calculate returns.")
else:
    # Calculate mean and standard deviation of returns
    mean_return = np.mean(stock_returns)
    std_dev_return = np.std(stock_returns)


    std_dev_value = std_dev_return.values[0]
    print(f"Standard deviation {std_dev_value: .2f}")

    # Define parameters for VaR and ES calculation
    confidence_level = 0.95
    z_score = stats.norm.ppf(1 - confidence_level)  # Z-score for 95% confidence

    # Weight of the asset (1 if considering just the stock)
    weight = 1

    # Time horizon (e.g., 1 month)
    time_horizon = 1  # For monthly VaR and ES, no need to scale time

    # Calculate the Parametric VaR at 95% Confidence Level
    VaR_95 = weight * std_dev_return * z_score * np.sqrt(time_horizon)
    VaR_95_value = VaR_95.values[0]
    print(f"Parametric VaR (95% Confidence): {VaR_95_value:.2f}")

    # Calculate the Parametric Expected Shortfall (ES) at 95% Confidence Level
    ES_95 = weight * (mean_return - z_score * std_dev_return) * np.sqrt(time_horizon)
    ES_95_value = ES_95.values[0]
    print(f"Parametric Expected Shortfall (95% Confidence): {ES_95_value:.2f}")

