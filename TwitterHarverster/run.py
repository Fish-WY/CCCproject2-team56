from TwitterAPItools import *
import sys


if __name__ == '__main__' :
    # harvester name
    mission = sys.argv[1]
    # target couch database name
    dbname = sys.argv[2]
    creatDB(dbname)
    if mission == 'carbrands':
        beginStream(dbname)
    else:
        print('no such mission')
    #Tsearch()
    pass
