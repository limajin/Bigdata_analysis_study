
import pandas as pd
import numpy as np

X_train = pd.read_csv('data/X_train.csv')
X_test = pd.read_csv('data/X_test.csv')
y_train = pd.read_csv('data/y_train.csv')

from sklearn.preprocessing import LabelEncoder
# import sklearn.preprocessing
# print(dir(sklearn.preprocessing))
lb =LabelEncoder()
cols =['주구매상품','주구매지점']
for col in cols:
	X_train[col] = lb.fit_transform(X_train[col])
	X_test[col] = lb.fit_transform(X_test[col])

X_train['환불금액'] = X_train['환불금액'].fillna(0)
X_test['환불금액'] = X_test[['환불금액']].fillna(0)
print(X_train)
# print(X_test)
print(X_train.info())

X_train = X_train.iloc[:,1:]
print(type(X_train))
X_test_custid = X_test[['cust_id']]
X_test =X_test.iloc[:,1:]
y_train = y_train['gender']
print(y_train)
print(y_train.shape)
print(X_train.shape)


from sklearn.ensemble import RandomForestClassifier

rdc =RandomForestClassifier(random_state=42, max_depth =10, n_estimators =100)
rdc.fit(X_train,y_train)
print(rdc.score(X_train,y_train))
from sklearn.metrics import roc_auc_score
pred = rdc.predict_proba(X_train)[:,1]
print(pred)

# test 데이터
pred_test = rdc.predict_proba(X_test)[:,1]
testdf = pd.DataFrame(pred_test,columns=['gender'])
print(testdf)
last = pd.concat([X_test_custid,testdf],axis=1)
print(last)





