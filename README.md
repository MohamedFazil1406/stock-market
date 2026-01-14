# Stock Market Data Backend (FastAPI)

This project is a backend stock market data platform built using **Python and FastAPI**.  
It fetches real stock data, cleans it, calculates financial metrics, and exposes REST APIs with Swagger documentation.

---

## Features

- Fetch 1-year historical stock data using yfinance
- Data cleaning and preprocessing
- Financial metrics:
  - Daily Returns
  - 7-Day Moving Average
  - 52-Week High & Low
  - Volatility
- REST APIs using FastAPI
- Swagger UI for API testing
- Optional data visualization using Matplotlib
- Top gainers and losers analysis

---

## Tech Stack

- Python
- FastAPI
- Pandas
- NumPy
- yfinance
- Matplotlib

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone <your-github-repo-url>
cd stock-market-backend
```

### 2. Create and activate virtual environment

```bash
python -m venv venv
source venv/bin/activate # Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the backend server

```bash
uvicorn app.main:app --reload
```

# API Documentation (Swagger)

## Once the server is running, open:

http://127.0.0.1:8000/docs

# Visualization (Optional)

-----A simple visualization is implemented using Matplotlib to: ------

-Plot stock closing prices
-Show 7-day moving average trends

-Display top gainers and losers

```bash
Run:

python -m app.visualization.plot_stock
python -m app.visualization.plot_top_movers~

```

# Demo Video

https://drive.google.com/file/d/15LH_PnaRjZh0d1aBFknO1-FvzKdkbO02/view?usp=sharing
