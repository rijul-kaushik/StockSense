import pandas as pd
import matplotlib.pyplot as plt

from factor_engine import compute_momentum, compute_volatility, clean_data
from scoring import compute_score
from rebalancer import rebalance
from backtester import backtest
from database import load_from_db

def sharpe_ratio(returns):
    return (returns.mean() / returns.std()) * (252 ** 0.5)

def calculate_cagr(series):
    years = len(series) / 252  # trading days
    return (series.iloc[-1] ** (1 / years)) - 1

df = load_from_db()

# Factors
momentum = clean_data(compute_momentum(df))
volatility = clean_data(compute_volatility(df))

# Score
score = compute_score(momentum, volatility)

# Rebalance
portfolios = rebalance(score, freq=120, top_n=15)

# Backtest
portfolio_values = backtest(df, portfolios)

if portfolio_values.empty:
    print("ERROR: No values generated")
    exit()

# Use directly (already cumulative)
cumulative = portfolio_values

# NIFTY
nifty = df["^NSEI"].pct_change().dropna()
nifty_cum = (1 + nifty).cumprod()

# Align by dates
common_index = cumulative.index.intersection(nifty_cum.index)

cumulative = cumulative.loc[common_index]
nifty_cum = nifty_cum.loc[common_index]


# Normalize both
cumulative = cumulative / cumulative.iloc[0]
nifty_cum = nifty_cum / nifty_cum.iloc[0]

# Plot
plt.figure()
cumulative.plot(label="Smart Index")
nifty_cum.plot(label="NIFTY 50")
plt.ylabel("Normalized Returns (Base = 1)")
plt.legend()
plt.title("Smart Index vs NIFTY")
plt.show()

def max_drawdown(series):
    roll_max = series.cummax()
    drawdown = series / roll_max - 1
    return drawdown.min()

print("Max Drawdown:", max_drawdown(cumulative))

# Calculate daily returns from portfolio
returns = cumulative.pct_change().dropna()

# Metrics
cagr = calculate_cagr(cumulative)
sharpe = sharpe_ratio(returns)

print(f"CAGR: {cagr:.2%}")
print(f"Sharpe Ratio: {sharpe:.2f}")