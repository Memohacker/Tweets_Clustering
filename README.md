# Tweets_Clustering

## Summary:
We made a machine learning module to cluster every tweet to the nearest topic of it by using the k-means algorithm after cleaning text data through the 
"DataCleaning" function which had been implemented by us, then we implemented the "is_converged" function to compare the previous centroid and new centroid by using the "jaccard_distance" function, also we used the "new_centroids" function to choose the best tweet to make it our centroid depending on the length after using the "assign_cluster" function. we used the "compute_SSE" function to compute the sum squared error by using the elbow method and this helped us to know the smallest error value, also we used "matplotlib" to plot the results at the end of this project.

## Functions Description: 
• "DataCleaning" function: we pass to it two parameters, "URL": the type of file format and "encoding": the type of format you want, then we clean the file by removing all special characters and punctuation marks by using built-in functions.

• "is_converged" function: we pass to it two parameters, "prev_centroid" and "new_centroids" to compare every word of them and know if there is a difference or not and this comparison has been made by using the "jaccard_distance" function. 

• "jaccard_distance" function: we pass to it two parameters, "tweet1" and "tweet2" to compare every word of them by using some built-in functions like "intersection" and "set", then we use the value of intersection in the formula of distance to know the value of the difference. 

• "assign_cluster" function: we pass to it two parameters, "tweets" and "centroids". after using the "jaccard_distance" function we should put the tweet to the nearest cluster of it depending on the value that we have taken from the "jaccard_distance" function.



