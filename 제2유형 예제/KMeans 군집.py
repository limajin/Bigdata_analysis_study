'''
KMeans를 이용하여 데이터들을 군집 3개로 분류하고 평가하라
'''


# 답안 제출 예시
# print(레코드 수)

import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('https://raw.githubusercontent.com/Datamanim/dataq/main/mtcars.csv', index_col='Unnamed: 0')

#print(df)

# KMeans로 군집을 3개로 분류 분석
from sklearn.cluster import KMeans
import sklearn
import sklearn.cluster
# print(help(sklearn.cluster.KMeans))

kmeans = KMeans(n_clusters=3, random_state=107).fit(df)
# print(kmeans.labels_)

# df에 군집 결과 컬럼 추가
df['cluster'] = kmeans.labels_
# print(df)

# df 실루엣계수 추가
import sklearn.metrics
# print(dir(sklearn.metrics))

from sklearn.metrics import silhouette_samples, silhouette_score
# siluhouette_samples 는 모든 개별 데이터에 실루엣 계수 값이 들어가는 열이 나옴
samples_score = silhouette_samples(df.drop('cluster', axis=1), df['cluster'])
df['silhouette_score'] = samples_score
# print(df.head(5))

# 모든 데이터의 평균 실루엣 계수
avg_score = silhouette_score(df.drop('cluster',axis=1), df['cluster'])
# print('모든 데이터의 평균 실루엣 계수', avg_score)

# 그룹바이하여 군집별로 평균 실루엣 계수 값 확인
# print(df.groupby('cluster').mean())
# print(df.groupby('cluster')['silhouette_score'].mean())