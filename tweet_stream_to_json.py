# The streaming api is quite different from the REST api because the REST api is used to pull data from twitter but the streaming api pushes messages to a persistent session. This allows the streaming api to download more data in real time than could be done using the REST API.
#
# In Tweepy, an instance of tweepy.Stream establishes a streaming session and routes messages to StreamListener instance. The on_data method of a stream listener receives all messages and calls functions according to the message type. The default StreamListener can classify most common twitter messages and routes them to appropriately named methods, but these methods are only stubs.
#
# Therefore using the streaming api has three steps.
#
# 1. Create a class inheriting from StreamListener
# 2. Using that class create a Stream object
# 3. Connect to the Twitter API using the Strea

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

import time
import os
import io
import credentials as cred

# Authentication variables
consumer_key = cred.CONSUMER_KEY
consumer_secret = cred.CONSUMER_SECRET
access_token_key = cred.ACCESS_TOKEN_KEY
access_token_secret = cred.ACCESS_TOKEN_SECRET

start_time = time.time()
keyword_list = ['trump']

# override tweepy.StreamListener
class listener(StreamListener):

	def __init__(self, start_time, time_limit=60):

		self.time = start_time
		self.limit = time_limit
		self.tweet_data = []

	def on_data(self, data):

		saveFile = io.open('raw_tweets.json', 'a', encoding='utf-8')

		while (time.time() - self.time) < self.limit:

			try:

				self.tweet_data.append(data)

				return True


			except BaseException, e:
				print 'failed ondata,', str(e)
				time.sleep(5)
				pass

		saveFile = io.open('raw_tweets.json', 'w', encoding='utf-8')
		saveFile.write(u'[\n')
		saveFile.write(','.join(self.tweet_data))
		saveFile.write(u'\n]')
		saveFile.close()
		exit()

	def on_error(self, status):

		print statuses

# authenticate API access
auth = OAuthHandler(consumer_key, consumer_secret) #OAuth object
auth.set_access_token(access_token_key, access_token_secret)

# initialize Stream object with a time out limit
twitterStream = Stream(auth, listener(start_time, time_limit=20))
# call the filter method to run the Stream Object
twitterStream.filter(track=keyword_list, languages=['en'])
