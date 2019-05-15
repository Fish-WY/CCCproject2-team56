'''
CCC2019 Team 56
Yishan Shi 883166
Huiya Chen 894933
Tong He 867488
Yao Wang 869992
Aaron Robins 694098
'''
from cloudant.client import CouchDB
import json
from pprint import pprint

# Create CouchDB client (need SSH -f in background)
USERNAME = 'admin56'
PASSWORD = 'admin56'

# http://172.26.37.222:5984/_utils/#database/history_tweet/_design/day_data_view/_view/day_view
client = CouchDB(USERNAME, PASSWORD, url='http://localhost:5984', connect=True)
# Perform client tasks...z
session = client.session()
print('Username: {0}'.format(session['userCtx']['name']))
print('Databases: {0}'.format(client.all_dbs()))

# default target database
dbname = 'test2'
# create a database with name
def creatDB(name ='car'):
    if name in client:
        print('DB',name,'exist')
        my_database = client[name]
    else:
        my_database = client.create_database(name)
        if my_database.exists():
            print('Create database ' + name)
        else:
            print('Create database fail')
    # change target database
    global dbname
    dbname = name

# get tweet(string) and insert it to couchDB
def postTweet(tweet, name = dbname):
    #print('post',name)
    if type(tweet) == 'str':
        Ddata = json.loads(tweet)
    else:
        Ddata = tweet
    #pprint(Ddata)
    #print(Ddata['carbrands'])
    my_document = client[name].create_document(Ddata)

    # Check that the document exists in the database
    # if my_document.exists():
    #     print('--------SUCCESS!!----------')
    #     # Display the document
    #     pprint(my_document)
    #     pass
    return True

def postTweets(tweets, name = dbname):
    for t in tweets:
        postTweet(t, name)




def getViewResult(dbname = 'car', ddocID = '_design/car' , viewID = 'superCar'):
    doc = client[dbname].get_design_document(ddocID)
    pprint(doc)
    view = doc.get_view(viewID)
    pprint(view)

    print('-'*15+'view'+'-'*15)
    #pprint(view.result)
    with view.custom_result(group_level = 0) as rslt:
        pprint(rslt)

        for doc in rslt.all():
            #print(type(doc))
            print(doc)
            pass
    return rslt



if __name__ == '__main__':
    getViewResult()








