import pandas as pd
from factor_engine import compute_returns, compute_momentum, compute_volatility, clean_data

# Load data
df = pd.read_csv("../data/stock_data.csv", index_col=0, parse_dates=True)

# Compute factors
returns = compute_returns(df)
momentum = compute_momentum(df)
volatility = compute_volatility(df)

# Clean
returns = clean_data(returns)
momentum = clean_data(momentum)
volatility = clean_data(volatility)

print("Returns:\n", returns.head())
print("\nMomentum:\n", momentum.head())
print("\nVolatility:\n", volatility.head())