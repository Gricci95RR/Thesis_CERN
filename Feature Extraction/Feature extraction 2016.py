import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from glob import iglob
import math
from scipy.optimize import curve_fit

def exponential(x, a, b, c):
    

	y = a * np.exp(-b * x) + c
	return y

def power_law(x, a, b, c):
    return a * np.power(x, b) + c

# import of i_col_info 2016
i_col_info = pd.read_csv(r'/Users/gianmarcoricci/Google Drive/UNI/Thesis CERN/Data/col_info/2016/i_col_info.csv')
# names of the files to import
filenames = iglob('/Users/gianmarcoricci/Google Drive/UNI/Thesis CERN/Data/GabyPhD2019-Training_data/data/no_spike/2016-04-02_i/*.csv')
#17
pos_sigma = []
spike_height = []
for i in filenames:
    df = pd.read_csv(i, header = None, nrows=1) # string
    df1 = pd.read_csv(i, header = None, skiprows=1) # values
    df1[2] = df1[2] * 1e06
    name = df.iat[0,2]
    name2 = name[17:]
    for j in i_col_info.index:
        if i_col_info.iat[j,0] == name2:
            # pos_sigma
            centre = i_col_info.iat[j,2]
            sigma_x = i_col_info.iat[j,3]
            sigma_y = i_col_info.iat[j,4]
            theta =  i_col_info.iat[j,1]
            pos_mm = df1.iat[0,1] #verify
            beam_size = math.sqrt((math.pow(sigma_x,2) * math.pow(math.cos(theta),2)) + (math.pow(sigma_y,2) * math.pow(math.sin(theta),2)))
            pos_sigma_a = (pos_mm - centre) / beam_size
            pos_sigma.append(pos_sigma_a)
            
            # Spike_height
            df_start = df1[df1[1] != pos_mm].index[0] #verify
            df_end = df_start + 200 #df_start + 2 sec (100cells = 1sec)
            #Search df subset for max value
            df_subset = df1.iloc[df_start:df_end]
            max_val = df_subset.iloc[:,2].max()
            max_index = df_subset[df_subset[2] == max_val].index[0]
            #Steady state average before spike
            df_prev = df1.iloc[:df_start]
            avg = df_prev[df_prev.columns[2]].sum() / len(df_prev)
            spike_height = max_val - avg
            
            # Exp fit
            end2 = max_index + 600 
            y = df1.iloc[max_index:end2,2] #time window of 6 seconds starting from the maximum value index
            x = np.arange(start=0, stop=len(y), step=1)
            try:
                popt, pcov = curve_fit(exponential, x, y)
            except RuntimeError as e:
                pass
            
            # Power fit
            try:
                popt2, pcov = curve_fit(power_law, x, y)
            except RuntimeError as e:
                pass
            
            print(i)
            print("Position sigma:" ,pos_sigma_a)
            print("Maximum value:", max_val)
            print("Spike height:", spike_height)
            print("Exp_a, Exp_b, Exp_c:", popt)
            print("Pow_a, Pow_b, Pow_c:", popt2)