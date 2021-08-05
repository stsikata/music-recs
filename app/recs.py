# adapted from: https://github.com/s2t2/my-spotify-app-py/blob/master/list_songs.py
# and adapted from: https://github.com/prof-rossetti/intro-to-python/blob/main/notes/python/packages/spotipy.md#basic-usage 

from dotenv import load_dotenv
import os

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

load_dotenv() # load environment variables

print("CLIENT ID:", os.environ.get("SPOTIPY_CLIENT_ID")) # env var used implicitly by the spotipy package
print("CLIENT SECRET:", os.environ.get("SPOTIPY_CLIENT_SECRET"))  # env var used implicitly by the spotipy package

# FYI, this client configuration approach expects / implicitly uses env vars named SPOTIPY_CLIENT_ID and SPOTIPY_CLIENT_SECRET
client_credentials_manager = SpotifyClientCredentials()
client = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# response = client.search(q="Springsteen on Broadway", limit=20)
search_term = input("please enter input: ")
response = client.search(q=search_term, type="artist", limit=20)

# breakpoint()

for i, track in enumerate(response['artists']['items']):
    print(' ', i, track['name'])

# for i, track in enumerate(response['tracks']['items']):
#     print(' ', i, track['name'])

