X_DOMAINS = '*'
X_MAX_AGE = 24 * 3600
X_HEADERS = ['Content-Type', 'Authorization', 'If-Match']

MONGO_HOST = 'localhost'
MONGO_PORT = 27017

MONGO_DBNAME = 'marketplace'

RESOURCE_METHODS = ['GET', 'POST']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

# Make the access methods public
#PUBLIC_METHODS = ['GET']
#PUBLIC_ITEM_METHODS = ['GET']


producers = {
    'resource_methods': ['GET', 'POST', 'DELETE'],
    'public_methods': ['GET'],
    'public_item_methods': ['GET'],
    'schema': {
        'name' : {
            'type': 'string',
            'minlength': 1,
            'maxlength': 64,
            'required': True,
            'unique': True
        }
    }
}

DOMAIN = {
    'producers': producers
}