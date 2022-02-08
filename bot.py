import tweepy


bearer_token="AAAAAAAAAAAAAAAAAAAAADoGZAEAAAAAybO1ZWhnLw2UQzeC4lFOVc%2BgsCM%3DYpAPbUNXsvIhBDDpkfFdAgTaZYxypa7pElWod7EsTm56GBhV0z"

consumer_key="AgvXckpRgsh3dluTHQKOpj8XU"
consumer_secret="Lg3IkJ89RHm3Jt7KS0WQmoLDmIQ3Fi3eCGfioWbl58vQGbRXs3"

access_token="1019176655787642888-36xAxO11OO6OUyl3hcSZFNSL3afB8E"
access_token_secret="5o6m4rpQq1garJG51xh79Ak6nKWpAu3Rt3Nxi0UFPsC6N"

# Authenticate to Twitter
client = tweepy.Client( bearer_token=bearer_token, 
                        consumer_key=consumer_key, 
                        consumer_secret=consumer_secret, 
                        access_token=access_token, 
                        access_token_secret=access_token_secret,
                       )
# response = client.get_user(username="mtdcncnetwork")
# print(response)

swarf = client.get_users_tweets(id="1048148217941123072", exclude="retweets")

swarf_tweets = swarf.data

for tweet in swarf_tweets:
    id = tweet.id
    print(tweet)

data = client.retweet(tweet_id=id)
retweets = swarf.data
print(retweets)

mtdcnc = client.get_users_tweets(id="90405805", exclude="retweets")

mtdcnc_tweets = mtdcnc.data

for tweet in mtdcnc_tweets:
    id = tweet.id
    print(id)

data = client.retweet(tweet_id=id)
retweets = mtdcnc.data
print(retweets)

network = client.get_users_tweets(id="3361002273", exclude="retweets")

network_tweets = network.data

for tweet in network_tweets:
    id = tweet.id
    print(id)

data = client.retweet(tweet_id=id)
retweets = network.data
print(retweets)

