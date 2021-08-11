# web_app/routes/home_routes.py

from flask import Blueprint, request, jsonify, render_template, redirect, flash

from app.artist_recs import fetch_artists

from dotenv import load_dotenv # helps us access .env variables
import os
import spotipy
import random
from spotipy.oauth2 import SpotifyClientCredentials
from pprint import pprint


load_dotenv() 
client_credentials_manager = SpotifyClientCredentials()
client = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
home_routes = Blueprint("home_routes", __name__)

#Initial Artist Form
@home_routes.route("/")
@home_routes.route("/artists")
def artist_form():
    print("HOME...")
    return render_template("music_rec_form.html")

#Confirmation Artist Form
@home_routes.route("/artist/search", methods=["POST"])
def artist_search():

    print("FORM DATA:", dict(request.form))
    request_data = dict(request.form)

    search_term = request_data.get("search_term")
    
    results = fetch_artists(search_term)
    if results: #recycled from weather app
        return render_template("confirm_page.html", results=results)
    else:
        return redirect("/")

#Final Artist Recommendations
@home_routes.route("/artist/confirm", methods=["POST"])
def confirm_search():

    print("FORM DATA:", dict(request.form))
    request_data = dict(request.form)

    mention = request_data.get("matching_artists")  #Pulled from artist_rec.py script upto line 61
    results = fetch_artists(mention) 
    matching_artists = [artist for artist in results if artist["name"] == mention] 
    
    try:
        matching_artist = matching_artists[0] # triggers an IndexError (list index out of range) 
        artists_id = matching_artist["id"]
    except IndexError: 
        print("OOPS - TRY AGAIN") 
        exit() 

    # GETS US NAME WHEN ARTIST ID IS KNOWN
    new_response = client.artist_related_artists(artist_id=artists_id)

    if results: #recycled from weather app
        return render_template("artist_results.html", new_response=new_response)
    else:
        return redirect("/")

