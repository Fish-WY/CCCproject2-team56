from CouchDBtools import *
import tweepy
from time import sleep
from tweepy.streaming import StreamListener
from tweepy import Stream
from APIconfig import *
from pprint import pprint
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from geotext import GeoText
from polygon import getRegion
import random

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
    #print(type(data))
    if isinstance(data,dict):
        raw = data['doc']
    else:
        raw = json.loads(data)
    #pprint(raw)

    tmp = {}


    # get userful info
    tmp['_id'] = raw['id_str']
    tmp['id'] = raw['id_str']
    tmp['geo'] = raw['geo']
    tmp['coordinates'] = raw['coordinates']
    tmp['place'] = raw['place']
    tmp['truncated'] = raw['truncated']
    if 'extended_tweet' in raw:
        tmp['text']= raw['extended_tweet']['full_text']
    else:
        tmp['text'] = raw['text']




    # check media
    if 'extended_entities' in raw:
        medias = set()
        for i in raw['extended_entities']['media']:
            medias.add(i['type'])
        tmp['includeMedia'] = 'video' in medias
        tmp['includePhoto'] = 'photo' in medias
    else:
        tmp['includeMedia'] = False
        tmp['includePhoto'] = False

    # todo check retweet
    if 'retweeted_status' in raw:
        tmp['retweet'] = {'text': raw['retweeted_status']['text']}
        tmp['retweet']['compound'] = analyzer.polarity_scores(raw['retweeted_status']['text'])['compound']
    else:
        tmp['retweet'] = {}


    # vader sentiment analysis
    # compound is the score [-1,1]
    vs = analyzer.polarity_scores(tmp['text'])['compound']
    tmp['compound'] = vs
    if vs <= -0.05 : tmp['sentiment'] = 'negative'
    elif vs >= 0.05 : tmp['sentiment'] = 'positive'
    else : tmp['sentiment'] = 'neutral'

    # if tmp['coordinates'] == None:
    #     postTweet(raw, 'trash')
    #     return

    # extract cities
    if 'key' in data:
        tmp['where'] = [data['key'][0]]
    else:
        # get city from API
        for city in ausCities:
            if raw['place']['full_name'].find(city) != -1:
                tmp['where'] = [city]
                break
        else:
            return

    # extract region
    if tmp['geo'] != None:
        y,x = tmp['geo']['coordinates']
        tmp['where'].append(getRegion([x,y]))
    elif tmp['coordinates'] != None:
        tmp['where'].append(getRegion(tmp['coordinates']['coordinates']))
    else:
        tmp['where'].append(random.choice(mymap[tmp['where'][0]]))
    # from raw text
    # tmp['where'] = {'city':[]}
    # if not raw['place'] == None:
    #     places = GeoText(raw['place']['full_name'])
    #     if len(places.cities) > 1:
    #         #print(places.cities)
    #         #print('cities > 1 error!!!')
    #         pass
    #     tmp['where']['city'] = places.cities
    #pprint(tmp)

    # check hashtags
    tmp['hashtags'] = []
    if 'extended_tweet' in raw:
        for tagentities in raw['extended_tweet']['entities']['hashtags']:
            tmp['hashtags'].append(tagentities['text'])
    else:
        for tagentities in raw['entities']['hashtags']:
            tmp['hashtags'].append(tagentities['text'])

    tmp['cartags'] = []
    for tag in ['supercar','luxurycar']:
        if tag in tmp['hashtags']:
            tmp['cartags'].append(tag)
    if tmp['cartags']:  postTweet(tmp,'cartags')

    # check carbrands in text
    tmp['carbrands'] = []
    signal = False
    for word in tmp['text'].split():
        if word.lower() in carBrandLower:
            signal = True
            tmp['carbrands'].append(word.lower())
    if not signal:
        # print('no car brand inside')
        return

    postTweet(tmp,'car')

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










