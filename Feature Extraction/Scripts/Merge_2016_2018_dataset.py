import pandas as pd

df1 = pd.read_csv('/Users/gianmarcoricci/Documents/GitHub/Thesis_CERN/Dataset/2016_dataset.csv').drop(['Maximum value'],axis=1)
df2 = pd.read_csv('/Users/gianmarcoricci/Documents/GitHub/Thesis_CERN/Dataset/2018_dataset_GR_NO_TCL.csv').drop(['Unnamed: 0'],axis=1)
df3 = pd.read_csv('/Users/gianmarcoricci/Documents/GitHub/Thesis_CERN/Dataset/2017_dataset.csv')
# Merge all dataframe in one
frames = [df1, df2, df3]
dataframe = pd.concat(frames)
dataframe.to_csv("dataset_2016_2017_2018(GR)_NO_TCL.csv",index = False)