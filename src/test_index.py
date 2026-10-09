import pandas as pd
from factor_engine import compute_momentum, compute_volatility, clean_data
from scoring import compute_score
from index_builder import select_top_stocks, assign_equal_weights, assign_weight_by_score

# Load data
df = pd.read_csv("../data/stock_data.csv", index_col=0, parse_dates=True)

# Factors
momentum = clean_data(compute_momentum(df))
volatility = clean_data(compute_volatility(df))

# Align
momentum, volatility = momentum.align(volatility, join="inner")

# Score
score = compute_score(momentum, volatility)

# Select stocks
selected = select_top_stocks(score, top_n=10)

# Assign weights
weights = assign_weight_by_score(score, selected)

print("Selected Stocks:", selected)
print("Weights:", weights)