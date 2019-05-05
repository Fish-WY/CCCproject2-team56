from cloudant.client import CouchDB
import json
from pprint import pprint

# Create CouchDB client (need SSH -f in background)
USERNAME = 'admin'
PASSWORD = 'admin'

client = CouchDB(USERNAME, PASSWORD, url='http://localhost:5985', connect=True)
# Perform client tasks...
session = client.session()
print('Username: {0}'.format(session['userCtx']['name']))
print('Databases: {0}'.format(client.all_dbs()))

# default target database
dbname = 'test'
# create a database with name
def creatDB(name ='car'):
    if name in client:
        print('DB exist')
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
def pushTweet(tweet,name = dbname):
    if type(tweet) == 'str':
        Ddata = json.loads(tweet)
    else:
        Ddata = tweet
    print(Ddata)
    my_document = client[name].create_document(Ddata)

    # Check that the document exists in the database
    if my_document.exists():
        #print('--------SUCCESS!!----------')
        # Display the document
        #pprint(my_document)
        pass
    return True

def pushTweets(tweets,name = dbname):
    for t in tweets:
        pushTweet(t,name)




def getViewResult(ddocID = '_design/testDoc' , viewID = 'occurrenceByPlace'):
    doc = client[dbname].get_design_document(ddocID)
    pprint(doc)
    view = doc.get_view(viewID)
    pprint(view)

    print('-'*15+'view'+'-'*15)
    #pprint(view.result)
    with view.custom_result(group=True) as rslt:
        for doc in rslt:
            print(doc)



if __name__ == '__main__':
    viewID = 'newview'
    getViewResult()








