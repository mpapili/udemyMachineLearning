# Hiearchal Clustering in R

# import dataset
dataset = read.csv('Mall_Customers.csv')
X = dataset[4:5]

# Use Dendrogram to find perfect number of clusters
dendrogram = hclust(dist(X, method='euclidean'),
                   method = 'ward.D')
plot(dendrogram,
     main = paste('Dendrogram'),
     xlab = 'Customers',
     ylab = 'Euclidean Distances')

### here we determine n_clusters = 5 is ideal

# fit it to our model
hc = hclust(dist(X, method='euclidean'),
                    method = 'ward.D')
# cut the full tree down to five
y_hc = cutree(hc, k=5)
# Visualising the clusters
library(cluster)
clusplot(dataset,
         y_hc,
         lines = 0,
         shade = TRUE,
         color = TRUE,
         labels = 2,
         plotchar = FALSE,
         span = TRUE,
         main = paste('Clusters of customers'),
         xlab = 'Annual Income',
         ylab = 'Spending Score')