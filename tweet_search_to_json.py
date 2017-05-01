import tweepy
from tweepy import OAuthHandler

import time
import os
import io
import json
import simplejson
import credentials as cred

import pprint

# Authentication variables
consumer_key = cred.CONSUMER_KEY
consumer_secret = cred.CONSUMER_SECRET
access_token_key = cred.ACCESS_TOKEN_KEY
access_token_secret = cred.ACCESS_TOKEN_SECRET

# start_time = time.time()
# keyword_list = ['trump']
file_name = 'draymond_tweets.json'

def save_to_json(tweets):

	# twitter_data = ','.join(tweets)
	print type(tweets)
	with io.open(file_name, 'w', encoding='utf-8') as saveFile:
		json.dump(tweets, saveFile)

	def on_error(self, status):
		print statuses

def basic_pretty_print(tweets):
	output = simplejson.loads(tweets)
	return simplejson.dumps(output, indent=4, sort_keys=True)


# authenticate API access and initialize API object
auth = OAuthHandler(consumer_key, consumer_secret) #OAuth object
auth.set_access_token(access_token_key, access_token_secret)
# api = tweepy.API(auth)
json_api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

# pass either items_count to Cursor.items() or page_count to Cursor.pages()
items_count = 10
page_count = None
params = '@money23green+since:2017-04-24'

##########################################
# Using the tweepy Cursor
##########################################
# construct tweepy Cursor, specify + call API object with query params
# twitterSearch = tweepy.Cursor(api.search, q=params).items(items_count)
# note that methods exhausts cursor --can't call more than 1 method on result set
# type_twitterSearch = type(twitterSearch)
# for tweet in twitterSearch:
# 	print tweet
# print type_twitterSearch
# save_to_json(twitterSearch)

##########################################
# Using the tweepy JSONParser
##########################################
twitterSearch = json_api.search(q=params)
statuses = twitterSearch['statuses']
for status in statuses:
	print status['created_at']
	print status['user']['screen_name']
	print status['text']
# for k, v in statuses[3]:
# 	print k, v
# pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(statuses[5])

print type(status)
print type(statuses)
print len(statuses)
save_to_json(statuses)

# key dictionary fields
# status_object['id']
# status_object['id_str']
# status_object['created_at']
# status_object['lang']
# if user['name'] == ___ for user in status_object['entities']['user_mentions']
# if user['screen_name'] == ___ for user in status_object['entities']['user_mentions']
