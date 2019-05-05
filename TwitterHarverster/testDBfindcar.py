from CouchDBtools import *
import tweepy
from time import sleep
from tweepy.streaming import StreamListener
from tweepy import Stream
from APIconfig import *
from pprint import pprint
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from geotext import GeoText
from cloudant.client import CouchDB
import json
from pprint import pprint

count = 0
for doc in client['test']:
    try:
        if doc['truncated']:
            print(doc['extended_tweet']['full_text'])
            for word in doc['extended_tweet']['full_text'].split():
                if word.lower() in carBrandLower:
                    signal = True
                    count += 1
                    print(count)
                    my_document = client['trash'].create_document(doc)
                    break
        else:
            print(doc['text'])
            for word in doc['text'].split():
                if word.lower() in carBrandLower:
                    signal = True
                    count += 1
                    print(count)
                    my_document = client['trash'].create_document(doc)
                    break
    except:
        pass
print('-'*35)
print('count = ',count)



