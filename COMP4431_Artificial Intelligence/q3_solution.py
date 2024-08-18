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
        X = X.reshape(X.shape[0], 5, 9, 9)
        y = data['label'].astype('int').values
        return X, y
    else:
        # for the private dataset, label column is not provided.
        X = data[column_list].values
        X = X.reshape(X.shape[0], 5, 9, 9)
        return X


X_public, y_public = read_data_from_csv('q3_public.csv')
print('Shape of X_public:', X_public.shape)  # n_sample, 5, 9, 9
print('Shape of y_public:', y_public.shape)  # n_sample (0, 1)

X_private = read_data_from_csv('q3_private.csv')
print('Shape of X_private:', X_private.shape)  # k_sample, m_feature

preds = np.full(len(X_private), -1, dtype=int)  # remove and make your own predictions.

from sklearn import tree
dtc = tree.DecisionTreeClassifier()
dtc = dtc.fit(np.hsplit(np.dstack(X_public).flatten(), len(y_public.flatten())), y_public.flatten())

preds = dtc.predict(np.hsplit(np.dstack(X_private).flatten(),len(preds.flatten())))

print(preds)

submission = pd.DataFrame({'label': preds})
submission.to_csv('q3_solution.csv', index=False)
