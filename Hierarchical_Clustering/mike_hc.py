#Hierarchical Clustering in Python


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# import our "mall" dataset
dataset = pd.read_csv('Mall_Customers.csv')
X = dataset.iloc[:, [3,4]].values

# use a dendogram to find optimal number of clusters
import scipy.cluster.hierarchy as sch
dendrogram = sch.dendrogram(sch.linkage(X,   # sch.linkage() is the HC method itself
                                        method='ward',    # minimize clusters by dissimilarity
                                        ))

#pyplot
plt.title('dendrogram')
plt.xlabel('customers')
plt.ylabel('euclidean distances between cluster centroids')
plt.show()

print('visualization tells us that 5 clusters is ideal!')

# Fitting the HC to our mall dataset
from sklearn.cluster import AgglomerativeClustering   # HC
hc = AgglomerativeClustering(n_clusters=5,   # number of clusters from above
                             affinity='euclidean',   # define what determines dissimilartiy
                             linkage='ward',    # difference based on distance from centroids of cluster
                             )
y_hc = hc.fit_predict(X)    # fit the hc model to our dataset

# visualize our clusters! (scatter plot)
plt.scatter(X[y_hc==0, 0], X[y_hc==0, 1],   # Xcoordinate for all points belonging to cluster zero
            s = 100, c = 'red', label = 'cluster 0')
plt.scatter(X[y_hc==1, 0], X[y_hc==1, 1],   # Xcoordinate for all points belonging to cluster zero
            s = 100, c = 'green', label = 'cluster 1')
plt.scatter(X[y_hc==2, 0], X[y_hc==2, 1],   # Xcoordinate for all points belonging to cluster zero
            s = 100, c = 'blue', label = 'cluster 1')
plt.scatter(X[y_hc==3, 0], X[y_hc==3, 1],   # Xcoordinate for all points belonging to cluster zero
            s = 100, c = 'purple', label = 'cluster 1')
plt.scatter(X[y_hc==4, 0], X[y_hc==4, 1],   # Xcoordinate for all points belonging to cluster zero
            s = 100, c = 'cyan', label = 'cluster 1')

plt.title('cluster of clients')
plt.xlabel('salaries')
plt.ylabel('spending score')
plt.show()