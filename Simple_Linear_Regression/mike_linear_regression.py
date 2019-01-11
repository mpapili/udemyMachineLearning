# Data Preprocessing Template

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values


# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)


# Feature Scaling
### feature scaling is handled in simple-linear regression, but not in all. Keep it in mind, but we won't feature scale


# fitting simple linear regression to the training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, # independent variables
	      y_train, # dependent variable
	      )


# predicting the Test set results
y_pred = regressor.predict(X_test)
print(y_pred)
print(y_test)


# visualizing the Training Set Results
plt.scatter(X_train, y_train, # X-vs-Y for scatter
	    color = 'red')
# plot a line for X_train vs predicted results from X_train
plt.plot(X_train, regressor.predict(X_train), # X_train vs expected y from x_train 
	 color = 'blue')
# give it a title
plt.title('Salary vs Experience (training set)')
# label to X axis
plt.xlabel('Years of Experience')
# label to Y axis
plt.ylabel('Salary')
plt.show()


# visualizing the Test Set Results
plt.scatter(X_test, y_test, # X-vs-Y for scatter
	    color = 'red')
# plot a line for X_train vs predicted results from X_train
plt.plot(X_train, regressor.predict(X_train), # X_train vs expected y from x_train (keep it the same!)
	 color = 'blue')
# give it a title
plt.title('Salary vs Experience (training set)')
# label to X axis
plt.xlabel('Years of Experience')
# label to Y axis
plt.ylabel('Salary')
plt.show()
