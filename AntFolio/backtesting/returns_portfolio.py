from AntFolio.utils.imports import *

def portfolio_pct_returns(data: pd.DataFrame, tickers: pd.DataFrame, weights: list) -> pd.DataFrame:
    tickers = tickers['symbol'].to_list()
    returns = data['Adj Close'].pct_change(fill_method=None)
    returns = returns.fillna(0)
    returns = returns[tickers].copy()
    returns = returns.dot(weights)
    return returns

def portfolio_cum_returns(data: pd.DataFrame, tickers: pd.DataFrame, weights: list) -> pd.DataFrame:
    returns = portfolio_pct_returns(data, tickers, weights)
    cumulative_returns = (1 + returns).cumprod()
    return cumulative_returns

def portfolio_log_returns(data: pd.DataFrame, tickers: pd.DataFrame, weights: list) -> pd.DataFrame:
    tickers = tickers['symbol'].to_list()
    log_returns = np.log(data['Adj Close'] / data['Adj Close'].shift(1))
    log_returns = log_returns.fillna(0)
    log_returns = log_returns[tickers].copy()
    log_returns = log_returns.dot(weights)
    return log_returns
