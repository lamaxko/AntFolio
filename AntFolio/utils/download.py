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

    tickers_in_data = data['Adj Close'].columns
    # make tickers in data to a df with the ticke as a rows in the column symbol and then merge with the tickers df
    tickers_in_data = pd.DataFrame(tickers_in_data, columns=['symbol'])
    tickers_in_data = tickers_df.merge(tickers_in_data, on='symbol', how='inner')
    
    # remove doublicate symbols for the tickers df
    tickers_in_data = tickers_in_data.drop_duplicates(subset='symbol')
    

    logging.info(f"From the initial {tickers_before} tickers, {len(tickers_in_data)} were successfully downloaded and retained.")

    # create combinded df wiht column one containing the tickers in the data cold and col 2 the ticker of the updated tickers df
    aligned_df = pd.DataFrame(data['Adj Close'].columns, columns=['symbol'])

    return data, tickers_in_data