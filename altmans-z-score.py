#Exchange rate of USD/GBP
EXCHANGE_RATE = 0.81
def calculate_altman_z(wc, ta, re, ebit, mve, bvl, sales):
    """
    Calculate Altman's Z-Score.

    Parameters:
        wc (float): Working Capital
        ta (float): Total Assets
        re (float): Retained Earnings
        ebit (float): Earnings Before Interest and Taxes
        mve (float): Market Value of Equity
        bvl (float): Book Value of Total Liabilities
        sales (float): Total Revenue or Sales

    Returns:
        float: Altman's Z-Score
    """
    # Calculate individual ratios
    x1 = wc / ta
    x2 = re / ta
    x3 = ebit / ta
    x4 = mve / bvl
    x5 = sales / ta

    # Altman Z-Score formula
    z_score = 1.2 * x1 + 1.4 * x2 + 3.3 * x3 + 0.6 * x4 + 0.999 * x5
    return z_score


# Values for calculating z-score
working_capital = -517 / EXCHANGE_RATE # Working capital converted in GBP
total_assets = 10864 / EXCHANGE_RATE  # Total assets converted in GBP
retained_earnings = 20447 / EXCHANGE_RATE # Retained Earnings in GBP
ebit = 1794 / EXCHANGE_RATE # EBIT in GBP
market_value_equity = 2560.116 # Market Value Equity
book_value_liabilities = 6900 / EXCHANGE_RATE # Total liabilities in GBP
sales = 6619 / EXCHANGE_RATE # Total Revenue in GBP

# Calculate Altman's Z-Score
z_score = calculate_altman_z(
    wc=working_capital,
    ta=total_assets,
    re=retained_earnings,
    ebit=ebit,
    mve=market_value_equity,
    bvl=book_value_liabilities,
    sales=sales
)

print(f"Altman's Z-Score: {z_score:.2f}")


