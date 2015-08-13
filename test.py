#initial setup
import tweepy, time, sys, json

key = 'VzwVkotHIbjr2Szpvvm7J6f8X'
secret = 'To6Ls1g4rDprQ3oocUhsPSsFYDXgcRsfM3FcXnPE9HOwApQL7B'
token = '3314467434-Xf69VmUj07HAKx24tzjk5JwsWiIplB2SIIfM1fG'
token_secret = 'K2EZVfpF0N2QSNoUnrf6jZh10x2wY0wqMlt0Y2jda6qmQ'
auth = tweepy.OAuthHandler(key, secret)
auth.set_access_token(token, token_secret)
api = tweepy.API(auth)
#initial setup

#Actual Program:
#API.update_status(status = "Beep Boop")
x = 0
while x == 1:
	results = api.search(q="retweet to win")
	for result in results:
		try:
			api.retweet(result.id)
			print result._json['text']
			print 'success! sleeping'
			for x in range(0, 30):
				time.sleep(1)
				print 'x'
			#user_id.follow()
			#print result
			data = api.get_status(result.id)._json
			user_id = data['entities']['user_mentions'][(0)]['id']
		except:
			print "error"
			time.sleep(.03)

