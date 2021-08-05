
import os
from dotenv import load_dotenv

load_dotenv()

clients_id = os.getenv("SPOTIPY_CLIENT_ID")
clients_secret = os.getenv("SPOTIPY_CLIENT_SECRET")

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# client_credentials_manager = SpotifyClientCredentials(client_id=clients_id, client_secret=clients_secret)
# sp = spotipy.Spotify(client_credentials_manager)

auth_manager = SpotifyClientCredentials(client_id=clients_id, client_secret=clients_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

playlists = sp.user_playlists('spotify')
while playlists:
    for i, playlist in enumerate(playlists['items']):
        print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
    if playlists['next']:
        playlists = sp.next(playlists)
    else:
        playlists = None

# artist_name = []
# track_name = []
# popularity = []
# track_id = []
# for i in range(0,10000,50):
#     track_results = sp.search(q='year:2018', type='track', limit=50,offset=i)
#     for i, t in enumerate(track_results['tracks']['items']):
#         artist_name.append(t['artists'][0]['name'])
#         track_name.append(t['name'])
#         track_id.append(t['id'])
#         popularity.append(t['popularity'])

# import pandas as pd
# track_dataframe = pd.DataFrame({'artist_name' : artist_name, 'track_name' : track_name, 'track_id' : track_id, 'popularity' : popularity})
# print(track_dataframe.shape)
# track_dataframe.head()