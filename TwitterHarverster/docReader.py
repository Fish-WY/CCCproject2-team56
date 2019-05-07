import time
from TwitterAPItools import *
import json
from APIconfig import ausCities

#read by line
total = 0
fname = './historytweets/adelaide2015.json'

creatDB('car')
for year in ['2015','2016']:
    for city in ausCities:
        print('star file',city,year)
        print('total tweets',total)
        fname = city + year + '.json'
        try:
            f = open('/data/'+fname,'r',encoding='UTF-8')
            #f = open('./historytweets/adelaide2015.json', 'r', encoding='UTF-8')

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
            print('docReader error')
            continue
        finally:
            pass

print('total tweets',total)

