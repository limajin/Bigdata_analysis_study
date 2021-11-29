'''
신뢰구간, 카이제곱 구하기
'''

import pandas as pd
pd.set_option('max_columns', None)
# 데이터프레임의 모든열을 보이게 출력

import numpy as np
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('https://raw.githubusercontent.com/Datamanim/dataq/main/mtcars.csv', index_col='Unnamed: 0')
print(df.head(5))


'''ddof=1이 불편추정'''
불편분산1 = np.round(np.var(df.mpg, ddof=1),3)
불편분산2 = df.mpg.var().round(3)
# print('불편분산1:', 불편분산1)
# print('불편분산2:', 불편분산2)

불편표준편차1 = np.round(np.std(df.mpg, ddof=1),3)
불편표준편차2 = df.mpg.std().round(3)
# print('불편표준편차1:', 불편표준편차1)
# print('불편표준편차2:', 불편표준편차2)

공분산행렬 = np.cov(df.mpg, df.am, ddof=1)
# print(공분산행렬)

상관행렬 = df[['mpg','am']].corr()
# print(상관행렬)

'''추측 통계 mpg 컬럼으로 해보기'''
mpg = df.mpg

평균 = mpg.mean().round(3)
# print('평균: ', 평균)

자유도 = len(mpg)-1
# print('자유도: ', 자유도)


표준오차1 = np.std(mpg, ddof=1)/ np.sqrt(len(mpg))
표준오차2 = mpg.std()/np.sqrt(len(mpg)-1)
# print(표준오차1)
# print(표준오차2)

'''신뢰구간 계산하기'''
from scipy import stats
import scipy
# print(help(stats.t.interval))
# print(scipy.__all__)

'''df는 degree of freedom으로 자유도'''
interval = stats.t.interval(alpha=0.95, df=자유도, loc=평균, scale=표준오차1)
# print(interval)


'''
하측신뢰한계, 상측신뢰한계 구하기, ppf(Percent Point Function) 이용
print(interval)과 같은 결과가 나온다.
'''
t_975 = stats.t.ppf(q=0.975, df=자유도)
하측 = 평균 - t_975 * 표준오차1
상측 = 평균 + t_975 * 표준오차1
# print(하측, 상측)

'''피벗테이블에서 카이제곱값 구하기'''
문제 = df[['vs','am','mpg']]
print(문제)
pivot = pd.pivot_table(문제, values='mpg', index='vs',columns='am',aggfunc='sum')
print(pivot)

chi2 = stats.chi2_contingency(pivot)
print("카이제곱: ", chi2)
# 첫줄에 나오는 건 카이스퀘어 통계량.
# 두번째 줄은 p값
# 세번째는 자유도
# 그 밑에 표는 귀무가설의 기대도수표이다.
print(chi2[0])