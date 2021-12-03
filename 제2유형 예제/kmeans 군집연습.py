import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('https://raw.githubusercontent.com/Datamanim/dataq/main/mtcars.csv', index_col='Unnamed: 0')

from sklearn.cluster import KMeans
# print(help(KMeans))

km = KMeans(n_clusters=3, random_state=42)
kmdf = km.fit(df)
df['cluster'] = kmdf.labels_
print(df)

from sklearn.metrics import silhouette_samples, silhouette_score
sample_score = silhouette_samples(df.drop('cluster',axis=1),df['cluster'])
df['silhouette_score'] = sample_score
print(df)