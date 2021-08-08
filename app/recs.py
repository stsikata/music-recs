# adapted from: https://github.com/s2t2/my-spotify-app-py/blob/master/list_songs.py
# and adapted from: https://github.com/prof-rossetti/intro-to-python/blob/main/notes/python/packages/spotipy.md#basic-usage 

from dotenv import load_dotenv # helps us access .env variables
import os

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

from pprint import pprint

load_dotenv() # load environment variables

print("CLIENT ID:", os.environ.get("SPOTIPY_CLIENT_ID")) # env var used implicitly by the spotipy package
print("CLIENT SECRET:", os.environ.get("SPOTIPY_CLIENT_SECRET"))  # env var used implicitly by the spotipy package

# FYI, this client configuration approach expects / implicitly uses env vars named SPOTIPY_CLIENT_ID and SPOTIPY_CLIENT_SECRET
client_credentials_manager = SpotifyClientCredentials()
client = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# response = client.search(q="Springsteen on Broadway", limit=20)
search_term = input("please enter input: ")
response = client.search(q=search_term, type="track", limit=20)

pprint(response)
exit()

#genre_artist = response["genres"]
#print(genre_artist)
# breakpoint()

# for i, track in enumerate(response['artists']['items']):
#     print(' ', i, track['name'])

# pprint(response)

# exit()

for i, track in enumerate(response['tracks']['items']):
    print(' ', i, track['name'])

print(type(response))