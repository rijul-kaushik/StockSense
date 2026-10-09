import pandas as pd

def compute_returns(price_df):
    return price_df.pct_change()

def compute_momentum(price_df, window=30):
    return price_df.pct_change(window)

def compute_volatility(price_df, window=30):
    return price_df.pct_change().rolling(window).std()

def clean_data(df):
    return df.dropna()