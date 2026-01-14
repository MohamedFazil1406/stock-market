from fastapi import FastAPI
from app.routes.stocks import router as stock_router
from app.visualization.plot_stock import plot_stock
from app.visualization.plot_stock import plot_stock
from app.visualization.plot_top_movers import plot_top_movers

app = FastAPI(title="Stock Market API")

app.include_router(stock_router)

@app.get("/")
def root():
    return {"message": "Stock Market Backend is running"}





