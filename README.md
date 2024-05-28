# AntFolio

Scaffolding to faster develop, backtest, and evaluate asset allocation strategies.

## Overview

AntFolio is designed to provide all the helper functions you may need, so you can focus on creating your strategy without constantly rewriting data fetching, formatting, plotting functions, and more.

## Features

### Built-in Tickers
AntFolio includes tickers for:
- MSCI World
- MSCI EM
- MSCI India
- MSCI China
- EUROSTOXX600
- NASDAQ100
- NIKKEI225
- S&P500

### Getting Started

1. **Get Tickers**: Use `get_tickers()` to retrieve the available tickers.
2. **Download Data**: Use `download_data()` to download the data for these tickers.
3. **Split Data**: Use `train_test_split()` to split the data into training and testing sets.

### Data Processing

AntFolio offers several processing functions:

- `get_pct_returns()`: Calculate percentage returns.
- `get_cum_returns()`: Calculate cumulative returns.
- `get_log_returns()`: Calculate logarithmic returns.
- `transform_to_uniform()`: Format returns to uniform margins using either their empirical CDF or the best fitting Copulas from Genextreme, normal, and logistic.

## Development

Further functionality is currently under development. Suggestions are welcome!

---
