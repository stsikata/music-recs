from dotenv import load_dotenv # helps us access .env variables
import os
import spotipy
import random
from spotipy.oauth2 import SpotifyClientCredentials
from pprint import pprint

load_dotenv() # load environment variables
#print("CLIENT ID:", os.environ.get("SPOTIPY_CLIENT_ID")) # env var used implicitly by the spotipy package
#print("CLIENT SECRET:", os.environ.get("SPOTIPY_CLIENT_SECRET"))  # env var used implicitly by the spotipy package

client_credentials_manager = SpotifyClientCredentials()
client = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def fetch_artists(search_term):
    response = client.search(q=search_term, type="artist", limit=20)
    return response["artists"]["items"]
        


# Main conditional, can be indented
if __name__ == "__main__":
   

    # USER SEARCHES FOR ARTIST
    search_term = input("Please enter the name of a musical artist you like: ")

    results = fetch_artists(search_term)


    # artist_list = []

    print("ARTIST CHOICES:")
    for artist_options in results:
      #  print(artist_options["name"]) #would be nice to have list number next to artist so user doesn't have to re-type full name.
        print(artist_options)  
    mention = input("Please type to confirm the name of the artist you were thinking of: ")


    matching_artists = [artist for artist in results if artist["name"] == mention]

    try:
        matching_artist = matching_artists[0] # triggers an IndexError (list index out of range)
        artists_id = matching_artist["id"]
    except IndexError:
        print("OOPS - TRY AGAIN")
        exit()



    # GETS US NAME WHEN ARTIST ID IS KNOWN
    new_response = client.artist_related_artists(artist_id=artists_id)
    # response = client.artist_related_artists(artist_id="66CXWjxzNUsdJxJ2JdwvnR")
    # pprint(new_response)
    print("These are your artist recommendations:")
    for a in new_response["artists"]:

        print(a["name"], ":", a["external_urls"]["spotify"],"Popularity:", a["popularity"]) #Added popularity, need to understand what that is