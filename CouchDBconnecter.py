from cloudant.client import CouchDB
from pprint import pprint

USERNAME = 'admin'
PASSWORD = 'admin'
client = CouchDB(USERNAME, PASSWORD, url='http://localhost:5985', connect=True)

# Perform client tasks...
session = client.session()
print('Username: {0}'.format(session['userCtx']['name']))
print('Databases: {0}'.format(client.all_dbs()))

# Open an existing database
my_database = client['twitter']

if __name__ == '__main__':
    # Create document content data
    simpledata = {
        '_id': 'julia30', # Setting _id is optional
        'name': 'Julia',
        'age': 30,
        'pets': ['cat', 'dog', 'frog']
        }

    # Create a document using the Database API
    my_document = my_database.create_document(simpledata)

    # Check that the document exists in the database
    if my_document.exists():
        print('SUCCESS!!')
        # Display the document
        my_document = my_database['julia30']
        pprint(my_document)


    # Disconnect from the server
    client.disconnect()
