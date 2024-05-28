import unittest
import pandas as pd
from AntFolio import get_tickers, download_data

class TestGetTickers(unittest.TestCase):
    datasets = {
        'eurostoxx600': {
            'first_row': ['NOVO B', 'NOVO NORDISK CLASS B', 'Health Care'],
            'last_row': ['CHF', 'CHF CASH', 'Cash and/or Derivatives'],
            'total': 622
        },
        'sp500': {
            'first_row': ['MMM', '3M', 'Industrials'],
            'last_row': ['ZTS', 'Zoetis', 'Health Care'],
            'total': 505
        },
        'nasdaq100': {
            'first_row': ['MSFT', 'MICROSOFT CORP', 'Information Technology'],
            'last_row': ['USD', 'USD/EUR', 'Cash and/or Derivatives'],
            'total': 108
        },
        'nikkei225': {
            'first_row': ['71N', 'NISSUI CORP.', 'Fishery'],
            'last_row': ['SFT', 'SOFTBANK GROUP CORP.', 'Communications'],
            'total': 225
        },
        'msciem': {
            'first_row': ['2330', 'TAIWAN SEMICONDUCTOR MANUFACTURING', 'Information Technology'],
            'last_row': ['FIVE', 'X5 RETAIL GROUP GDR NV', 'Consumer Staples'],
            'total': 919
        },
        'msciworld': {
            'first_row': ['MSFT', 'MICROSOFT CORP', 'Information Technology'],
            'last_row': ['SEK', 'SEK/USD', 'Cash and/or Derivatives'],
            'total': 1493
        },
        'msciindia': {
            'first_row': ['RELIANCE', 'RELIANCE INDUSTRIES LTD', 'Energy'],
            'last_row': ['ZVLM4', 'MSCI INDIA INDEX JUN 24', 'Cash and/or Derivatives'],
            'total': 144
        },
        'mscichina': {
            'first_row': ['700', 'TENCENT HOLDINGS LTD', 'Communication'],
            'last_row': ['MCYM4', 'MSCI CHINA A 50 CONNECT JUN 24', 'Cash and/or Derivatives'],
            'total': 710
        }
    }

    def test_get_tickers(self):
        for dataset, expected in self.datasets.items():
            with self.subTest(dataset=dataset):
                df = get_tickers(dataset)
                self.assertEqual(df.shape[0], expected['total'], f"Total rows mismatch for {dataset}")
                self.assertEqual(df.iloc[0].tolist(), expected['first_row'], f"First row mismatch for {dataset}")
                self.assertEqual(df.iloc[-1].tolist(), expected['last_row'], f"Last row mismatch for {dataset}")

if __name__ == '__main__':
    unittest.main()
