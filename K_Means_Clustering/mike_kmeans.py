# k means clustering in python

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset with pandas
dataset = pd.read_csv('Mall_Customers.csv')
X = dataset.iloc[:, [3, 4]].values

from sklearn.cluster import KMeans
# find smallest Within-Cluster-Sum-of-Squares value for k-clusters
wcss = []
for k in range(1,11):
    kmeans = KMeans(n_clusters=k,
                    init='k-means++',    # initialization of centroids to avoid random trap
                    max_iter=300,   # limit because this can become near-infinite
                    n_init=10,
                    random_state=0, # seed for randomzation for centroids
                    )
    kmeans.fit(X)   # fit the algorithm to your data
    # inertia is our WCSS value
    wcss.append(kmeans.inertia_)

# plot k's vs wcss's
plt.plot(range(1,11), wcss)
plt.title('the elbow method')
plt.xlabel('N Clusters (K)')
plt.ylabel('Within Cluster Sum of Squares (WCSS)')
plt.show()

#### here we found out that "5" is our magic number

# applying our good k-value
kmeans = KMeans(n_clusters=5,
                init='k-means++',    # initialization of centroids to avoid random trap
                max_iter=300,   # limit because this can become near-infinite
                n_init=10,
                random_state=0, # seed for randomzation for centroids
                )
y_kmeans = kmeans.fit_predict(X)

print(f'Our clusters results are as-follows:\n{y_kmeans}')


# visualize the clusters with a scatter-plot and centroids!
plt.scatter(X[y_kmeans==0, 0], X[y_kmeans==0, 1],   # Xcoordinate for all points belonging to cluster zero
            s = 100, c = 'red', label = 'cluster 0')
plt.scatter(X[y_kmeans==1, 0], X[y_kmeans==1, 1],   # Xcoordinate for all points belonging to cluster zero
            s = 100, c = 'green', label = 'cluster 1')
plt.scatter(X[y_kmeans==2, 0], X[y_kmeans==2, 1],   # Xcoordinate for all points belonging to cluster zero
            s = 100, c = 'blue', label = 'cluster 1')
plt.scatter(X[y_kmeans==3, 0], X[y_kmeans==3, 1],   # Xcoordinate for all points belonging to cluster zero
            s = 100, c = 'purple', label = 'cluster 1')
plt.scatter(X[y_kmeans==4, 0], X[y_kmeans==4, 1],   # Xcoordinate for all points belonging to cluster zero
            s = 100, c = 'cyan', label = 'cluster 1')
# plot the centroids
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 300, c = 'yellow', label='centroids')
plt.title('cluster of clients')
plt.xlabel('salaries')
plt.ylabel('spending score')
plt.show()