import sys
from class_vis import prettyPicture, output_image
from prep_terrain_data import makeTerrainData

import numpy as np
import pylab as pl

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
features_train, labels_train, features_test, labels_test = makeTerrainData()



#################################################################################


########################## DECISION TREE #################################



#### your code goes here
clf = DecisionTreeClassifier(min_samples_split=60)
clf.fit(features_train, labels_train)
pred = clf.predict(features_test)


acc = accuracy_score(pred, labels_test)
### be sure to compute the accuracy on the test set

prettyPicture(clf, features_test, labels_test)
output_image("test.png", "png", open("test.png", "rb").read())

def submitAccuracies():
  return {"acc":round(acc,3)}

print(submitAccuracies())