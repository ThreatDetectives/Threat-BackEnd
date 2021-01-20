import pandas as pd
import urllib
import json                 # Used to load data into JSON format
from pprint import pprint   # pretty-print

# df = pd.read_json(r)
# df.to_csv("output.csv")


url = "https://api.twitter.com/2/tweets/search/recent"
response = urllib.request.urlopen(url)
print(response)
