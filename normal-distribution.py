from scipy import stats
from analysis import stock_returns

# Shapiro-Wilk test for normality
stat, p_value = stats.shapiro(stock_returns)
print(f"Shapiro-Wilk Test Statistic: {stat:.4f}, p-value: {p_value:.4f}")

if p_value < 0.05:
    print("Reject the null hypothesis: The returns are not normally distributed.")
else:
    print("Fail to reject the null hypothesis: The returns are normally distributed.")

# Plot the distribution of returns
plt.figure(figsize=(10, 6))

# Plot histogram of stock returns
sns.histplot(stock_returns, kde=True, color='blue', stat='density', bins=30)

# Overlay a normal distribution curve for comparison
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = stats.norm.pdf(x, np.mean(stock_returns), np.std(stock_returns))
plt.plot(x, p, 'k', linewidth=2)

plt.title(f'Distribution of Stock Returns for {stock_ticker}')
plt.xlabel('Stock Returns')
plt.ylabel('Density')
plt.show()
