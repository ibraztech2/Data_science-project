import numpy as np
from numpy.random import randn

np.random.seed(101)
from pandas import *

np.random.seed(101)

df = DataFrame(randn(5, 4),["A","B","C","D","E"],["W","X","Y","Z"] )
# pick = df[["W","X"]]
df["new"] = df["W"] + df["X"]
# pick= df.loc(1)
# print(pick)
# print(df.drop("E",axis=0))
# print(df.drop("new",axis=1,inplace=True))
# print(df.loc["A"])
# print(df.iloc[1])
# print(df.loc["A","W"])
# print(df.loc[["A","B"],["W","Y"]])