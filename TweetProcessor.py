#!/usr/bin/python
#title			:TweetProcessor.py
#description		:The program extracts the tweet texts, converts them to lowercase and removes all non-alphabetic characters except spaces.
#author			:Natasha A Thomas
#date			:20140905
#usage			:python TweetProcessor.py <input-file>
#notes			:
#python_version		:2.7.6
#=============================================================================

import re
import sys

inputFile = open (str((sys.argv)[1]), 'r')
outputFile = open ('PreprocessedTweets.txt', 'w')
for line in inputFile:
		pattern = re.compile('[^a-zA-Z ]*') #regular expression to identify all non-alphabetic characters except spaces
		line = re.sub (pattern, '', line) #patterns which match the RE are replaced by a ' '
		line = line.lower()
		outputFile.write(line + '\n')

inputFile.close()
outputFile.close()
