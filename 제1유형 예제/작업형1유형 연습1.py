
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('https://raw.githubusercontent.com/Datamanim/dataq/main/mtcars.csv', index_col= 0)
print(df)
# minmaxscale
from sklearn.preprocessing import MinMaxScaler
mm = MinMaxScaler()
df['qsec'] = mm.fit_transform(df[['qsec']])
# print(len(df[df['qsec'] > 0.5]))

# wt 컬럼 이상치
Q1 = df.wt.quantile(0.25)
Q3 = df.wt.quantile(0.75)
IQR = Q3 -Q1

outlier = df.wt[(df.wt >= Q3 + IQR * 1.5)|(df.wt <= Q1 - IQR *1.5)]
print(outlier)

# 상관게수

# print(df.corr()[['mpg']][1:].sort_values('mpg',ascending=False))

# mtcars 데이터셋에서 mpg변수를 제외하고 데이터 정규화 (standardscaler) 과정을 진행한 이후
# PCA를 통해 변수 축소를 하려한다.
# 누적설명 분산량이 92%를 넘기기 위해서는 몇개의 주성분을 선택해야하는지 설명

df1 = df.iloc[:,1:]
print(df1)
from sklearn.preprocessing import StandardScaler
ss= StandardScaler()
ss_df1 = ss.fit_transform(df1)
print(ss_df1)

# PCA
from sklearn.decomposition import PCA
num = 10
pca = PCA(n_components =num)
printpca = pca.fit_transform(ss_df1)
printpca_df = pd.DataFrame(printpca)
print(printpca_df)

componentDF = pd.DataFrame(pca.explained_variance_ratio_, columns =['cumsumVariance']).cumsum().reset_index()
componentDF['index'] +=1
componentDF = componentDF.rename(columns ={'index':'componentCount'})
print(componentDF)