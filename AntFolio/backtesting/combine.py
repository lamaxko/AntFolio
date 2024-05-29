from AntFolio.utils.imports import *

def combine_cumulative_returns(*cumulative_returns, portfolio_names):
    combined_df = pd.concat(cumulative_returns, axis=1)
    combined_df.columns = portfolio_names
    return combined_df