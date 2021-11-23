# data 출처: https://www.kaggle.com/lavanya321/mtcars

# 자동차 데이터 셋
# 특정 컬럼(qsec)을 Min-Max Scale로 변환 후
# 0.5보다 큰 값을 가지는 레코드(row) 수를 묻는 문제

# 방법1
import pandas as pd
from sklearn.preprocessing import *
data = pd.read_csv('data')
data['qsec'] = minmax_scale(data['qsec'])

print(sum(data['qsec']>0.5))
print(len(data(data['qsec'] > 0.5)))

# 방법2
data2 = pd.read_csv('data')

# minmax_scale 공식을 직접 함수로 만들 수 있음
def min_max(data):
    data = (data - min(data))/ (max(data) - min(data))
    return data

data2['qsec'] = min_max(data2['qsec'])
print(len(data2(data2['qsec'] > 0.5)))