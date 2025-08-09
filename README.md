# Mini Algo-Trading System in Python

## Overview

This project implements a simple algorithmic trading system that:

- Fetches daily stock data for selected NIFTY 50 stocks using the Yahoo Finance API (`yfinance`).
- Applies a trading strategy based on RSI (Relative Strength Index) and Moving Average crossover signals.
- Backtests the strategy over six months of historical data.
- Uses a Decision Tree machine learning model to predict next-day stock price movement based on technical indicators.
- Logs trades, profit & loss summary, and win ratios automatically to Google Sheets.
- Designed with modular, easy-to-understand Python scripts.

## Features

- Data ingestion from Yahoo Finance  
- RSI and 20-day / 50-day moving average crossover strategy  
- Backtesting with detailed trade logs and P&L calculations  
- Basic ML model for price movement prediction with accuracy output  
- Google Sheets integration for trade and summary logging  
- Modular codebase for easy maintenance and extensions

## Installation

1. Clone the repository


2. Create and activate a Python virtual environment:

python -m venv venv

# On Windows
venv\Scripts\activate

3. Install dependencies:

pip install -r requirements.txt

4. Set up Google Sheets API credentials:

# Create a Google Cloud project and enable Google Sheets API.
# Create a service account and download the JSON credentials file.
# Rename the file to gcp_credentials.json and place it in the project root.

5. Run the main script

python main.py

# The script will fetch stock data, run the backtest, train the ML model, and log trade results to Google Sheets.

# Monitor console output for trade logs, P&L summary, and ML accuracy.

6. File Structure
main.py — Runs the full pipeline

data_fetcher.py — Fetches stock data

strategy.py — RSI + Moving Average strategy and backtesting

ml_model.py — Machine learning model for price movement prediction

google_sheets.py — Logs trades and summaries to Google Sheets

utils.py — Helper functions for CSV handling and metrics

telegram_alert.py (optional) — Telegram alerts for trades

requirements.txt — List of Python dependencies

7. Extending the Project
Add additional technical indicators (e.g., MACD, Bollinger Bands)

Use intraday data for more granular strategies

Enhance ML model with hyperparameter tuning or other algorithms

Build an interactive dashboard with Streamlit or Dash

Automate script execution with cron or Task Scheduler

8. License
# MIT License
