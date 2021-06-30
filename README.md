# Threat-BackEnd

This repo is to contain the scraper and API calls, hold a copy of the trained model, and the logic for processing the threat percentage.

# How to test API with HTTPie in the Command Line
- run `$ http POST 127.0.0.1:8000/ APIKEY=OOpyDDYsqOympOP96qUpBV2aA twitterHandle=hexx_king`
- HTTPie takes the HTTP request, the URL, the APIKEY, and the twitter user's screen name

# Resources
- tweet dumper reference code from https://gist.github.com/yanofsky/5436496 all credit goes to yanofsky
- [Deploying a Machine Learning Model as a REST API](https://towardsdatascience.com/deploying-a-machine-learning-model-as-a-rest-api-4a03b865c166)
- [How to Make Predictions with scikit-learn](https://machinelearningmastery.com/make-predictions-scikit-learn/)
- [Deploy Machine Learning Models with Django](https://www.deploymachinelearning.com/)
