# This script extract the features from the folder: 
# 2018_IONS_Collisions
import os, glob
import pandas as pd

# 1-test_2018
path = "/Users/gianmarcoricci/Google Drive/UNI/Thesis CERN/Data/Auto_data/2018_IONS_Collisions"
all_files = glob.glob(os.path.join(path, "*Align_features"))

all_df = []
for f in all_files:
    df = pd.read_csv(f)
    df['full path'] = f
    df['alignment'] = f.split('/')[-1]
    all_df.append(df)
    
IONS_Collisions_2018 = pd.concat(all_df, ignore_index=True, sort=True)


collimator_type = []
beam_type = []
beam_state = []
for i in IONS_Collisions_2018.index:
    name_l=IONS_Collisions_2018.iat[i,0]
    name_l=name_l[11:]
    beam_type.append('ION')
    beam_state.append('COLLISION')
    for kk in range(0, len(name_l)):
        if name_l[kk] == "." and kk<6:
            collimator_type.append(name_l[:kk])

IONS_Collisions_2018['collimator_type'] = collimator_type
IONS_Collisions_2018['beam_type'] = beam_type
IONS_Collisions_2018['beam_state'] = beam_state

print(IONS_Collisions_2018)
IONS_Collisions_2018.to_csv("2018_IONS_Collisions.csv")

