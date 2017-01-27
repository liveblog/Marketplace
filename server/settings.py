import os

X_DOMAINS = '*'
X_MAX_AGE = 24 * 3600
X_HEADERS = ['Content-Type', 'Authorization', 'If-Match']

MONGO_HOST = 'localhost'
MONGO_PORT = 27017

MONGO_DBNAME = 'marketplace'

RESOURCE_METHODS = ['GET', 'POST']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

URL_PREFIX = 'api'

def env(variable, fallback_value=None):
    env_value = os.environ.get(variable, '')
    return env_value if len(env_value) != 0 else fallback_value

SENTINEL_MANAGEMENT_USERNAME=env('ADMIN_USERNAME', 'admin')
SENTINEL_MANAGEMENT_PASSWORD=env('ADMIN_PASSWORD', 'admin')

RETURN_MEDIA_AS_BASE64_STRING = False
RETURN_MEDIA_AS_URL = True
MEDIA_ENDPOINT = 'media'


marketers = {
    'resource_methods': ['GET', 'POST', 'DELETE'],
    'public_methods': ['GET'],
    'public_item_methods': ['GET'],
    'schema': {
        'name': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 64,
            'required': True,
            'unique': True
        },
        'url': {
            'type': 'string',
            'required': True
        },
        'email': {
            'type': 'string',
            'required': True
        },
        'phone': {
            'type': 'string'
        },
        'picture_url': {
            'type': 'media'
        }
    }
}

blogs = {
    'public_methods': ['GET'],
    'public_item_methods': ['GET'],
    'schema': {
        'marketer': {
            'type': 'objectid',
            'required': True,
            'data_relation': {
                'resource': 'marketers',
                'field': '_id',
                'embeddable': True
            }
        },
        'marketer_blog_id': {
            'type': 'string',
            'required': True
        },
        'title': {
            'type': 'string',
            'required': True
        },
        'description':  {
            'type': 'string',
            'required': True
        },
        'picture_url': {
            'type': 'string'
        },
        'public_url': {
            'type': 'string',
            'required': True
        },
        'category': {
            'type': 'string',
            'default': ''
        },
        'start_date': {
            'type': 'datetime',
            'default': None
        }
    }
}

DOMAIN = {
    'marketers': marketers,
    'blogs': blogs
}
