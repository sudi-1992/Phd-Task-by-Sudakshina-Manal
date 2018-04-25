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



        

     
