import pandas as pd
import matplotlib.pyplot as plt

timeframe = "M15"
symbol = "SPX500"
timezone = "America/New_York"


def price_data(symbol):
    '''Load data for a given symbol from a CSV file and process it.

    Parameters
    ----------
    symbol : str
        The ticker symbol of the asset whose price data is being loaded.

    Returns
    -------
    pandas.DataFrame
        A DataFrame containing the price data, with 'Datetime' as the index,
        localized to the specified timezone and filtered from '2020-12-31' onward.
    '''

    df = pd.read_csv(f"data/{symbol}_{timeframe}.csv",parse_dates=["Datetime"],index_col="Datetime")
    df.index = pd.to_datetime(df.index, utc=True).tz_convert(timezone)
    df = df.loc["2019-12-31":]
    return df




