import pandas as pd

df1 = pd.read_csv('/Users/gianmarcoricci/Documents/GitHub/Thesis_CERN/Dataset/2016_dataset.csv').drop(['Maximum value'],axis=1)
df2 = pd.read_csv('/Users/gianmarcoricci/Documents/GitHub/Thesis_CERN/Dataset/Auto_2018_dataset_.csv').drop(['Unnamed: 0'],axis=1)

# Merge all dataframe in one
frames = [df1, df2]
dataframe = pd.concat(frames)
dataframe.to_csv("dataset.csv",index = False)