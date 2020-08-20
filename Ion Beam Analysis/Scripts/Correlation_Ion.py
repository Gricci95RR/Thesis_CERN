import seaborn as sns
from glob import iglob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load of all features
path = r'/Users/gianmarcoricci/Google Drive/UNI/Thesis CERN/Data/Auto_data/2018_IONS_Collisions/*_Align_features'

all_rec = iglob(path, recursive=True)     
dataframes = (pd.read_csv(f) for f in all_rec)
all_features = pd.concat(dataframes, ignore_index=True)

# Load of all losses
path = r'/Users/gianmarcoricci/Google Drive/UNI/Thesis CERN/Data/Auto_data/2018_IONS_Collisions/*_Align'

all_rec = iglob(path, recursive=True)     
dataframes = (pd.read_csv(f) for f in all_rec)
all_losses = pd.concat(dataframes, ignore_index=True)

# Plot Correlation Heatmap
plt.figure(figsize=(15, 8))
correlation = all_features.corr(method="spearman")
heatmap = sns.heatmap(correlation,vmin=-1, vmax=1, annot=True);
heatmap.set_title('Correlation Heatmap', fontdict={'fontsize':12}, pad=12);
