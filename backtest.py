import pandas as pd
import matplotlib.pyplot as plt

timeframe = "M15"
symbol = "SPX500"
timezone = "America/New_York"

df = pd.read_csv(f"data/{symbol}_{timeframe}.csv",parse_dates=["Datetime"],index_col="Datetime")
df.index = pd.to_datetime(df.index, utc=True).tz_convert(timezone)
df = df.loc["2019-12-31":]

