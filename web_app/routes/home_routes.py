# web_app/routes/home_routes.py

from flask import Blueprint, request, jsonify, render_template, redirect, flash

from app.artist_recs import fetch_artists

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
@home_routes.route("/artists")
def artist_form():
    print("HOME...")
    #return "Welcome Home"
    return render_template("music_rec_form.html")

@home_routes.route("/artist/search", methods=["POST"])
def artist_search():

    print("FORM DATA:", dict(request.form))
    request_data = dict(request.form)

    search_term = request_data.get("search_term")
    
    results = fetch_artists(search_term)
    if results:
       # flash("Weather Forecast Generated Successfully!", "success")
        return render_template("confirm_page.html", results=results)
    else:
        #flash("Geography Error. Please try again!", "danger")
        return redirect("/")

@home_routes.route("/artist/confirm", methods=["POST"])
def confirm_search():

    print("FORM DATA:", dict(request.form))
    request_data = dict(request.form)

    matching_artists = request_data.get("matching_artists") 
    
    results = fetch_artists(matching_artists)
    if results:
      # flash("Weather Forecast Generated Successfully!", "success")
         return render_template("artist_results.html", results=results)
    else:
         #flash("Geography Error. Please try again!", "danger")
         return redirect("/")