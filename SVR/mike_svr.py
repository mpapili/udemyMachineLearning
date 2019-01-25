# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values

# Splitting the dataset into the Training set and Test set
"""from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)"""

# Feature Scaling
print('we need to feature-scale our levels vs our salary before going on')
print('SVR does not handle feature-scaling for us, and levels-vs-salary are wildly different')
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
sc_y = StandardScaler()
X = sc_X.fit_transform(X)
y = sc_y.fit_transform(np.array([y]).reshape(-1,1))

# Fitting the SVR Model to the dataset
from sklearn.svm import SVR
print('the kernel is the most important argument we will be passing')
regressor = SVR(kernel='rbf')   # rbf is default
				# linear makes no sense for our model
				# gassian = rbf, polynomial would work too
regressor.fit(X, y)   # fit our regressor


# Predicting a new result
# we need to scale our input "6.5" and then UNSCALE our output 
	# we use sc_X for input scaling
	# we use sc_y for output inverse scaling
y_pred = sc_y.inverse_transform(regressor.predict(sc_X.transform(np.array([6.5]).reshape(-1,1))))
print(y_pred)

# Visualising the SVR results
plt.scatter(X, y, color = 'red')
plt.plot(X, regressor.predict(X), color = 'blue')
plt.title('Truth or Bluff (Regression Model)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()

# Visualising the SVR results (for higher resolution and smoother curve)
X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, y, color = 'red')
plt.plot(X_grid, regressor.predict(X_grid), color = 'blue')
plt.title('Truth or Bluff (Regression Model)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()
