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
print("Find yourself at a loss for new music recommendations?")
search_term = input("Enter the name of a musical artist you like: ")
response = client.search(q=search_term, type="artist", limit=20)

artist_list = [] ## not sure if we need this list anymore

print("ARTIST CHOICES:")
for option in response["artists"]["items"]:
    artist_list.append(option)
    print(option["name"]) #would be nice to have list number next to artist so user doesn't have to re-type full name.

###
mention = input("Please type your artist's name exactly as it appears above to confirm which one you were thinking of: ")

# ## TRYING TO ADD ERROR MESSAGE BUT STRUGGLING
# for option in response["artists"]["items"]:
#     if option["name"] == mention:
#         #print("SUCCESS!!")
#         artists_id = option["id"]
        # print(artists_id)
    # else:
    #    print("fail :(")



###
for option in artist_list:
    if option["name"] == mention:
        #print("SUCCESS!!")
        artists_id = option["id"]
        # print(artists_id)
        break


## Come back to this after fixing   
# for option in response["artists"]["items"]:
#     while True:
#         try:
#             # mention = input("enter name again")
#             if mention == option["name"]:
#                 artists_id = option["id"]
#                 print("Correct", artists_id)
#                 break
#             else:
#                 print("not a correct entry")
#                 break
#         except:
#             continue
#         # except NameError:
#         #     print("OOPS")
#         #     break
#         # else:
#         #     print("yay success")

# ### Right now the below is cycling through them one at a time, but not checking for all of them at once
# for option in response["artists"]["items"]:
#     if option["name"] == mention:
#         #print("SUCCESS!!")
#         artists_id = option["id"]
#         # print(artists_id)
#     else:
#        print("fail :(")
    
# print(artists_id)


# GETS US NAME WHEN ARTIST ID IS KNOWN
new_response = client.artist_related_artists(artist_id=artists_id)

print("We think you'll like:")
for a in new_response["artists"]:
    print(a["name"], "|", a["external_urls"]["spotify"],"| Popularity:", a["popularity"]) #Added popularity, need to understand what that is

# print("NEW RESPONSE: ", new_response)
# print(type(new_response)) ## It's a dictionary