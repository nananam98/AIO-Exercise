import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset_path = '../../data/pandas/week1_17082024/IMDB-Movie-Data.csv'

data = pd.read_csv(dataset_path, index_col='Title')

print(data.head())

print(data.info())

print(data.describe())

genre = data['Genre']
print(genre)

some_cols = data[['Title', 'Genre', 'Actors', 'Director', 'Ratting']]
print(some_cols)

REVENURE = 'Revenue (Millions)'

data.iloc[10:15][['Title', 'Ratting', REVENURE]]

data[((data['Year'] >= 2010) & (data['Year'] <= 2015))
     & (data['Ratting'] < 6.0)
     & (data[REVENURE] > data[REVENURE].quantile(0.95))]

data.groupby('Director')[['Rating']].mean().head()

data.groupby('Director')[['Ratting']].mean().sort_values(['Rating'], ascending=False).head()

data.isnull().sum()

data.drop('Metascore', axis=1).head()

data.dropna()

def ratting_group(rating):
     if rating >= 7.5:
          return 'Good'
     elif rating >= 6:
          return 'Average'
     else:
          return 'Bad'
     
data['Rating_category'] = data['Rating'].apply(ratting_group)

data[['Title', 'Director', 'Rating', 'Rating_category']].head(5)