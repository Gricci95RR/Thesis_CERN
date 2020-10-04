#---Spike height (Max val - Average of steady state before spike)

#--------2016

df_start = df[df[POS_COL] == pos].index[0]
df_end = after 2 seconds...

#Search df subset for max value
df_subset = df.iloc[df_start:df_end]
max_val = df_subset[df_subset.columns[2]].max()
max_index = df_subset[df_subset[df_subset.columns[2]] == max_val].index[0]

#Steady state average before spike
df_prev = df.iloc[:df_start]
avg = df_prev[df_prev.columns[2]].sum() / len(df_prev)

spike_height = max_val - avg

#--------2018

#Search data for max value
#flattop - [30:75], injection - [80:125]
max_val = df_data[df_data.columns[0]].loc[80:125].max()
max_index = df_data[df_data[df_data.columns[0]] == max_val].index[0]

#Steady state average before spike
spike_start = max_index - 10 	#point when collimator moves in
df_steady = df_data.iloc[:spike_start]
avg = df_steady[df_steady.columns[0]].sum() / len(df_steady)

spike_height = max_val - avg








