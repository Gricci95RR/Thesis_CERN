# This script extract the features from the folders: 
# 1-test_2018, 2-test_2018, 3-inj_2018, 4-flat_2018, 2018_MD3, 2018_MD4
import os, glob
import pandas as pd

# 1-test_2018
path = "/Users/gianmarcoricci/Google Drive/UNI/Thesis CERN/Data/Auto_data/1-test_2018"
all_files = glob.glob(os.path.join(path, "*Align_features"))

all_df = []
for f in all_files:
    df = pd.read_csv(f)
    df['full path'] = f
    df['alignment'] = f.split('/')[-1]
    all_df.append(df)
    
test_1_2018 = pd.concat(all_df, ignore_index=True, sort=True)

collimator_type = []
beam_type = []
beam_state = []
for i in test_1_2018.index:
    name_l=test_1_2018.iat[i,0]
    name_l=name_l[11:]
    beam_type.append('PROTON')
    beam_state.append('I')
    for kk in range(0, len(name_l)):
        if name_l[kk] == "." and kk<6:
            collimator_type.append(name_l[:kk])

test_1_2018['collimator_type'] = collimator_type
test_1_2018['beam_type'] = beam_type
test_1_2018['beam_state'] = beam_state

# 2-test_2018
path = "/Users/gianmarcoricci/Google Drive/UNI/Thesis CERN/Data/Auto_data/2-test_2018"
all_files = glob.glob(os.path.join(path, "*Align_features"))

all_df = []
for f in all_files:
    df = pd.read_csv(f)
    df['full path'] = f
    df['alignment'] = f.split('/')[-1]
    all_df.append(df)
    
test_2_2018 = pd.concat(all_df, ignore_index=True, sort=True)


collimator_type = []
beam_type = []
beam_state = []
for i in test_2_2018.index:
    name_l=test_2_2018.iat[i,0]
    name_l=name_l[11:]
    beam_type.append('PROTON')
    beam_state.append('I')
    for kk in range(0, len(name_l)):
        if name_l[kk] == "." and kk<6:
            collimator_type.append(name_l[:kk])

test_2_2018['collimator_type'] = collimator_type
test_2_2018['beam_type'] = beam_type
test_2_2018['beam_state'] = beam_state

# 3-inj_2018
path = "/Users/gianmarcoricci/Google Drive/UNI/Thesis CERN/Data/Auto_data/3-inj_2018"
all_files = glob.glob(os.path.join(path, "*Align_features"))

all_df = []
for f in all_files:
    df = pd.read_csv(f)
    df['full path'] = f
    df['alignment'] = f.split('/')[-1]
    all_df.append(df)
    
inj_3_2018 = pd.concat(all_df, ignore_index=True, sort=True)


collimator_type = []
beam_type = []
beam_state = []
for i in inj_3_2018.index:
    name_l=inj_3_2018.iat[i,0]
    name_l=name_l[11:]
    beam_type.append('PROTON')
    beam_state.append('I')
    for kk in range(0, len(name_l)):
        if name_l[kk] == "." and kk<6:
            collimator_type.append(name_l[:kk])

inj_3_2018['collimator_type'] = collimator_type
inj_3_2018['beam_type'] = beam_type
inj_3_2018['beam_state'] = beam_state

# 4-flat_2018
path = "/Users/gianmarcoricci/Google Drive/UNI/Thesis CERN/Data/Auto_data/4-flat_2018"
all_files = glob.glob(os.path.join(path, "*Align_features"))

all_df = []
for f in all_files:
    df = pd.read_csv(f)
    df['full path'] = f
    df['alignment'] = f.split('/')[-1]
    all_df.append(df)
    
flat_4_2018 = pd.concat(all_df, ignore_index=True, sort=True)


collimator_type = []
beam_type = []
beam_state = []
for i in flat_4_2018.index:
    name_l=flat_4_2018.iat[i,0]
    name_l=name_l[11:]
    beam_type.append('PROTON')
    beam_state.append('FT')
    for kk in range(0, len(name_l)):
        if name_l[kk] == "." and kk<6:
            collimator_type.append(name_l[:kk])

flat_4_2018['collimator_type'] = collimator_type
flat_4_2018['beam_type'] = beam_type
flat_4_2018['beam_state'] = beam_state

# 2018_MD3
path = "/Users/gianmarcoricci/Google Drive/UNI/Thesis CERN/Data/Auto_data/2018_MD3"
all_files = glob.glob(os.path.join(path, "*Align_features"))

all_df = []
for f in all_files:
    df = pd.read_csv(f)
    df['full path'] = f
    df['alignment'] = f.split('/')[-1]
    all_df.append(df)
    
MD3_2018 = pd.concat(all_df, ignore_index=True, sort=True)


collimator_type = []
beam_type = []
beam_state = []
for i in MD3_2018.index:
    name_l=MD3_2018.iat[i,0]
    name_l=name_l[11:]
    beam_type.append('PROTON')
    beam_state.append('I')
    for kk in range(0, len(name_l)):
        if name_l[kk] == "." and kk<6:
            collimator_type.append(name_l[:kk])

MD3_2018['collimator_type'] = collimator_type
MD3_2018['beam_type'] = beam_type
MD3_2018['beam_state'] = beam_state

# 2018_MD4
path = "/Users/gianmarcoricci/Google Drive/UNI/Thesis CERN/Data/Auto_data/2018_MD4"
all_files = glob.glob(os.path.join(path, "*Align_features"))

all_df = []
for f in all_files:
    df = pd.read_csv(f)
    df['full path'] = f
    df['alignment'] = f.split('/')[-1]
    all_df.append(df)
    
MD4_2018 = pd.concat(all_df, ignore_index=True, sort=True)


collimator_type = []
beam_type = []
beam_state = []
for i in MD4_2018.index:
    name_l=MD4_2018.iat[i,0]
    name_l=name_l[11:]
    beam_type.append('PROTON')
    beam_state.append('I')
    for kk in range(0, len(name_l)):
        if name_l[kk] == "." and kk<6:
            collimator_type.append(name_l[:kk])

MD4_2018['collimator_type'] = collimator_type
MD4_2018['beam_type'] = beam_type
MD4_2018['beam_state'] = beam_state

# Merge all dataframes in one
frames = [test_1_2018, test_2_2018, inj_3_2018, flat_4_2018, MD3_2018, MD4_2018]
total_dataframe = pd.concat(frames)
print(total_dataframe)
total_dataframe.to_csv('2018_dataset_Gabriella.csv')