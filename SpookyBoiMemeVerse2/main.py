

import tensorflow as tf 
import pandas as pd 
import numpy as np 
import matplotlib as mpl
import matplotlib.pyplot as plt

print( np.zeros((4,4)))
df = pd.DataFrame(
{"a" : [4, 5, 6],
"b" : [7, 8, 9],
"c" : [10, 11, 12]},
index = [1, 2, 3])

print(df)