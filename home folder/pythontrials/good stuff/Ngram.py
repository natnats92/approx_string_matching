#!/usr/bin/python
#title			:Ngram.py
#description		:The program uses N-Gram Distance Matching Strategy to find approximate matches for location names in tweet texts. 
#author			:Natasha A Thomas
#date			:20140905
#usage			:python Ngram.py
#notes			:
#python_version		:2.7.6
#=============================================================================

import re

queryFile = open ("PreprocessedGeonames.txt", "r")
opFile = open ("NgramData.txt", "w")
#numresults = 0
n = 4 #value of n to form ngrams
threshold = 75 #threshold for similarity percentage
for query in queryFile:
	#query = "los angeles"
	querylist = query.split()
	numNgramsPattern = len(zip(*[''.join(querylist)[i:] for i in range(n)])) #list of ngrams in the pattern query
	lineCount = 0
	ipFile = open ("PreprocessedTweets.txt", "r")
	for line in ipFile:
		#line = "los angeles movie theatre"
		words = line.split()
		strings = zip(*[words[i:] for i in range(len(querylist))]) #list of strings with the same number of tokens as the query
		for token in strings:
			string = ''.join(token)
			ngrams = zip(*[string[i:] for i in range(n)]) #list of ngrams in the string
			numNgrams = len(ngrams)
			count = 0
			for ngram in ngrams:
				ng = ''.join(ngram)
				if re.search(ng, ''.join(querylist)): #searching for the presence of ngram in the pattern
					count = count + 1
			if (numNgrams != 0 and (count * 100/numNgramsPattern) > threshold): 
				opFile.write("Query: ")
				opFile.write(query + '\n')
				opFile.write("Approx. match: ")
				opFile.write(' '.join(token) + '\n') 
				tweets = open("Tweets.txt", "r")
				tweetCount = 0
				for tweet in tweets:
					if (tweetCount == lineCount):
						opFile.write("Tweet ID: ")
						opFile.write(str(tweet.split('\t')[1]) + '\n')
						break
					tweetCount = tweetCount + 1
				opFile.write("Tweet: ")
				opFile.write(line + '\n\n')
				#numresults = numresults + 1
				tweets.close() 
		lineCount = lineCount + 1
		#if numresults == 20:
			#break
	ipFile.close()
	#break
   
			

