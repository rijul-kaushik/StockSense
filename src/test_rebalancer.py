import pandas as pd
from factor_engine import compute_momentum, compute_volatility, clean_data
from scoring import compute_score
from rebalancer import rebalance

# Load data
df = pd.read_csv("../data/stock_data.csv", index_col=0, parse_dates=True)

# Factors
momentum = clean_data(compute_momentum(df))
volatility = clean_data(compute_volatility(df))

# Align
momentum, volatility = momentum.align(volatility, join="inner")

# Score
score = compute_score(momentum, volatility)

# Rebalance
portfolios = rebalance(score, freq=30, top_n=5)

# Print first few
for p in portfolios[:5]:
    print(p)