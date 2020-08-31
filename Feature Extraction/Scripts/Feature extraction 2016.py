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
filenames = iglob(
    '/Users/gianmarcoricci/Google Drive/UNI/Thesis CERN/Data/GabyPhD2019-Training_data/data/no_spike/2016-04-02_i/*.csv')

pos_sigma = []
spike_height = []
max_value = []
exp = []
beam_state = []
beam_type = []
spike = []
jaw = []
collimator_type = []
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
            pos_mm = df1.iat[len(df1)-1,1] 
            beam_size = math.sqrt((math.pow(sigma_x,2) * math.pow(math.cos(theta),2)) + (math.pow(sigma_y,2) * math.pow(math.sin(theta),2)))
            if i[109:114] == 'Right' or i[106:111] == 'Right':
                pos_sigma_a = (centre - pos_mm) / beam_size
                pos_sigma.append(pos_sigma_a)
            elif i[109:113] == 'Left' or i[106:110] == 'Left':
                pos_sigma_a = (pos_mm - centre) / beam_size
                pos_sigma.append(pos_sigma_a)
            
            # Spike_height
            df_start = df1[df1[1] == pos_mm].index[0] 
            df_end = df_start + 200 #df_start + 2 sec (100cells = 1sec)
            #Search df subset for max value
            df_subset = df1.iloc[df_start:df_end]
            max_val = df_subset.iloc[:,2].max()
            max_index = df_subset[df_subset[2] == max_val].index[0]
            #Steady state average before spike
            df_prev = df1.iloc[:df_start]
            avg = df_prev[df_prev.columns[2]].sum() / len(df_prev)
            spike_height_a = max_val - avg
            spike_height.append(spike_height_a)
            max_value.append(max_val)
            
            # Exp fit
            end2 = max_index + 600 
            y = df1.iloc[max_index:end2,2] #time window of 6 seconds starting from the maximum value index
            x = np.arange(start=0, stop=len(y), step=1)
            
            try:
                popt, pcov = curve_fit(exponential, x, y)
                exp.append(popt)
            except RuntimeError as e:
                pass
            
            # Power fit
            try:
                popt2, pcov = curve_fit(power_law, x, y)
            except RuntimeError as e:
                pass
            
            # Beam state (Inj or FT)
            if i[103:105] == '_i' or i[106:108] == '_i':
                beam_state.append('I')
            elif i[103:105] == '_f' or i[106:108] == '_f':
                beam_state.append('FT')
            
            # Beam type
            beam_type.append('PROTON')
            
            # Spike
            if i[87:95] == 'no_spike':
                spike.append(0)
            elif i[87:92] == 'spike': #verify
                spike.append(1)
             
            # Jaw (0 = Left, 1 = Right)
            if i[109:114] == 'Right' or i[106:111] == 'Right':
                jaw.append(1)
            elif i[109:113] == 'Left' or i[106:110] == 'Left':
                jaw.append(0)
            
            # collimator type
            collimator_name = df.iloc[0][2]
            collimator_name = collimator_name[17:]
            
            for kk in range(0, len(collimator_name)):
                if collimator_name[kk] == "." and kk<6:
                    collimator_type.append(collimator_name[:kk])
                
                
            
                   
            '''    
            print(i)
            print("Position sigma:" ,pos_sigma_a)
            print("Maximum value:", max_val)
            print("Spike height:", spike_height_a)
            print("Exp_a, Exp_b, Exp_c:", popt)
            print("Pow_a, Pow_b, Pow_c:", popt2)
            '''

exp_a = []
exp_b = []
exp_c = []
for j in range(0,len(exp)):
    exp_a.append(exp[j][0])
    exp_b.append(exp[j][1])   
    exp_c.append(exp[j][2])
 
data = {'Jaw': jaw,
        'Spike height': spike_height,
        'Position in sigma': pos_sigma,
        'Maximum value': max_value,
        'Exp_a': exp_a,
        'Exp_b': exp_b,
        'Exp_c': exp_c,
        'Spike': spike,
        'Collimator type': collimator_type,
        'Beam Type': beam_type,
        'Beam State': beam_state
        }

df2 = pd.DataFrame (data) 
print(df2)

df2.to_csv('2016-04-02_i.csv')
