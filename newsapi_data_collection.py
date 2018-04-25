import aylien_news_api
from aylien_news_api.rest import ApiException
import pymongo
from pymongo import MongoClient

# Configure API key authorization: app_id
aylien_news_api.configuration.api_key['X-AYLIEN-NewsAPI-Application-ID'] = 'e1ef64f9'
# Configure API key authorization: app_key
aylien_news_api.configuration.api_key['X-AYLIEN-NewsAPI-Application-Key'] = 'b83ce8b5ed0fca4d5f71c6fc474ff43c'

# create an instance of the API class
api_instance = aylien_news_api.DefaultApi()

text = '"JAVASCRIPT" AND "PYTHON"'
language = ['es','fr']
since = 'NOW-1000DAYS'
until = 'NOW'

client = MongoClient()
db = client.news_db
news_collection = db.news_collection
news_collection.create_index([("id", pymongo.ASCENDING)],unique = True) # make sure the collected tweets are unique

try:
    # List stories
    api_response = api_instance.list_stories(text=text, language=language, published_at_start=since, published_at_end=until)
    print(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_stories: %s\n" % e)


