import tweepy
import json
from time import sleep
from TwitterAPI import TwitterAPI
from tweepy.streaming import StreamListener

# Variables that contains the user credentials to access Twitter API
consumer_key = 'xjOiODN7QXUWNW1TS7Yy7BFgj'
consumer_secret = 'VvvEYbUCBSNIBTynZZWVmqxjvYx04CasXV1I0PG8PkbGakiLJt'
access_token_key = '1119208072763756545-j8CZp18HWbujs5blyzm9ww3fzudbl3'
access_token_secret = 'Fx4xEfVE5WO8xhBU0cFeT8UsJvHV5vMTUVkkuhPa2CwIO'



# Create a class inheriting from StreamListener
class TwitterStream(StreamListener):

    def __init__(self, api=None, ):
        self.api = api

    def on_data(self, data):
        print
        "hello~~~~~~~~!!!"
        if 'in_reply_to_status' in data:
            self.on_status(data)
        elif 'delete' in data:
            delete = json.loads(data)['delete']['status']
            if self.on_delete(delete['id'], delete['user_id']) is False:
                return False
        elif 'limit' in data:
            if self.on_limit(json.loads(data)['limit']['track']) is False:
                return False
        elif 'warning' in data:
            warning = json.loads(data)['warnings']
            print
            warning['message']
            return False

    def on_status(self, status):
        print
        status
        # print remaining

    def on_error(self, status):
        if status == 420:
            print
            status
            self.on_timeout()

    ''' Rate Limit '''

    def on_timeout(self):
        print("~~~~~~~~Timeout, sleeping for 60 seconds...\n")
        sleep(60)
        return
























