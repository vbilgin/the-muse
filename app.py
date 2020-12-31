import os
import requests
import json
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

client = WebClient(token=os.environ.get('SLACK_BOT_TOKEN'))
channel_id = 'C01H85G2VV5'

# Get a random poem from PoetryDB and convert the output to JSON that's readable by Python.
def get_rand_poem():
  res = requests.get('https://poetrydb.org/random')
  poem = json.loads(res.text)
  return poem[0]

try:
    poem = get_rand_poem()
    poem_title = poem['title']
    poem_author = poem['author']
    poem_text = ''

    for line in poem['lines']:
      poem_text = poem_text + line + '\n'

    result = client.chat_postMessage(
        channel= channel_id, 
        text= f'*Title*: {poem_title}\n*Author*: {poem_author}\n\n {poem_text}'
    )

except SlackApiError as e:
    logger.error(f"Error posting message: {e}")