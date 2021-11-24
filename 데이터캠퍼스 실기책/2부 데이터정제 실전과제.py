# 데이터캠퍼스 책 108page
# 6.5 선형회귀 적용

import pandas as pd
data = pd.read_csv("제공자료/house_raw.csv")

# X 와 y 데이터로 나누기
X = data[data.columns[:5]]
y = data[['house_value']]

# 학습, 테스트
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state =42)

# minmax_scale 정규화
from sklearn.preprocessing import minmax_scale
X_train_minmax = minmax_scale(X_train) # minmax_scale(데이터)
X_test_minmax = minmax_scale(X_test)

# 모델
# sklearn.linear_model
from sklearn.linear_model import LinearRegression
model = LinearRegression() # 괄호 필수
model.fit(X_train_minmax, y_train)
pred_X_train = model.predict(X_train_minmax)
print("훈련정확도:",model.score(X_train_minmax, y_train))

# 테스트데이터
pred_X_test = model.predict(X_test_minmax)
print("테스트 정확도:", model.score(X_test_minmax,y_test))
