import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

pd.set_option('max_columns',None)

## 순서
# 1. 데이터 로드
# 2. 라벨인코딩
# 3. 스케일
# 4. train_test_split
# 5. 모델 + 그리드서치

# 데이터 로드
X_train = pd.read_csv('data/X_train.csv', encoding='euc-kr')
y_train = pd.read_csv('data/y_train.csv', encoding='euc-kr')

# print(X_train)
print(y_train)


# X와 y 합치기
df = pd.concat([X_train, y_train], axis=1)
print(df)
# print(df.info())

'''
회귀라고 가정하고 '총구매액'을 종속변수로 지정하기.
'''

# 불필요 컬럼 삭제
df = df.drop(['cust_id'], axis =1)

# 결측치있는 컬럼 확인하고 결측치 처리하기
# print(df.isnull().sum())
# '환불금액' 널값 존재
# 널값을 환불금액이 0원인 것으로 처리
df['환불금액'].fillna(0,inplace =True)
df['환불금액'] = df['환불금액'].astype(int)
# print(df.info())


############ 라벨인코딩 #################

# object 타입 레이블 인코딩하기 : LabelEncoder
# '주구매상품', '주구매지점'
from sklearn.preprocessing import LabelEncoder
LE = LabelEncoder()
cols = ['주구매상품','주구매지점']
for col in cols:
    df[col] = LE.fit_transform(df[col])

# print(df.info())


############ 스케일 #################

# log 스케일
# print(df.describe())
# 평균과 50% 차이가 많은 '환불금액'
df['환불금액'] = np.log1p(df.환불금액)
# print(df.환불금액.describe().T[['mean', '50%']])

# 모든 컬럼 minmax스케일링 하기
from sklearn.preprocessing import MinMaxScaler
MMS =MinMaxScaler()
총구매액 = df[['총구매액']]
df.drop('총구매액', axis = 1, inplace =True)
df.drop('gender',inplace=True,axis =1)
# print(df)
mms_df = MMS.fit_transform(df)
# print(mms_df)
# print(총구매액)


from sklearn.model_selection import train_test_split
X = mms_df
y = 총구매액

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size =0.2, random_state =42)
# print(X_train)
# print(y_train)

'''xgboost 모델 적용 GridSearchCV로 교차검증 실시'''
from xgboost import XGBRegressor
from sklearn.model_selection import GridSearchCV

# print(help(XGBRegressor))
print(X_train)

xgb = XGBRegressor(n_jobs=-1, random_state=42)
params = {'n_estimators': [300], 'max_depth': [2,5], 'learning_rate':[0.01]}
grid =GridSearchCV(xgb, param_grid =params, n_jobs =-1, cv=4)
grid.fit(X_train,y_train)
print('최적 하이퍼파라미터:', grid.best_params_)
best_grid =grid.best_estimator_
pred = best_grid.predict(X_test)

from sklearn.metrics import mean_squared_error ,r2_score
mse = mean_squared_error(y_test,pred)
r2 = r2_score(y_test, pred)
print(f'mse: {mse}, r2score: {r2}')

'''X_test.csv로 예측'''
X_test = pd.read_csv('data/X_test.csv',encoding = 'euc-kr')
X_test_col =X_test.copy()

# print(X_test)

X_test.drop('cust_id', axis=1, inplace =True)
X_test['환불금액'].fillna(0, inplace=True)
X_test['환불금액']=X_test['환불금액'].astype(int)

X_test['환불금액'] = np.log1p(X_test.환불금액)

from sklearn.preprocessing import LabelEncoder
LE = LabelEncoder()
cols =['주구매상품','주구매지점']
for col in cols:
    X_test[col] = LE.fit_transform(X_test[col])
print(X_test)


from sklearn.preprocessing import MinMaxScaler
mms = MinMaxScaler()
mms_df = mms.fit_transform(X_test.drop('총구매액', axis =1))
# print(mms_df)
pred_test = best_grid.predict(mms_df)

# print(pred_test)

제출 = pd.DataFrame(pred_test, columns= ['pred'], index = X_test_col.cust_id).reset_index()
print(제출)
제출.to_csv('result/수험번호_회귀연습.csv')