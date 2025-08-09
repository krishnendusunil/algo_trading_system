import streamlit as st
import pandas as pd
from utils import save_trades_to_csv, read_trades_from_csv

st.title("Trade Logger")

# Sample trades data
trades = [
    {"stock": "AAPL", "price": 150.0, "quantity": 10},
    {"stock": "TSLA", "price": 720.5, "quantity": 5}
]

if st.button("Save Trades"):
    df_trades = pd.DataFrame(trades)
    save_trades_to_csv(df_trades)
    st.success("Trades saved to CSV")

if st.button("Load Trades"):
    df = read_trades_from_csv()
    st.dataframe(df)
