import pandas as pd
import os

def save_trades_to_csv(trades_df, filename="trades.csv"):
    """Saves a DataFrame of trades to a CSV file."""
    if not trades_df.empty:
        if os.path.exists(filename) and os.path.getsize(filename) > 0:
            trades_df.to_csv(filename, mode='a', header=False, index=False)
        else:
            trades_df.to_csv(filename, mode='a', header=True, index=False)
        print(f"Trades logged to {filename}")

def read_trades_from_csv(filename="trades.csv"):
    """Reads trades from a CSV file."""
    if os.path.exists(filename):
        return pd.read_csv(filename)
    return pd.DataFrame()

def calculate_pnl_summary(trades_df):
    """Calculates summary P&L and win ratio from a trades DataFrame."""
    if trades_df.empty or ('P&L' not in trades_df.columns and 'PnL' not in trades_df.columns):
        return {'Total P&L': 0, 'Win Ratio': 0, 'Total Trades': 0}

    pnl_col = 'P&L' if 'P&L' in trades_df.columns else 'PnL'
    total_pnl = float(trades_df[pnl_col].sum())

    winning_trades = (trades_df[pnl_col] > 0).sum()
    total_trades = len(trades_df)
    win_ratio = (winning_trades / total_trades) * 100 if total_trades > 0 else 0

    return {
        'Total P&L': total_pnl,
        'Win Ratio': f"{win_ratio:.2f}%",
        'Total Trades': total_trades
    }

def update_summary_csv(summary_data, filename="summary_pnl.csv"):
    """Saves summary data to a CSV file, overwriting old data."""
    summary_df = pd.DataFrame([summary_data])
    summary_df.to_csv(filename, index=False)
    print(f"Summary P&L updated in {filename}")

def update_win_ratio_csv(win_ratio_data, filename="win_ratio.csv"):
    """Saves win ratio data to a CSV file, overwriting old data."""
    win_ratio_df = pd.DataFrame([win_ratio_data])
    win_ratio_df.to_csv(filename, index=False)
    print(f"Win Ratio updated in {filename}")
