import pandas as pd

import numpy as np

train_X = pd.read_csv('data/X_train.csv')

train_y = pd.read_csv('data/y_train.csv')

train_X.fillna(0, inplace= True)



#1 데이터 전처리(이상치 제거 생략)

product = pd.get_dummies(train_X['주구매상품'])

place = pd.get_dummies(train_X['주구매지점'])

train_X = train_X.drop(columns = ['cust_id','주구매지점','주구매상품'], axis =1)

train_X = pd.concat([train_X,product], axis= 1)

train_X = pd.concat([train_X,place], axis= 1)

train_X = train_X.drop(columns = ['소형가전'], axis =1)



#2 데이터 정규화

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

scaler.fit(train_X)

X = scaler.transform(train_X)

y = train_y['gender']

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.2, random_state =10)




#3 알고리즘 적용

from sklearn.ensemble import RandomForestClassifier

xgb = RandomForestClassifier(n_estimators = 50, max_depth =10, random_state= 10)

xgb.fit(X_train, y_train)

y_hat = xgb.predict(X_test)




#4 결과 확인

from sklearn.metrics import roc_auc_score, accuracy_score

roc = roc_auc_score(y_hat, y_test)

acc = accuracy_score(y_hat, y_test)

print(roc)

print(acc)




#5 테스트 데이터에 적용

test_X = pd.read_csv('data/X_test.csv')

test_X.fillna(0, inplace= True)

product = pd.get_dummies(test_X['주구매상품'])

place = pd.get_dummies(test_X['주구매지점'])

test_X = test_X.drop(columns = ['cust_id','주구매지점','주구매상품'], axis =1)

test_X = pd.concat([test_X,product], axis= 1)

test_X = pd.concat([test_X,place], axis= 1)



#6 질문 부분 (2 부분에서 scaler를 fit 해주었습니다. 그 이후에는 이렇게 transform(test_X) 에만 해주면 정규화가 되는 것인가요?)

X = scaler.transform(test_X)

predict = xgb.predict_proba(X)

predict= pd.DataFrame(predict)

print(predict[1])