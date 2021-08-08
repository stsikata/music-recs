from dotenv import load_dotenv # helps us access .env variables
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from pprint import pprint

load_dotenv() # load environment variables
print("CLIENT ID:", os.environ.get("SPOTIPY_CLIENT_ID")) # env var used implicitly by the spotipy package
print("CLIENT SECRET:", os.environ.get("SPOTIPY_CLIENT_SECRET"))  # env var used implicitly by the spotipy package

client_credentials_manager = SpotifyClientCredentials()
client = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# USER SEARCHES FOR ARTIST
search_term = input("Please enter the name of a musical artist you like: ")
response = client.search(q=search_term, type="artist", limit=20)

artist_list = []

print("ARTIST CHOICES:")
for artist_options in response["artists"]["items"]:
    artist_list.append(artist_options)
    print(artist_options["name"])

mention = input("Please type to confirm the name of the artist you were thinking of: ")

### Right now the below is cycling through them one at a time, but not checking for all of them
for artist_options in response["artists"]["items"]:
    if artist_options["name"] == mention:
        # print("SUCCESS!!")
        artists_id = artist_options["id"] ## need it to take the artist id
        print(artists_id)
    # else:
    #     print("fail :(")

# print(type(artists_id))


# GETS US NAME WHEN ARTIST ID IS KNOWN

new_response = client.artist_related_artists(artist_id=artists_id)
# response = client.artist_related_artists(artist_id="66CXWjxzNUsdJxJ2JdwvnR")
# pprint(new_response)
print("These are your artist recommendations:")
for a in new_response["artists"]:
    print(a["name"], ":", a["external_urls"]["spotify"])


# breakpoint()

# for i, track in enumerate(response['artists']['items']):
#     print(' ', i, track['name'])

# pprint(response)

# for i, track in enumerate(response['tracks']['items']):
#     print(' ', i, track['name'])

# print(type(response))