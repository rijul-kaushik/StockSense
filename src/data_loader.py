import yfinance as yf
import pandas as pd
import os
from database import save_to_db

def get_stock_data(tickers, start="2018-01-01", end="2024-01-01"):
    print("Fetching stock data...")
    
    data = yf.download(tickers, start=start, end=end)

    # Extract Adjusted Close prices
    price_df = data["Close"]

    return price_df


def save_data(df, path="../data/stock_data.csv"):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_csv(path)
    print(f"Data saved at {path}")


if __name__ == "__main__":
    stocks = [
    "RELIANCE.NS","TCS.NS","INFY.NS","HDFCBANK.NS","ICICIBANK.NS",
    "HINDUNILVR.NS","SBIN.NS","BAJFINANCE.NS","KOTAKBANK.NS","LT.NS",
    "AXISBANK.NS","ASIANPAINT.NS","MARUTI.NS","SUNPHARMA.NS","ULTRACEMCO.NS",
    "WIPRO.NS","NTPC.NS","POWERGRID.NS","TITAN.NS","NESTLEIND.NS",
    "HCLTECH.NS","TECHM.NS","ONGC.NS","COALINDIA.NS","JSWSTEEL.NS",
    "TATASTEEL.NS","INDUSINDBK.NS","ADANIENT.NS","ADANIPORTS.NS",
    "BAJAJFINSV.NS","DIVISLAB.NS","DRREDDY.NS","CIPLA.NS",
    "GRASIM.NS","BRITANNIA.NS","EICHERMOT.NS","HEROMOTOCO.NS",
    "SHREECEM.NS","BPCL.NS","IOC.NS","UPL.NS","M&M.NS","^NSEI"
]

    df = get_stock_data(stocks)

    # Clean data
    df = df.dropna()

    print(df.head())

    save_data(df)
    save_to_db(df)