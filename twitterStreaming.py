from tweepy.streaming import StreamListener
import pymongo
from pymongo import MongoClient
from tweepy import OAuthHandler
from tweepy import Stream
import time


access_token="1512880592-HWIU2og8OE7PsaW5zTYh9oW9SrVH65sOWUHx6S3"
access_token_secret="e6dNnCe7rS9bPo70VenQJCY0TOfQetFQbHCocBR7duolr"
consumer_key="1i1jREIxqSZQiYtL0Z5yk8gne"
consumer_secret="7hQAdZ5hpfyxptfMOcPkM9GX756O710Lcl8tgP5RxdAGA9v5Ob"


client = MongoClient()
db = client.tweetPython_db
tweet_collection = db.tweet_collection
tweet_collection.create_index([("id", pymongo.ASCENDING)],unique = True) # make sure the collected tweets are unique


class StdOutListener(StreamListener):

    def on_data(self, data):
        try:
            print (data)
            savefile=open("d://twitter.txt","a")
            savefile.write(data)
            savefile.write("\n")
            savefile.close()
            return True

        except BaseException (e):
            print('Failed on Data',str(e))
            time.sleep(5)

            def on_error(self,status):
                print(status)


if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    stream.filter(track=['salesforce','javascript','python'])

