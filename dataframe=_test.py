from pandas import *
from numpy import *


resistance_1 = [i for i in range(10,10000,46)]
resistance = []
resistance_mapping = []
resistance_2 = 500
voltage = 5
for i in resistance_1:
    effect_r = (i * resistance_2) /(resistance_2 + i)
    resistance.append(effect_r)
    resistance_mapping = (list(zip(resistance_1,resistance,)))
data_frame_index = [i for i in range(1,len(resistance) +1)]
df= DataFrame(resistance_mapping,data_frame_index,columns=["resistance","Effective_resistance"])
df["current"] = voltage/ df["resistance"]
df_current  = df["current"]
df["power"] = (df_current **2) * voltage
print(f" voltage {voltage}, resistance {resistance_2}")
print(df)
print(df.shape)
