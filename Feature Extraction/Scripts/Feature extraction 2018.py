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

def stampa(i,pos_sigma,max_val,s_h,popt,jaw_):
    print(i)
    print("Position sigma right:", pos_sigma)
    #print("Maximum value:", max_val)
    print("Spike_height:", s_h)
    print("Exp_a, Exp_b, Exp_c:", popt)
    print('Jaw:',jaw_) 

# import of i_col_info
i_col_info = pd.read_csv(r'/Users/gianmarcoricci/Google Drive/UNI/Thesis CERN/Data/col_info/2018/i_col_info.csv')
# names of the files to import
filenames = iglob('/Users/gianmarcoricci/Google Drive/UNI/Thesis CERN/Data/Auto_data/1-test_2018/*_Align')

pos_sigma = []
spike_height = []
max_value = []
exp = []
collimator_type = []

beam_state = []
beam_type = []
spike = []
jaw = []

for i in filenames:
    df = pd.read_csv(i, sep="=", header = None, nrows=9)
    df2 = pd.read_csv(i, skiprows=10, header = None)
    df3 = pd.concat([df, df2])
    df4 = pd.read_csv(i, skiprows=11, header = None) # dataframe with only BLM values
    df4 = df4 * 1000000
    theta = df3.iat[2,1]
    LU = df3.iat[5,1] 
    RU = df3.iat[7,1] 
    try:
        name = df3.iat[9,0]
        name2 = name[17:]
    except:
        # only for 1-test-2018
        name1 = i[89:]
        for kk in range(0, len(name1)):
                    if name1[kk] == "_":
                        name2 = name1[:kk]
    
    
    for j in i_col_info.index:
        if i_col_info.iat[j,0] == name2:
            # pos_sigma
            centre = i_col_info.iat[j,2]
            sigma_x = i_col_info.iat[j,3]
            sigma_y = i_col_info.iat[j,4]
            beam_size = math.sqrt((math.pow(sigma_x,2) * math.pow(math.cos(theta),2)) + (math.pow(sigma_y,2) * math.pow(math.sin(theta),2)))
            
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
            
            # exp fit
            y = df4.iloc[max_index:,0] # decay
            x = np.arange(start=0, stop=len(y), step=1)
            try:
                popt, pcov = curve_fit(exponential, x, y)
                if df3.iat[3,1] == 0: #if (left_step_size == 0) jaw=right
                    jaw_=1
                    jaw.append(jaw_)
                    pos_sigma_ = np.abs(RU) / beam_size 
                    pos_sigma.append(pos_sigma_)
                    beam_type.append('PROTON')
                    beam_state.append('I')
                    spike_height.append(s_h)
                    max_value.append(max_val)
                    exp.append(popt)
                    # collimator type
                    for kk in range(0, len(name2)):
                        if name2[kk] == "." and kk<6:
                            collimator_type.append(name2[:kk])
                    if(i[89:]=='TCP.D6L7.B1_Align'):
                        stampa(i,pos_sigma_,max_val,s_h,popt,jaw_)        
                elif df3.iat[4,1] == 0:
                    jaw_=0
                    jaw.append(jaw_)
                    pos_sigma_ = np.abs(LU) / beam_size #left
                    pos_sigma.append(pos_sigma_)
                    beam_type.append('PROTON')
                    beam_state.append('I')
                    spike_height.append(s_h)
                    max_value.append(max_val)
                    exp.append(popt)
                    # collimator type
                    for kk in range(0, len(name2)):
                        if name2[kk] == "." and kk<6:
                            collimator_type.append(name2[:kk])
                    if(i[89:]=='TCP.D6L7.B1_Align'):
                        stampa(i,pos_sigma_,max_val,s_h,popt,jaw_) 
                elif df3.iat[3,1] != 0 and df3.iat[4,1] !=0:
                    jaw_=1
                    jaw.append(jaw_)
                    pos_sigma_ = np.abs(RU) / beam_size 
                    pos_sigma.append(pos_sigma_)
                    jaw_=0
                    jaw.append(jaw_)
                    spike_height.append(s_h)
                    max_value.append(max_val)
                    beam_type.append('PROTON')
                    beam_state.append('I')
                    exp.append(popt)
                    for kk in range(0, len(name2)):
                        if name2[kk] == "." and kk<6:
                            collimator_type.append(name2[:kk])
                    if(i[89:]=='TCP.D6L7.B1_Align'):
                        stampa(i,pos_sigma_,max_val,s_h,popt,jaw_) 
                    
                    pos_sigma_ = np.abs(LU) / beam_size #left
                    pos_sigma.append(pos_sigma_)
                    beam_type.append('PROTON')
                    beam_state.append('I')
                    spike_height.append(s_h)
                    max_value.append(max_val)
                    exp.append(popt)
                    # collimator type
                    for kk in range(0, len(name2)):
                        if name2[kk] == "." and kk<6:
                            collimator_type.append(name2[:kk])
                    if(i[89:]=='TCP.D6L7.B1_Align'):
                        stampa(i,pos_sigma_,max_val,s_h,popt,jaw_) 
            except RuntimeError as e:
                pass
            
            pass
        

exp_a = []
exp_b = []
exp_c = []
for j in range(0,len(exp)):
    exp_a.append(exp[j][0])
    exp_b.append(exp[j][1])   
    exp_c.append(exp[j][2])           

data = {
        'jaw': jaw,
        'height': spike_height,
        'position': pos_sigma,
        'Maximum value': max_value,
        'decay_a': exp_a,
        'decay_b': exp_b,
        'decay_c': exp_c,
        #'spike': spike,
        'collimator_type': collimator_type,
        'beam_type': beam_type,
        'beam_state': beam_state
        }

print(len(jaw))
print(len(spike_height))
print(len(max_value))
print(len(exp_a))
print(len(exp_b))
print(len(exp_c))
print(len(spike))
print(len(collimator_type))
print(len(beam_type))
print(len(beam_state))

df2 = pd.DataFrame (data) 
#print(df2)

#df2.to_csv('2016-07-31_f.csv')
