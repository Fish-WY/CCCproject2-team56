from collections import Counter
import json
from pprint import pprint
import sys
import re

#read and strip each row of twitter only maintain its GEO and hashtag
def stripTwitter(t):
    data = {
        'geo': getGeo(t),
        'hashtags': getTag(t),
        'text': t['text']
    }
    return data

def getGeo(t):
    try:
        if t['value']['geometry']['coordinates'] :
            return t['value']['geometry']['coordinates']
    except:
        pass
    try:
        if t['doc']['coordinates']['coordinates']:
            return t['doc']['coordinates']['coordinates']
    except:
        pass
    try:
        if t['geo']['coordinates']:
            x , y = t['geo']['coordinates']
            return [y,x]
    except:
        pass
    return []


def getTag(t):
    #extract tag
    finaltags = set([i['text'].lower() for i in t['doc']['entities']['hashtags']])
    #raw = t['value']['properties']['text']
    raw = t['doc']['text']
    #print(raw)

    #print(raw,"\n",finaltags)
    '''
    # solution 2 via regular expression
    rawtags = re.findall(r' #[\S]+',raw)
    #print(rawtags)
    for t in rawtags:
        finaltags.add(t[2:].lower())
        #print(t[2:].lower())
    
    '''
    # get tags from raw text
    '''
    for token in raw.split():
    #print(token)
    if token[0] == '#' and len(token) > 1:
        #print('find')
        finaltags.add(token[1:].lower())


    '''
    #print('hashtags\n',finaltags)
    return list(finaltags)

#find which grid the twitter belongs to
def getGrid(geo,grid):
    x , y = geo
    if x < 114.70 or x > 145.45 or y < -38.1 or y > -37.5:
        return None
    for i in grid:
        # The box on the right or higher takes precedence
        if x > i['xmin'] and x <= i['xmax'] and y >= i['ymin'] and y < i['ymax']:
            return i['id']
    return None

def record(geo,tags,grid,occur,gridNums):
    id = getGrid(geo,grid)
    if id:
        #total occurance in id Grid
        gridNums[id] += 1
        for tag in tags:
            occur[id][tag] += 1

#test sample (draft)
if __name__ == '__main__':
    #specify the dataset
    fname = 'smallTwitter.json'
    if len(sys.argv) > 1:
        fname = sys.argv[0]
        print(fname)

    #load melbGrid
    with open("melbGrid.json", 'r') as f:
        grid = json.loads(f.read())
        #print(grid['features'])
        grid = [ i['properties'] for i in grid['features']]


    occur = {}
    for i in grid:
        #print(i)
        occur[i['id']] = Counter()
    #read by line
    total = 0
    #with open(fname,'r') as f:
    try:
        f = open(fname,'r')
        f.readline()
        for line in f:
            '''
            if total == 5:
                pprint(twi)
                print(tags)
                print(geo)
            '''
            twi = json.loads(line.rstrip(',\n'))
            pprint(twi)
            geo = getGeo(twi)
            tags = getTag(twi)
            #modify Counter by geo & tags
            #recrod(geo, tags, grid, occur)
            total += 1
            #print(tags)
        #print(f.readline())
        #twi = json.loads(f.readline()[:-2])
        #pprint(twi)
        #pprint(twi['rows'][0]['doc']['entities']['hashtags'])
        #pprint(twi['rows'][0]['doc']['coordinates']['coordinates'])
        #pprint(twi['rows'][0])
            break
    except:
        #last line error
        pass
    finally:
        f.close()
    #pprint(occur)
    print(total)

