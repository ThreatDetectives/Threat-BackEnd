from django.http import JsonResponse
from .tweet_dumper import get_all_tweets
import numpy as np
import nltk
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import re
import pickle
import string
import json
from collections import Counter
from django.views.decorators.csrf import csrf_exempt
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


class NLPModel(object):
    def __init__(self):
        # open pickled vectorizer
        vectorizer_path = BASE_DIR / "vectorizer_pickle.pkl"
        with open(vectorizer_path, "rb") as file:
            self.vectorizer = pickle.load(file)

        # import and open pickled model
        classifier_path = BASE_DIR / "finalized_model.pkl"
        with open(classifier_path, "rb") as file:
            self.classifier = pickle.load(file)

    def remove_RT_user(self, text):
        tweet = re.sub("@[^\s]+", "", text)
        hashtag = re.sub("#[\w|\d]+", "", tweet)
        remove_http = re.sub("(https?[a-zA-Z0-9]+)|(http?[a-zA-Z0-9]+)", "", hashtag)
        no_rt = re.sub("RT", "", remove_http)
        return no_rt

    def remove_punctuation(self, text):
        no_punct = [words for words in text if words not in string.punctuation]
        words_wo_punct = "".join(no_punct)
        return words_wo_punct

    def tokenize(self, text):
        split = re.split("\W+", text)
        return split

    def vectorizer_transform_toarray(self, tweets):
        tweet_list = tweets.explode()
        tweet_list = self.vectorizer.transform(tweet_list).toarray()
        return tweet_list

    def detector(self, tweet_list):
        predictions = self.classifier.predict(tweet_list)
        predic_list = list(predictions)
        length = len(predic_list)
        frequencies = Counter(predic_list)
        hate_speech = frequencies[0] / length
        offensive_language = frequencies[1] / length
        neither = frequencies[2] / length
        return (
            "Threatening : ",
            # TODO will need to update the line below with threatening speech numbers after new data has been applied
            str(round(hate_speech * 100)) + "%",
            "Conspiracy Theory : ",
            # TODO will need to update the line below with conspiracy theory speech numbers after new data has been applied
            str(round(hate_speech * 100)) + "%",
            "Hate Speech : ",
            str(round(hate_speech * 100)) + "%",
            "Offensive Language : ",
            str(round(offensive_language * 100)) + "%",
            "Neither : ",
            str(round(neither * 100)) + "%",
        )

# next step is to replace culk with data from a post
# request.POST['name_of_user']
@csrf_exempt
def data_view(request):
    # get the user name from the request object
    twitterhandle = json.loads(request.body)["twitterHandle"]
    # return JsonResponse({"result" : twitterhandle})
    get_all_tweets(twitterhandle)
    # get_all_tweets("hexx_king") # hard coded for testing only
    dataset = pd.read_csv("./temp.csv", encoding="ISO-8859-1")

    # we have a CSV with all tweets in it
    model = NLPModel()
    dataset["text"] = dataset["text"].apply(lambda x: model.remove_RT_user(x))

    dataset["text"] = dataset["text"].apply(lambda x: model.remove_punctuation(x))
    dataset["text"] = dataset["text"].apply(lambda x: model.tokenize(x))
    tweet_list = model.vectorizer_transform_toarray(dataset["text"])
    prediction = model.detector(tweet_list)
    # json_prediction = json.dumps(str(list(prediction)))
    return JsonResponse({"ThreatReport": prediction})
    # print(dataset)
    # return JsonResponse({"result": twitterhandle})
