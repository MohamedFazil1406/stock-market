from fastapi import APIRouter
from app.data.stocks import fetch_stock_data, clean_stock_data
from app.services.metrics import calculate_metrics
from app.data.company import get_companies_stocks

router = APIRouter(prefix="/stocks", tags=["Stocks"])

@router.get("/companies")
def companies():
    return get_companies_stocks()

@router.get("/compare")
def compare_stocks(stock1: str, stock2: str):
    # Stock 1
    df1 = fetch_stock_data(stock1)
    df1 = clean_stock_data(df1)
    metrics1 = calculate_metrics(df1)

    # Stock 2
    df2 = fetch_stock_data(stock2)
    df2 = clean_stock_data(df2)
    metrics2 = calculate_metrics(df2)

    return {
        "stock_1": {
            "symbol": stock1,
            "metrics": metrics1
        },
        "stock_2": {
            "symbol": stock2,
            "metrics": metrics2
        }
    }

@router.get("/top-movers")
def top_gainers_losers():
    companies = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA"]
    results = []

    for symbol in companies:
        df = fetch_stock_data(symbol)
        df = clean_stock_data(df)

        # calculate daily return
        df["daily_return"] = df["Close"].pct_change()

        latest = df.tail(1)

        if not latest.empty:
            results.append({
                "symbol": symbol,
                "daily_return": float(latest["daily_return"].values[0])
            })

    # sort gainers & losers
    gainers = sorted(results, key=lambda x: x["daily_return"], reverse=True)[:3]
    losers = sorted(results, key=lambda x: x["daily_return"])[:3]

    return {
        "top_gainers": gainers,
        "top_losers": losers
    }


@router.get("/{symbol}")
def get_stock(symbol: str):
    df = fetch_stock_data(symbol)
    df = clean_stock_data(df)

    return df.tail(5).to_dict(orient="records")

@router.get("/{symbol}/summary")
def stock_summary(symbol: str):
    df = fetch_stock_data(symbol)
    df = clean_stock_data(df)

    return calculate_metrics(df)


