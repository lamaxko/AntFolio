from AntFolio.utils.imports import *

def benchmark_equal_weights(tickers: pd.DataFrame) -> pd.DataFrame:
    tickers = tickers['symbol'].to_list()
    weights = [1/len(tickers) for _ in tickers]
    
    return weights