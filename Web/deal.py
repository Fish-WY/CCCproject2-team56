import json
import linkDB


def loadaurin():
    aurindata = linkDB.get_data('aurin','income1234')

    citydata = []

    for city in aurindata["features"]:
        regionInfo = {}
        pro = city["properties"]
        regionInfo["code"] = pro["sa4_code16"]
        regionInfo["name"] = pro["sa4_name16"]
        regionInfo["high"] = pro["i_3500_3999_tot"]
        regionInfo["low"] = pro["i_300_399_tot"]
        citydata.append(regionInfo)

    #citydata = sorted(citydata, key=lambda e: e['high'], reverse=True)
    return citydata

def pick_region(reg):
    info = linkDB.getViewResult1();
    for index in range(0,len(info)):
        if(reg == info[index]["region"]):
            return info[index]["brand"]

    return []

def statistics(city):
    australia = [{"name":"New South Wales","hightotal":0,"lowtotal":0,"city":[]},{"name":"Victoria","hightotal":0,"lowtotal":0,"city":[]},
                 {"name": "Queensland","hightotal":0,"lowtotal":0, "city": []},{"name":"South Australia","hightotal":0,"lowtotal":0,"city":[]},
                 {"name": "Western Australia","hightotal":0,"lowtotal":0, "city": []},{"name":"Tasmania","hightotal":0,"lowtotal":0,"city":[]},
                 {"name": "Northern Territory","hightotal":0,"lowtotal":0, "city": []},{"name":"Australian Capital Territory","hightotal":0,"lowtotal":0,"city":[]}]

    for city in city:
        if(city["code"][0]) == '1':
            australia[0]["hightotal"] = australia[0]["hightotal"] + city["high"]
            australia[0]["lowtotal"] = australia[0]["lowtotal"] + city["low"]
            australia[0]["city"].append(city)

        if (city["code"][0]) == '2':
            australia[1]["hightotal"] = australia[1]["hightotal"] + city["high"]
            australia[1]["lowtotal"] = australia[1]["lowtotal"] + city["low"]
            australia[1]["city"].append(city)

        if (city["code"][0]) == '3':
            australia[2]["hightotal"] = australia[1]["hightotal"] + city["high"]
            australia[2]["lowtotal"] = australia[1]["lowtotal"] + city["low"]
            australia[2]["city"].append(city)

        if (city["code"][0]) == '4':
            australia[3]["hightotal"] = australia[1]["hightotal"] + city["high"]
            australia[3]["lowtotal"] = australia[1]["lowtotal"] + city["low"]
            australia[3]["city"].append(city)

        if (city["code"][0]) == '5':
            australia[4]["hightotal"] = australia[1]["hightotal"] + city["high"]
            australia[4]["lowtotal"] = australia[1]["lowtotal"] + city["low"]
            australia[4]["city"].append(city)

        if (city["code"][0]) == '6':
            australia[5]["hightotal"] = australia[1]["hightotal"] + city["high"]
            australia[5]["lowtotal"] = australia[1]["lowtotal"] + city["low"]
            australia[5]["city"].append(city)

        if (city["code"][0]) == '7':
            australia[6]["hightotal"] = australia[1]["hightotal"] + city["high"]
            australia[6]["lowtotal"] = australia[1]["lowtotal"] + city["low"]
            australia[6]["city"].append(city)

        if (city["code"][0]) == '8':
            australia[7]["hightotal"] = australia[1]["hightotal"] + city["high"]
            australia[7]["lowtotal"] = australia[1]["lowtotal"] + city["low"]
            australia[7]["city"].append(city)

    return australia


#print(statistics(loadaurin()))
