import tweepy

key = 'YH0Yk3ZJUiyCg72aDFjqjd8OC'
secret = '1f2T9Bqgu3fsQm9fIIwIy2KanznQtiFYEhQAWjWsbKXTKg4bwW'
token = '3314467434-Jj7A6dBueSzGbQebgLJtleR2HUmnY0HBOT4yzZ0'
token_secret = 'e0aqxPYMnmPjehImsaByApIv0e5QfjSkm10xuu1vObDxD'

auth = tweepy.OAuthHandler(key, secret)
auth.set_access_token(token, token_secret)
API = tweepy.API(auth)
API.update_status(status = "Beep Boop")

