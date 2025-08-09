import gspread
from datetime import datetime
import pandas as pd

def _df_to_rows(df):
    return [df.columns.tolist()] + df.astype(str).values.tolist()

def log_to_google_sheets(final_trades_df, summary_dict, spreadsheet_name="Algo_Trading_Logs", creds_json="gcp_credentials.json"):
    """
    Logs 3 sheets:
    - 'trade_log' : final_trades_df
    - 'summary' : single-row summary from summary_dict
    - 'win_ratio' : single-row with win ratio info
    """
    gc = gspread.service_account(filename=creds_json)
    try:
        sh = gc.open(spreadsheet_name)
    except gspread.SpreadsheetNotFound:
        sh = gc.create(spreadsheet_name)
        print(f"Created new spreadsheet: {spreadsheet_name}")
        # Remember to share this sheet with your service account email manually

    # Trade log
    try:
        ws = sh.worksheet("trade_log")
        sh.del_worksheet(ws)
    except gspread.WorksheetNotFound:
        pass
    ws_trade = sh.add_worksheet("trade_log", rows=str(len(final_trades_df)+10), cols="20")
    ws_trade.update("A1", _df_to_rows(final_trades_df))

    # Summary
    try:
        ws = sh.worksheet("summary")
        sh.del_worksheet(ws)
    except gspread.WorksheetNotFound:
        pass
    ws_sum = sh.add_worksheet("summary", rows="10", cols="5")
    sum_df = pd.DataFrame([summary_dict])
    ws_sum.update("A1", _df_to_rows(sum_df))

    # Win ratio
    try:
        ws = sh.worksheet("win_ratio")
        sh.del_worksheet(ws)
    except gspread.WorksheetNotFound:
        pass
    ws_wr = sh.add_worksheet("win_ratio", rows="5", cols="5")
    win_df = pd.DataFrame([{
        'Win Ratio': summary_dict.get('Win Ratio', 0.0),
        'Wins': summary_dict.get('Wins', 0),
        'Sells': summary_dict.get('Number of Sells', 0),
        'Logged At': datetime.now().isoformat()
    }])
    ws_wr.update("A1", _df_to_rows(win_df))

    print("✅ Logged to Google Sheets:", spreadsheet_name)
