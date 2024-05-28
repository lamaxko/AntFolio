from .imports import *

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def download_data(tickers_df: pd.DataFrame, start_date: str, end_date: str) -> (pd.DataFrame):
    try:
        tickers = tickers_df['symbol'].tolist()
        data = yf.download(tickers, start=start_date, end=end_date)
    except Exception as e:
        return pd.DataFrame(), tickers_df
    
    failed_downloads = list(shared._ERRORS.keys())
    tickers_to_remove = []
    tickers_before = len(tickers)

    if failed_downloads:
        tickers_to_remove.extend(failed_downloads)
        logging.info(f"Tickers identified for removal due to download failures: {failed_downloads}")

    cols_with_all_nan = [col for col in data.columns if data[col].isna().all()]
    if cols_with_all_nan:
        data = data.drop(columns=cols_with_all_nan)

    tickers_remaining = [ticker for ticker in tickers if ticker not in tickers_to_remove]
    updated_tickers_df = tickers_df[tickers_df['symbol'].isin(tickers_remaining)]

    logging.info(f"From the initial {tickers_before} tickers, {len(tickers_remaining)} were successfully downloaded and retained.")

    return data, updated_tickers_df
