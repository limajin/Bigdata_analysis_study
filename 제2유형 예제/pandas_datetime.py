'''
판다스의 to_datetime을 이용해
시계열 컬럼을 생성하고 원하는 시간을 추출하고
타임 델타도 계산해보기
'''

import pandas as pd

pd.set_option('max_columns', None)
df = pd.read_csv('https://raw.githubusercontent.com/Datamanim/dataq/main/mtcars.csv', index_col='Unnamed: 0')

'''날짜생성'''
print(df)
date =[]
for i in range(1,33):
    if i <= 9:
        i =str(i)
        a = '2021-06-0'+ i
        date.append(a)
    elif i <=30:
        i = str(i)
        b = '2021-06-'+i
        date.append(b)
    else:
        i = i -30
        i = str(i)
        c= '2021-07-'+i
        date.append(c)

# print(date)

'''
날짜 리스트를 df에 컬럼으로 추가
date컬럼은 당연히 오브젝트이므로
datetime형태로 바꾸자.
'''

df['date'] = date
print(df.info())

df['date'] = pd.to_datetime(df['date'])

print(df.info())

'''
date에서 년, 달, 일을 뽑아보자
dt. 활용
'''

df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day'] = df['date'].dt.day
# Period객체는 to_period(freq='기간인수')
# tetime변수에 대해 어떤 기간에 따른 자료형을 생성
df['date_m'] = df['date'].dt.to_period(freq='M')

# 7월 데이터만 출력
# print(df[df.month == 7])

'''2020-06-13과의 날짜 차이를 계산해보기'''
past = pd.to_datetime('2020-6-13')
df['time_delta'] = df.date - past
print(df)