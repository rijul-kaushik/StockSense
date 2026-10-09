import sqlite3
import pandas as pd

def save_to_db(df):
    conn = sqlite3.connect("../data/stocks.db")
    df.to_sql("prices", conn, if_exists="replace", index=True)
    conn.close()
    print("Data saved to database")

def load_from_db():
    conn = sqlite3.connect("../data/stocks.db")
    df = pd.read_sql("SELECT * FROM prices", conn, index_col="Date", parse_dates=True)
    conn.close()
    return df