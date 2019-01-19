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
print('WE WONT USE THE ABOVE REGRESSOR -')

# self-teaching backwards elim in R
regressor_backwards_elim = lm(formula = Profit ~ ., data = na.omit(training_set))
step(regressor_backwards_elim, direction = 'backward', trace=FALSE)

# predicting the Test Results
y_pred = predict(regressor_backwards_elim, newdata = test_set)


### backwards elimination by-hand
regressor = lm(formula = Profit ~ R.D.Spend + Administration + Marketing.Spend + State,
                              data = dataset)
print('lets select 5% p=0.05 as our significance level to aim for')
print(summary(regressor))
print('state2 and state3 are so awful we can safely remove both at once')
regressor = lm(formula = Profit ~ R.D.Spend + Administration + Marketing.Spend,
               data = dataset)
print(summary(regressor))
print('administration is getting kicked out!')
regressor = lm(formula = Profit ~ R.D.Spend + Marketing.Spend,
               data = dataset)
print(summary(regressor))
print('our model is most-powerful with only RND spend as an independnet variable')


### automatic backwards elimination

backElim <- function(x, sl) {
  numVars = length(x)
  for (i in c(1:numVars)){   # for i = each index in vector 1-len(x)
    regressor = lm(formula = Profit ~ ., data=x) # make our regressor
    maxVar = max(coef(summary(regressor))[c(2:numVars), "Pr(>|t|)"])
    if (maxVar > sl){
      j = which(coef(summary(regressor))[c(2:numVars), "Pr(>|t|)"] == maxVar)
      x = x[, -j]   # strip out index j
    }
    numVars = numVars - 1
  }
  return(regressor)
}
SL = 0.05
dataset = dataset[, c(1,2,3,4,5)] # all rows, each column by-index
regressor = backElim(dataset, SL)
print(summary(regressor))
print(coef(summary(regressor)))