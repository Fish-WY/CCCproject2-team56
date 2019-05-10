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
    print('___________Twitter Stream API begin______________')
    beginStream(dbname)
