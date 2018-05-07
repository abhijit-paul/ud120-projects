from sklearn.tree import DecisionTreeClassifier
import numpy

def classify(features_train, labels_train):

    ### your code goes here--should return a trained decision tree classifer


    clf = DecisionTreeClassifier()
    clf.fit(numpy.array(features_train), numpy.array(labels_train))

    return clf