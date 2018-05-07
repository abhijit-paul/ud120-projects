from sklearn.naive_bayes import GaussianNB
import numpy
def classify(features_train, labels_train):   
    ### import the sklearn module for GaussianNB
    ### create classifier
    ### fit the classifier on the training features and labels
    ### return the fit classifier
    
    
    ### your code goes here!
    
    cif = GaussianNB()
    return cif.fit(numpy.array(features_train), numpy.array(labels_train))

