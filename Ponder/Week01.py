# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GGEqmhG8aJQWqHDq8Bkw_2h98B64CCmy
"""

import pandas as pd
import numpy as np
from fractions import Fraction
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

url = "https://byui-cs.github.io/cs450-course/week01/iris.data"
data = pd.read_csv(url)
data.to_numpy()

features,y, targets = np.hsplit(data,np.array([4,4]))

train_data, test_data, train_targets, test_targets = train_test_split(features, targets, test_size=.3)

classifier = GaussianNB()
classifier.fit(train_data, train_targets)
targets_predicted = classifier.predict(test_data)

result = np.equal(test_targets.to_numpy().flatten(), targets_predicted)
np.count_nonzero(result == 1)

class HardCodedClassifier():
  def fit(self, data, targets):
    self.train_data = data
    self.train_target = targets
  def predict(self, data):
    predict_list =[]
    for index, row in data.iterrows():
      predict_list.append("Iris-setosa")
    return predict_list

hcClassifier = HardCodedClassifier()
hcClassifier.fit(train_data, train_targets)
targets_predicted = hcClassifier.predict(test_data)

result = np.equal(test_targets.to_numpy().flatten(), targets_predicted)
accuracy = np.count_nonzero(result == 1) / len(test_data)
accuracy