# Team 56
# Yishan Shi 883166
# Huiya Chen 894933
# Tong He 867488
# Yao Wang 869992
# Aaron Robins 694098

from cloudant.client import CouchDB
import json

USERNAME = 'admin56'
PASSWORD = 'admin56'
client = CouchDB(USERNAME,PASSWORD,url='http://172.26.38.69:5984',connect=True)
session = client.session()

def get_aurindata(db,file):

    my_database = client[db]
    my_document = my_database[file]

    return my_document

def get_supercar(dbname = 'car', ddocID = '_design/car' , viewID = 'superCar'):

    doc = client[dbname].get_design_document(ddocID)
    view = doc.get_view(viewID)
    result = []
    with view.custom_result(group_level=2) as rslt:
        for doc in rslt.all():
            #print(doc)
            if doc["key"][1] is not None :
                map={}
                map["region"] = doc["key"][1]
                map["vader"] = doc["value"]["sum"]/doc["value"]["count"]
                result.append(map)

    return result


def get_count_score(dbname = 'twitter', ddocID = '_design/time' , viewID = 'score',region = ''):

    doc = client[dbname].get_design_document(ddocID)
    view = doc.get_view(viewID)
    result = []
    with view.custom_result(group_level=3) as rslt:
        for doc in rslt.all():

            if region == doc["key"][2]:
                #print(doc)
                map={}
                map["time"] = doc["key"][0]
                map["count"] = doc["value"]["count"]
                map["score"] = doc["value"]["sum"]/doc["value"]["count"]
                result.append(map)

    return result

def region_brand(dbname = 'car', ddocID = '_design/car' , viewID = 'byRegion', region = ''):
    doc = client[dbname].get_design_document(ddocID)
    view = doc.get_view(viewID)

    brand_vader = []

    with view.custom_result(group_level = 2) as rslt:
        for doc in rslt.all():
            #print(doc)
            if region == doc["key"][0]:
                map = {}
                map["brand"] = doc["key"][1]
                map["vader"] = doc["value"]["sum"]/doc["value"]["count"]
                brand_vader.append(map)

    return brand_vader

def total_count(dbname = 'twitter', ddocID = '_design/time' , viewID = 'count'):
    doc = client[dbname].get_design_document(ddocID)
    view = doc.get_view(viewID)
    count=0
    with view.custom_result(group_level = 0) as rslt:
        for doc in rslt.all():
            print(doc)
            return doc["value"]

    return count

total_count()
