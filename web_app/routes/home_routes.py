# web_app/routes/home_routes.py

from flask import Blueprint, request, jsonify, render_template, redirect, flash

from app.artist_recs import fetch_artists

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
@home_routes.route("/home")
def index():
    print("HOME...")
    return "Welcome Home"
    #return render_template("home.html")

@home_routes.route("/about")
def about():
    print("ABOUT...")
    return "About Me"
    #return render_template("about.html")