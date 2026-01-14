import matplotlib.pyplot as plt
from app.routes.stocks import top_gainers_losers

def plot_top_movers():
    data = top_gainers_losers()

    gainers = data["top_gainers"]
    losers = data["top_losers"]

    symbols = [x["symbol"] for x in gainers + losers]
    returns = [x["daily_return"] for x in gainers + losers]

    plt.figure()
    plt.bar(symbols, returns)
    plt.axhline(0)
    plt.title("Top Gainers and Losers")
    plt.ylabel("Daily Return")
    plt.show()



if __name__ == "__main__":
    plot_top_movers()