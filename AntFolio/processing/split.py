from AntFolio.utils.imports import *

def train_test_split(data: pd.DataFrame, train_start: str, train_end: str, test_start: str, test_end: str) -> tuple:
    train_start = pd.to_datetime(train_start)
    train_end = pd.to_datetime(train_end)
    test_start = pd.to_datetime(test_start)
    test_end = pd.to_datetime(test_end)
  
    train_data = data.loc[train_start:train_end].copy()
    test_data = data.loc[test_start:test_end].copy()

    return train_data, test_data