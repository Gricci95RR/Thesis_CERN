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
    name = df.iat[0,2]
    name2 = name[17:]
    for j in i_col_info.index:
        if i_col_info.iat[j,0] == name2:
            # pos_sigma
            centre = i_col_info.iat[j,2]
            sigma_x = i_col_info.iat[j,3]
            sigma_y = i_col_info.iat[j,4]
            pos_mm = df1.iat[0,1]
            theta = 2e-06 # verify
            beam_size = math.sqrt((math.pow(sigma_x,2) * math.pow(math.cos(theta),2)) + (math.pow(sigma_y,2) * math.pow(math.sin(theta),2)))
            pos_sigma_a = (pos_mm - centre) / beam_size
            pos_sigma.append(pos_sigma_a)
            
            print(i)
            print("Position sigma:" ,pos_sigma_a)
