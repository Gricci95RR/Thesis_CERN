import seaborn as sns
from glob import iglob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import svm
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


# SVM linear kernel
model2 = svm.SVC(kernel='linear')
model2.fit(x_train, y_train)
predictions2 = model2.predict(x_test)
accuracy2 = accuracy_score(y_test, predictions2)
print("Linear Kernel\nAccuracy (normalized): " + str(accuracy2))
print("Precision:",metrics.precision_score(y_test, predictions2))
print("\n")

'''
# SVM
model3 = svm.SVC(kernel="poly", degree = 1)
model3.fit(x_train, y_train)
predictions3 = model3.predict(x_test)
accuracy3 = accuracy_score(y_test, predictions3)
print("Polinomial Kernel\nAccuracy (normalized): " + str(accuracy3))
print("Precision:",metrics.precision_score(y_test, predictions3))
print("\n")
'''
'''
# SVM
model1 = svm.SVC(kernel="rbf")
model1.fit(x_train, y_train)
predictions1 = model1.predict(x_test)
accuracy1 = accuracy_score(y_test, predictions1)
print("RBF Kernel\nAccuracy (normalized): " + str(accuracy1))
print("Precision:",metrics.precision_score(y_test, predictions1))
print("\n")

'''
# Confusion Matrix
cm = metrics.confusion_matrix(y_test, predictions2)
# Plot CM
plt.figure(figsize=(10,10))
sns.heatmap(cm, annot=True, fmt=".3f", linewidths=.5, square = True, cmap = 'Blues_r');
plt.ylabel('Actual label');
plt.xlabel('Predicted label');
all_sample_title = 'Precision: '+ str(metrics.precision_score(y_test, predictions2))
plt.title(all_sample_title, size = 15);
