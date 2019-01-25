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
dataset$Level3 = dataset$Level ** 3   # add on a column that's level^3
dataset$Level4 = dataset$Level ** 4   # add on a column that's level^4
dataset$Level5 = dataset$Level ** 5   # test 5th power??

poly_reg = lm(formula = Salary ~ .,
             data = dataset)   
print(summary(poly_reg))

# install.packages(‘ggplot2’)   # no need to install as we already have it

# visualize the linear data
library(ggplot2)
ggplot() + 
  geom_point(aes(x = dataset$Level, y = dataset$Salary),   # graph our real points
             colour = 'red') + 
  geom_line(aes(x = dataset$Level, y = predict(lin_reg, newdata = dataset)),
                colour = 'blue') + 
  ggtitle('Levels vs Salary (Bad Linear Model)') +
  xlab('level') + 
  ylab('salary')


# visualize the polynomial data
ggplot() + 
  geom_point(aes(x = dataset$Level, y = dataset$Salary),   # graph our real points
             colour = 'red') + 
  geom_line(aes(x = dataset$Level, y = predict(poly_reg, newdata = dataset)),
            colour = 'blue') + 
  ggtitle('Levels vs Salary (Good Polynomial Model)') +
  xlab('level') + 
  ylab('salary')


# Predicting a result with the linear regressor
# create dataframe containing 6.5 value
y_pred = predict(lin_reg, data.frame(Level = 6.5))
print(y_pred)

# Predicting a result with the polynomial regressor
y_pred = predict(poly_reg, data.frame(Level = 6.5,
                                      Level2 = 6.5^2,
                                      Level3 = 6.5^3,
                                      Level4 = 6.5^4,
                                      Level5 = 6.5^5))
print(y_pred)
print("this is much better")