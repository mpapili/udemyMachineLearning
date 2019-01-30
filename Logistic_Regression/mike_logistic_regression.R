# Logistic Regression

# Importing the dataset
dataset = read.csv('Social_Network_Ads.csv')
dataset = dataset[, 3:5]

# Splitting the dataset into the Training set and Test set
# # install.packages('caTools')
library(caTools)
set.seed(123)
split = sample.split(dataset$Purchased, SplitRatio = 0.75)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

# Feature Scaling
training_set[, 1:2] = scale(training_set[, 1:2])
test_set[, 1:2] = scale(test_set[, 1:2])

# Fitting the Regression Model to the dataset
classifier = glm(formula = Purchased ~ .,
                 family = binomial,   # type of regression for logistic
                 data = training_set,
                 )

# Predicting a new result
print('usually we can do this in one-step, but we will do it in two')
prob_pred = predict(classifier,
                    type = 'response',   # probabilities in single vector
                    newdata = test_set[-3])   # test-set minus column 3 (dependent variable)
print(prob_pred)  # vector of probabilities

y_pred = ifelse(prob_pred > 0.5, 1, 0)    # if y-value is over 0.5, it's 1, else 0

# Making the Confusion Matrix
cm = table(test_set[, 3], y_pred)
print(cm)
# Visualising the Regression Model results
# install.packages('ggplot2')
library(ggplot2)
ggplot() +
  geom_point(aes(x = dataset$Level, y = dataset$Salary),
             colour = 'red') +
  geom_line(aes(x = dataset$Level, y = predict(regressor, newdata = dataset)),
            colour = 'blue') +
  ggtitle('Truth or Bluff (Regression Model)') +
  xlab('Level') +
  ylab('Salary')

# Visualising the Regression Model results (for higher resolution and smoother curve)
# install.packages('ElemStatLearn')
library(ElemStatLearn)
set = training_set   # so it's easier to switch to test later
X1 = seq(min(set[, 1]) - 1, max(set[, 1]) + 1, by = 0.01)
X2 = seq(min(set[, 2]) - 1, max(set[, 2]) + 1, by = 0.01)
grid_set= expand.grid(X1, X2)
colnames(grid_set) = c('Age', 'EstimatedSalary')
prob_set = predict(classifier, type='response', newdata = grid_set)
y_grid = ifelse(prob_set > 0.5, 1, 0)
plot(set[, -3],
     main = 'Logistic Regression (Training Set)',
     xlab = 'Age', ylab = 'Estimated Salary',
     xlim = range(X1), ylim = range(X2))
contour(X1, X2, matrix(as.numeric(y_grid), length(X1), length(X2)), add= TRUE)
points(grid_set, pch = '.', col = ifelse(y_grid == 1, 'springgreen3', 'tomato'))
points(set, pch = 21, bg = ifelse(set[, 3] == 1, 'green4', 'red3'))

# Test Data
library(ElemStatLearn)
set = test_set   # so it's easier to switch to test later
X1 = seq(min(set[, 1]) - 1, max(set[, 1]) + 1, by = 0.01)   # build grid (size min-to-max)
X2 = seq(min(set[, 2]) - 1, max(set[, 2]) + 1, by = 0.01)   # build other axis (size mid-to-max)
grid_set= expand.grid(X1, X2)    # builds the grid from lines above
colnames(grid_set) = c('Age', 'EstimatedSalary')    # since it's a matrix we give names to columns
prob_set = predict(classifier, type='response', newdata = grid_set)    # use classifier to predict results 
y_grid = ifelse(prob_set > 0.5, 1, 0)   # transoform probs into yes/no (1/0) results
plot(set[, -3],    # plot the FULL graph
     main = 'Logistic Regression (TEST Set)',
     xlab = 'Age', ylab = 'Estimated Salary',
     xlim = range(X1), ylim = range(X2))
contour(X1, X2, matrix(as.numeric(y_grid), length(X1), length(X2)), add= TRUE)
points(grid_set, pch = '.', col = ifelse(y_grid == 1, 'springgreen3', 'tomato'))
points(set, pch = 21, bg = ifelse(set[, 3] == 1, 'green4', 'red3'))