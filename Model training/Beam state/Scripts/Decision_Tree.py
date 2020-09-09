import seaborn as sns
from glob import iglob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.metrics import accuracy_score
from sklearn import metrics

all_features = pd.read_csv('/Users/gianmarcoricci/Documents/GitHub/Thesis_CERN/Dataset/dataset_2016_2018.csv')

# Split Dataset
x = all_features.drop(["spike","jaw", 'collimator_type',  'beam_type',  'beam_state'],axis = 1)
inj_dataframe = all_features.loc[all_features['beam_state'] == 'I']
y_inj = inj_dataframe.spike
inj_dataframe = inj_dataframe.drop(['beam_state',"spike","jaw", 'collimator_type',  'beam_type',  'beam_state'],axis=1)

ft_dataframe = all_features.loc[all_features['beam_state'] == 'FT']
y_ft = ft_dataframe.spike
ft_dataframe = ft_dataframe.drop(['beam_state',"spike","jaw", 'collimator_type',  'beam_type',  'beam_state'],axis=1)
x_train, x_test, y_train, y_test = train_test_split(inj_dataframe, y_inj, test_size=0.25, random_state=100, shuffle="true")

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