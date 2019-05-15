'''
CCC2019 Team 56
Yishan Shi 883166
Huiya Chen 894933
Tong He 867488
Yao Wang 869992
Aaron Robins 694098
'''
from TwitterAPItools import *
import sys

class listener(StreamListener):

    def on_data(self, data):
        #print(type(data)) # str
        print('---got one---')
        #pprint(data)
        processData(data)


    def on_error(self, status):
        print('on_error')
        print(status)
        return True

    def on_timeout(self):
        print("~~~~~~~~Timeout, sleeping for 100 seconds...\n")
        sleep(100)
        return

def beginStream(dbname,query = carBrand):
    twitterStream = Stream(auth, listener())
    print('begin listening')
    #track=carBrandLower
    twitterStream.filter(locations= geoBlock['aus'],languages = ['en'])



if __name__ == '__main__' :
    if len(sys.argv) > 1:
        # Variables that contains the user credentials to access Twitter API
        k = int(sys.argv[1])
        consumer_key = machine[k]['consumer_key']
        consumer_secret = machine[k]['consumer_secret']
        access_token_key = machine[k]['access_token']
        access_token_secret = machine[k]['access_secret']

        # developer verification and get API interface
        # Create authentication objects
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        # set access token & access secret
        auth.set_access_token(access_token_key, access_token_secret)
        # Pass in the auth parameter to create the API object
        global api
        api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    print('___________Twitter Stream API begin______________')
    beginStream(dbname)
