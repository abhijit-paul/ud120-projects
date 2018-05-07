# Decision Tree
    Decision boundary := The point of split to break a problem in separate individual problem to be solved by machine learning
    (naiive baise or support vector classifier)
    
.    
    Entropy of data := The amount of impurities in the data. The idea is to reduce entropy by properly choosing decision boundary
    In order to do so, we need to choose parameters effectively on which we should draw decision boundaries.
    There is a mathematical representation of Entropy 
      = Sigma(p. + log2(p.)), where p. is the fraction of each of the decision choices
`The value of entropy lies between 0 and 1`
    
.
    Information gain := How much of initial impurity in the dataset or entropy can be reduced 
    by the choice of parameter in choosing the decision boudary.
    The challenge is finding the parameter that can reduce the initial entropy order to maximize the information gain.
    Information gain has a mathematical expression as follows:
      = Entropy of parent(impurity in decision choices) - [Weighted AVG]*Entropy of parent(impurity in the chosen parameter) 



The trick is to pick one decision choice and find out how to reduce the amount of impurity such that this particular decision
choice can be predicted with utmost correction.
Hence, we start off with one decision choice and then calculate the entropy of a parameter within the boundary of that decision choice only
For eg, if we are trying to find whether a team will win IPL, we first find the entropy of each team winning the IPL (Ep)
    Ep = Probability of KKR * log2(Probability of KKR) + Probability of CSK * log2(Probability of CSK) + ....
    Possible parameters = Number of overseas players | Number of hardhitters | Owner's money | Death ball bowlers
.

From previous years' data, we see that teams win/loss has been tabulated as follows
    | Overseas      | Indians | Hardhitters            | Money          | Deathbowlers |  Win/Lose |
    |   6(more)     |     4   |     3(2-3)H2 >2(T)     |   1M  (>1)T  |      3(>3)F  |     W     |
    |   3(less)     |     7   |     4(4  )H3 >2(T)     |   1.4M(>1)T  |      5(>3)T  |     W     |
    |   4(less)     |     6   |     1(<2) H1 >2(F)     |   2M  (>1)T  |      4(>3)T  |     L     |
    |   2(less)     |     8   |     5(5-6)H4 >2(T)     |   2.2M(>1)T  |      4(>3)T  |     W     |


So, entropy of decision point i.e W
    = - [ 3/4*log2(3/4) + 1/4*log2(1/4)]
    = 0.81

`If the ratio of win/loss is equal, entropy 0.5*log2(0.5)+0.5*log2(0.5) = 1(highest entropy/most impure)`

    
Now, weighted avg entropy with respective parameters are:
    Overseas = 3/4 * (- (1/3)*log2(1/3)+(2/3)*log2(2/3)) + 1/4 * (0) = 3/4 * 0.91 + 1/4 * 0 = 0.6825
    Hardhitters = - 3 * (1/3)*log2(1/3) = 1.5(Value Err > 1 =? bad parameter). Need to choose one boundary only
    Revisit Hardhitters = 0
    Money = 1
    Deathbowlers = - (1/3)*log2(1/3)+(2/3)*log2(2/3) = 0.91*3/4 = 0.6825

Information gains:
    = Ep - [Weighted AVG]*Ec
    = 0.81 - 0.6825 = 0.1275
    = 0.81 - 0 = 0.81


More the number of features, the more complex the decision tree becomes.

What do you think SelectPercentile is doing? It is chosing the number of features to use out of the total dataset based on how much percentile of data we wish to use for our training.
Would a large value for percentile lead to a more complex or less complex decision tree, all other things being equal? Note the difference in training time depending on the number of features. More complex; large value of percentile means we wish to train our learning algorithm on wider array over data. For percentile 1, it means we wish to process over only 1 of 100 equal grouping data only. 40 percentile means we wish to pick 40 groups out of 100 equal groups of data and process over it.

    Percentile: Lets say the entire data set is broken into 100 equal groups. Total size of data = N. After distribution there are 100 sets of size N/100 each. 
    For 1 percentile, pick only 1 such group. Hence total count = N/100 elements.
    For 40 percentile, pick 40 such groups. Hence total count = N/100 * 40 elements

. 
    Hence using lesser percentile will decrease the accuracy of the algorithm
