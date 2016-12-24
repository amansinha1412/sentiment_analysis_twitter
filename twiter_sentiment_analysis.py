from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sentiment_mod as s

#consumer key, consumer secret, access token, access secret.

atoken = '710542566576365568-DOKd8oGpTneMpXGkBnzDthBWDyoQMXJ'
asecret='FVqac78eKyVce7wVVBOojUcNU31XBm47zZTLC17es7a6N'
ckey = 'ZVEIzeIf2boHMU51kpdlsfSak'
csecret = 'OLHDCkcNpRogzLcf9BO0LarIYmv1UrLcF5JRUMQq3YB8E89cOg'


class listener(StreamListener):

    def on_data(self, data):

		all_data = json.loads(data)

		tweet = all_data["text"]
		sentiment_value, confidence = s.sentiment(tweet)
		print(tweet, sentiment_value, confidence)

		if confidence*100 >= 80:
			output = open("out_put/twitter-out.txt","a")
			output.write(sentiment_value)
			output.write('\n')
			output.close()

		return True

    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["batman"])
