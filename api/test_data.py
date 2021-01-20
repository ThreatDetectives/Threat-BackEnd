import twitter

# initialize api instance
twitter_api = twitter.Api(
    consumer_key="YOUR_CONSUMER_KEY",
    consumer_secret="YOUR_CONSUMER_SECRET",
    access_token_key="YOUR_ACCESS_TOKEN_KEY",
    access_token_secret="YOUR_ACCESS_TOKEN_SECRET",
)

# test authentication
print(twitter_api.VerifyCredentials())

# ------------------------------------------------------------------------


def buildTestSet(search_keyword):
    try:
        tweets_fetched = twitter_api.GetSearch(search_keyword, count=100)

        print(
            "Fetched "
            + str(len(tweets_fetched))
            + " tweets for the term "
            + search_keyword
        )

        return [{"text": status.text, "label": None} for status in tweets_fetched]
    except:
        print("Unfortunately, something went wrong..")
        return None


# ------------------------------------------------------------------------

search_term = input("Enter a search keyword: ")
testDataSet = buildTestSet(search_term)

print(testDataSet[0:4])

# ------------------------------------------------------------------------


# corpusFile = "YOUR_FILE_PATH/corpus.csv"
# tweetDataFile = "YOUR_FILE_PATH/tweetDataFile.csv"

# trainingData = buildTrainingSet(corpusFile, tweetDataFile)

# ------------------------------------------------------------------------

import re
from nltk.tokenize import word_tokenize
from string import punctuation
from nltk.corpus import stopwords


class PreProcessTweets:
    def __init__(self):
        self._stopwords = set(
            stopwords.words("english") + list(punctuation) + ["AT_USER", "URL"]
        )

    def processTweets(self, list_of_tweets):
        processedTweets = []
        for tweet in list_of_tweets:
            processedTweets.append((self._processTweet(tweet["text"]), tweet["label"]))
        return processedTweets

    def _processTweet(self, tweet):
        tweet = tweet.lower()  # convert text to lower-case
        tweet = re.sub("((www\.[^\s]+)|(https?://[^\s]+))", "URL", tweet)  # remove URLs
        tweet = re.sub("@[^\s]+", "AT_USER", tweet)  # remove usernames
        tweet = re.sub(r"#([^\s]+)", r"\1", tweet)  # remove the # in #hashtag
        tweet = word_tokenize(
            tweet
        )  # remove repeated characters (helloooooooo into hello)
        return [word for word in tweet if word not in self._stopwords]


tweetProcessor = PreProcessTweets()
preprocessedTrainingSet = tweetProcessor.processTweets(trainingData)
preprocessedTestSet = tweetProcessor.processTweets(testDataSet)

# ------------------------------------------------------------------------

import nltk


def buildVocabulary(preprocessedTrainingData):
    all_words = []

    for (words, sentiment) in preprocessedTrainingData:
        all_words.extend(words)

    wordlist = nltk.FreqDist(all_words)
    word_features = wordlist.keys()

    return word_features


# ------------------------------------------------------------------------


def extract_features(tweet):
    tweet_words = set(tweet)
    features = {}
    for word in word_features:
        features["contains(%s)" % word] = word in tweet_words
    return features


# ------------------------------------------------------------------------

# Now we can extract the features and train the classifier
word_features = buildVocabulary(preprocessedTrainingSet)
trainingFeatures = nltk.classify.apply_features(
    extract_features, preprocessedTrainingSet
)

# ------------------------------------------------------------------------

NBayesClassifier = nltk.NaiveBayesClassifier.train(trainingFeatures)

# ------------------------------------------------------------------------

NBResultLabels = [
    NBayesClassifier.classify(extract_features(tweet[0]))
    for tweet in preprocessedTestSet
]

# ------------------------------------------------------------------------

# get the majority vote
if NBResultLabels.count("positive") > NBResultLabels.count("negative"):
    print("Overall Positive Sentiment")
    print(
        "Positive Sentiment Percentage = "
        + str(100 * NBResultLabels.count("positive") / len(NBResultLabels))
        + "%"
    )
else:
    print("Overall Negative Sentiment")
    print(
        "Negative Sentiment Percentage = "
        + str(100 * NBResultLabels.count("negative") / len(NBResultLabels))
        + "%"
    )
