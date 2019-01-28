# Decision Tree Regression

# Regression Template

# Importing the dataset
dataset = read.csv('Position_Salaries.csv')
dataset = dataset[2:3]

print('no need to split the set, too small')

print('no feature scaling needed for decision trees as distance is not used')

# Fitting the Regression Model to the dataset
#install.packages('rpart')
library(rpart)
print('we need to force a minimum amount of splits')
regressor = rpart(formula = Salary ~ .,
                  data=dataset,
                  control = rpart.control(minsplit = 1))

# Predicting a new result
y_pred = predict(regressor, data.frame(Level = 6.5))
print('y_pred for 6.5 level test is')
print(y_pred)


# Visualising the Regression Model results (for higher resolution and smoother curve)
# install.packages('ggplot2')
library(ggplot2)
x_grid = seq(min(dataset$Level), max(dataset$Level), 0.01)
ggplot() +
  geom_point(aes(x = dataset$Level, y = dataset$Salary),
             colour = 'red') +
  geom_line(aes(x = x_grid, y = predict(regressor, newdata = data.frame(Level = x_grid))),
            colour = 'blue') +
  ggtitle('Truth or Bluff (Decision Tree Model)') +
  xlab('Level') +
  ylab('Salary')