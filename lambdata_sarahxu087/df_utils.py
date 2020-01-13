"""
utility functions for working with DataFrames
"""

import pandas

TEST_DF = pandas.DataFrame([1,2,3])

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
from sklearn.metrics import confusion_matrix
confusion_matrix(y_val, y_pred)