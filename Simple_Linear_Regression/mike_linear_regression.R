# Importing the dataset
dataset = read.csv('Salary_Data.csv')

# Splitting the dataset into the Training set and Test set
# install.packages('caTools')
library(caTools)
set.seed(123)
split = sample.split(dataset$Salary, SplitRatio = 2/3)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

# Fit Simple Linear Regression to the Training Set
regressor = lm(formula = Salary ~ YearsExperience, # "~" = proportional
               data = training_set)

summary(regressor)   # print out some amazingly useful data
y_pred = predict(regressor, newdata = test_set)   # build vector of predictions

# plotting the data
library(ggplot2)    # import ggplot2
ggplot() +
  geom_point(aes(x = training_set$YearsExperience, # scatterplot our points
                 y = training_set$Salary),
             colour = 'red') +
  geom_line(aes(x = training_set$YearsExperience,   # plot our regression line
                y = predict(regressor, newdata = training_set)),
            colour = 'blue') +
  ggtitle('Salary vs Experience (training set)') +
  xlab('Years of Experience') +
  ylab('Salary')

# plot our trained regressor vs TEST data
ggplot() +
  geom_point(aes(x = test_set$YearsExperience, # scatterplot our points
                 y = test_set$Salary),
             colour = 'red') +
  geom_line(aes(x = training_set$YearsExperience,   # plot our regression line
                y = predict(regressor, newdata = training_set)),
            colour = 'blue') +
  ggtitle('Salary vs Experience (test set)') +
  xlab('Years of Experience') +
  ylab('Salary')


