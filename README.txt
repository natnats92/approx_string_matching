Project			: Approximate String Search for Geolocation of Tweets

Author			: Natasha A. Thomas

Date			: 4/9/14

Files			: TweetProcessor.py
		  	  GeonamesPreprocessor.py
		  	  Ngram.py
		  	  GlobalDistance1.py
		  	  GlobalDistance2.py

Python Version		: 2.7.6

Usage			: 1) python TweetProcessor.py <input-file> 
			     (Input: training_set_tweets_0.001.txt Output: PreprocessedTweets.txt)
			  2) python GeonamesPreprocessor.py <input-file>
			     (Input: US_0.001.txt Output: PreprocessedGeonames.txt)
			  3) python Ngram.py
			     (Input: PreprocessedTweets.txt and PreprocessedGeonames.txt Output: NgramData.txt) 
			  4) python GlobalDistance1.py
			     (Input: PreprocessedTweets.txt and PreprocessedGeonames.txt Output: Data1.txt)
			  5) python GlobalDistance2.py
			     (Input: PreprocessedTweets.txt and PreprocessedGeonames.txt Output: Data2.txt)
