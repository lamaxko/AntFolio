from AntFolio.utils.imports import *
from .returns import *

warnings.filterwarnings('ignore', category=RuntimeWarning)  # Suppress specific runtime warnings

def fit_best_distribution(stock_returns: pd.Series) -> tuple:
    distributions = {
        'genextreme': stats.genextreme,
        'logistic': stats.logistic,
        'norm': stats.norm
    }
    
    best_distribution = None
    best_p_value = -np.inf
    
    for dist_name, dist in distributions.items():
        params = dist.fit(stock_returns)
        D, p_value = stats.kstest(stock_returns, dist_name, args=params)
        
        if p_value > best_p_value:
            best_p_value = p_value
            best_distribution = dist_name, params
    
    return best_distribution

def transform_to_uniform(data: pd.DataFrame, empirical=False) -> pd.DataFrame:
    pct_returns = get_pct_returns(data)
    uniform_returns = pd.DataFrame(index=pct_returns.index)

    for column in pct_returns.columns:
        if empirical:
            ecdf = ECDF(pct_returns[column].dropna())
            cdf_values = ecdf(pct_returns[column])
        else:
            dist_name, params = fit_best_distribution(pct_returns[column])
            dist = getattr(stats, dist_name)
            cdf_values = dist.cdf(pct_returns[column], *params)
        
        uniform_data = stats.uniform.ppf(cdf_values)
        uniform_returns[column] = uniform_data
    
    return uniform_returns
