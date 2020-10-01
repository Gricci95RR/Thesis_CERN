from glob import iglob
import pandas as pd
import numpy as np

# 1) "1-test_2018"
# Load of all TCP features from "1-test_2018"
path = r'/Users/gianmarcoricci/Google Drive/UNI/Thesis CERN/Data/Auto_data/1-test_2018/*_TCP*_Align_features'
all_rec = iglob(path, recursive=True)     
for f in all_rec:
    TCP_features = pd.read_csv(f)
    #TCP_features = pd.concat(dataframes, ignore_index=True)
    # Add a column to the dataframe that represents the collimator type (TCP, TCSG, TCLA, TCT, TCDQ)
    TCP_features["collimator_type"] = "TCP"
    # Add a column to the dataframe that represents the beam type type (ION or PROTON)
    TCP_features["beam_type"] = "PROTON"
    # Add a column to the dataframe that represents the beam state (Injection (I) or Flat top (FT))
    TCP_features["beam_state"] = "I"
    # Add a column to the dataframe that represents the path
    TCP_features["path"] = f
    TCP_features = pd.concat(TCP_features, ignore_index=True)
'''
# Load of all TCSG features from "1-test_2018"
path = r'/Users/gianmarcoricci/Google Drive/UNI/Thesis CERN/Data/Auto_data/1-test_2018/*_TCSG*_Align_features'
all_rec = iglob(path, recursive=True)     
dataframes = (pd.read_csv(f) for f in all_rec)
TCSG_features = pd.concat(dataframes, ignore_index=True)
TCSG_features
# Add a column to the dataframe that represents the collimator type (TCP, TCSG, TCLA, TCT, TCDQ)
TCSG_features["collimator_type"] = "TCSG"
# Add a column to the dataframe that represents the beam type type (ION or PROTON)
TCSG_features["beam_type"] = "PROTON"
# Add a column to the dataframe that represents the beam state (Injection (I) or Flat top (FT))
TCSG_features["beam_state"] = "I"

# Load of all TCLA features from "1-test_2018"
path = r'/Users/gianmarcoricci/Google Drive/UNI/Thesis CERN/Data/Auto_data/1-test_2018/*_TCLA*_Align_features'
all_rec = iglob(path, recursive=True)     
dataframes = (pd.read_csv(f) for f in all_rec)
TCLA_features = pd.concat(dataframes, ignore_index=True)
TCLA_features
# Add a column to the dataframe that represents the collimator type (TCP, TCSG, TCLA, TCT, TCDQ)
TCLA_features["collimator_type"] = "TCLA"
# Add a column to the dataframe that represents the beam type type (ION or PROTON)
TCLA_features["beam_type"] = "PROTON"
# Add a column to the dataframe that represents the beam state (Injection (I) or Flat top (FT))
TCLA_features["beam_state"] = "I"

# Load of all TCT features from "1-test_2018"
path = r'/Users/gianmarcoricci/Google Drive/UNI/Thesis CERN/Data/Auto_data/1-test_2018/*_TCT*_Align_features'
all_rec = iglob(path, recursive=True)     
dataframes = (pd.read_csv(f) for f in all_rec)
TCT_features = pd.concat(dataframes, ignore_index=True)
TCT_features
# Add a column to the dataframe that represents the collimator type (TCP, TCSG, TCLA, TCT, TCDQ)
TCT_features["collimator_type"] = "TCT"
# Add a column to the dataframe that represents the beam type type (ION or PROTON)
TCT_features["beam_type"] = "PROTON"
# Add a column to the dataframe that represents the beam state (Injection (I) or Flat top (FT))
TCT_features["beam_state"] = "I"

# Merge all dataframe in one
frames = [TCP_features, TCSG_features, TCLA_features, TCT_features]
I_test_2018_dataframe = pd.concat(frames)
I_test_2018_dataframe.to_csv("I_test_2018_dataframe.csv")

# 2) "2-test_2018"
# Load of all TCP features
path = r'/Users/gianmarcoricci/Google Drive/UNI/Thesis CERN/Data/Auto_data/2-test_2018/*_TCP*_Align_features'
all_rec = iglob(path, recursive=True)     
dataframes = (pd.read_csv(f) for f in all_rec)
TCP_features = pd.concat(dataframes, ignore_index=True)
# Add a column to the dataframe that represents the collimator type (TCP, TCSG, TCLA, TCT, TCDQ)
TCP_features["collimator_type"] = "TCP"
# Add a column to the dataframe that represents the beam type type (ION or PROTON)
TCP_features["beam_type"] = "PROTON"
# Add a column to the dataframe that represents the beam state (Injection (I) or Flat top (FT))
TCP_features["beam_state"] = "I"

# Load of all TCSG features
path = r'/Users/gianmarcoricci/Google Drive/UNI/Thesis CERN/Data/Auto_data/2-test_2018/*_TCSG*_Align_features'
all_rec = iglob(path, recursive=True)     
dataframes = (pd.read_csv(f) for f in all_rec)
TCSG_features = pd.concat(dataframes, ignore_index=True)
# Add a column to the dataframe that represents the collimator type (TCP, TCSG, TCLA, TCT, TCDQ)
TCSG_features["collimator_type"] = "TCSG"
# Add a column to the dataframe that represents the beam type type (ION or PROTON)
TCSG_features["beam_type"] = "PROTON"
# Add a column to the dataframe that represents the beam state (Injection (I) or Flat top (FT))
TCSG_features["beam_state"] = "I"

# Load of all TCLA features
path = r'/Users/gianmarcoricci/Google Drive/UNI/Thesis CERN/Data/Auto_data/2-test_2018/*_TCLA*_Align_features'
all_rec = iglob(path, recursive=True)     
dataframes = (pd.read_csv(f) for f in all_rec)
TCLA_features = pd.concat(dataframes, ignore_index=True)
TCLA_features
# Add a column to the dataframe that represents the collimator type (TCP, TCSG, TCLA, TCT, TCDQ)
TCLA_features["collimator_type"] = "TCLA"
# Add a column to the dataframe that represents the beam type type (ION or PROTON)
TCLA_features["beam_type"] = "PROTON"
# Add a column to the dataframe that represents the beam state (Injection (I) or Flat top (FT))
TCLA_features["beam_state"] = "I"


path = r'/Users/gianmarcoricci/Google Drive/UNI/Thesis CERN/Data/Auto_data/2-test_2018/*_TCT*_Align_features'
all_rec = iglob(path, recursive=True)     
dataframes = (pd.read_csv(f) for f in all_rec)
TCT_features = pd.concat(dataframes, ignore_index=True)
TCT_features
# Add a column to the dataframe that represents the collimator type (TCP, TCSG, TCLA, TCT, TCDQ)
TCT_features["collimator_type"] = "TCT"
# Add a column to the dataframe that represents the beam type type (ION or PROTON)
TCT_features["beam_type"] = "PROTON"
# Add a column to the dataframe that represents the beam state (Injection (I) or Flat top (FT))
TCT_features["beam_state"] = "I"

# Merge all dataframe in one
frames = [TCP_features, TCSG_features, TCLA_features,TCT_features]
II_test_2018_dataframe = pd.concat(frames)
II_test_2018_dataframe.to_csv("II_test_2018_dataframe.csv")

# 3) "2017_MD"
# Load of all TCP features
path = r'/Users/gianmarcoricci/Google Drive/UNI/Thesis CERN/Data/Auto_data/2017_MD/*_TCP*_Align_features'
all_rec = iglob(path, recursive=True)     
dataframes = (pd.read_csv(f) for f in all_rec)
TCP_features = pd.concat(dataframes, ignore_index=True)
# Add a column to the dataframe that represents the collimator type (TCP, TCSG, TCLA, TCT, TCDQ)
TCP_features["collimator_type"] = "TCP"
# Add a column to the dataframe that represents the beam type type (ION or PROTON)
TCP_features["beam_type"] = "PROTON"
# Add a column to the dataframe that represents the beam state (Injection (I) or Flat top (FT))
TCP_features["beam_state"] = "I"

# Load of all TCSG features
path = r'/Users/gianmarcoricci/Google Drive/UNI/Thesis CERN/Data/Auto_data/2017_MD/*_TCSG*_Align_features'
all_rec = iglob(path, recursive=True)     
dataframes = (pd.read_csv(f) for f in all_rec)
TCSG_features = pd.concat(dataframes, ignore_index=True)
TCSG_features
# Add a column to the dataframe that represents the collimator type (TCP, TCSG, TCLA, TCT, TCDQ)
TCSG_features["collimator_type"] = "TCSG"
# Add a column to the dataframe that represents the beam type type (ION or PROTON)
TCSG_features["beam_type"] = "PROTON"
# Add a column to the dataframe that represents the beam state (Injection (I) or Flat top (FT))
TCSG_features["beam_state"] = "I"

# Load of all TCLA features
path = r'/Users/gianmarcoricci/Google Drive/UNI/Thesis CERN/Data/Auto_data/2017_MD/*_TCLA*_Align_features'
all_rec = iglob(path, recursive=True)     
dataframes = (pd.read_csv(f) for f in all_rec)
TCLA_features = pd.concat(dataframes, ignore_index=True)
TCLA_features
# Add a column to the dataframe that represents the collimator type (TCP, TCSG, TCLA, TCT, TCDQ)
TCLA_features["collimator_type"] = "TCLA"
# Add a column to the dataframe that represents the beam type type (ION or PROTON)
TCLA_features["beam_type"] = "PROTON"
# Add a column to the dataframe that represents the beam state (Injection (I) or Flat top (FT))
TCLA_features["beam_state"] = "I"

# Load of all TCT features
path = r'/Users/gianmarcoricci/Google Drive/UNI/Thesis CERN/Data/Auto_data/2017_MD/*_TCT*_Align_features'
all_rec = iglob(path, recursive=True)     
dataframes = (pd.read_csv(f) for f in all_rec)
TCT_features = pd.concat(dataframes, ignore_index=True)
TCT_features
# Add a column to the dataframe that represents the collimator type (TCP, TCSG, TCLA, TCT, TCDQ)
TCT_features["collimator_type"] = "TCT"
# Add a column to the dataframe that represents the beam type type (ION or PROTON)
TCT_features["beam_type"] = "PROTON"
# Add a column to the dataframe that represents the beam state (Injection (I) or Flat top (FT))
TCT_features["beam_state"] = "I"

# Merge all dataframe in one
frames = [TCP_features, TCSG_features, TCLA_features]
MD_2017_dataframe = pd.concat(frames)
MD_2017_dataframe.to_csv("2017_MD_dataframe.csv")

# 4) "2018_MD3"
# Load of all TCP features
path = r'/Users/gianmarcoricci/Google Drive/UNI/Thesis CERN/Data/Auto_data/2018_MD3/*_TCP*_Align_features'
all_rec = iglob(path, recursive=True)     
dataframes = (pd.read_csv(f) for f in all_rec)
TCP_features = pd.concat(dataframes, ignore_index=True)
# Add a column to the dataframe that represents the collimator type (TCP, TCSG, TCLA, TCT, TCDQ)
TCP_features["collimator_type"] = "TCP"
# Add a column to the dataframe that represents the beam type type (ION or PROTON)
TCP_features["beam_type"] = "PROTON"
# Add a column to the dataframe that represents the beam state (Injection (I) or Flat top (FT))
TCP_features["beam_state"] = "I"

# Load of all TCSG features
path = r'/Users/gianmarcoricci/Google Drive/UNI/Thesis CERN/Data/Auto_data/2018_MD3/*_TCSG*_Align_features'
all_rec = iglob(path, recursive=True)     
dataframes = (pd.read_csv(f) for f in all_rec)
TCSG_features = pd.concat(dataframes, ignore_index=True)
TCSG_features
# Add a column to the dataframe that represents the collimator type (TCP, TCSG, TCLA, TCT, TCDQ)
TCSG_features["collimator_type"] = "TCSG"
# Add a column to the dataframe that represents the beam type type (ION or PROTON)
TCSG_features["beam_type"] = "PROTON"
# Add a column to the dataframe that represents the beam state (Injection (I) or Flat top (FT))
TCSG_features["beam_state"] = "I"

# Load of all TCLA features
path = r'/Users/gianmarcoricci/Google Drive/UNI/Thesis CERN/Data/Auto_data/2018_MD3/*_TCLA*_Align_features'
all_rec = iglob(path, recursive=True)     
dataframes = (pd.read_csv(f) for f in all_rec)
TCLA_features = pd.concat(dataframes, ignore_index=True)
TCLA_features
# Add a column to the dataframe that represents the collimator type (TCP, TCSG, TCLA, TCT, TCDQ)
TCLA_features["collimator_type"] = "TCLA"
# Add a column to the dataframe that represents the beam type type (ION or PROTON)
TCLA_features["beam_type"] = "PROTON"
# Add a column to the dataframe that represents the beam state (Injection (I) or Flat top (FT))
TCLA_features["beam_state"] = "I"

# Load of all TCT features
path = r'/Users/gianmarcoricci/Google Drive/UNI/Thesis CERN/Data/Auto_data/2018_MD3/*_TCT*_Align_features'
all_rec = iglob(path, recursive=True)     
dataframes = (pd.read_csv(f) for f in all_rec)
TCT_features = pd.concat(dataframes, ignore_index=True)
TCT_features
# Add a column to the dataframe that represents the collimator type (TCP, TCSG, TCLA, TCT, TCDQ)
TCT_features["collimator_type"] = "TCT"
# Add a column to the dataframe that represents the beam type type (ION or PROTON)
TCT_features["beam_type"] = "PROTON"
# Add a column to the dataframe that represents the beam state (Injection (I) or Flat top (FT))
TCT_features["beam_state"] = "I"

# TCLIA features
path = r'/Users/gianmarcoricci/Google Drive/UNI/Thesis CERN/Data/Auto_data/2018_MD3/*_TCLIA*_Align_features'
all_rec = iglob(path, recursive=True)     
dataframes = (pd.read_csv(f) for f in all_rec)
TCLIA_features = pd.concat(dataframes, ignore_index=True)
TCLIA_features
# Add a column to the dataframe that represents the collimator type (TCP, TCSG, TCLA, TCT, TCDQ)
TCLIA_features["collimator_type"] = "TCLIA"
# Add a column to the dataframe that represents the beam type type (ION or PROTON)
TCLIA_features["beam_type"] = "PROTON"
# Add a column to the dataframe that represents the beam state (Injection (I) or Flat top (FT))
TCLIA_features["beam_state"] = "I"

# TCLIB features
path = r'/Users/gianmarcoricci/Google Drive/UNI/Thesis CERN/Data/Auto_data/2018_MD3/*_TCLIB*_Align_features'
all_rec = iglob(path, recursive=True)     
dataframes = (pd.read_csv(f) for f in all_rec)
TCLIB_features = pd.concat(dataframes, ignore_index=True)
TCLIB_features
# Add a column to the dataframe that represents the collimator type (TCP, TCSG, TCLA, TCT, TCDQ)
TCLIB_features["collimator_type"] = "TCLIB"
# Add a column to the dataframe that represents the beam type type (ION or PROTON)
TCLIB_features["beam_type"] = "PROTON"
# Add a column to the dataframe that represents the beam state (Injection (I) or Flat top (FT))
TCLIB_features["beam_state"] = "I"

# Merge all dataframe in one
frames = [TCP_features, TCSG_features, TCLA_features, TCT_features, TCLIB_features, TCLIA_features]
MD3_2018_dataframe = pd.concat(frames)
MD3_2018_dataframe.to_csv("2018_MD3_dataframe.csv")

# 5) "2018_MD4"
# Load of all TCP features
path = r'/Users/gianmarcoricci/Google Drive/UNI/Thesis CERN/Data/Auto_data/2018_MD4/*_TCP*_Align_features'
all_rec = iglob(path, recursive=True)     
dataframes = (pd.read_csv(f) for f in all_rec)
TCP_features = pd.concat(dataframes, ignore_index=True)
# Add a column to the dataframe that represents the collimator type (TCP, TCSG, TCLA, TCT, TCDQ)
TCP_features["collimator_type"] = "TCP"
# Add a column to the dataframe that represents the beam type type (ION or PROTON)
TCP_features["beam_type"] = "PROTON"
# Add a column to the dataframe that represents the beam state (Injection (I) or Flat top (FT))
TCP_features["beam_state"] = "I"

# Load of all TCSG features
path = r'/Users/gianmarcoricci/Google Drive/UNI/Thesis CERN/Data/Auto_data/2018_MD4/*_TCSG*_Align_features'
all_rec = iglob(path, recursive=True)     
dataframes = (pd.read_csv(f) for f in all_rec)
TCSG_features = pd.concat(dataframes, ignore_index=True)
TCSG_features
# Add a column to the dataframe that represents the collimator type (TCP, TCSG, TCLA, TCT, TCDQ)
TCSG_features["collimator_type"] = "TCSG"
# Add a column to the dataframe that represents the beam type type (ION or PROTON)
TCSG_features["beam_type"] = "PROTON"
# Add a column to the dataframe that represents the beam state (Injection (I) or Flat top (FT))
TCSG_features["beam_state"] = "I"

# Load of all TCT features
path = r'/Users/gianmarcoricci/Google Drive/UNI/Thesis CERN/Data/Auto_data/2018_MD4/*_TCT*_Align_features'
all_rec = iglob(path, recursive=True)     
dataframes = (pd.read_csv(f) for f in all_rec)
TCT_features = pd.concat(dataframes, ignore_index=True)
TCT_features
# Add a column to the dataframe that represents the collimator type (TCP, TCSG, TCLA, TCT, TCDQ)
TCT_features["collimator_type"] = "TCT"
# Add a column to the dataframe that represents the beam type type (ION or PROTON)
TCT_features["beam_type"] = "PROTON"
# Add a column to the dataframe that represents the beam state (Injection (I) or Flat top (FT))
TCT_features["beam_state"] = "I"

# Merge all dataframe in one
frames = [TCP_features, TCSG_features, TCT_features]
MD4_2018_dataframe = pd.concat(frames)
MD4_2018_dataframe.to_csv("2018_MD4_dataframe.csv")

# 6) "3-inj_2018"
# Load of all TCP features
path = r'/Users/gianmarcoricci/Google Drive/UNI/Thesis CERN/Data/Auto_data/3-inj_2018/*_TCP*_Align_features'
all_rec = iglob(path, recursive=True)     
dataframes = (pd.read_csv(f) for f in all_rec)
TCP_features = pd.concat(dataframes, ignore_index=True)
# Add a column to the dataframe that represents the collimator type (TCP, TCSG, TCLA, TCT, TCDQ)
TCP_features["collimator_type"] = "TCP"
# Add a column to the dataframe that represents the beam type type (ION or PROTON)
TCP_features["beam_type"] = "PROTON"
# Add a column to the dataframe that represents the beam state (Injection (I) or Flat top (FT))
TCP_features["beam_state"] = "I"

# Load of all TCSG features
path = r'/Users/gianmarcoricci/Google Drive/UNI/Thesis CERN/Data/Auto_data/3-inj_2018/*_TCSG*_Align_features'
all_rec = iglob(path, recursive=True)     
dataframes = (pd.read_csv(f) for f in all_rec)
TCSG_features = pd.concat(dataframes, ignore_index=True)
TCSG_features
# Add a column to the dataframe that represents the collimator type (TCP, TCSG, TCLA, TCT, TCDQ)
TCSG_features["collimator_type"] = "TCSG"
# Add a column to the dataframe that represents the beam type type (ION or PROTON)
TCSG_features["beam_type"] = "PROTON"
# Add a column to the dataframe that represents the beam state (Injection (I) or Flat top (FT))
TCSG_features["beam_state"] = "I"

# Load of all TCLA features
path = r'/Users/gianmarcoricci/Google Drive/UNI/Thesis CERN/Data/Auto_data/3-inj_2018/*_TCLA*_Align_features'
all_rec = iglob(path, recursive=True)     
dataframes = (pd.read_csv(f) for f in all_rec)
TCLA_features = pd.concat(dataframes, ignore_index=True)
TCLA_features
# Add a column to the dataframe that represents the collimator type (TCP, TCSG, TCLA, TCT, TCDQ)
TCLA_features["collimator_type"] = "TCLA"
# Add a column to the dataframe that represents the beam type type (ION or PROTON)
TCLA_features["beam_type"] = "PROTON"
# Add a column to the dataframe that represents the beam state (Injection (I) or Flat top (FT))
TCLA_features["beam_state"] = "I"

# Load of all TCT features
path = r'/Users/gianmarcoricci/Google Drive/UNI/Thesis CERN/Data/Auto_data/3-inj_2018/*_TCT*_Align_features'
all_rec = iglob(path, recursive=True)     
dataframes = (pd.read_csv(f) for f in all_rec)
TCT_features = pd.concat(dataframes, ignore_index=True)
TCT_features
# Add a column to the dataframe that represents the collimator type (TCP, TCSG, TCLA, TCT, TCDQ)
TCT_features["collimator_type"] = "TCT"
# Add a column to the dataframe that represents the beam type type (ION or PROTON)
TCT_features["beam_type"] = "PROTON"
# Add a column to the dataframe that represents the beam state (Injection (I) or Flat top (FT))
TCT_features["beam_state"] = "I"
TCT_features

# TCLIA features
path = r'/Users/gianmarcoricci/Google Drive/UNI/Thesis CERN/Data/Auto_data/3-inj_2018/*_TCLIA*_Align_features'
all_rec = iglob(path, recursive=True)     
dataframes = (pd.read_csv(f) for f in all_rec)
TCLIA_features = pd.concat(dataframes, ignore_index=True)
# Add a column to the dataframe that represents the collimator type (TCP, TCSG, TCLA, TCT, TCDQ)
TCLIA_features["collimator_type"] = "TCLIA"
# Add a column to the dataframe that represents the beam type type (ION or PROTON)
TCLIA_features["beam_type"] = "PROTON"
# Add a column to the dataframe that represents the beam state (Injection (I) or Flat top (FT))
TCLIA_features["beam_state"] = "I"

# TCLIB features
path = r'/Users/gianmarcoricci/Google Drive/UNI/Thesis CERN/Data/Auto_data/3-inj_2018/*_TCLIB*_Align_features'
all_rec = iglob(path, recursive=True)     
dataframes = (pd.read_csv(f) for f in all_rec)
TCLIB_features = pd.concat(dataframes, ignore_index=True)
# Add a column to the dataframe that represents the collimator type (TCP, TCSG, TCLA, TCT, TCDQ)
TCLIB_features["collimator_type"] = "TCLIB"
# Add a column to the dataframe that represents the beam type type (ION or PROTON)
TCLIB_features["beam_type"] = "PROTON"
# Add a column to the dataframe that represents the beam state (Injection (I) or Flat top (FT))
TCLIB_features["beam_state"] = "I"

# Merge all dataframe in one
frames = [TCP_features, TCSG_features, TCLA_features, TCT_features, TCLIB_features, TCLIA_features]
III_inj_2018_dataframe = pd.concat(frames)
III_inj_2018_dataframe.to_csv("III_inj_2018_dataframe.csv")

# 7) "4-flat_2018"
# Load of all TCP features
path = r'/Users/gianmarcoricci/Google Drive/UNI/Thesis CERN/Data/Auto_data/4-flat_2018/*_TCP*_Align_features'
all_rec = iglob(path, recursive=True)     
dataframes = (pd.read_csv(f) for f in all_rec)
TCP_features = pd.concat(dataframes, ignore_index=True)
# Add a column to the dataframe that represents the collimator type (TCP, TCSG, TCLA, TCT, TCDQ)
TCP_features["collimator_type"] = "TCP"
# Add a column to the dataframe that represents the beam type type (ION or PROTON)
TCP_features["beam_type"] = "PROTON"
# Add a column to the dataframe that represents the beam state (Injection (I) or Flat top (FT))
TCP_features["beam_state"] = "FT"

# Load of all TCSG features
path = r'/Users/gianmarcoricci/Google Drive/UNI/Thesis CERN/Data/Auto_data/4-flat_2018/*_TCSG*_Align_features'
all_rec = iglob(path, recursive=True)     
dataframes = (pd.read_csv(f) for f in all_rec)
TCSG_features = pd.concat(dataframes, ignore_index=True)
TCSG_features
# Add a column to the dataframe that represents the collimator type (TCP, TCSG, TCLA, TCT, TCDQ)
TCSG_features["collimator_type"] = "TCSG"
# Add a column to the dataframe that represents the beam type type (ION or PROTON)
TCSG_features["beam_type"] = "PROTON"
# Add a column to the dataframe that represents the beam state (Injection (I) or Flat top (FT))
TCSG_features["beam_state"] = "FT"

# Load of all TCLA features
path = r'/Users/gianmarcoricci/Google Drive/UNI/Thesis CERN/Data/Auto_data/4-flat_2018/*_TCLA*_Align_features'
all_rec = iglob(path, recursive=True)     
dataframes = (pd.read_csv(f) for f in all_rec)
TCLA_features = pd.concat(dataframes, ignore_index=True)
TCLA_features
# Add a column to the dataframe that represents the collimator type (TCP, TCSG, TCLA, TCT, TCDQ)
TCLA_features["collimator_type"] = "TCLA"
# Add a column to the dataframe that represents the beam type type (ION or PROTON)
TCLA_features["beam_type"] = "PROTON"
# Add a column to the dataframe that represents the beam state (Injection (I) or Flat top (FT))
TCLA_features["beam_state"] = "FT"

# Load of all TCT features
path = r'/Users/gianmarcoricci/Google Drive/UNI/Thesis CERN/Data/Auto_data/4-flat_2018/*_TCT*_Align_features'
all_rec = iglob(path, recursive=True)     
dataframes = (pd.read_csv(f) for f in all_rec)
TCT_features = pd.concat(dataframes, ignore_index=True)
TCT_features
# Add a column to the dataframe that represents the collimator type (TCP, TCSG, TCLA, TCT, TCDQ)
TCT_features["collimator_type"] = "TCT"
# Add a column to the dataframe that represents the beam type type (ION or PROTON)
TCT_features["beam_type"] = "PROTON"
# Add a column to the dataframe that represents the beam state (Injection (I) or Flat top (FT))
TCT_features["beam_state"] = "FT"

# Merge all dataframe in one
frames = [TCP_features, TCSG_features, TCLA_features, TCT_features]
IV_flat_2018_dataframe = pd.concat(frames)
IV_flat_2018_dataframe.to_csv("IV_flat_2018_dataframe.csv")

# 8) 2018_IONS_Collisions
# Load of all TCP features
path = r'/Users/gianmarcoricci/Google Drive/UNI/Thesis CERN/Data/Auto_data/2018_IONS_Collisions/*_TCP*_Align_features'
all_rec = iglob(path, recursive=True)     
dataframes = (pd.read_csv(f) for f in all_rec)
TCP_features = pd.concat(dataframes, ignore_index=True)
# Add a column to the dataframe that represents the collimator type (TCP, TCSG, TCLA, TCT, TCDQ)
TCP_features["collimator_type"] = "TCP"
# Add a column to the dataframe that represents the beam type type (ION or PROTON)
TCP_features["beam_type"] = "ION"
# Add a column to the dataframe that represents the beam state (Injection (I) or Flat top (FT))
TCP_features["beam_state"] = " "

# Load of all TCSG features
path = r'/Users/gianmarcoricci/Google Drive/UNI/Thesis CERN/Data/Auto_data/2018_IONS_Collisions/*_TCSG*_Align_features'
all_rec = iglob(path, recursive=True)     
dataframes = (pd.read_csv(f) for f in all_rec)
TCSG_features = pd.concat(dataframes, ignore_index=True)
# Add a column to the dataframe that represents the collimator type (TCP, TCSG, TCLA, TCT, TCDQ)
TCSG_features["collimator_type"] = "TCSG"
# Add a column to the dataframe that represents the beam type type (ION or PROTON)
TCSG_features["beam_type"] = "ION"
# Add a column to the dataframe that represents the beam state (Injection (I) or Flat top (FT))
TCSG_features["beam_state"] = " "

# Load of all TCLA features
path = r'/Users/gianmarcoricci/Google Drive/UNI/Thesis CERN/Data/Auto_data/2018_IONS_Collisions/*_TCLA*_Align_features'
all_rec = iglob(path, recursive=True)     
dataframes = (pd.read_csv(f) for f in all_rec)
TCLA_features = pd.concat(dataframes, ignore_index=True)
# Add a column to the dataframe that represents the collimator type (TCP, TCSG, TCLA, TCT, TCDQ)
TCLA_features["collimator_type"] = "TCLA"
# Add a column to the dataframe that represents the beam type type (ION or PROTON)
TCLA_features["beam_type"] = "ION"
# Add a column to the dataframe that represents the beam state (Injection (I) or Flat top (FT))
TCLA_features["beam_state"] = " "

# Merge all dataframe in one
frames = [TCP_features, TCSG_features, TCLA_features]
ION_dataframe = pd.concat(frames)
ION_dataframe.to_csv("ION_dataframe.csv")

# Total dataset
frames = [I_test_2018_dataframe, II_test_2018_dataframe, MD3_2018_dataframe, MD4_2018_dataframe, III_inj_2018_dataframe, IV_flat_2018_dataframe]
total_dataframe = pd.concat(frames)
total_dataframe.to_csv("Auto_2018_dataset_NO_TCL.csv")
'''