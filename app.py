from flask import Flask, render_template, jsonify, redirect
from flask_pymongo import PyMongo
import scrape_Mars


app = Flask(__name__)


mongo = PyMongo(app)


@app.route('/')
def index():
    surfing = mongo.db.Mars.find_one()
    return render_template('index.html', Mars=Mars)


@app.route('/scrape')
def scrape():
    surfing = mongo.db.Mars
    data = scrape_Mars.scrape()
    surfing.update(
        {},
        data,
        upsert=True
    )
    return redirect("http://localhost:5000/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
