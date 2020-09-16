import pandas as pd

df1 = pd.read_csv('/Users/gianmarcoricci/Documents/GitHub/Thesis_CERN/Feature Extraction/ 2018 dataframe extracted (no TCL)/1-test_2018.csv')
df2 = pd.read_csv('/Users/gianmarcoricci/Documents/GitHub/Thesis_CERN/Feature Extraction/ 2018 dataframe extracted (no TCL)/2-test_2018.csv')
df3 = pd.read_csv('/Users/gianmarcoricci/Documents/GitHub/Thesis_CERN/Feature Extraction/ 2018 dataframe extracted (no TCL)/3-inj_2018.csv')
df4 = pd.read_csv('/Users/gianmarcoricci/Documents/GitHub/Thesis_CERN/Feature Extraction/ 2018 dataframe extracted (no TCL)/4-flat_2018.csv')
df5 = pd.read_csv('/Users/gianmarcoricci/Documents/GitHub/Thesis_CERN/Feature Extraction/ 2018 dataframe extracted (no TCL)/2018_MD3.csv')
# Merge all dataframe in one
frames = [df1, df2, df3, df4, df5]
dataframe = pd.concat(frames)
dataframe.to_csv("2018_dataset_GR_NO_TCL.csv",index = False)

