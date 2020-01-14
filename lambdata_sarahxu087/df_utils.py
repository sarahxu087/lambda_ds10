"""
utility functions for working with DataFrames
"""

from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
import pandas
import numpy as np

TEST_DF = pandas.DataFrame([1, 2, 3, 4, 5, 6])
a = np.array([1, 0, 1, 1, 0, 1])
b = np.array([0, 1, 0, 1, 0, 0])


class Randomsplit:
    """
    random split the dataframe
    """

    def __init__(self, dataframe):
        self.dataframe = dataframe

    def get_split(self):
        train, test = train_test_split(
            self.dataframe, test_size=0.2, random_state=1)
        print(f'train{train},test{test}.')


"""
Test if the class work
"""
dataframe = Randomsplit(TEST_DF)
dataframe.get_split()


class Confusion_matrix:
    """
    make a confusion_matrix
    """

    def __init__(self, dataframe1, dataframe2):
        self.dataframe1 = dataframe1
        self.dataframe2 = dataframe2

    def show_confusion_matrix(self):
        print(confusion_matrix(self.dataframe1, self.dataframe2))


"""
Test if the class work
"""

new_confusion_matrix = Confusion_matrix(a, b)
new_confusion_matrix.show_confusion_matrix()
