import sys
from class_vis import prettyPicture
from prep_terrain_data import makeTerrainData

import matplotlib.pyplot as plt
import numpy as np
import pylab as pl
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
features_train, labels_train, features_test, labels_test = makeTerrainData()



########################## DECISION TREE #################################


### your code goes here--now create 2 decision tree classifiers,
### one with min_samples_split=2 and one with min_samples_split=50
### compute the accuracies on the testing data and store
### the accuracy numbers to acc_min_samples_split_2 and
### acc_min_samples_split_50, respectively

clf_2 = DecisionTreeClassifier(min_samples_split=2)
clf_2.fit(np.array(features_train), np.array(labels_train))
pred2 = clf_2.predict(features_test)
acc_min_samples_split_2 = accuracy_score(pred2, labels_test)

clf_50 = DecisionTreeClassifier(min_samples_split=50)
clf_50.fit(np.array(features_train), np.array(labels_train))
pred50 = clf_50.predict(features_test)
acc_min_samples_split_50 = accuracy_score(pred50, labels_test)



def submitAccuracies():
  return {"acc_min_samples_split_2":round(acc_min_samples_split_2,3),
          "acc_min_samples_split_50":round(acc_min_samples_split_50,3)}

print(submitAccuracies())
