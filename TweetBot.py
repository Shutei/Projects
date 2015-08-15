#initial setup
import tweepy, time, sys, json
from random import randint
import ctypes

key = 'NbYA7Zph5zxDSs3GbqAjH3XHB'
secret = '2fyxYvKXkMOwSUNhi4bLxI6C8QxeWBQI4GK68w8VW6JxMlBr2i'
token = '3314638471-RLy4ro6v9eGDRlVDJLPyYz8oxwZG51Xu6axmx7l'
token_secret = 'UaPR3t9Ar8knC5Ijr7dZj8MUQZBp3FZlF3TaKVUFMzvv6'
auth = tweepy.OAuthHandler(key, secret)
auth.set_access_token(token, token_secret)
api = tweepy.API(auth)
#initial setup

#Actual Program:
#API.update_status(status = "Beep Boop")

rRetweeted = [] #list of already retweeted ids
x = 0    #make this 0 when you want to stop the code
c = 10    #how many iterations

for count in range(0, c):
	results = api.search(q="retweet win", count=1)
	for result in results:
		t = 10 + 3 * randint(2, 15)
		for x in range(0, t):
			time.sleep(1)
			print x,
		try:
			api.retweet(result._json['retweeted_status']['id'])
			data = api.get_status(result.id)._json
			user_id = data['entities']['user_mentions'][(0)]['id']
			api.create_friendship(user_id)
			print user_id
			print result
			print 'success! sleeping'
			for x in range(0, 5):
				time.sleep(1)
				print x,
			print '\n'			
		except tweepy.TweepError as e:
			if (e.message[0]['code'] == 226):
				#ctypes.windll.user32.MessageBoxA(0, "Too many requests, pausing", "Bot Error", "1")
				time.sleep(120)
			else:
				print e.message[0]['code']
				print e.message
		except KeyError as k:
			print k



#Retweet Give Away search

	results = api.search(q="retweet give away", count=1)
	for result in results:
		t = 10 + 3 * randint(2, 15)
		for x in range(0, t):
			time.sleep(1)
			print x,
		try:
			api.retweet(result._json['retweeted_status']['id'])
			data = api.get_status(result.id)._json
			user_id = data['entities']['user_mentions'][(0)]['id']
			api.create_friendship(user_id)
			print user_id
			print result
			print 'success! sleeping'
			for x in range(0, 5):
				time.sleep(1)
				print x,
			print '\n'			
		except tweepy.TweepError as e:
			if (e.message[0]['code'] == 226):
				#ctypes.windll.user32.MessageBoxA(0, "Too many requests, pausing", "Bot Error", "1")
				time.sleep(120)
			else:
				print e.message[0]['code']
				print e.message
		except KeyError as k:
			print k

