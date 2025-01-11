from flask import Flask, render_template, redirect, url_for
from .config import Config
from random import choice, randint
from .tweets import tweets
from app.form.form import TweetForm
from datetime import datetime



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
        new_tweet = {
            "id": len(tweets) + 1,
            "author": form.author.data,
            "tweet": form.tweet.data,
            "date": datetime.now().strftime("%m/%d/%y"),
            "likes": randint(0, 1_000_000),
            "liked": False,
        }
        tweets.append(new_tweet)
        return redirect(url_for("feed"))
    return render_template("new_tweet.html", form=form)

@app.route("/like/<int:tweet_id>", methods=["POST"])
def like(tweet_id):
    # Find the tweet by ID
    tweet = next((t for t in tweets if t["id"] == tweet_id), None)
    if tweet:
        # Toggle the liked status
        tweet["liked"] = not tweet["liked"]
        # Increment or decrement likes based on the liked status
        if tweet["liked"]:
            tweet["likes"] += 1
        else:
            tweet["likes"] -= 1
    return redirect(url_for("feed"))
