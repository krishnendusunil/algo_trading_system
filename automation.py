import pandas as pd

def apply_indicators_without_talib(df):
    # Make sure 'Close' column exists and drop NA if any
    df = df.dropna(subset=['Close']).copy()

    # Calculate moving averages
    df['20DMA'] = df['Close'].rolling(window=20).mean()
    df['50DMA'] = df['Close'].rolling(window=50).mean()

    # Calculate RSI without talib
    delta = df['Close'].diff(1)
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    avg_gain = gain.ewm(com=13, adjust=False).mean()
    avg_loss = loss.ewm(com=13, adjust=False).mean()

    rs = avg_gain / avg_loss
    df['RSI'] = 100 - (100 / (1 + rs))

    return df


def generate_signals(df):
    df = apply_indicators_without_talib(df)
    df['Buy_Signal'] = (df['RSI'] < 30) & (df['20DMA'] > df['50DMA'])
    df['Sell_Signal'] = (df['RSI'] > 70) & (df['20DMA'] < df['50DMA'])
    return df


# Example usage:
# import yfinance as yf
# df = yf.download('AAPL', start='2022-01-01', end='2023-01-01')
# df_signals = generate_signals(df.copy())
# print(df_signals[['Close', 'RSI', 'Buy_Signal', 'Sell_Signal']].tail())
