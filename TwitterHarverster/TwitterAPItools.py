from CouchDBtools import *
import tweepy
from time import sleep
from tweepy.streaming import StreamListener
from tweepy import Stream
from APIconfig import *
from pprint import pprint
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from geotext import GeoText

analyzer = SentimentIntensityAnalyzer()

# Variables that contains the user credentials to access Twitter API
consumer_key = machine3['consumer_key']
consumer_secret = machine3['consumer_secret']
access_token_key = machine3['access_token']
access_token_secret = machine3['access_secret']

auth = tweepy.OAuthHandler( consumer_key, consumer_secret )
auth.set_access_token( access_token_key, access_token_secret )
api = tweepy.API( auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True )

# connect to Twitter API
# Create authentication objects
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# set access token & access secret
auth.set_access_token(access_token_key, access_token_secret)
# Pass in the auth parameter to create the API object
api = tweepy.API(auth)
print('Twitter API created')

def testTweepyStatus(ts):
    for a in ts:
        print('-'*15+'test'+'-'*15)
        print(a.geo)
        print(a.coordinates)
        pprint(a.place)
        print(a.retweets)
        print(a.created_at)
        print(a.text)
        print(a.id)
        print(a.id_str)
        print(a.parse)
        pprint(a.entities)


def processTweet(tweet):
    # get raw text part
    # print(tweet.user.screen_name,"Tweeted:",tweet.text)

    pTweet = dict(
        _id = tweet.id,
        geo = tweet.geo,
        coordinates = tweet.coordinates,
        place = tweet.palce,


    )

def showMytweets():
    public_tweets = api.home_timeline()
    for tweet in public_tweets:
       print(tweet.text)


def Tsearch(query = 'a',language = "en",geo = geoNode['sydney']):
    # The keyword you are looking for   query = "sports"
    # The language code (ISO 639-1)     language = "en"
    #results = api.search(q=query, lang=language,geocode=geo)
    results = api.search(geocode=geo)

    # new_tweets = api.search(
    #     q=query,
    #     geocode=geo,
    #     count=searchLimits)

    testTweepyStatus(results)
    return results

def Tgeo(geo = ''):
    results = api.reverse_geocode(granularity='city',)
    testTweepyStatus(results)

def processData(data):
    # extract useful info and compute sentiment parameter
    raw = json.loads(data)
    #pprint(raw)
    tmp = dict(
        _id = raw['id_str'],
        id = raw['id'],
        geo = raw['geo'],
        coordinates = raw['coordinates'],
        place = raw['place'],
        text = raw['text'],
        retweeted = raw['retweeted'],
        hashtags = raw['entities']['hashtags']
    )

    # vader sentiment analysis
    # compound is the score [-1,1]
    vs = analyzer.polarity_scores(raw['text'])['compound']
    tmp['compound'] = vs
    if vs <= -0.05 : tmp['sentiment'] = 'negative'
    elif vs >= 0.05 : tmp['sentiment'] = 'positive'
    else : tmp['sentiment'] = 'neutral'

    # extract cities from raw text
    places = GeoText(raw['text'])
    tmp['mentioned'] = dict(
        cities = places.cities,
        counties = places.country_mentions
    )
    #pprint(tmp)

    pushDic(tmp)

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

def beginStream():
    twitterStream = Stream(auth, listener())
    #track=["sports"]

    print('begin listening')
    #track=["a", "the", "i", "you", "u"]
    twitterStream.filter(locations= geoBlock['aus'],languages = ['en'])




def getOne():
    tweets = Tsearch()
    return tweets[0]













