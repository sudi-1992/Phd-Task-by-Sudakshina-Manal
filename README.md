<h3> <u><b>For twitter Streaming </b><u/> </h3>
<p>
  Twitter supports a very easy to use API library named TWEEPY for python <p>
  To install tweepy, follow the step: <p><br>
  1. Goto command promt<p>
  2. Write the command <font color ="blue"><b>"pip install tweepy"</b></font><p>
  3.import tweepy <p>
  <br>
  <p>  
 MongoDB is used here to save the collected tweets.Around 10000 tweets collected here in <b>twitter.txt</b> file.<p>
beforing going to stream data ,an application is need to be created in <b>developer.twitter.com</b>.Initialize access token and        consumer key in the codebase for streaming tweets.
      
          access_token=""
          access_token_secret=""
          consumer_key=""
          consumer_secret=""
 

Initiate a MongoDb instance to collect data .

            client = MongoClient()
            db = client.tweetPython_db
            tweet_collection = db.tweet_collection
            tweet_collection.create_index([("id", pymongo.ASCENDING)],unique = True) # make sure the collected tweets are unique
            
 filters are applied for a specific search .
 
             stream.filter(track=['salesforce','javascript','python'])
             
<h3> <u><b>For twitter Parsing </b><u/> </h3>

collected tweets are analysed are from <b> twitter.txt</b> in a json format.

              import json
To analyse tweets and plot it in a graph we uses following libraries: 
<i>Pandas,Matplotlib,Pylib</i>

To print total number of tweets following line is used.

            print (len(tweets_data))
Tweets are mapped accoring to their named entities i.e text,lang,country.

<br>
 To show the total tweets in a bargraph we used :

        tweets_by_country = tweets['country'].value_counts()

        fig, ax = plt.subplots()
        ax.tick_params(axis='x', labelsize=15)
        ax.tick_params(axis='y', labelsize=10)
        ax.set_xlabel('Countries', fontsize=15)
        ax.set_ylabel('Number of tweets' , fontsize=15)
        ax.set_title('Top 5 countries', fontsize=15, fontweight='bold')
        tweets_by_country[:5].plot(ax=ax, kind='bar', color='blue')
        plt.show()
        
 <h3>Sentiment Analysis on twitter data </h3>
    
  For natural language processing (NLP) textblob  is used :
  
          from textblob import TextBlob
          
 Here, sentiment analysis is performed based on some query : 
 Example: 
 
            searchTerm = input("enter keyword/hashtag to search about:") : <i>IPL</i>
            noOfSearchTerms = int(input("enter how many tweets to analyze:"))<i> 00</i>
            
Sentiment analysis are performed based on positive,negetive,neutral tweets.<p>
A pie chart will be plotted to present a trend of tweets:<p>
  
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
        
        
        
 <H3> NewsAPI News Collection </h3>
 
  Aylien NEWSAPI used here to collects news from various sources.Following libraries are necessry for collecting news using NEWSAPI <p>
          
          import aylien_news_api
          from aylien_news_api.rest import ApiException
          
MongoDb is used as a database to store collected news.For this a new client instance of MongoDB is initiated.<p>
To configure the api ,a application is need to be created first to access news from Aylien: 
  
          aylien_news_api.configuration.api_key['X-AYLIEN-NewsAPI-Application-ID'] = ''
          # Configure API key authorization: app_key
          aylien_news_api.configuration.api_key['X-AYLIEN-NewsAPI-Application-Key'] = ''
          
 Search criteria is given is following code snippet to retrieve news in different languages:
 
            text = '"JAVASCRIPT" AND "PYTHON"'
            language = ['es','fr']
            since = 'NOW-1000DAYS'
            until = 'NOW'

<h3>Live news Streaming </h3>
Live news are streamed here. <p>
Search criteria can be following to retrieve perticular filter based news:
  
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
  
  News will be printed in the following manner: <p>

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
At the time of running this perticular  script in python power shell following command is used to store the streamed news in a text file.<p>
    <b> project path>> python live_news_streaming.py > news.text <b/>
      
MongoDb is used as usual like previous scripts as a database. <p>
  <br>

  
  <h3>Sentiment analysis on News </h3>
  
 In this script file news are analyzed according to sentiment based filter.
 
      text = 'trump'
      country = ['MX']
      sentiment = 'negative'
      since = 'NOW-100DAYS'
      until = 'NOW'
Results printed in console in json format according to their sentiment stated above. <p>
  
 <p>
  <p>
  <h2>NOTE:</h2>
  <p>
  **I did not find any satisfactory source to plot the sentiments in a graph for collected news<p>
  **Tried a lot in different news api library like graphapi for facebook, newsapi for google news etc.<p>
  ** Due to non availability of resourses in news api  I could not fetched news in csv or text file during this short period of time.<p>
  
  ********************************************************************************************************













        

     
