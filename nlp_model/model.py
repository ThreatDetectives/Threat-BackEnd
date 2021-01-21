import nltk
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
import re
import pickle


class NLPModel(object):

  def __init__(self):
    self.vectorizer = CountVectorizer(max_features = 2000) 
    self.classifier = LogisticRegression()
    self.class_prediction = MultinomialNB()


  def remove_RT_user(self, text):
    tweet = re.sub("@[^\s]+", "", text)
    hashtag = re.sub("#[\w|\d]+", "", tweet)
    remove_http = re.sub("(https?[a-zA-Z0-9]+)|(http?[a-zA-Z0-9]+)", "", hashtag)
    no_rt = re.sub("RT", "", remove_http)
    return no_rt

  def remove_punctuation(self, text):
    no_punct=[words for words in text if words not in string.punctuation]
    words_wo_punct=''.join(no_punct)
    return words_wo_punct

  def tokenize(self, text):
    split = re.split("\W+", text)
    return split

  def vectorizer_fit_transform_toarray(self, tweets):
    # tweet_list = tweets.explode()
    # return tweet_list # I think I return it?
    return vectorizer.fit_transform(tweet_list).toarray()

  def train(self, tweet_text, y):
    # tweet_text_train, tweet_text_test, y_train, y_test = train_test_split(tweet_text, y, test_size=0.33, random_state=0, stratify=y)
    tweet_text_train = [inner[0] for inner in tweet_text_train]
    tweet_text_test = [inner[0] for inner in tweet_text_test]
    X_train = vectorizer.transform(tweet_text_train)
    X_test  = vectorizer.transform(tweet_text_test)
    return classifier.fit(X_train, y_train) # what do I return here?

# binary classification returns percentage
  def detector(self, X_train, y_train):
    score = classifier.score(X_test, y_test)
    print("Threat Detected:", str(round(score * 100)) + "%")


# the probability of the data instance belonging to each class
# returns the probability of the samples for each class in the model
  def predict_proba(self, X_test):
    score = class_prediction.predict_proba(X_test)
    return score
