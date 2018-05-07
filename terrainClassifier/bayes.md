# Bayes Theorem
Probability of a team winning the IPL:

        P(Pos) : Win prediction.

.

    Sensitivity = P(Pos|Win) = Probability of positive(Win) prediction when actual result is Win

.

    Specitivity = P(Neg|Lose) = Probability of negative(Lose) prediction when actual result is not Win(Lose)

.

    Sensitivity  1-Specitivity
    P(Pos|Win)   P(Pos|Lose)    
        x            x
    P(PriorWin)  P(PriorWin)
    -------------------------
    P(Pos|Win)   P(Pos|Lose)    `==>Posterier`  P(Pos) = P(Pos|Win) + P(Pos|Lose) 
        /	          /
     P(Pos)        P(Pos)
    -------------------------
    P(Win/Pos)   P(Lose/Pos)     `==>Posterior probability`

.

    P(Win/Pos) : Probability of winning the IPL when prediction is positive(Win)

    P(Lose/Pos) : Probability of not winning(losing) the IPL when prediction is positive(Win)
