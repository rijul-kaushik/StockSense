def rebalance(score_df, freq=30, top_n=5):
    portfolios = []

    for i in range(freq, len(score_df), freq):
        current_scores = score_df.iloc[:i]

        latest_scores = current_scores.iloc[-1]
        selected = latest_scores.nlargest(top_n).index.tolist()

        portfolios.append({
            "day": i,
            "stocks": selected
        })

    return portfolios