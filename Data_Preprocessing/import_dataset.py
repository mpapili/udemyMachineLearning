#! /usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# importing the dataset
dataset = pd.read_csv('Data.csv')

# separating FEATURES from DEPENDENT VARIABLE
X = dataset.iloc[:, :-1].values   # everything but last column
y = dataset.iloc[:, 3]

# fill in the missing data with mean-values
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis=0)
imputer = imputer.fit(X[:, 1:3])	# use all rows and columns 1 and 2 (1:3 because upper-limit is excluded)
X[:, 1:3] = imputer.transform(X[:, 1:3])

# encode categorical data (strings)
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
X[:, 0] = labelencoder_X.fit_transform(X[:, 0])	# all rows, column 0
onehotencoder = OneHotEncoder(categorical_features = [0])
X = onehotencoder.fit_transform(X).toarray()
labelencoder_Y = LabelEncoder()
y = labelencoder_Y.fit_transform(y)

# splitting the dataset into train and test
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y,
						    test_size = 0.2,
						    random_state = 0)


# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
# notice we remove "fit"
X_test = sc_X.transform(X_test)
print(X_train)
