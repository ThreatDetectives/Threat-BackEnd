from searchtweets import collect_results, load_credentials, gen_request_parameters

search_args = load_credentials(
    ".twitter_keys.yaml", yaml_key="search_tweets_v2", env_overwrite=False
)
print(search_args)
query = gen_request_parameters("kill", results_per_call=100)
print(query)
tweets = collect_results(query, max_tweets=100, result_stream_args=search_args)
[print(tweet["text"], end="\n\n") for tweet in tweets[0:10]]
