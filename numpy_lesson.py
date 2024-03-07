import numpy as np
from numpy.random import randn

np.random.seed(101)
from pandas import *

np.random.seed(101)

df = DataFrame(randn(5, 4),["A","B","C","D","E"],["W","X","Y","Z"] )
print(df)