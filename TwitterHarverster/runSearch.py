from TwitterAPItools import *


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
                results = api.search(q='car',geocode=geocode,lang = lang,include_entities = True,since_id = since_id,result_type='mixed')
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
        else:
            print("wait 1 min for more tweet")
            sleep(60)
    return results

if __name__ == '__main__':
    print('___________Twitter search API begin______________')
    Tsearch()