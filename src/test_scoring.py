import pandas as pd
from factor_engine import compute_momentum, compute_volatility, clean_data
from scoring import compute_score

# Load data
df = pd.read_csv("../data/stock_data.csv", index_col=0, parse_dates=True)

# Compute factors
momentum = clean_data(compute_momentum(df))
volatility = clean_data(compute_volatility(df))

# Align data (IMPORTANT)
momentum, volatility = momentum.align(volatility, join="inner")

# Compute score
score = compute_score(momentum, volatility)

print(score.tail())