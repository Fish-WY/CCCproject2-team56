
import json

# load a Geojson file
def loadGrid(filePath):
    gridMap = []
    twitternum={}
    
    with open(filePath) as file:
        info = json.load(file)
        # loop each region in the file
        for region in info["features"]:
            regionInfo = {}
            polygon = region["geometry"]
            regionInfo["bound"]=polygon["coordinates"]
            #number of polygon
            regionInfo["count"]=len(regionInfo["bound"])
            prop=region["properties"]
            #get the infomation of region
            regionInfo["id"] = prop["feature_code"]
            regionInfo["name"] = prop["feature_name"]
            regionInfo["money"] = prop["median_income_per_employed_aud_persons"]
            
            gridMap.append(regionInfo)
            twitternum[regionInfo["name"]]=0
            #print (region)
            #break
    #with open("out.json","w") as out:
    #    out.writelines(gridMap)
    print(len(twitternum))
    #print(gridMap)
    return (gridMap,twitternum)

# input: point need to be judged.
#        start point of edge
#        end point of edge
#        all input are in format [lng,lat]
def intersect(poi,start_point,end_point): 

    # edge above the ray
    if start_point[1]>poi[1] and end_point[1]>poi[1]: 
        return False
    # edge under the ray
    if start_point[1]<poi[1] and end_point[1]<poi[1]: 
        return False
        
    # exclude parallel and coincident with the ray, the end and end of the line overlap
    if start_point[1]==end_point[1]: 
        return False
    # The intersection point is the lower endpoint, corresponding to spoint
    if start_point[1]==poi[1] and end_point[1]>poi[1]: 
        return False
    # The intersection point is the lower endpoint, corresponding to spoint
    if end_point[1]==poi[1] and start_point[1]>poi[1]: 
        return False
    # edge is in the left of ray
    if start_point[0]<poi[0] and end_point[0]<poi[0]: #线段在射线左边
        return False
    # find intersection
    xseg=end_point[0]-(end_point[0]-start_point[0])*(end_point[1]-poi[1])/(end_point[1]-start_point[1]) 
    # intersect is in the lect of ray point
    if xseg<poi[0]: 
        return False

    return True  

# input: point:[lng, lat]
#        polygon: [[[lng, lat],[lng, lat],……,[lng, lat],[lng, lat]],[[lng, lat],……[lng, lat]]]
 
def pointInPolygon(poi,poly):
    
    intersection=0 #number of  intersectiono
    for each_polygon in poly: #loop each polygon in multiple polygons->each polygon 
        for i in range(len(each_polygon[0])-1): #loop each edge in polygon
            start_point=each_polygon[0][i]
            end_point=each_polygon[0][i+1]
            if intersect(poi,start_point,end_point):
                intersection+=1 
    # in the polygon if the number of intersection is odd
    return True if intersection%2==1 else  False

(grid,twitterCount)=loadGrid("data.json")


def getRegion(position):
    for region in grid:
        name=region["name"]
        if pointInPolygon(position, region["bound"]):
            return name

