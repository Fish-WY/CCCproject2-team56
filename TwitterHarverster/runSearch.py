'''
CCC2019 Team 56
Yishan Shi 883166
Huiya Chen 894933
Tong He 867488
Yao Wang 869992
Aaron Robins 694098
'''
from TwitterAPItools import *

# developer verification and return API interface
def getAPI(machine):
    consumer_key = machine['consumer_key']
    consumer_secret = machine['consumer_secret']
    access_token_key = machine['access_token']
    access_token_secret = machine['access_secret']

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token_key, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    return api

# recursively run search api with multi user
def Tsearch(query = carBrand,lang = "en",geo = geoNode['sydney'],dbname = 'car'):
    # Parameters reference
    # https://developer.twitter.com/en/docs/tweets/search/api-reference/get-search-tweets.html
    current_id = {city: 0 for city in ausCities}
    while True:
        for city in ausCities:
            geocode = geoNode[city]
            since_id = current_id[city]
            print('-'*15,city,since_id,'-'*15)
            try:
                results = api.search(geocode=geocode,lang = lang,include_entities = True,since_id = since_id,result_type='mixed')
                print(len(results))
                for r in results:
                    current_id[city] = max(current_id[city],r.id)
                    #print(r.text)
                    processData(r._json)
                current_id[city] += 1
            except tweepy.RateLimitError as e:
                print('RateLimitError !!! lets sleep 15 min')
                sleep(15*60)
            except tweepy.TweepError as e:
                print(e.response.text)
                return
            sleep(5)
        else:
            print("wait 1 min for more tweet")
            sleep(60)
    return results

if __name__ == '__main__':
    print('___________Twitter search API begin______________')
    Tsearch()