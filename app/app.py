## Step 1: user inputs genre
# need to figure out which genres Spotify recognizes to match
# fail gracefully and prompt user again if they enter a genre it doesn't recognize

## Step 2: comp returns random selection of artists from genre
# randomize artist list from genre

## Step 3: user clicks links to Spotify
# generate link to Spotify artist(s)

import os
from dotenv import load_dotenv

load_dotenv()

clients_id = os.getenv("SPOTIPY_CLIENT_ID")
clients_secret = os.getenv("SPOTIPY_CLIENT_SECRET")

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

import requests
import json

# client_credentials_manager = SpotifyClientCredentials(client_id=clients_id, client_secret=clients_secret)
# sp = spotipy.Spotify(client_credentials_manager)

# urn = "spotify:artist:3jOstUTkEu2JkjvRdBA5Gu"
auth_manager = SpotifyClientCredentials(client_id=clients_id, client_secret=clients_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

# artist = sp.artist(urn)
# print("KEYS:", artist.keys())
# print("ARTIST:", artist)

#### Attempting to access API

# request_url = "https://accounts.spotify.com/authorize"
# requests_url = "https://accounts.spotify.com/api/token"
# response = requests.get(request_url)
# print(type(response))
# print(response.status_code) # the part of http response that lets us know how successful
# print(response.text) # actual body of the response

# print("---------")

# responses = requests.get(requests_url)
# print(type(responses))
# print(responses.status_code) # the part of http response that lets us know how successful
# print(responses.text) # actual body of the response

# shows artist info for a URN or URL

import sys
import pprint
import random

print("~~~~~~~~~~~~~~~~~~~~~~~~~")

if len(sys.argv) > 1:
    search_str = sys.argv[1]
else:
    search_str = input("Please enter a search term: ")
    # search_str = 'Radiohead'
print(type(search_str))

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
result = sp.search(search_str)
pprint.pprint(result)
print(type(result))
print(result.keys())


