from .imports import *

def get_tickers(dataset: str = 'sp500') -> pd.DataFrame:
    """
    Fetches ticker data from a specified dataset.

    Parameters:
    dataset (str): The dataset to fetch tickers from. Default is 'sp500'.

    Returns:
    pd.DataFrame: DataFrame containing ticker data.
    
    Raises:
    ValueError: If the specified dataset is not supported.
    """
    datasets = ['eurostoxx600', 'sp500', 'nasdaq100', 'nikkei225', 'msciem', 'msciworld', 'msciindia', 'mscichina']
    if dataset not in datasets:
        raise ValueError(f"Dataset '{dataset}' is not supported. Please choose from {datasets}.")
    
    file_path = f'AntFolio/data/{dataset}.csv'
    return pd.read_csv(file_path, delimiter=';')