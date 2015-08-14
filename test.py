#initial setup
import tweepy, time, sys, json
from random import randint


key = 'zIZBfKC4UVvHiDzYBZGwqBmRD'
secret = 'oGIw5qsv5HINfWJzms42XLBG6TC0XcEvvQcEdBlyuaJIZfH8Kj'
token = '3314638471-TFSEhmAuIvzdAVaFQ06jrbRaCU9McnyA1ULXJxO'
token_secret = 'FcrqeSxBppGBqlWp8gnlgR5zMSbboP0djVgRn3WEomQad'
auth = tweepy.OAuthHandler(key, secret)
auth.set_access_token(token, token_secret)
api = tweepy.API(auth)
#initial setup

#Actual Program:
#API.update_status(status = "Beep Boop")
rRetweeted = [] #list of already retweeted ids
x = 1
while x == 1:
	results = api.search(q="retweet to win")
	for result in results:
		time.sleep((20 + randint(5, 15)))
		try:
			api.retweet(result._json['entities']['media'][(0)]['source_status_id'])
			rRetweeted.append(result._json['entities']['media'][(0)]['source_status_id'])
			print result
			print 'success! sleeping'
			for x in range(0, 50):
				time.sleep(1)
				print x
			data = api.get_status(result.id)._json
			user_id = data['entities']['user_mentions'][(0)]['id']
			#user_id.follow()
		except tweepy.TweepError as e:
			print e.message[0]['code']
			rRetweeted.append(result._json['entities']['media'][(0)]['source_status_id'])
			print rRetweeted
		except KeyError as k:
			print result
			break


