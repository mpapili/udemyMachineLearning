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



#### SEE HOMEWORK.AUTOMATIC.PY FOR OUR RECURSIVE WAY TO DO THE FOLLOWING
#### THIS IS ONLY TO SHOW THE THOUGHT-PROCESS DRAWN-OUT


# Building the optimal model using Backwards Elimination
import statsmodels.formula.api as sm
X = np.append(arr = np.ones((50, 1)).astype(int), values=X, axis = 1)
X_opt = X[ :, [0, 1, 2, 3, 4, 5] ]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
my_Summary = regressor_OLS.summary()
print(my_Summary)
print('index 2 was worst - trying without index 2')
X_opt = X[ :, [0, 1, 3, 4, 5] ]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
my_Summary = regressor_OLS.summary()
print(my_Summary)
print('index 1 was the worst trying without index 1 now..')
print('rememeber index zero is our constant row...')
X_opt = X[:, [0, 3, 4, 5] ]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
mySummary = regressor_OLS.summary()
print(mySummary)
print('okay now we see that index x2 (4 at this point) is the varaible to remove')
X_opt = X[:, [0, 3, 5] ]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
mySummary = regressor_OLS.summary()
print(mySummary)
print('barelyyyy index 5 doesnt make it')
print('the rnd spend should be the only variable that we can use')
X_opt = X[:, [0, 3, ] ]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
mySummary = regressor_OLS.summary()
print(mySummary)
print('look how fast and easy it was to figure this out with copy/paste. Obviously doing this with code recursively would be way faster')

