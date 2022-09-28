import random
import re
import math
import string
import matplotlib.pyplot as plt
import time

Black = "\033[30m"       # Black
Red = "\033[31m"         # Red
Green = "\033[32m"       # Green
Yellow = "\033[33m"      # Yellow
Blue = "\033[34m"        # Blue
Purple = "\033[35m"      # Purple
Cyan = "\033[36m"        # Cyan
White = "\033[0m"        # White
BB = "\033[40m"          # Black Background

def DataCleaning(url, encodingg):
    if encodingg == "utf8":
        f = open(url, "r", encoding = "utf8")
    else:
        f = open(url, "r")
        
    tweets = list(f)
    TweetsList = []

    for i in range(len(tweets)):
        tweets[i] =  tweets[i].rstrip()
        tweets[i] = tweets[i][50:]
        tweets[i] = " ".join(filter(lambda x: x[0] != '@', tweets[i].split()))
        tweets[i] = re.sub(r"http\S+", "", tweets[i])
        tweets[i] = re.sub(r"www\S+", "", tweets[i])
        tweets[i] = tweets[i].strip()
        tweet_len = len(tweets[i])
        
        if tweet_len > 0:
            if tweets[i][len(tweets[i]) - 1] == ':':
                tweets[i] = tweets[i][:len(tweets[i]) - 1]

        tweets[i] = tweets[i].replace('#', '')
        tweets[i] = tweets[i].lower()
        tweets[i] = tweets[i].translate(str.maketrans('', '', string.punctuation))
        tweets[i] = " ".join(tweets[i].split())

        TweetsList.append(tweets[i].split(' '))
    f.close()

    return TweetsList



def k_means(tweets, k=3, max_iterations=20):

    centroids = []

    # Select random K points for centroids
    count = 0
    ll = [None] * len(tweets)
    
    for h in range(k):
        if count >= k:
            break
        random_tweet_idx = random.randint(0, len(tweets) - 1)
        
        if ll[random_tweet_idx] == None:
            count += 1
            ll[random_tweet_idx] == 1
            centroids.append(tweets[random_tweet_idx])
        else:
            h -= 1

    iter_count = 1
    prev_centroids = []

    # Run the iterations until not converged or until the max iteration in not reached
    while (is_converged(prev_centroids, centroids)) == False and (iter_count <= max_iterations):

        print("Running iteration " + str(iter_count) + ".......")
        
        # Assign each data point to their closest centroid
        clusters = assign_cluster(tweets, centroids)

        # Check if k-means converges, keep track of prev_centroids
        prev_centroids = centroids

        # Reassign each datapoint to the new closest centroid of each cluster
        centroids = new_centroids(clusters)
        iter_count = iter_count + 1

    if (iter_count >= max_iterations):
        print("\nMaximum number of iterations reached, K Means not converged.\n")
    else:
        print("\nK Means converged.\n")

    sse = compute_SSE(clusters,centroids)

    return clusters, sse 



def is_converged(prev_centroid, new_centroids):

    n = 0
    
    for c in range(len(new_centroids) and len(prev_centroid)):
          if jaccard_distance(prev_centroid[c], new_centroids[c]) == 0:
            n = n + 1
    
    if n == len(new_centroids):
        return True
    else:
        return False



def assign_cluster(tweets, centroids):

    clusters = dict()
    
    # For every tweet iterate each centroid and assign closest centroid to a it
    for t in range(len(tweets)):
        min_dis = math.inf
        cluster_idx = -1;
        
        for c in range(len(centroids)):
            dis = jaccard_distance(centroids[c], tweets[t])
            # Look for a closest centroid for a tweet

            if centroids[c] == tweets[t]:
                cluster_idx = c
                min_dis = 0
                break
            elif dis < min_dis:
                cluster_idx = c
                min_dis = dis
           
        # Randomise the centroid assignment to a tweet if nothing is common
        if min_dis == 1:
           cluster_idx = random.randrange(0,len(centroids))
          
        # Assign the closest centroid to a tweet
        if cluster_idx in clusters:
            clusters[cluster_idx].append(tweets[t])
        else:
            clusters[cluster_idx]=[]
            clusters[cluster_idx].append(tweets[t])
            
    return clusters



def jaccard_distance(tweet1, tweet2):
    
    intersection = set(tweet1).intersection(tweet2)
    distance = 1 - ((len(intersection))/((len(tweet1) + len(tweet2))-len(intersection)))
    
    return distance
    


def new_centroids(clusters):
    
    centroids = []
    
    for cluster in range(len(clusters)):
        min_distance = math.inf
        centroid_index = -1
        
        for tweet1 in range(len(clusters[cluster])):
            tweet_dis = 0
            
            for tweet2 in range(len(clusters[cluster])):
                tweet_dis += jaccard_distance(clusters[cluster][tweet1], clusters[cluster][tweet2])
                    
            if min_distance > tweet_dis:
                min_distance = tweet_dis
                centroid_index = tweet1
                
        centroids.append(clusters[cluster][centroid_index])
    return centroids
        


def compute_SSE(clusters,centroids):

    sse = 0
    
    for c in range(len(clusters)):
        
        for t in range(len(clusters[c])):
            n = jaccard_distance(centroids[c], clusters[c][t])
            sse += n*n
    return sse


total = 0

if __name__ == '__main__':
    
    ss = "\t\t\t  Tweets Clustering"
    m = [Green, Yellow, Blue, Purple, Cyan, White]
    
    for i in range(len(ss)):
        time.sleep(0.25)
        q = random.randint(0, 5)
        print(m[q] + ss[i] + m[q] , end = "")
    
    flag = 'yes'
    while(flag == 'yes'):
        # Default file
        file = 'bbchealth.txt'
        
        answer = input(White + "\nDo you want to use the default file 'bbchealth.txt' (Yes / No) : " + White)
        while True:
            if answer == '-1':
                raise SystemExit(0)
                
            answer = answer.lower()
            
            if answer == 'no':
                print("1) bbchealth.txt\n2) cnnhealth.txt\n3) everydayhealth.txt\n4) foxnewshealth.txt\n5) gdnhealthcare.txt\n6) goodhealth.txt\n7) KaiserHealthNews.txt\n8) latimeshealth.txt\n9) msnhealthnews.txt\n10) NBChealth.txt\n11) nprhealth.txt\n12) nytimeshealth.txt\n13) reuters_health.txt\n14) usnewshealth.txt\n15) wsjhealth.txt\n16) cbchealth.txt") 
                filee = {'1' : "bbchealth.txt", '2' : "cnnhealth.txt", '3' : "everydayhealth.txt", '4' : "foxnewshealth.txt", '5' : "gdnhealthcare.txt", '6' : "goodhealth.txt", '7' : "KaiserHealthNews.txt", '8' : "latimeshealth.txt", '9' : "msnhealthnews.txt", '10' : "NBChealth.txt", '11' : "nprhealth.txt", '12' : "nytimeshealth.txt", '13' : "reuters_health.txt", '14' : "usnewshealth.txt", '15' : "wsjhealth.txt", '16' : "cbchealth.txt"}
                file = input("Enter the number of the desired file: ")
    
                while True:
                    if file == '-1':
                        raise SystemExit(0)
                        
                    found = False
                    
                    for i in filee.keys():
                        if file == i:
                            if file == '4' or file == '7' or file == '9' or file == '10' or file == '15':
                                encodingg = ""
                            else:
                                encodingg = "utf8"
                            found = True
                            file = filee[i]
                            print("\nYou haave choosen " + filee[i])
                            break
                        
                    if found:
                        break
                    if not found:
                        file = input("Wrong entry, try again with press on one of the above numbers to choose the file or press (-1) to exit from the program: ")
                        
                if found:
                    break
                
            elif answer == "yes":
                encodingg = "utf8"
                break
            
            else:
                answer = input("Wrong entry, try again with typing only (Yes) or (No), or press (-1) to exit from the program: ")
                
        
        
        
        tweets = DataCleaning(file, encodingg)
        
        # Default number of experiments
        experiments = 5
        # Default value of K
        k = 3
        
        # Select the number K to decide the number of clusters
        answer = input("Do you want to use the default values K = 3, experiments = 5 (Yes / No) : " )
        answer = answer.lower()
        if answer == "no":
            k = int(input("Enter the value of K: "))
            experiments = int(input("Enter the number of experiments: "))
        
        
        # For SSE plot
        sse_Y = []
        k_X = []
        
        # For every experiment 'e', run K-means
        for e in range(experiments):
            print("\n--------------------------------------------------\nRunning K Means for experiment number " + str((e + 1)) + ", K = " + str(k) + '\n--------------------------------------------------\n')
            start = time.time()
            
    
            clusters, sse = k_means(tweets, k)
            
    
            # Print size of each cluster
            for c in range(len(clusters)):
                print("Cluster " + str(c+1) + ":", str(len(clusters[c])) + " tweets")
    
                
            # Print SSE value
            print("\nSum of squared error (SSE): " + str(sse) + '\n')
            #do some stuff
            stop = time.time()
            duration = stop - start
            total += duration
            
            x = "Time taken running this iteration: {:.2f}"
            print(BB + x.format((duration)), "seconds" + White)
            
    
            sse_Y.append(sse)
            k_X.append(k)
                        
            # Plot SSE 
            plt.style.use("bmh")
            ax = plt.axes()
            ax.set_facecolor("floralwhite")
            plt.plot(k_X, sse_Y, color = 'black')
            plt.title("Tweets Clustering")
            plt.xlabel("Number of clusters")
            plt.ylabel("Sum of squared error")
            plt.show()
            
            # Increment k after every experiment
            k = k + 1
        
        print('\n__________________________________________')
        x = "\nTotal time taken running in all iterations: {:.2f}"
        print(BB + x.format((total)), "seconds" + White)
        flag = input("Do you want to continue (Yes / No) : ")
        flag = flag.lower()
        total = 0