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


X_public, y_public = read_data_from_csv('q2_public.csv')
print('Shape of X_public:', X_public.shape)  # n_sample, m_feature
print('Shape of y_public:', y_public.shape)  # n_sample (0, 1)

X_private = read_data_from_csv('q2_private.csv')
print('Shape of X_private:', X_private.shape)  # k_sample, m_feature
preds = np.full(len(X_private), -1, dtype=int)  # remove and make your own predictions.

from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_public, y_public)

preds = model.predict(X_private)
print('Result:', preds)

submission = pd.DataFrame({'label': preds})
submission.to_csv('q2_solution.csv', index=False)
