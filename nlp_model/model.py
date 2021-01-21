import nltk
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
import re

class NLPModel(object):

  def __init__(self):
    self.dt_transformed = dataset[['class', 'tweet']]
    self.tweets = dt_transformed['tweet_wo_RT_username_punct_split']
    self.vectorizer = CountVectorizer(max_features = 2000) 
    self.tweet_text = tweets.values
    self.y = dt_transformed['class'].values
    self.classifier = LogisticRegression()
    self.predict_proba = MultinomialNB()

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
    tweet_list = tweets.explode()
    vectorizer.fit_transform(tweet_list).toarray()
    return tweet_list # I think I return it?

  def train(self, tweet_text, y):
    tweet_text_train, tweet_text_test, y_train, y_test = train_test_split(tweet_text, y, test_size=0.33, random_state=0, stratify=y)
    tweet_text_train = [inner[0] for inner in tweet_text_train]
    tweet_text_test = [inner[0] for inner in tweet_text_test]
    X_train = vectorizer.transform(tweet_text_train)
    X_test  = vectorizer.transform(tweet_text_test)
    return X_train # what do I return here?

# binary classification returns percentage
  def classifier(self, classifier):
    classifier.fit(X_train, y_train)
    score = classifier.score(X_test, y_test)
    return score # TODO : find method for turning decimal into percentage


# the probability of the data instance belonging to each class
# returns the probability of the samples for each class in the model
  def predict_proba(self, X_test):
    score = predict_proba(X_test)
    return score
