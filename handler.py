import re
import json
import random
import tweepy
import os


def main(data, context):
    with open('./songs.json') as f:
        data = json.load(f)

    lyrics = random.choice(data['songs'])['lyrics']
    songWithoutBrackets = re.sub(r'\[.*?\]', '', lyrics).split('\n')
    lineToTweet = random.choice(
        list(filter(lambda x: x != "", songWithoutBrackets)))

    auth = tweepy.OAuthHandler(os.environ['CONSUMER_KEY'],
                               os.environ['CONSUMER_SECRET'])
    auth.set_access_token(os.environ['ACCESS_KEY'],
                          os.environ['ACCESS_SECRET'])
    api = tweepy.API(auth)
    api.update_status(status=lineToTweet)


if __name__ == "__main__":
    main()