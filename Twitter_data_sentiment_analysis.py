from textblob import TextBlob
import sys
from tweepy import OAuthHandler
import matplotlib.pyplot as plt
import tweepy

def percentage(part,whole):
    return 100 * float(part)/float(whole)


access_token="1512880592-HWIU2og8OE7PsaW5zTYh9oW9SrVH65sOWUHx6S3"
access_token_secret="e6dNnCe7rS9bPo70VenQJCY0TOfQetFQbHCocBR7duolr"
consumer_key="1i1jREIxqSZQiYtL0Z5yk8gne"
consumer_secret="7hQAdZ5hpfyxptfMOcPkM9GX756O710Lcl8tgP5RxdAGA9v5Ob"


auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api =  tweepy.API(auth)

searchTerm = input("enter keyword/hashtag to search about:")
noOfSearchTerms = int(input("enter how many tweets to analyze:"))

tweets = tweepy.Cursor(api.search, q=searchTerm ,lang="English").items(noOfSearchTerms)



positive = 0
negetive = 0
neutral = 0
polarity = 0


for tweets in tweets:
       foo = tweets.text.encode('utf-8').strip()
       print(foo)
       analysis = TextBlob(tweets.text)
       polarity += analysis.sentiment.polarity

       if(analysis.sentiment.polarity == 0):
            neutral += 1
       elif (analysis.sentiment.polarity < 0.00):
            negetive += 1

       elif (analysis.sentiment.polarity > 0.00):
            positive += 1


positive = percentage(positive ,noOfSearchTerms)
negetive = percentage(negetive ,noOfSearchTerms)
neutral = percentage(neutral ,noOfSearchTerms)

positive = format(positive , '2f')
negetive = format(negetive , '2f')
neutral = format(neutral , '2f')

print("How people are reacting " + searchTerm + " by analyzing " + str(noOfSearchTerms) + " Tweets.")

if (polarity == 0):
 print("Neutral")
elif (polarity < 0):
 print("negetive")
elif (polarity > 0):
 print("positive")

labels = ['Positive ['+str(positive)+'%]' , 'Neutral [' +str(neutral) +'%]' ,'Negetive ['+str(negetive)+'%] ']
sizes = [positive,neutral,negetive]
colors = ['yellowgreen','gold' , 'red']
patches, texts = plt.pie(sizes,colors=colors, startangle = 90)
plt.legend(patches, labels, loc = "best")
plt.title('how are you reacting on '+searchTerm+' by analyzing '+str(noOfSearchTerms)+' Tweets.')
plt.axis('equal')
plt.tight_layout()
plt.show()









