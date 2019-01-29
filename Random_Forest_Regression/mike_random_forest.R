# Random Forest Regression
# Regression Template

# Importing the dataset
dataset = read.csv('Position_Salaries.csv')
dataset = dataset[2:3]

print('cannot split data, sets too small')
print('feature scaling not needed for random forest')

# Fitting the Regression Model to the dataset
set.seed(1234)
library(randomForest)
regressor = randomForest(x = dataset[1],   # dataframe
                         y = dataset$Salary,   # vector
                         ntree = 130)   # num of trees

# Predicting a new result
y_pred = predict(regressor, data.frame(Level = 6.5))
sprintf('y_pred was: %s', y_pred)


# Visualising the Regression Model results (for higher resolution and smoother curve)
# install.packages('ggplot2')
library(ggplot2)
x_grid = seq(min(dataset$Level), max(dataset$Level), 0.01)
ggplot() +
  geom_point(aes(x = dataset$Level, y = dataset$Salary),
             colour = 'red') +
  geom_line(aes(x = x_grid, y = predict(regressor, newdata = data.frame(Level = x_grid))),
            colour = 'blue') +
  ggtitle('Truth or Bluff (Random Forest Model)') +
  xlab('Level') +
  ylab('Salary')