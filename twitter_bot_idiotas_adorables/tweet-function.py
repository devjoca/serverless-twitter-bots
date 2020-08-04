import re
import json
import random

with open('./songs.json') as f:
    data = json.load(f)

lyrics = random.choice(data['songs'])['lyrics']
songWithoutBrackets = re.sub(r'\[.*?\]', '', lyrics).split('\n')
lineToTweet = random.choice(
    list(filter(lambda x: x != "", songWithoutBrackets)))
print(lineToTweet)
