#initial setup
import tweepy, time, sys, json

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
x = 1
while x == 1:
	results = api.search(q="retweet to win")
	for result in results:
		time.sleep(20)
		try:
			api.retweet(result._json['entities']['media'][(0)]['source_status_id'])
			print result.text
			print 'success! sleeping'
			for x in range(0, 50):
				time.sleep(1)
				print x
			user_id.follow()
			print result
			data = api.get_status(result.id)._json
			user_id = data['entities']['user_mentions'][(0)]['id']
		except:
			print "error"


