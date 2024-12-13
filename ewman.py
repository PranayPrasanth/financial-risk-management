import yfinance as yf
import numpy as np
import pandas as pd
from analysis import stock_returns


# Define the smoothing parameter for EWMA
lambda_param = 0.94

# Calculate EWMA volatility using the formula
ewma_volatility = stock_returns.ewm(span=(2 / (1 - lambda_param)) - 1).std()

# The latest predicted volatility (use .iloc[-1] for the last row)
latest_ewma_volatility = ewma_volatility.values[-1]

print(f"Latest EWMA volatility estimate:{latest_ewma_volatility}")
