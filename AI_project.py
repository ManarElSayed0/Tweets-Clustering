import random as rd
import re
import math
import os.path
file_name=input("enter file name: ")
def check():
    if(os.path.isfile(file_name)==True):
        return True
    else:
        return False

def preprocessing(k):

    Tweets = list(k)
    list_of_tweets = []

    for i in range(len(Tweets)):

        Tweets[i] = Tweets[i].strip('\n')

        Tweets[i] = Tweets[i][50:]

        Tweets[i] = " ".join(filter(lambda x: x[0] != '@', Tweets[i].split()))

        Tweets[i] = re.sub(r"http\S+", "", Tweets[i])
        Tweets[i] = re.sub(r"www\S+", "", Tweets[i])

        Tweets[i] = Tweets[i].strip()
        
        Tweets[i] = Tweets[i].replace('#', '')
        Tweets[i] = Tweets[i].lower()

        Tweets[i] =re.sub(r'[^\w\s]', '', Tweets[i])
        Tweets[i] = " ".join(Tweets[i].split())

        list_of_tweets.append(Tweets[i].split(' '))

    k.close()

    return list_of_tweets


def k_means(Tweets, k):
    max_iterations=50
    centroids = []
    counter = 0
    #hash maap
    map = dict()
    while counter < k:
        #random tweet index
        random_index = rd.randint(0, len(Tweets) - 1)
        if random_index not in map:
            counter += 1
            map[random_index] = True
            centroids.append(Tweets[random_index])
   
    number_of_iteration = 0
    prev_centroids = []
    x=True 
    while x==True:
        if isConverged(prev_centroids, centroids) == False and number_of_iteration < max_iterations:

            clusters = assignCluster(Tweets, centroids)
            prev_centroids = centroids
            centroids = updateCentroids(clusters)
            number_of_iteration = number_of_iteration + 1
        else :
            x=False
    sse = SSE(clusters)

    return clusters, sse

def isConverged(prev_centroid, new_centroids):

    if len(prev_centroid) != len(new_centroids):
        return False

    for c in range(len(new_centroids)):
        if " ".join(new_centroids[c]) != " ".join(prev_centroid[c]):
            return False
    return True

def assignCluster(Tweets, centroids):

    clusters = dict()

    for t in range(len(Tweets)):
        minDistance = math.inf
        clusterindex = -1;
        for c in range(len(centroids)):
            dis = JaccardDistance(centroids[c], Tweets[t])
    
            if centroids[c] == Tweets[t]:
                clusterindex = c
                minDistance = 0
                break

            if dis < minDistance:
                clusterindex = c
                minDistance = dis

        clusters.setdefault(clusterindex, []).append([Tweets[t]])
        last_tweet_idx = len(clusters.setdefault(clusterindex, [])) - 1
        clusters.setdefault(clusterindex, [])[last_tweet_idx].append(minDistance)
    return clusters
    




def updateCentroids(clusters):

    centroids = []


    for i in range(len(clusters)):
        Sum_of_minDistance = math.inf
        centroidindex = -1
        for j in range(len(clusters[i])):
            
            sum_of_distance = 0
            
            for t2 in range(len(clusters[i])):
                dis = JaccardDistance(clusters[i][j][0], clusters[i][t2][0])

                sum_of_distance += dis
               
            if sum_of_distance < Sum_of_minDistance:
                Sum_of_minDistance= sum_of_distance
                centroidindex = j
        
        centroids.append(clusters[i][centroidindex][0])
    return centroids



def JaccardDistance(Tweet_1, Tweet_2):

    T1=set(Tweet_1)
    T2=set(Tweet_2)
    I = T1.intersection(T2)
    O= T1.union(T2)
    dis=1 - (len(I) / len(O))
    return dis


def SSE(clusters):
    sse = 0   
    for c in range(len(clusters)):
        for t in range(len(clusters[c])):
            sse = sse + (math.pow(clusters[c][t][1],2))
    return sse


def main():
    if(check()):
        data_url=file_name
    else:
        print("unexcepted file name")
        return False
    try:
        f= open(data_url, encoding='utf8')
        Tweets = preprocessing(f)
    except:
        f = open(data_url, encoding='cp1252')
        Tweets = preprocessing(f)
    
    experiments = int(input("Enter Number Of experiments : "))
   
    k=int(input("Enter K_mean : "))

    for e in range(experiments):

        print("experiment no. " + str((e + 1)) + " for k = " + str(k))

        clusters, sse = k_means(Tweets, k)

        for c in range(len(clusters)):
            print(str(c+1) + ": ", str(len(clusters[c])) + " tweets")
cnnhealth            # # to print tweets in a cluster
            #for t in range(len(clusters[c])):
             #    print("t" + str(t) + ", " + (" ".join(clusters[c][t][0])))

        print("SSE : " + str(sse))
        print('\n')

        # increment k after every experiment
        k = k + 1


main()