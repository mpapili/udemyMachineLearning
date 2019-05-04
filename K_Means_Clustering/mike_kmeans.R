dataset <- read.csv('Mall_Customers.csv')

X <- dataset[4:5] # columns 4-5
# finding the optimal k-clusters value:

set.seed(0) # make sure everything uses the same random-seed for centroids
wcss <- vector()   # empty-vector
for (i in 1:10) wcss[i] <- sum(kmeans(X, i)$withinss)
plot(1:10, wcss, type='b',
     xlab='clusters',
     ylab='wcss')


