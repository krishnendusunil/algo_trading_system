import yfinance as yf
import pandas as pd
import time

def fetch_stock_data(tickers, period='1y', interval='1d'):
    """
    Fetch stock data for given tickers using yfinance.
    Returns a dictionary {ticker: DataFrame}.
    """
    stock_data = {}
    for ticker in tickers:
        print(f"Fetching data for {ticker}...")
        try:
            df = yf.download(ticker, period=period, interval=interval, auto_adjust=True)
            if not df.empty:
                df.dropna(inplace=True)
                stock_data[ticker] = df
            else:
                print(f"No data for {ticker}")
                stock_data[ticker] = pd.DataFrame()
        except Exception as e:
            print(f"Error fetching {ticker}: {e}")
            stock_data[ticker] = pd.DataFrame()
        time.sleep(1)  # Avoid hitting API limits
    return stock_data
