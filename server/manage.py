import requests
from flask_script import Manager
from app import app
from requests.exceptions import RequestException
from requests.packages.urllib3.exceptions import MaxRetryError

manager = Manager(app)

# Update blogs of all marketers
@manager.command
def update_blogs():
    marketers_collection = app.data.driver.db['marketers']
    marketers = marketers_collection.find({})
    for marketer in marketers:
        url = marketer['url']
        if not url.endswith('/'):
            url = '{}/'.format(url)

        url = '{}marketed/blogs'.format(url)
        try:
            response = requests.request('GET', url, headers={
                'Content-Type': 'application/json'
            }, params=None, data=None, timeout=5)

        except (ConnectionError, RequestException, MaxRetryError):
            app.logger.info('No connection for ' + marketer['url'])
            continue

        if response.status_code != 200:
            app.logger.info('status code ' + str(response.status_code))
            continue

        blogs_collection = app.data.driver.db['blogs']
        jsonresponse = response.json()

        # For caching ids of blogs which have been returned - any which haven't are to be deleted
        blog_ids = []

        for blog in jsonresponse['_items']:
            blog_ids.append(blog['_id'])

            category = blog['category'] if 'category' in blog.keys() else ""
            start_date = blog['start_date'] if 'start_date' in blog.keys() and blog['start_date'] is not None else blog['_created']
            picture_url = blog['picture_url'] if 'picture_url' in blog.keys() else None
            language = blog['theme_settings']['language'] if 'theme_settings' in blog.keys() and 'language' in blog['theme_settings'] else ""
            blogs_collection.replace_one(
                {
                    'marketer._id': marketer['_id'],
                    'marketer_blog_id': blog['_id']
                },
                {
                    'marketer': marketer,
                    'marketer_blog_id': blog['_id'],
                    'title': blog['title'],
                    'description': blog['description'],
                    'public_url': blog['public_url'],
                    'category': category,
                    'start_date': start_date,
                    'picture_url': picture_url,
                    'language': language
                },
                True
            )

        # Delete any blogs not in latest list
        blogs_collection.delete_many({'marketer._id': marketer['_id'], 'marketer_blog_id': {'$nin': blog_ids}})

if __name__ == "__main__":
    manager.run()
