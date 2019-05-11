import time
from TwitterAPItools import *
import json
from APIconfig import ausCities
import sys

#read by line
total = 0
fname = './historytweets/adelaide2015.json'



def readDoc(fname):
    print('docReader.py read',fname)
    global total
    print('total tweets', total)
    try:
        f = open('/data/' + fname, 'r', encoding='UTF-8')
        #f = open('./historytweets/' + fname, 'r', encoding='UTF-8')

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
            if total % 500 == 0: print(total, 'tweets read')
            # pprint(twi)
            processData(twi)

        f.close()
    except IOError as e:
        print(e)
        print('doc open error')
        return
    finally:
        pass


if len(sys.argv) > 1:
    # city = sys.argv[1]
    # year = sys.argv[2]
    # fname = city + year + '.json'
    print(sys.argv)
    fname = sys.argv[1]
    readDoc(fname)
else:
    for year in range(2016,2020):
        year = str(year)
        for city in ausCities:
            fname = city + year + '.json'

            readDoc(fname)

print('docReader  finish!!!')
print('total tweets',total)

