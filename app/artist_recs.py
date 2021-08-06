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
#  search_term = input("please enter input: ")

# # GETS US NAME WHEN ARTIST ID IS KNOWN
# response = client.artist_related_artists(artist_id="6nfN5B7Jmi853SHa9106Hz")
# pprint(response)
# for a in response["artists"]:
#     print(a["name"], ":", a["external_urls"]["spotify"])


# breakpoint()

# for i, track in enumerate(response['artists']['items']):
#     print(' ', i, track['name'])

# pprint(response)

# for i, track in enumerate(response['tracks']['items']):
#     print(' ', i, track['name'])

# print(type(response))