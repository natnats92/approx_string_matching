#!/usr/bin/python
#title			:GlobalDistance2.py
#description		:The program uses Global Edit Distance Matching Strategy to find approximate matches for location names in tweet texts. This 				 version considers multi-word queries as single strings.
#author			:Natasha A Thomas
#date			:20140905
#usage			:python GlobalDistance2.py
#notes			:
#python_version		:2.7.6
#=============================================================================

def editDistance(str1, str2, weight=1):
    len1 = len(str1)
    len2 = len(str2)
    matrix = [[0] * (len2 + 1) for j in range(len1 + 1)]
    for i in xrange(len1 + 1):
        for j in xrange(len2 + 1):
            if min(i, j) == 0:
                matrix[i][j] = max(i, j) 
            else:
                addValue = 0 if str1[i-1] == str2[j-1] else weight
                matrix[i][j] = min(matrix[i-1][j-1] + addValue, 
                                matrix[i-1][j] + 1,    
                                matrix[i][j-1] + 1)    
    return matrix[len1][len2]


queryFile = open ("PreprocessedGeonames.txt", "r")
opFile = open ("Data2.txt", "w")
#numresults = 0
threshold = 40 #threshold for dissimilarity percentage
for query in queryFile:
	#query = "los angeles"
	count = 0
	querylist = query.split()
	ipFile = open ("PreprocessedTweets.txt", "r")
	for line in ipFile:
		names = line.split()
		tokens = zip(*[names[i:] for i in range(len(querylist))]) #list of strings with the same number of tokens as the query
		for i in range(0,len(tokens)):
			dist = editDistance (query, ' '.join(tokens[i]))
			if ((dist * 100)/len(query) < threshold):
				opFile.write("Query: ")
				opFile.write(query + '\n')
				opFile.write("Approx. match: ")
				opFile.write(' '.join(tokens[i]) + '\n') 
				tweets = open("Tweets.txt", "r")
				tweetCount = 0
				for tweet in tweets:
					if (tweetCount == count):
						opFile.write("Tweet ID: ")
						opFile.write(str(tweet.split('\t')[1]) + '\n')
						break
					tweetCount = tweetCount + 1
				opFile.write("Tweet: ")
				opFile.write(line + '\n\n')
				#numresults = numresults + 1
				tweets.close() 
		count = count + 1   
		#if numresults == 20:
		#	break
	ipFile.close()
	#break
			  
    

