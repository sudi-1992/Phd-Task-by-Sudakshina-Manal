import time
import datetime
import aylien_news_api
from aylien_news_api.rest import ApiException
import pymongo
from pymongo import MongoClient

def fetch_new_stories(params={}):
  print('------------')
  
  fetched_stories = []
  stories = None
  
  while stories is None or len(stories) > 0:
    try:
      response = api_instance.list_stories(**params)
    except ApiException as e:
      if ( e.status == 429 ):
        print('Usage limit are exceeded. Wating for 5 seconds...')
        time.sleep(5)
        continue
        
    stories = response.stories
    params['cursor'] = response.next_page_cursor
    
    fetched_stories += stories
    print("Fetched %d stories. Total story count so far: %d" %
      (len(stories), len(fetched_stories)))
     
  return fetched_stories


# Configure API key authorization: app_id
aylien_news_api.configuration.api_key['X-AYLIEN-NewsAPI-Application-ID'] = 'e1ef64f9'
# Configure API key authorization: app_key
aylien_news_api.configuration.api_key['X-AYLIEN-NewsAPI-Application-Key'] = 'b83ce8b5ed0fca4d5f71c6fc474ff43c'

client = MongoClient()
db = client.newsstream_db
tweet_collection = db.tweet_collection
tweet_collection.create_index([("id", pymongo.ASCENDING)],unique = True) # make sure the collected tweets are unique

# create an instance of the API class
api_instance = aylien_news_api.DefaultApi()

params = {
  'title': 'Apple OR Amazon OR Facebook OR PayPal OR Microsoft OR Ebay OR Cisco OR Netflix OR IBM',
  'language': ['en','fr','de'],
  'published_at_start': 'NOW-24HOUR',
  'published_at_end': 'NOW',
  'cursor': '*',
  'per_page': 5,
  'sort_by': 'published_at',
  'sort_direction': 'desc'
}

while True:
  stories = fetch_new_stories(params)
  
  print('************')
  print("Fetched %d stories which were published between %s and %s" %
    (len(stories), params['published_at_start'], params['published_at_end']))
  
  if len(stories) > 0:
    last_fetched_at = stories[0].published_at + datetime.timedelta(seconds=1)
    params['published_at_start'] = last_fetched_at.isoformat()[:-6] + 'Z'
    params['cursor'] = '*'
    
  print('Sleep for 5 seconds until next poll...')
  print('------------')
  time.sleep(5)

  
                
