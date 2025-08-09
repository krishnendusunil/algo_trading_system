import pandas as pd

def rsi(series, period=14):
    delta = series.diff()
    gain = delta.where(delta > 0, 0.0)
    loss = -delta.where(delta < 0, 0.0)

    avg_gain = gain.rolling(window=period, min_periods=period).mean()
    avg_loss = loss.rolling(window=period, min_periods=period).mean()

    rs = avg_gain / avg_loss
    rsi_series = 100 - (100 / (1 + rs))
    return rsi_series

def generate_signals(df, rsi_period=14, rsi_overbought=70, rsi_oversold=30):
    df = df.copy()

    # Flatten multi-index columns from yfinance
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = ['_'.join(col).strip() if isinstance(col, tuple) else col for col in df.columns]

    close_col = [col for col in df.columns if 'Close' in col][0]
    df['Close'] = pd.to_numeric(df[close_col], errors='coerce')

    df['RSI'] = rsi(df['Close'], period=rsi_period)

    df['Signal'] = 0
    df.loc[df['RSI'] < rsi_oversold, 'Signal'] = 1  # Buy
    df.loc[df['RSI'] > rsi_overbought, 'Signal'] = -1  # Sell

    return df

def backtest_strategy(df, ticker=None, initial_balance=100000):
    df = generate_signals(df)
    balance = initial_balance
    position = 0
    trade_log = []
    last_buy_price = None

    for i in range(len(df)):
        signal = df['Signal'].iloc[i]
        close_price = df['Close'].iloc[i]

        if pd.isna(close_price):
            continue

        if signal == 1 and position == 0:
            position = balance / close_price
            balance = 0
            last_buy_price = close_price
            trade_log.append({'Date': df.index[i], 'Action': 'BUY', 'Price': close_price, 'P&L': 0})

        elif signal == -1 and position > 0:
            balance = position * close_price
            pnl = (close_price - last_buy_price) * position
            position = 0
            trade_log.append({'Date': df.index[i], 'Action': 'SELL', 'Price': close_price, 'P&L': pnl})

    final_value = balance + (position * df['Close'].iloc[-1])
    total_profit = final_value - initial_balance

    trades_df = pd.DataFrame(trade_log)
    if ticker:
        trades_df["Ticker"] = ticker

    return trades_df, total_profit
