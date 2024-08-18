import os

import numpy as np
import pandas as pd
import sklearn

df = pd.read_csv("q3_public.csv")
X_public = df.drop(['label'],axis=1)
y_public = df['label']
print('Shape of X_public:', X_public.shape)  # n_sample, 5, 9, 9
print('Shape of y_public:', y_public.shape)  # n_sample (0, 1)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X_public, y_public, test_size=0.33, random_state=42)

print('Shape of X_train:', X_train.shape)  
print('Shape of y_train:', y_train.shape)  
print('Shape of X_test:', X_test.shape)  
print('Shape of y_test:', y_test.shape)  

from sklearn import svm
clf = svm.SVC()
clf.fit(X_train, y_train)

preds = clf.predict(X_test)

from sklearn import metrics
print("SVM Accuracy:",metrics.accuracy_score(y_test,preds))

from sklearn import tree
dtc = tree.DecisionTreeClassifier()
dtc = dtc.fit(X_train, y_train)
preds2 = dtc.predict(X_test)
print("DTC Accuracy:",metrics.accuracy_score(y_test,preds2))

from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()
preds3 = gnb.fit(X_train, y_train).predict(X_test)
print("NB Accuracy:",metrics.accuracy_score(y_test,preds3))


