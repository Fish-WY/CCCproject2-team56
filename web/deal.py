# Team 56
# Yishan Shi 883166
# Huiya Chen 894933
# Tong He 867488
# Yao Wang 869992
# Aaron Robins 694098

import json
import linkDB

regionMap = {
 'adelaide': ['Adelaide - Central and Hills',
              'Adelaide - North',
              'Adelaide - South',
              'Adelaide - West'],
 'brisbane': ['Brisbane - East',
              'Brisbane - North',
              'Brisbane - South',
              'Brisbane - West',
              'Brisbane Inner City',
              'Ipswich'],
 'canberra': ['Australian Capital Territory'],
 'hobart': ['Hobart'],
 'melbourne': ['Melbourne - Inner',
               'Melbourne - Inner East',
               'Melbourne - Inner South',
               'Melbourne - North East',
               'Melbourne - North West',
               'Melbourne - Outer East',
               'Melbourne - South East',
               'Melbourne - West',
               'Geelong'],
 'perth': ['Perth - Inner',
           'Perth - North East',
           'Perth - North West',
           'Perth - South East',
           'Perth - South West'],
 'sydney': ['Sydney - Baulkham Hills and Hawkesbury',
            'Sydney - Blacktown',
            'Sydney - City and Inner South',
            'Sydney - Eastern Suburbs',
            'Sydney - Inner South West',
            'Sydney - Inner West',
            'Sydney - North Sydney and Hornsby',
            'Sydney - Northern Beaches',
            'Sydney - Outer South West',
            'Sydney - Outer West and Blue Mountains',
            'Sydney - Parramatta',
            'Sydney - Ryde',
            'Sydney - South West',
            'Sydney - Sutherland']}


def loadaurin():
    aurindata = linkDB.get_aurindata('aurin','cd19601ff48fec927421d634e205006d')

    #print(aurindata)
    incomedata = []

    for city in aurindata["features"]:
        regionInfo = {}
        pro = city["properties"]
        if(pro["sa4_name16"] in regionMap["adelaide"] or pro["sa4_name16"] in regionMap["brisbane"]
                or pro["sa4_name16"] in regionMap["canberra"] or pro["sa4_name16"] in regionMap["hobart"]
                or pro["sa4_name16"] in regionMap["melbourne"] or pro["sa4_name16"] in regionMap["perth"]
                or pro["sa4_name16"] in regionMap["sydney"]):
            regionInfo["name"] = pro["sa4_name16"]
            regionInfo["high"] = pro["hi_4000_more_tot"]
            incomedata.append(regionInfo)

    incomedata = sorted(incomedata, key=lambda e: e["name"], reverse=False)
    return incomedata

def pick_region(reg):

    result = linkDB.get_count_score(region=reg)

    return result

def pick_brand(reg):
    result = linkDB.region_brand(region=reg)
    result = sorted(result, key=lambda e: e["vader"], reverse=False)
    return result

def income_drilldown():
    city = loadaurin()
    australia = [{"name":"adelaide","hightotal":0,"region":[]},{"name":"brisbane","hightotal":0,"region":[]},
                 {"name": "canberra", "hightotal": 0, "region": []},{"name":"hobart","hightotal":0,"region":[]},
                 {"name": "melbourne", "hightotal": 0, "region": []},{"name":"perth","hightotal":0,"region":[]},
                 {"name": "sydney", "hightotal": 0, "region": []},]

    for city in city:
        if(city["name"] in regionMap["adelaide"]):
            australia[0]["hightotal"] = australia[0]["hightotal"] + city["high"]
            australia[0]["region"].append(city)

        if city["name"] in regionMap["brisbane"]:
            australia[1]["hightotal"] = australia[1]["hightotal"] + city["high"]
            australia[1]["region"].append(city)

        if city["name"] in regionMap["canberra"]:
            australia[2]["hightotal"] = australia[1]["hightotal"] + city["high"]
            australia[2]["region"].append(city)

        if city["name"] in regionMap["hobart"]:
            australia[3]["hightotal"] = australia[1]["hightotal"] + city["high"]
            australia[3]["region"].append(city)

        if city["name"] in regionMap["melbourne"]:
            australia[4]["hightotal"] = australia[1]["hightotal"] + city["high"]
            australia[4]["region"].append(city)

        if city["name"] in regionMap["perth"]:
            australia[5]["hightotal"] = australia[1]["hightotal"] + city["high"]
            australia[5]["region"].append(city)

        if city["name"] in regionMap["sydney"]:
            australia[6]["hightotal"] = australia[1]["hightotal"] + city["high"]
            australia[6]["region"].append(city)


    return australia

def income_supercar():
    income = loadaurin()
    vader = linkDB.get_supercar()

    #print(len(income))
    #print(len(vader))

    for i1 in range(0,len(vader)):
        for i2 in range(0, len(income)):
            if income[i2]["name"] == vader[i1]["region"]:
                vader[i1]["people"] = income[i2]["high"]

    #print(vader)
    return vader


def update_tweet():
    res = linkDB.total_count()
    return  res
#income_supercar()

#print(income_drilldown())



