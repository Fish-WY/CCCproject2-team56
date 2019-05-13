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
consumer_key = kris_api['consumer_key']
consumer_secret = kris_api['consumer_secret']
access_token_key = kris_api['access_token']
access_token_secret = kris_api['access_secret']

# developer verification and get API interface
# Create authentication objects
auth = tweepy.OAuthHandler( consumer_key, consumer_secret )
# set access token & access secret
auth.set_access_token( access_token_key, access_token_secret )
# Pass in the auth parameter to create the API object
api = tweepy.API( auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True )

print('Twitter API created')

'''
normal API return an object  status._json >> str
but stream API return a string  
so there is a bit different in there
'''


def Tgeo(geo = ''):
    results = api.reverse_geocode(granularity='city',)
    return  results

# process StreamListener data by carbrand
# extract useful info and compute sentiment parameter
def processData(data, onlycarbrand = False):
    #print(type(data))
    if isinstance(data,dict):
        if 'doc' in data:
            raw = data['doc']
        else:
            raw = data
    else:
        raw = json.loads(data)
    #pprint(raw)

    tmp = {}


    # get userful info
    tmp['_id'] = raw['id_str']
    tmp['when'] = raw['created_at']
    tmp['id'] = raw['id_str']
    tmp['geo'] = raw['geo']
    tmp['coordinates'] = raw['coordinates']
    tmp['place'] = raw['place']
    tmp['truncated'] = raw['truncated']
    if 'extended_tweet' in raw:
        tmp['text']= raw['extended_tweet']['full_text']
    else:
        tmp['text'] = raw['text']

    #print(tmp['text'])

    # check carbrands in text
    tmp['carbrands'] = []
    carbrandsignal = False
    for word in tmp['text'].split():
        word = word.lower()
        if word in carBrandLower:
            carbrandsignal = True
            tmp['carbrands'].append(carBrandmap[word])
            if word == 'car' or word == 'cars':
                cartagsignal = True
    else:
        if onlycarbrand and carbrandsignal == False:
            return

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
    if 'key' in data and 'value' in data:
        tmp['where'] = [data['key'][0]]
    elif raw['place']:
        # get city from API
        for city in ausCities:
            if raw['place']['full_name'].find(city) != -1:
                tmp['where'] = [city]
                break
        else:
            return
    else: return

    # extract region
    if tmp['geo'] or tmp['coordinates']:
        y,x = tmp['geo']['coordinates']
        tmp['where'].append(getRegion([x,y]))
    elif tmp['coordinates']:
        tmp['where'].append(getRegion(tmp['coordinates']['coordinates']))
    else:
        tmp['where'].append(random.choice(regionMap[tmp['where'][0]]))
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

    # tmp['cartags'] = []
    # cartagsignal = False
    # for tag in ['car']:
    #     if tag in tmp['hashtags']:
    #         tmp['cartags'].append(tag)
    # if tmp['cartags']:
    #     cartagsignal = True



    #print('---post one---')
    postTweet(tmp,name = 'twitter')
    if carbrandsignal: postTweet(tmp,name = 'car')
    #if cartagsignal: postTweet(tmp,'cartags')



# def getOne():
#     tweets = Tsearch()
#     return tweets[0]


if __name__ == '__main__':
    print('___________Twitter API test____________')

    #Tsearch()










