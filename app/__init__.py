from flask import Flask, render_template
from .config import Config
from random import choice
from .tweets import tweets



app = Flask(__name__)
app.config.from_object(Config)

@app.route("/")
def index():
    random_tweet = choice(tweets)
    return render_template("index.html", tweet=random_tweet)

@app.route("/feed")
def feed():
    return render_template("feed.html", tweets=tweets)
