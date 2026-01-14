import yfinance as yf
import pandas as pd

def fetch_stock_data(symbol: str):
    stock = yf.Ticker(symbol)
    
    df = stock.history(period="1y")

    df.reset_index(inplace=True)
    print(df.head())

    return df

def clean_stock_data(df: pd.DataFrame):
    df = df.dropna()

    df["Date"] = pd.to_datetime(df["Date"])

    return df

