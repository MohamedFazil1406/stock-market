import matplotlib.pyplot as plt
from app.data.stocks import fetch_stock_data, clean_stock_data

def plot_stock(symbol: str):
    df = fetch_stock_data(symbol)
    df = clean_stock_data(df)

    df["ma_7"] = df["Close"].rolling(7).mean()

    plt.figure()
    plt.plot(df["Date"], df["Close"], label="Close Price")
    plt.plot(df["Date"], df["ma_7"], label="7-Day Moving Average")

    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.title(f"{symbol} Stock Price Trend")
    plt.legend()
    plt.show()



if __name__ == "__main__":
    plot_stock("AAPL")
