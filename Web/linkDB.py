from cloudant.client import CouchDB
import json

USERNAME = 'admin'
PASSWORD = 'admin'
client = CouchDB(USERNAME,PASSWORD,url='http://localhost:5985',connect=True)
session = client.session()

def get_data(db,file):

    my_database = client[db]
    my_document = my_database[file]

    return my_document


client1 = CouchDB(USERNAME,PASSWORD,url='http://45.113.235.214:5985',connect=True)
session1 = client1.session()

# def getViewResult(dbname = 'car', ddocID = '_design/car' , viewID = 'occurrenceByPlace'):
#     doc = client1[dbname].get_design_document(ddocID)
#     view = doc.get_view(viewID)
#
#     city = [{"city":"Adelaide","total":0,"area":[]},{"city":"Brisbane","total":0,"area":[]},
#             {"city": "Canberra", "total": 0, "area": []},{"city":"Melbourne","total":0,"area":[]},
#             {"city": "Perth", "total": 0, "area": []},{"city":"Sydney","total":0,"area":[]}]
#
#     #pprint(view.result)
#     with view.custom_result(group_level=3,reduce=True) as rslt:
#         for doc in rslt:
#             print(doc)
#             map = {}
#             map["name"] = doc["key"][1]
#             map["count"] = doc["value"]
#             if(doc["key"][0]=="adelaide"):
#                 city[0]["total"] = city[0]["total"] + map["count"]
#                 city[0]["area"].append(map)
#             elif(doc["key"][0] == "brisbane"):
#                 city[1]["total"] = city[1]["total"] + map["count"]
#                 city[1]["area"].append(map)
#             elif (doc["key"][0] == "canberra"):
#                 city[2]["total"] = city[2]["total"] + map["count"]
#                 city[2]["area"].append(map)
#             elif (doc["key"][0] == "melbourne"):
#                 city[3]["total"] = city[3]["total"] + map["count"]
#                 city[3]["area"].append(map)
#             elif (doc["key"][0] == "perth"):
#                 city[4]["total"] = city[4]["total"] + map["count"]
#                 city[4]["area"].append(map)
#             elif (doc["key"][0] == "sydney"):
#                 city[5]["total"] = city[5]["total"] + map["count"]
#                 city[5]["area"].append(map)
#
#     return city

def getViewResult1(dbname = 'car', ddocID = '_design/car' , viewID = 'byRegion'):
    doc = client1[dbname].get_design_document(ddocID)
    view = doc.get_view(viewID)

    region_car_score = []

    with view.custom_result(group_level = 2) as rslt:
        for doc in rslt.all():
            #print(doc)
            region = doc["key"][0]
            brand = doc["key"][1]
            score = doc["value"]

            index = 0
            while index < len(region_car_score):
                reg = region_car_score[index]
                if reg["region"] == region:
                    map = {}
                    map["name"] = brand
                    map["score"] = score
                    reg["brand"].append(map)
                    break
                index = index + 1

            if index == len(region_car_score):
                map = {}
                map["region"] = region
                map["brand"] = []
                map1 = {}
                map1["name"] = brand
                map1["score"] = score
                map["brand"].append(map1)
                region_car_score.append(map)

    return region_car_score


