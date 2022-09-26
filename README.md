# Tweets_Clustering

## Description:
We made a machine learning module to cluster every tweet to the nearest topic of it by using the k-means algorithm after cleaning text data through the "DataCleaning" function which had been implemented by us, then we implemented the "is_converged" function to compare the previous centroid and new centroid by using the "jaccard_distance" function, also we used the "new_centroids" function to choose the best tweet to make it our centroid depending on the length after using the "assign_cluster" function. we used the "compute_SSE" function to compute the sum squared error by using the elbow method and this helped us to know the smallest error value, also we used "matplotlib" to plot the results at the end of this project.
![Screenshot 2022-04-20 001056](https://user-images.githubusercontent.com/90388102/192195056-0d859873-38e0-4c90-9482-12c21b9fbef8.png)
