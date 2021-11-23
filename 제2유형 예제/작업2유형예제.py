# data 출처: https://www.dataq.or.kr/ - 공지사항 - 759번 제2회 빅데이터분석기사 실기 안내 - 첨부파일

import pandas as pd
from sklearn.preprocessing import * # 전처리
from sklearn.ensemble import * # 모델링

# 데이터로드
X_train = pd.read_csv('X_train.csv', encoding='euc-kr')
X_test = pd.read_csv('X_test.csv', encoding='euc-kr')
y_train = pd.read_csv('y_train.csv', encoding='euc-kr')
print(X_train)
print(X_test)
print(y_train)

# 간단한 eda
# print('X_train_shape:', X_train.shape)
# print('X_test_shape:', X_test.shape)
# print('y_train_shape:', y_train.shape)
# print(X_train)
# print(X_test)
# print(y_train.head())


# 결측치 확인
# isnull(), sum() 괄호 꼭 써주기
print(X_train.isnull().sum())


# 기초 통계
print(X_train.describe())
print(X_train.head(10))

# 범주형 변수 확인
print('범주형변수', X_train.describe(include='object'))

# 라벨 데이터 확인
print('label:', y_train['gender'].value_counts())


# 데이터 전처리

# 결측치 환불금액이 비어있으면 0으로 채움
X_train = X_train.fillna(0)
X_test = X_test.fillna(0)


# 학습에는 cust_id 필요하지 않음
X_train = X_train.drop(['cust_id'], axis=1)

# 결과 값에는 cust_id 필요 우선 변수에 담아둔다.
X_test_cust_id= X_test['cust_id']
X_test = X_test.drop(['cust_id'], axis=1)

print(X_train.columns)
# 피처 엔지니어링
# 범주형 변수 레이블 인코딩 진행
# 주구매상품, 주구매지점 (범주형)
cols =['주구매상품', '주구매지점']
for col in cols:
    lb = LabelEncoder()
    X_train[col] = lb.fit_transform(X_train[col])
    X_test[col] = lb.fit_transform(X_test[col])

print("범주형 인코딩 후:", X_train.head(10))

# 모델링 하이퍼파라미터 튜닝
model = RandomForestClassifier(n_estimators=100, max_depth =5, random_state=42)
model.fit(X_train, y_train['gender']) # 정답을 주고 학습
print('정확도: ', model.score(X_train, y_train['gender']))
print(X_test)
pred = model.predict_proba(X_test)
print('pred: ', pred[:,1])
print('pred자체:', pred)

# csv 생성
output = pd.DataFrame({'cust_id': X_test_cust_id, 'gender':pred[:,1]})

print(output)

#저장
output.to_csv('result/수험번호.csv',index = False)

# 헷갈리지 말자
# X_train 과 y_train 이 짝궁
# X_test 로 pred를 만든다
# 헷갈리면 train_x 로 변수명을 설정해도 좋을 것 같음
