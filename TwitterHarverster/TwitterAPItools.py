from CouchDBtools import *
import tweepy
from time import sleep
from tweepy.streaming import StreamListener
from tweepy import Stream
from APIconfig import *
from pprint import pprint
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from geotext import GeoText
import string

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
'''
normal API return an object #processTweet
but stream API return a string  #processData
so there is a bit different in there
'''
def processTweet(tweet):
    # get raw text part
    # print(tweet.user.screen_name,"Tweeted:",tweet.text)

    pTweet = dict(
        _id = tweet.id,
        geo = tweet.geo,
        coordinates = tweet.coordinates,
        place = tweet.palce,
    )

def stripTweetByCar(tweet):
    pass

def showMytweets():
    public_tweets = api.home_timeline()
    for tweet in public_tweets:
       print(tweet.text)


def Tsearch(query = carBrand,lang = "en",geo = geoNode['sydney'],dbname = 'car'):
    # Parameters reference
    # https://developer.twitter.com/en/docs/tweets/search/api-reference/get-search-tweets.html
    results = api.search(geocode=geo,lang = lang,)
    for r in results:
        print(r.text)

    return results

def Tgeo(geo = ''):
    results = api.reverse_geocode(granularity='city',)
    testTweepyStatus(results)

# process StreamListener data by carbrand
# extract useful info and compute sentiment parameter
def processData(data):

    raw = json.loads(data)
    #pprint(raw)
    print(raw['text'])
    tmp = dict(carbrands = [])
    # check carbrands in rawtext
    signal = False
    for word in raw['text'].split():
        if word.lower() in carBrandLower:
            signal = True
            tmp['carbrands'].append(word.lower())
    if not signal:
        print('no car brand inside')
        return

    # get userful info
    tmp['_id'] = raw['id_str']
    tmp['id'] = raw['id']
    tmp['geo'] = raw['geo']
    tmp['coordinates'] = raw['coordinates']
    tmp['place'] = raw['place']
    tmp['text'] = raw['text']
    tmp['retweeted'] = raw['retweeted']
    tmp['hashtags'] = raw['entities']['hashtags']['text']

    # check media
    medias = set()
    for i in raw['extended_entities']['media']:
        medias.add(i['type'])
    tmp['includeMedia'] = 'video' in medias
    tmp['includePhoto'] = 'photo' in medias

    # check retweet
    # todo


    # vader sentiment analysis
    # compound is the score [-1,1]
    vs = analyzer.polarity_scores(raw['text'])['compound']
    tmp['compound'] = vs
    if vs <= -0.05 : tmp['sentiment'] = 'negative'
    elif vs >= 0.05 : tmp['sentiment'] = 'positive'
    else : tmp['sentiment'] = 'neutral'

    # extract cities from raw text
    places = GeoText(raw['place']['full_name'])
    if len(places.cities) > 1:
        print('cities > 1 error!!!')
    tmp['where'] = dict(
        city = places.cities[0]
        #counties = places.country_mentions
    )
    #pprint(tmp)

    # check hashtags
    # todo
    tmp['hashtags'] = []
    for tagentities in raw['entities']['hashtags']:
        tmp['hashtags'].append(tagentities['text'])
    pushTweet(tmp,'car')

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
    #track=["sports"]

    print('begin listening')
    #track=["a", "the", "i", "you", "u"]
    twitterStream.filter(locations= geoBlock['aus'],languages = ['en'])




def getOne():
    tweets = Tsearch()
    return tweets[0]


if __name__ == '__main__':
    query = carBrand
    lang = "en"
    geo = geoNode['sydney']
    dbname = 'car'
    results = api.search(geocode=geo, lang=lang,fromDate = '201712220000',toDate = '201812220000' )
    for r in results:
        pprint(r)










