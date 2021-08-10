from dotenv import load_dotenv # helps us access .env variables
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from pprint import pprint

load_dotenv() # load environment variables
#print("CLIENT ID:", os.environ.get("SPOTIPY_CLIENT_ID")) # env var used implicitly by the spotipy package
#print("CLIENT SECRET:", os.environ.get("SPOTIPY_CLIENT_SECRET"))  # env var used implicitly by the spotipy package

client_credentials_manager = SpotifyClientCredentials()
client = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# USER SEARCHES FOR ARTIST
search_term = input("Enter the name of a musical artist you like: ")
response = client.search(q=search_term, type="artist", limit=20)

artist_list = [] ## not sure if we need this list anymore

print("ARTIST CHOICES:")
for option in response["artists"]["items"]:
    artist_list.append(option)
    print(option["name"]) #would be nice to have list number next to artist so user doesn't have to re-type full name.

###
# mention = input("Please type your artist's name exactly as it appears above to confirm which one you were thinking of: ")

# ## TRYING TO ADD ERROR MESSAGE BUT STRUGGLING
# for option in response["artists"]["items"]:
#     if option["name"] == mention:
#         #print("SUCCESS!!")
#         artists_id = option["id"]
        # print(artists_id)
    # else:
    #    print("fail :(")


###
# for option in artist_list:
#     if option["name"] == mention:
#         #print("SUCCESS!!")
#         artists_id = option["id"]
#         # print(artists_id)
#         break



### when user enter's a name not in the list > print("WHOOPS")

# something like if artists_id is not defined or is an empty string > do something
# maybe len(artists_id) = 0

# should loop back and allow the user to try inputing a name on the list again

## WHILE VERSION

while True:
    mention = input("choose an artist name")
    matching_artists = [opt for opt in artist_list if opt["name"] == mention]
    try:
        matching_artist = matching_artists[0]
        artists_id = option["id"]
        print(artists_id)
        break
    except KeyError:
        print("OOPS FOUND NO MATCHING ARTIST")
        # pass

# print(matching_artist) # do something with the matching artist
# ### OG OPTION cycles through them one at a time
# for option in response["artists"]["items"]:
#     if option["name"] == mention:
#         #print("SUCCESS!!")
#         artists_id = option["id"]
#         # print(artists_id)
#     else:
#        print("fail :(")


# GETS US NAME WHEN ARTIST ID IS KNOWN
new_response = client.artist_related_artists(artist_id=artists_id)

print("We think you'll like:")
for a in new_response["artists"]:
    print(a["name"], "|", a["external_urls"]["spotify"],"| Popularity:", a["popularity"]) #Added popularity, need to understand what that is

# print("NEW RESPONSE: ", new_response)
# print(type(new_response)) ## It's a dictionary