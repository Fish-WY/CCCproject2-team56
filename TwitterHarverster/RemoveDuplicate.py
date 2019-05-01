from cloudant.client import CouchDB
from TwitterHarverster.TwitterProcessor import *
#import CouchDBconnecter




# Create CouchDB client (need SSH -f in background)
USERNAME = 'admin'
PASSWORD = 'admin'
client = CouchDB(USERNAME, PASSWORD, url='http://localhost:5985', connect=True)
# Perform client tasks...
session = client.session()
print('Username: {0}'.format(session['userCtx']['name']))
print('Databases: {0}'.format(client.all_dbs()))

# Open 'twitter' database
my_database = client['test']


jdata = {
    "_id": "39abeb083f271561395ae3ecb3001744",
    "_rev": "1-ffa9b950ffd62466742c50382654060a",
    "created_at": "Tue Apr 23 23:44:01 +0000 2019",
    "GF": "HT",
    'BG':'WY'
}
#jdata = stripTwitter(jdata)
my_document = my_database.create_document(jdata)

if my_document.exists():
    print('--------SUCCESS!!----------')
    # Display the document
    pprint(my_document)
    pprint(my_database['39abeb083f271561395ae3ecb3001744'])

client.disconnect()













