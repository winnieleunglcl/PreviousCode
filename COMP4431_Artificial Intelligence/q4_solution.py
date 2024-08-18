import os

import numpy as np
import pandas as pd
import sklearn


def read_data_from_csv(path):
    """Load datasets from CSV files.

    Args:
        path (str): Path to the CSV file.

    Returns:
        X (np.ndarray): Features of samples.
        y (np.ndarray): Labels of samples, only provided in the public datasets.
    """

    assert os.path.exists(path), f'File not found: {path}!'
    assert os.path.splitext(path)[
        -1] == '.csv', f'Unsupported file type {os.path.splitext(path)[-1]}!'

    data = pd.read_csv(path)
    column_list = data.columns.values.tolist()

    if 'label' in column_list:
        # for the public dataset, label column is provided.
        column_list.remove('label')
        X = data[column_list].values
        y = data['label'].astype('int').values
        return X, y
    else:
        # for the private dataset, label column is not provided.
        X = data[column_list].values
        return X


X_train, y_train = read_data_from_csv('q4_public_train.csv')
print('Shape of X_train:', X_train.shape)  # n_sample, m_feature
print('Shape of y_train:', y_train.shape)  # n_sample (0, 1)

X_val, y_val = read_data_from_csv('q4_public_val.csv')
print('Shape of X_val:', X_val.shape)  # n_sample, m_feature
print('Shape of y_val:', y_val.shape)  # n_sample (0, 1)

merged_X_train = np.concatenate((X_train,X_val))
merged_y_train = np.concatenate((y_train,y_val))

#first, normalize X_train with X_val
from sklearn import preprocessing
normalized_X_train = preprocessing.normalize(merged_X_train)

X_private = read_data_from_csv('q4_private.csv')
print('Shape of X_private:', X_private.shape)  # k_sample, m_feature

preds = np.full(len(X_private), -1, dtype=int)  # remove and make your own predictions.

#second, normalize X_test
normalized_X_test = preprocessing.normalize(X_private)

from sklearn import tree
dtc = tree.DecisionTreeClassifier()
dtc = dtc.fit(normalized_X_train, merged_y_train)
preds = dtc.predict(normalized_X_test)

print(preds)

submission = pd.DataFrame({'label': preds})
submission.to_csv('q4_solution.csv', index=False)
