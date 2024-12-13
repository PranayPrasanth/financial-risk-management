# import yfinance as yf
# import numpy as np
# import pandas as pd
# from arch import arch_model
# from analysis import stock_returns
#
#
# # Fit GARCH(1,1) model to returns
# model = arch_model(stock_returns, vol='Garch', p=1, q=1, rescale=False)
# garch_fit = model.fit()
#
# # Display the results
# print(garch_fit.summary())
#
# # Forecast volatility for the next month (1-step ahead forecast)
# forecast = garch_fit.forecast(horizon=1)
# predicted_volatility = np.sqrt(forecast.variance.values[-1, :])  # Forecasted volatility
# print(f"Predicted Volatility (GARCH): {predicted_volatility[0]:.4f}")
