import time
from TwitterAPItools import *
import json
from APIconfig import ausCities

#read by line
total = 0
fname = './historytweets/adelaide2015.json'

creatDB('car')
for year in range(2014,2020):
    year = str(year)
    for city in ausCities:
        fname = city + year + '.json'
        print('start file',fname)
        print('total tweets',total)
        try:
            f = open('/data/'+fname,'r',encoding='UTF-8')
            #f = open('./historytweets/perth2016.json', 'r', encoding='UTF-8')

            print(f.readline())

            for line in f:
                line = f.readline()
                twi = None
                try:
                    twi = json.loads(line.rstrip(',\n'))
                except:
                    print('JSONDecodeError !!!')
                    continue
                total += 1  # conunt total twitters
                #pprint(twi)
                processData(twi)

            f.close()
        except IOError as e:
            print(e)
            print('doc open error')
            continue
        finally:
            pass
print('docReader  finish!!!')
print('total tweets',total)

