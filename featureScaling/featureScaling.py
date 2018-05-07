""" quiz materials for feature scaling clustering """
from functools import reduce
### FYI, the most straightforward implementation might
### throw a divide-by-zero error, if the min and max
### values are the same
### but think about this for a second--that means that every
### data point has the same value for that feature!
### why would you rescale it?  Or even use it at all?
def featureScaling(arr):
    min = reduce(lambda x,y: x if x < y else y, arr)
    max = reduce(lambda x,y: x if x > y else y, arr)
    range = max - min
    return [round((x-min)*1.0/range, 3) for x in arr]

# tests of your feature scaler--line below is input data
data = [115, 140, 175]
print(featureScaling(data))
