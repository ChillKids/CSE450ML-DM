# -*- coding: utf-8 -*-
"""Assignment2.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qTn-J9sVY76v-vn1DQYCako6zNAGLBVn
"""

import pandas as pd
import numpy as np
from fractions import Fraction
from collections import Counter
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

url = "https://byui-cs.github.io/cs450-course/week01/iris.data"
data = pd.read_csv(url)
data = data.to_numpy()

features,y, targets = np.hsplit(data,np.array([4,4]))
train_data, test_data, train_targets, test_targets = train_test_split(features, targets, test_size=.3)

classifier = KNeighborsClassifier(n_neighbors=3)
classifier.fit(train_data, train_targets)
predictions = classifier.predict(test_data)
print(predictions)

result = np.equal(test_targets.flatten(), predictions)
accuracy = np.count_nonzero(result == 1) / len(predictions)

accuracy

class kNN_classifier():
  def fit(self, data, targets):
    self.data = data
    self.targets = targets

  def calc_distance(self, x1, x2):
    dist = np.linalg.norm(x1-x2)
    return dist
  
  def predict_roll(self, test_roll, k):
    dist_list = []
    for train_roll in self.data:
      dist_list.append(self.calc_distance(test_roll, train_roll))
    sorted_index = sorted(range(len(dist_list)), key=lambda k: dist_list[k])
    sorted_index = sorted_index[0:k]
    #print("sorted index: ",sorted_index)
    
    k_list = []
    for index in sorted_index:
      k_list.append(self.targets[index][0])
    #print ("klist : ",k_list)
    k_count = Counter(k_list)
    prediction = k_count.most_common(1)
    return prediction[0][0]
  

  def predict(self, data, k):
    predict_list = []
    for test_roll in data:
        predict_list.append(self.predict_roll(test_roll, k))
    print(predict_list)
    return predict_list

myClassifier = kNN_classifier()
myClassifier.fit(train_data, train_targets)
predictions = myClassifier.predict(test_data, 3)
print(predictions)

result = np.equal(test_targets.flatten(), predictions)
accuracy = np.count_nonzero(result == 1) / len(predictions)

accuracy