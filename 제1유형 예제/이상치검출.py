'''
이상치 검출 및 제거
실제 실기시험에선 평균으로부터 표준편차의 1.5배 만큼 떨어진
데이터를 이상값으로 찾는 문제가 출제되었음
'''


import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import numpy as np

pd.set_option('max_columns', None)
df = pd.read_csv('https://raw.githubusercontent.com/Datamanim/dataq/main/mtcars.csv', index_col='Unnamed: 0')

# print(df)

###################################
####quantile로 이상치 검출 및 제거####
###################################

Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)

IQR = Q3 -Q1

# print(IQR)

#조건으로 찾기
cond = (df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 *IQR))
# print(df[cond])
# print(cond[cond.mpg == True].index[0])


#데이터프레임으로 찾기
outlier = df[(df < Q1 - 1.5 *IQR) | (df > Q3 + 1.5 *IQR)]
# print(outlier[outlier['mpg'].notnull()].index[0])


###################################
####describe로 이상치 검출 및 제거####
###################################

'''
iloc는 인덱싱, 슬라이싱, 팬시 인덱싱은 제공, 불린인덱싱은 제공하지 않음
'''

# df.reset_index(inplace=True)
# print(df)
# print(df.loc[0,'hp'])

# print(df.describe())
일분위 = df.describe().iloc[4]
삼분위 = df.describe().iloc[6]
iqr = 삼분위 - 일분위
# print(iqr)

condition = (df<일분위-1.5*iqr)|(df>삼분위+1.5*iqr)
# print(condition.mpg)
# print(df[condition.mpg==True].index[0]) # .index[0] 그리고 True만 뽑아오는 것 !!

'''컬럼별로 뽑는 방법'''
#print(df.describe())
#print(df.disp.describe())
iqr2 = df.carb.describe()[6] - df.carb.describe()[4]
# print(iqr2)

#이상치 검출
#condition1 = (df.carb < (df.carb.describe()[4] -1.5*iqr)) | (df.carb > (df.carb.describe()[6] +1.5*iqr))
#print(condition)
# print(df[condition1]) # 이러면 이상치가 나온다.


# print('-'*20)
print(df.carb.describe())
일분위 = df.carb.describe().iloc[4]
삼분위 = df.carb.describe().iloc[6]
iqr = 삼분위 - 일분위
#이상치를 제거한 df
condition2 = (df.carb > (df.carb.describe()[4] -1.5*iqr)) & (df.carb < (df.carb.describe()[6] +1.5*iqr))
print(df[condition2])