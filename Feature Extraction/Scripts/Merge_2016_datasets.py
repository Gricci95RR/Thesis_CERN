import pandas as pd

# no spike
df1 = pd.read_csv('/Users/gianmarcoricci/Documents/GitHub/Thesis_CERN/Feature Extraction/2017 dataset extracted/no_spike/2017-04-30_f.csv').drop(['Unnamed: 0'],axis=1)
df2 = pd.read_csv('/Users/gianmarcoricci/Documents/GitHub/Thesis_CERN/Feature Extraction/2017 dataset extracted/no_spike/2017-05-01_f.csv').drop(['Unnamed: 0'],axis=1)
df3 = pd.read_csv('/Users/gianmarcoricci/Documents/GitHub/Thesis_CERN/Feature Extraction/2017 dataset extracted/no_spike/2017-05-07_f.csv').drop(['Unnamed: 0'],axis=1)
df4 = pd.read_csv('/Users/gianmarcoricci/Documents/GitHub/Thesis_CERN/Feature Extraction/2017 dataset extracted/no_spike/2017-05-09_f.csv').drop(['Unnamed: 0'],axis=1)
df5 = pd.read_csv('/Users/gianmarcoricci/Documents/GitHub/Thesis_CERN/Feature Extraction/2017 dataset extracted/no_spike/2017-05-13_f.csv').drop(['Unnamed: 0'],axis=1)
df6 = pd.read_csv('/Users/gianmarcoricci/Documents/GitHub/Thesis_CERN/Feature Extraction/2017 dataset extracted/no_spike/2017-09-17_f.csv').drop(['Unnamed: 0'],axis=1)
# spike
df11 = pd.read_csv('/Users/gianmarcoricci/Documents/GitHub/Thesis_CERN/Feature Extraction/2017 dataset extracted/spike/2017-05-01_f.csv').drop(['Unnamed: 0'],axis=1)
df22 = pd.read_csv('/Users/gianmarcoricci/Documents/GitHub/Thesis_CERN/Feature Extraction/2017 dataset extracted/spike/2017-04-30_f.csv').drop(['Unnamed: 0'],axis=1)
df33 = pd.read_csv('/Users/gianmarcoricci/Documents/GitHub/Thesis_CERN/Feature Extraction/2017 dataset extracted/spike/2017-05-13_f.csv').drop(['Unnamed: 0'],axis=1)



# Merge all dataframe in one
frames = [df1, df2, df3, df4, df5, df11, df22, df33, df6]
dataframe = pd.concat(frames)
dataframe.to_csv("2017_dataset.csv",index = False)

