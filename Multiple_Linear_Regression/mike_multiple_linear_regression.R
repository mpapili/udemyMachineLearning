# Multiple Linear Regression

# Importing the dataset
dataset = read.csv('50_Startups.csv')

# encode the categorical data
dataset$State = factor(dataset$State,
                       levels = c('New York', 'California', 'Florida'),
                       labels = c(1, 2, 3))

# Splitting the dataset into the Training set and Test set
# install.packages('caTools')
library(caTools)
set.seed(123)
split = sample.split(dataset$Profit, SplitRatio = 0.8)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

# Fitting a Multiple Linear Regression to the Training Set
### regressor = lm(formula = Profit ~ R.D.Spend + Administration + Marketing.Spend + State)
regressor = lm(formula = Profit ~ .,
               data = training_set)    # "." tells R to use all independent variablesß
summary(regressor)

# self-teaching backwards elim in R
regressor_backwards_elim = lm(formula = Profit ~ ., data = na.omit(training_set))
step(regressor_backwards_elim, direction = 'backward', trace=FALSE)