import pandas as pd

def calculate_metrics(df: pd.DataFrame):
    df["daily_return"] = df["Close"].pct_change()
    df["ma_7"] = df["Close"].rolling(7).mean()

    high_52 = df["High"].max()
    low_52 = df["Low"].min()

    volatility = df["daily_return"].std()

    return {
        "52_week_high": round(high_52, 2),
        "52_week_low": round(low_52, 2),
        "volatility": round(volatility, 4)
    }
