import pandas as pd  
import numpy as np
import seaborn as sn
import matplotlib.pyplot as plt

df =pd.read_csv("../data/13-04.csv")

attrs = list(df)[1:]

corr_matrix = df[attrs].corr()
sn.heatmap(corr_matrix, annot=True, vmin = -1, vmax = 1)
plt.show()