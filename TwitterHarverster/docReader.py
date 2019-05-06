import time
from TwitterAPItools import *
import json
from APIconfig import ausCities

#read by line
total = 0
fname = 'adelaide2015.json'

creatDB('trash')
for city in ausCities:
    fname = city + '2015.json'
    try:
        f = open('./historytweets/'+fname,'r',encoding='UTF-8')

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
    except :
        print()
    finally:
        f.close()


