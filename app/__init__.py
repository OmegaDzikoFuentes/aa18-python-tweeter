from flask import Flask, render_template, redirect, url_for
from .config import Config
from random import choice
from .tweets import tweets
from app.form.form import TweetForm



app = Flask(__name__)
app.config.from_object(Config)

@app.route("/")
def index():
    random_tweet = choice(tweets)
    return render_template("index.html", tweet=random_tweet)

@app.route("/feed")
def feed():
    return render_template("feed.html", tweets=tweets)

@app.route("/new", methods=["GET", "POST"])
def new():
    form = TweetForm()
    if form.validate_on_submit():
        author = form.author.data
        tweet = form.tweet.data
        return redirect(url_for("home"))
    return render_template("new_tweet.html", form=form)
