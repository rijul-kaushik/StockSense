import pandas as pd

def compute_score(momentum, volatility):
    # Rank values between 0 and 1
    momentum_rank = momentum.rank(axis=1, pct=True)
    volatility_rank = volatility.rank(axis=1, pct=True)

    # Higher momentum = good
    # Lower volatility = good (so subtract)
    score = (momentum_rank * 0.6) - (volatility_rank * 0.4)

    return score