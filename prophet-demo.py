#prophet-demo.py

import pandas as pd
import seaborn as sns
from fbprophet import Prophet

df = pd.read_csv('DATA/time_series_60min_singleindex.csv',  usecols=['utc_timestamp','AT_solar_generation_actual'], names=['ds','y'], parse_dates =['utc_timestamp'], infer_datetime_format=True,  nrows=100000)

sns.lineplot(x='utc_timestamp', y='AT_solar_generation_actual', data=df)