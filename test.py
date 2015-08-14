#initial setup
import tweepy, time, sys, json

key = 'hk28iR2vdOmpLLdOKzKGR69g3'
secret = 'NZTOXtZIzH5v2idzJyaE6bpptJtme30zf2ypBaCOldfC8Wluza'
token = '3314638471-fTScfbeQiXWwwP5HEUip7fyN9d40pHvN5rjAzuG'
token_secret = 'pfM0lWbvQGX5MUjruyUj3pUgb2TbmHfs8UIQZAhTJYoPe'
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
		time.sleep(2)
		try:
			api.retweet(result._json['entities']['media'][(0)]['source_status_id'])
			print 'success! sleeping'
			for x in range(0, 30):
				time.sleep(1)
				print x
			user_id.follow()
			print result
			data = api.get_status(result.id)._json
			user_id = data['entities']['user_mentions'][(0)]['id']
		except:
			print "error"


