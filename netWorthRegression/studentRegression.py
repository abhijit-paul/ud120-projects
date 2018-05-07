from sklearn.linear_model import LinearRegression
import numpy
def studentReg(ages_train, net_worths_train):
    ### import the sklearn regression module, create, and train your regression
    ### name your regression reg

    ### your code goes here!

    reg = LinearRegression()
    reg.fit(numpy.array(ages_train), numpy.array(net_worths_train))

    return reg