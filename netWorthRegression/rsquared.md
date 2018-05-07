# Concept of r squared
Defines how much of an effect the output parameter has based on the change in input parameter(s).
From the deinition itself it is evident, that the best case of regression would be if the rsquared value is maximal i.e. we would want the output parameter to be as much as possible be affected by input param(s).
But how would this value actually increase? 
    By choosing better parameters
    By choosing more number of input parameters to find the regression

What is the upper limit on the maximum value of rsquared? 1
Why? It is ingrained in the mathematical modelling of this value. Calculated as:
    1-u/v. 
    u = Sum of squares of residual values = sum[(Yactual - Ypred)^2]
    v = Sum of squares of actual values = sum[(Yactual - Ymean)^2]
 
    Yactual = Actual value of a data point
    Ypred = Predicted value of that data point
    Ymean = Mean of all the actual values of all the given data points

    Since the value is 1 - positive quantity, max value of r^2 is 1


The reason why there is only 1 solution to this:
![reg ques](https://preview.ibb.co/mKPW4H/reg_q.png)

Rememeber the way to identify "what makes a good linear regression"?
It is r^2. Now, think about this from which ones can have r^2 closer to 1
Most of the graphs cannot be explained by linear equation at all. 
Hence, those are disqualified by ethos.

Now, only 1 and 4 can be identified using linear equation.
The problem with 1st one is the change in value of y cannot be explained by the change in x at all. x(input) stays constant, while y(output) value keeps changing.
Hence, r^2 is 0; hence very bad for linear regression.
Or, we can look at it from the point of view of slope/coefficient of regression, 
the slope would be infinity. Hence bad for regression

Now think of the 4th one. The value of y stays same all the time, there is no change at all.
But there is a steady change of x. Now, evaluating r^2, we see that if there is no change at all in output(y), the amount of change itself is 0.
Hence the value of u(sum of residual values squared) is 0. Hence r^2 is 1.
Or, we can look at it from the point of view of slope/coefficient of regression,
the slope would be 0. Hence the slope has been minimized; the change in y is minimized. 
Hence, best for linear regression
