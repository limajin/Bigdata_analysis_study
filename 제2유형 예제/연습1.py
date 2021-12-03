import pandas as pd
import numpy as np

train_X = pd.read_csv('data/X_train.csv',encoding='euc-kr')
train_y = pd.read_csv('data/y_train.csv',encoding='euc-kr')

pd.set_option('max_columns',None)
# print(train_X)
# print(train_X.info())

# 결측치 저리
train_X['환불금액'].fillna(0, inplace=True)

# print(train_X.info())

# 데이터 전처리
# 범주형 데이터 라벨인코딩
from sklearn.preprocessing import *
cols =['주구매상품','주구매지점']
for col in cols:
    lb =LabelEncoder()
    train_X[col] = lb.fit_transform(train_X[col])

# print(train_X)

# 필요없는 컬럼삭제
train_X.drop('cust_id',inplace=True, axis =1)



# 데이터 정규화
minmax =MinMaxScaler()
scaled_train = minmax.fit_transform(train_X)
y = train_y['gender']

# from sklearn.decomposition import PCA
# num = 2
# pca =PCA(n_components = num)
# pca_scaled = pca.fit_transform(scaled_train)
# pca_df = pd.DataFrame(data=pca_scaled, columns=['component' + str(x) for x in range(num)])
# print(pca_df)



# 학습데이터를 검증데이터로 나눴음
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(scaled_train, y, stratify =y, test_size =0.2, random_state =42)

# 알고리즘 적용
from sklearn.ensemble import RandomForestClassifier

xgb = RandomForestClassifier(n_estimators = 50, max_depth=10, random_state =42)
xgb.fit(X_train,y_train)
score = xgb.score(X_train,y_train)
print('정확도: ',score)
pred = xgb.predict(X_test)



from sklearn.metrics import roc_auc_score, accuracy_score
roc= roc_auc_score(pred,y_test)
acc =accuracy_score(pred, y_test)
print('roc',roc)
print('acc',acc)


# 테스트 데이터에 적용
test_X = pd.read_csv('data/X_test.csv',encoding='euc-kr')
test_Xc =test_X.copy()
test_X.fillna(0,inplace=True)
for col in cols:
    test_X[col] = lb.fit_transform(test_X[col])

test_X.drop('cust_id',inplace=True, axis =1)
print(test_X)
scale_test = minmax.transform(test_X)
# scale_test =pca.transform(scale_test)
print("궁금",scale_test)
pred_test = xgb.predict_proba(scale_test)[:,1]
pred_testdf = pd.DataFrame(pred_test,columns=['pred'],index=test_Xc.cust_id).reset_index()

print(pred_testdf)

