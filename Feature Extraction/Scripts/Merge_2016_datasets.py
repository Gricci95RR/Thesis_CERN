import pandas as pd

# no spike
df1 = pd.read_csv('/Users/gianmarcoricci/Documents/GitHub/Thesis_CERN/Feature Extraction/No Spike/2016-04-02_i.csv').drop(['Unnamed: 0'],axis=1)
df2 = pd.read_csv('/Users/gianmarcoricci/Documents/GitHub/Thesis_CERN/Feature Extraction/No Spike/2016-04-06_f.csv').drop(['Unnamed: 0'],axis=1)
df3 = pd.read_csv('/Users/gianmarcoricci/Documents/GitHub/Thesis_CERN/Feature Extraction/No Spike/2016-04-19_f.csv').drop(['Unnamed: 0'],axis=1)
df4 = pd.read_csv('/Users/gianmarcoricci/Documents/GitHub/Thesis_CERN/Feature Extraction/No Spike/2016-07-29_f.csv').drop(['Unnamed: 0'],axis=1)
df5 = pd.read_csv('/Users/gianmarcoricci/Documents/GitHub/Thesis_CERN/Feature Extraction/No Spike/2016-07-31_f.csv').drop(['Unnamed: 0'],axis=1)
# spike
df11 = pd.read_csv('/Users/gianmarcoricci/Documents/GitHub/Thesis_CERN/Feature Extraction/Spike/2016-04-02_i.csv').drop(['Unnamed: 0'],axis=1)
df22 = pd.read_csv('/Users/gianmarcoricci/Documents/GitHub/Thesis_CERN/Feature Extraction/Spike/2016-04-06_f.csv').drop(['Unnamed: 0'],axis=1)
df33 = pd.read_csv('/Users/gianmarcoricci/Documents/GitHub/Thesis_CERN/Feature Extraction/Spike/2016-04-19_f.csv').drop(['Unnamed: 0'],axis=1)
df44 = pd.read_csv('/Users/gianmarcoricci/Documents/GitHub/Thesis_CERN/Feature Extraction/Spike/2016-07-29_f.csv').drop(['Unnamed: 0'],axis=1)
df55 = pd.read_csv('/Users/gianmarcoricci/Documents/GitHub/Thesis_CERN/Feature Extraction/Spike/2016-07-31_f.csv').drop(['Unnamed: 0'],axis=1)


# Merge all dataframe in one
frames = [df1, df2, df3, df4, df5, df11, df22, df33, df44, df55]
dataframe = pd.concat(frames)
dataframe.to_csv("2016_dataset.csv",index = False)

