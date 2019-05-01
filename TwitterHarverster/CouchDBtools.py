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
dbname = "test"
if dbname in client:
    my_database = client[dbname]
else:
    my_database = client.create_database(dbname)

# get tweet(string) and insert it to couchDB
def pushToCouchDB(data):
    jdata = json.loads(data)
    my_document = my_database.create_document(jdata)

    # Check that the document exists in the database
    if my_document.exists():
        print('--------SUCCESS!!----------')
        # Display the document
        pprint(my_document)
    return True















