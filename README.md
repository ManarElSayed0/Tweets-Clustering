# Tweets_Clustring
Twitter provides a service for posting short messages. In practice, many of the tweets are very similar to each other and can be clustered together. By clustering similar tweets together, we can generate a more concise and organized representation of the raw tweets, which will be very useful for many Twitter-based applications (e.g., truth discovery, trend analysis, search ranking, etc.)
Here, the tweets are clustered using Jaccard distance metric and K-means clustering algorithm.
Jaccard Distance
The Jaccard distance, which measures dissimilarity between two sample sets (A and B). It is defined as the difference of the sizes of the union and the intersection of two sets divided by the size of the union of the sets.
Dist(A, B) = 1 - |A intersection B|/|A union B|
For example, consider the following tweets:
Tweet A: the long march
Tweet B: ides of march
|A intersection B | = 1 and |A union B | = 5, therefore the distance is 1 – (1/5)
Jaccard Distance Dist(A, B) between tweet A and B has the following properties:
1.	It is small if tweet A and B are similar.
2.	It is large if they are not similar.
3.	It is 0 if they are the same.
4.	It is 1 if they are completely different (i.e., no overlapping words).
# Dataset :
https://archive.ics.uci.edu/ml/datasets/Health+News+in+Twitter
