from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_costa

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/weather_app")

#INSTRUCTIONS: * In `app.py`, complete the `/scrape` route to store
#  the Python dictionary as a document in a mongo database collection.
#* In `app.py`, complete the `/` route to read one entry from mongo 
#  and render the flask template with the mongo data.

# Route to render index.html template using data from Mongo
@app.route("/")
def home():
    # PREVIOUS EXAMPLE:
    #listings = mongo.db.listings.find_one()
    #return render_template("index.html", listings=listings)

    # Find one record of data from the mongo database
    # @TODO: YOUR CODE HERE!
    destination_data = mongo.db.collection.find_one()

    # Return template and data
    return render_template("index.html", vacation=destination_data)

# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():
    # PREVIOUS EXAMPLE:
    # listings = mongo.db.listings
    # listings_data = scrape_costa.scrape()
    # listings.update({}, listings_data, upsert=True)
    # return redirect("/", code=302)

    # Run the scrape function and save the results to a variable
    # @TODO: YOUR CODE HERE!
    costa_data = scrape_costa.scrape_info()

    # Update the Mongo database using update and upsert=True
    # @TODO: YOUR CODE HERE!
    mongo.db.collection.update_one({}, {"$set": costa_data}, upsert=True)
    # Redirect back to home page
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
