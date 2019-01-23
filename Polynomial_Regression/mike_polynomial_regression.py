# Data Preprocessing Template

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values  # just levels, we need :2 (even though it's excluded) to make sure it's not a vector but a matrix
y = dataset.iloc[:, 2].values  # just salaries

print('no need to split train/test set, small dataset means we cant afford to use anything to test')

# making a simple linear regressor so we can see how bad it is 
from sklearn.linear_model import LinearRegression
linReg = LinearRegression()
linReg.fit(X, y)  # fit it, no train/test split in this example


# making the polynomial regression model
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 4)   # we're going to use X^1 and X^2 and X^3 and X^4
X_poly = poly_reg.fit_transform(X)   # change X into X^1, X^2.. etc
print(X_poly) # let's take a look
lin_reg_2 = LinearRegression()   # new regressor object
lin_reg_2.fit(X_poly, y)   # fit it to X_poly and y


# visualizing the (bad) simple linear regressor:
plt.scatter(X, y,
	    color = 'red') # scatterpolot of X vs y
plt.plot(X, linReg.predict(X),
	 color = 'blue')  # line plot of our predicted y values
plt.title('Salary vs Levels (Bad Simple Linear Regressor)')
plt.xlabel = 'position level'
plt.ylabel = 'salary'
plt.show()


# visualizing the (good) polynomial regressor
X_grid = np.arange(min(X), max(X), 0.01)  # steps of 0.1 instead of 1
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, y,
	    color = 'red')
plt.plot(X_grid, lin_reg_2.predict(poly_reg.fit_transform(X_grid)),
	 color = 'green')
plt.title('Salary vs Levels (Polynomial Regressor)')
plt.xlabel = 'position level'
plt.ylabel = 'salary'
plt.show()


# Predicting a new result with Linear Regression (bad)
y_pred = linReg.predict( np.array( [ [ 6.5 ] ] ) )  # create 1d array
print(f'linear regressor suggests someone at level 6.5 would make {y_pred}')   # what should someone at level 6.5 make?

# Predicting a new result with Polynomial Regression (good)
y_pred = lin_reg_2.predict(poly_reg.fit_transform( np.array( [ [ 6.5 ] ] )))
print(f'polynomial regressor suggests someone at level 6.5 would make {y_pred}')
