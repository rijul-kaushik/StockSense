import pandas as pd

def backtest(price_df, portfolios):
    returns = price_df.pct_change().dropna()

    portfolio_value = 1
    values = []

    for i in range(len(portfolios) - 1):
        current = portfolios[i]
        next_p = portfolios[i + 1]

        start = current["day"]
        end = next_p["day"]

        stocks = current["stocks"]

        # Equal weights (more stable)
        weight = min(1 / len(stocks), 0.15)

        period_returns = returns.iloc[start:end][stocks]

        if period_returns.empty:
            continue

        # Apply transaction cost ONCE per rebalance
        transaction_cost = 0.004  # 0.4%
        portfolio_value *= (1 - transaction_cost)

        for _, row in period_returns.iterrows():
            # Calculate weighted return
            daily_return = sum(weight * row[s] for s in stocks)

            # Prevent extreme spikes (safety, not hack)
            if abs(daily_return) > 0.05:
                daily_return = 0.05 if daily_return > 0 else -0.05

            portfolio_value *= (1 + daily_return)
            values.append(portfolio_value)

    # Attach proper dates
    return pd.Series(values, index=returns.index[:len(values)])