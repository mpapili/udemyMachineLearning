# problem to solve:
# get our model down to where the highest p-value for an independent variable-
# is above the significance level of p=0.05
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('50_Startups.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 4].values	# profit column

# Encode the Categorical Variable! (States)
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
X[:, 3] = labelencoder_X.fit_transform(X[:, 3])
onehotencoder = OneHotEncoder(categorical_features = [3])
X = onehotencoder.fit_transform(X).toarray()

# Avoiding the Dummy Variable Trap!
X = X[:, 1:]	# remove first column! That's factored into constant b0
		# always remove one column of dummy-variables

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)


# Fit the Multiple Linear Regression to the Training Set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)	# fit regressor to our training set


# Predicting the Test Set's Results
y_pred = regressor.predict(X_test)	# prediction vector

# Building the optimal model using Backwards Elimination
import statsmodels.formula.api as sm

SL = 0.05

def backwards_elim(X_opt, y):

	regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
	maxVar = max(regressor_OLS.pvalues).astype(float)

	if SL < maxVar:
		for element in range(0,len(X_opt[0])):
			if maxVar == regressor_OLS.pvalues[element]:
				X_opt = np.delete(X_opt, element, 1)
				X_opt = backwards_elim(X_opt, y)
	return(X_opt)

# add a column of ones as constant in the first position
X = np.append(arr = np.ones((50, 1)).astype(int), values=X, axis = 1)


X_opt = X[ :, [0, 1, 2, 3, 4, 5] ]
X_opt = backwards_elim(X_opt, y)
print(f'our final X_opt is {X_opt}')
