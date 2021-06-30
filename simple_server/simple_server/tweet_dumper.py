import tweepy
import csv
from decouple import config
import os

# Twitter API credentials
consumer_key = config("APIKEY")
consumer_secret = config("APISECRET")
access_key = ""
access_secret = ""


def get_all_tweets(screen_name):
    # Twitter only allows access to a users most recent 3240 tweets with this method

    # authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    # initialize a list to hold all the tweepy Tweets
    alltweets = []

    # make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name=screen_name, count=200)

    # save most recent tweets
    alltweets.extend(new_tweets)

    # save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1

    # keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        # print(f'getting tweets before {oldest}')

        # all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(
            screen_name=screen_name, count=200, max_id=oldest
        )

        # save most recent tweets
        alltweets.extend(new_tweets)

        # update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1

        # print(f"...{len(alltweets)} tweets downloaded so far")

    # transform the tweepy tweets into a 2D array that will populate the csv
    outtweets = [[tweet.text] for tweet in alltweets]

    # write the csv
    with open("temp.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(["text"])
        writer.writerows(outtweets)

    with open("temp.csv", "r") as f:
        content = f.readlines()
    return len(content)


if __name__ == "__main__":
    # pass in the username of the account you want to download
    get_all_tweets("vgdunkey")
