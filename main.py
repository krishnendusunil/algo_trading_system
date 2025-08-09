import pandas as pd
from data_fetcher import fetch_stock_data
from strategy import backtest_strategy

def main():
    print("Starting Algo-Trading System...")

    tickers = ['RELIANCE.NS', 'TCS.NS', 'INFY.NS']
    all_trades = []

    stock_data = fetch_stock_data(tickers, period='6mo')

    for ticker, df in stock_data.items():
        print(f"\n--- Processing {ticker} ---")

        if df is not None and not df.empty:
            trades_df, total_pnl = backtest_strategy(df, ticker)

            try:
                total_pnl = float(total_pnl)
            except (TypeError, ValueError):
                total_pnl = 0.0

            if not trades_df.empty:
                print(f"Total P&L for {ticker}: {total_pnl:.2f}")
                trades_df['Ticker'] = ticker
                all_trades.append(trades_df)
            else:
                print(f"No trades were generated for {ticker}.")
        else:
            print(f"Skipping {ticker} due to no data.")

    if all_trades:
        final_trades_df = pd.concat(all_trades, ignore_index=True)
        pnl_col = 'PnL' if 'PnL' in final_trades_df.columns else 'P&L'

        print("\n--- Summary of All Trades ---")
        print(final_trades_df)
        print(f"\nOverall System P&L: {final_trades_df[pnl_col].sum():.2f}")
    else:
        print("\nNo trades were executed across all tickers.")

if __name__ == '__main__':
    main()
