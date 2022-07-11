
# to use Flask and MongoDB
from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scraping

# setup flask
app = Flask(__name__)


# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)


# route for the html page
@app.route("/")
def index():
   mars = mongo.db.mars.find_one()
   return render_template("index.html", mars=mars)

# route for scraping data
@app.route("/scrape")
def scrape():
   mars = mongo.db.mars
   mars_data = scraping.scrape_all()
   mars.update_one({}, {"$set":mars_data}, upsert=True)
   return redirect('/', code=302)


# run the app
if __name__ == "__main__":
   app.run()