# Polynomial Regression
# Importing the dataset
dataset = read.csv('Position_Salaries.csv')
dataset = dataset[2:3]  # ditch the "position" field

print('no need for training/test split')

print('no need for feature-scaling')


# fitting the LINEAR regressor (bad)
lin_reg = lm(formula = Salary ~ .,
             data = dataset)   
print(summary(lin_reg))

# fitting the polynomial regressor (good)
dataset$Level2 = dataset$Level ** 2   # add on a column that's level^2
poly_reg = lm(formula = Salary ~ .,
             data = dataset)   
print(summary(poly_reg))
