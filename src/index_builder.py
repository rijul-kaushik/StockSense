def select_top_stocks(score_df, top_n=5):
    latest_scores = score_df.iloc[-1]
    return latest_scores.nlargest(top_n).index.tolist()


def assign_equal_weights(stocks):
    weight = 1 / len(stocks)
    return {stock: weight for stock in stocks}


def assign_weight_by_score(score_df, selected_stocks):
    latest_scores = score_df.iloc[-1][selected_stocks]
    total = latest_scores.sum()
    weights = latest_scores / total
    return weights.to_dict()