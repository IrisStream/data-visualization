import pandas as pd 
import numpy as np   

df = pd.read_csv("../data/13-04.csv")

attrs = list(df)[1:]

df[attrs] = df[attrs].replace({',':''}, regex=True)     #Remove all , in a number (Ex: 22,223,687)
df[attrs] = df[attrs].replace({' ':''}, regex=True)     #Remove all leading space (Ex: " 22,223,687 ")
# df[attrs] = pd.to_numeric(df[attrs])
df[attrs] = df[attrs].apply(pd.to_numeric)              #Convert all data to numeric
df[attrs] = df[attrs].replace(np.nan, 0, regex=True)    #fill all missing value with 0

df.to_csv("../data/13-04.csv")