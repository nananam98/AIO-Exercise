import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataset_path = '../../data/pandas/week1_17082024/opsd_germany_daily.csv'

opsd_daily = pd.read_csv(dataset_path)

print(opsd_daily.shape)
print(opsd_daily.dtypes)
opsd_daily.head(3)

opsd_daily = opsd_daily.set_index('Date')
opsd_daily.head(3)

opsd_daily = pd.read_csv(dataset_path, index_col=0, parse_dates=True)

opsd_daily['Year'] = opsd_daily.index.year
opsd_daily['Month'] = opsd_daily.index.month
opsd_daily['Weekday Name'] = opsd_daily.index.day_name()

print(opsd_daily.sample(5, random_state=0))

print(opsd_daily.loc['2014-01-20':'2014-01-22'])

print(opsd_daily.loc['2012-02'])

sns.set(rc={'figure.figsize':(11, 4)})
opsd_daily['Consumption'].plot(linewidth=0.5)