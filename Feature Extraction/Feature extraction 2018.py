import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from glob import iglob
import math
from scipy.optimize import curve_fit

#Fit exponential curve to data
# x - x value
# a - y-intercept
# b	- gradient
# c	- y-asymptote
#Returns y value
def exponential(x, a, b, c):
    y = a * np.exp(-b * x) + c
    return y

def power_law(x, a, b, c):
    return a * np.power(x, b) + c

# import of i_col_info
i_col_info = pd.read_csv(r'/Users/gianmarcoricci/Google Drive/UNI/Thesis CERN/Data/col_info/2018/i_col_info.csv')
# names of the files to import
filenames = iglob('/Users/gianmarcoricci/Google Drive/UNI/Thesis CERN/Data/Auto_data/2-test_2018/*_Align')

pos_sigma1 = []
pos_sigma2 = []
spike_height = []
for i in filenames:
    df = pd.read_csv(i, sep="=", header = None, nrows=9)
    df2 = pd.read_csv(i, skiprows=10, header = None)
    df3 = pd.concat([df, df2])
    df4 = pd.read_csv(i, skiprows=11, header = None) # dataframe with only BLM values
    theta = df3.iat[2,1]
    LU = df3.iat[5,1] 
    RU = df3.iat[7,1] 
    name = df3.iat[9,0]
    name2 = name[17:]
    for j in i_col_info.index:
        if i_col_info.iat[j,0] == name2:
            # pos_sigma
            centre = i_col_info.iat[j,2]
            sigma_x = i_col_info.iat[j,3]
            sigma_y = i_col_info.iat[j,4]
            beam_size = math.sqrt((math.pow(sigma_x,2) * math.pow(math.cos(theta),2)) + (math.pow(sigma_y,2) * math.pow(math.sin(theta),2)))
            pos_sigma_a = np.abs(LU) / beam_size
            pos_sigma_b = np.abs(RU) / beam_size
            pos_sigma1.append(pos_sigma_a)
            pos_sigma2.append(pos_sigma_b)
            
            # spike_height
            #Search data for max value
            #flattop - [30:75], injection - [80:125]
            max_val = df4.iloc[80:125,0].max()
            max_index = df4[df4[0] == max_val].index[0]
            #Steady state average before spike
            spike_start = max_index - 10 	#point when collimator moves in
            df_steady = df4.iloc[0:spike_start,0]
            avg = df_steady.sum() / len(df_steady)
            s_h = max_val - avg
            spike_height.append(s_h)
            
            # exp fit
            y = df4.iloc[max_index:,0] # decay
            x = np.arange(start=0, stop=len(y), step=1)
            try:
                popt, pcov = curve_fit(exponential, x, y)
            except RuntimeError as e:
                pass
            
            
            try:
                popt2, pcov = curve_fit(power_law, x, y)
            except RuntimeError as e:
                pass
            
            print(i)
            print("Position sigma 1:", pos_sigma_a)
            print("Position sigma 2:", pos_sigma_b)
            print("Maximum value:", max_val)
            print("Spike_height:", s_h)
            print("Exp_a, Exp_b, Exp_c:", popt)
            print("Pow_a, Pow_b, Pow_c:", popt2)


