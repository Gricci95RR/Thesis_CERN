import seaborn as sns
from glob import iglob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.metrics import accuracy_score
from sklearn import metrics

# Load of all features
path = r'/Users/gianmarcoricci/Google Drive/UNI/Thesis CERN/Data/Auto_data/2018_IONS_Collisions/*_Align_features'

all_rec = iglob(path, recursive=True)     
dataframes = (pd.read_csv(f) for f in all_rec)
all_features = pd.concat(dataframes, ignore_index=True)

# Split Dataset
x = all_features.drop(["spike","jaw","decay_c"],axis = 1)
y = all_features.spike
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=100)

# DT
DTclf = tree.DecisionTreeClassifier(criterion='entropy', splitter='best', max_depth = 5, min_samples_leaf=1)
model = DTclf.fit(x_train,y_train)
plt.figure(figsize=(20, 14))
tree.plot_tree(DTclf) 
predictions = DTclf.predict(x_test)
print("Precision:",metrics.precision_score(y_test, predictions))
print("Accuracy:",metrics.accuracy_score(y_test, predictions))

# Confusion Matrix
cm = metrics.confusion_matrix(y_test, predictions)
# Plot CM
plt.figure(figsize=(10,10))
sns.heatmap(cm, annot=True, fmt=".3f", linewidths=.5, square = True, cmap = 'Blues_r');
plt.ylabel('Actual label');
plt.xlabel('Predicted label');
all_sample_title = 'Precision: '+ str(metrics.precision_score(y_test, predictions))
plt.title(all_sample_title, size = 15);