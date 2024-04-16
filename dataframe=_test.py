from pandas import *
from os import *
from numpy import *


resistance_1 = [i for i in range(1,100,3)]
resistance = []
resistance_mapping = []
resistance_2 = 20
voltage = 5
for i in resistance_1:
    effect_r = (i * resistance_2) /(resistance_2 + i)
    resistance.append(effect_r)
    resistance_mapping = (list(zip(resistance_1,resistance,)))
data_frame_index = [i for i in range(1,len(resistance) +1)]
df= DataFrame(resistance_mapping,data_frame_index,columns=["resistance","Effective_resistance"])
df["current"] = voltage/ df["resistance"]
df_current  = df["current"]
df_current_analysed = []
for i in df_current:
    if (i - 1) < 0:
        i = i * 1000
        i = f'{i:.2f} mw'
    else:
        i = f'{i:.3f} w'
    df_current_analysed.append(i)


df["power"] = (df_current **2) * voltage
print(f" voltage {voltage}, resistance {resistance_2}")
# print(df)
df["df_current_analysed"] = df_current_analysed
print(df)
bool_df = df["current"]

# print(bool_df)guijkm,i6i8u7
