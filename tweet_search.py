import tweepy
from tweepy import OAuthHandler
import jsonpickle
import credentials as cred

auth = OAuthHandler(cred.CONSUMER_KEY, cred.CONSUMER_SECRET) #OAuth object
auth.set_access_token(cred.ACCESS_TOKEN_KEY, cred.ACCESS_TOKEN_SECRET)
auth.secure = True
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

max_id = -1L
maxTweets = 1000000
tweetCount = 0
tweetsPerQry = 1000
searchQuery = params = '@kdtrey5%20since:2017-04-24%20tweet_mode=extended'
fName = 'kd_tweets2.json'
sinceId = None

print "Downloading max {0} tweets".format(maxTweets)
with open(fName, 'w') as f:
    while tweetCount < maxTweets:
        try:
            if (max_id <= 0):
                if (not sinceId):
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry)
                else:
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry,
                                            since_id=sinceId)
            else:
                if (not sinceId):
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry,
                                            max_id=str(max_id - 1))
                else:
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry,
                                            max_id=str(max_id - 1),
                                            since_id=sinceId)
            if not new_tweets:
                print("No more tweets found")
                break
            for tweet in new_tweets:
                f.write(jsonpickle.encode(tweet._json, unpicklable=False) +
                        '\n')
            tweetCount += len(new_tweets)
            print("Downloaded {0} tweets".format(tweetCount))
            max_id = new_tweets[-1].id
        except tweepy.TweepError as e:
            # Just exit if any error
            print("some error : " + str(e))
            break

print ("Downloaded {0} tweets, Saved to {1}".format(tweetCount, fName))
