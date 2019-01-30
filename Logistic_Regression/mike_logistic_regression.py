# Data Preprocessing Template

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Social_Network_Ads.csv')
X = dataset.iloc[:, [2, 3]].values
y = dataset.iloc[:, 4].values

print(f'{X}\n{y}')

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
print('no need to feature scale y of course')

# Fitting Logistic Regression to the Training Set
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state = 0)	# just setting random-state to match tutorial
print(f'debug {y_train.shape}')
classifier.fit(X_train, y_train)	# fit to our training set

# Predicting the test-set results
y_pred = classifier.predict(X_test)
print(f'{y_pred}\nvs\n{y_test}')

# Making the Confusion Matrix to see what our prediction got right
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test,	# ground truth
		      y_pred)	# predictions
print(cm)
