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

# Open 'twitter' database
dbname = "test2"
if dbname in client:
    my_database = client[dbname]
else:
    my_database = client.create_database(dbname)
    if my_database.exists():
        print('Create database '+dbname)
    else:
        print('Create database fail')

# get tweet(string) and insert it to couchDB
def pushTweet(tweet,dbname = 'test2'):

    jdata = json.loads(tweet)
    my_document = client[dbname].create_document(jdata)

    # Check that the document exists in the database
    if my_document.exists():
        print('--------SUCCESS!!----------')
        # Display the document
        #pprint(my_document)
    return True

def pushTweets(tweets):
    for t in tweets:
        pushTweet(t)

def pushDic(data, dbname ='test2'):
    # data : dic()
    my_document = client[dbname].create_document(data)

    return True














