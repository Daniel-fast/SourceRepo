import numpy as np

matrix4d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
print(matrix4d)
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]
#  [13 14 15 16]]
# this is a 4 x 4 matrix and - is kind of a list inside another list [[]]
print(matrix4d.shape) # A tuple (4, 4)
print()
# we can create matrices already populated
newZerosMatrix = np.zeros((4, 4))
print(newZerosMatrix)
print()
# [[0. 0. 0. 0.]
#  [0. 0. 0. 0.]
#  [0. 0. 0. 0.]
#  [0. 0. 0. 0.]]
#by default all numbers are float ones but we can create as integer - take a look
newZerosMatrix = np.zeros((4, 4), dtype=int)
print(newZerosMatrix)
# [[0 0 0 0]
#  [0 0 0 0]
#  [0 0 0 0]
#  [0 0 0 0]]

# we can create matrices already populated with ones
newOnesMatrix = np.ones((4, 4), dtype=int)
print(newOnesMatrix)
# [[1 1 1 1]
#  [1 1 1 1]
#  [1 1 1 1]
#  [1 1 1 1]]

# we can also specify the number to be fulfill
newFullMatrix = np.full((4, 4), 7, dtype=int)
print(newFullMatrix)
print()
# [[7 7 7 7]
#  [7 7 7 7]
#  [7 7 7 7]
#  [7 7 7 7]]

# we can also fulfill with random values
newRandomMatrix = np.random.random((4, 4))
print(newRandomMatrix)
print()
# [[0.7407236  0.33407264 0.01512649 0.0670851 ]
#  [0.40120533 0.93672343 0.80881249 0.24993994]
#  [0.55942077 0.02151626 0.31507067 0.43690911]
#  [0.61156383 0.36110981 0.34674451 0.60683736]]

# we can also get a value of an especific coordinate (like 0, 0 )
print(newRandomMatrix[0, 0])
print()
# [[0.89869866 0.97685415 0.36848251 0.04973221]
#  [0.1303867  0.49451111 0.61723908 0.00785188]
#  [0.98902097 0.07310791 0.95694847 0.88445577]
#  [0.8379675  0.07671975 0.27241851 0.86802288]]

# 0.8986986609647938

# we can check conditions for each value of a matrix
newConditionalMatrix = np.random.random((4, 4))
print(newConditionalMatrix > 0.2)
print()
# [[0.25824706 0.70425021 0.46878446 0.54962358]
#  [0.65031831 0.07116862 0.02276055 0.23620869]
#  [0.87315045 0.30505354 0.9065687  0.93418167]
#  [0.75703203 0.24682809 0.09289031 0.32201778]]

# 0.25824706093931593

# [[ True  True  True  True]
#  [ True  True False  True]
#  [ True  True  True  True]
#  [ True  True  True  True]]

# Or even print only values whose criteria matches

newCriterialMatrix = np.random.random((4, 4))
print(newCriterialMatrix [newCriterialMatrix > 0.2])
print()
# [0.53751004 0.84698976 0.80694249 0.46106006 0.81923853 0.31138266
#  0.61927108 0.40592384 0.32183429 0.58093566 0.52265231 0.80556218
#  0.78372761 0.66270232]


# We have a bunch of computation functions
print(np.sum(newCriterialMatrix))
print()
# [0.90497512 0.35489874 0.74990748 0.25814951 0.84804418 0.660019
#  0.79241872 0.79218874 0.66591043 0.97100897]

# 7.840743144774996

