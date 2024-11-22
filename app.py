from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
from sqlalchemy import text
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
db = SQLAlchemy(app)

# Define models in my database
class Destination(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    destination = db.Column(db.String, nullable=False)
    country = db.Column(db.String, nullable=False)
    region = db.Column(db.String, nullable=True)
    city = db.Column(db.String, nullable=False)

class Address(db.Model):
    address_id = db.Column(db.Integer, primary_key=True)
    destination_id = db.Column(db.Integer, db.ForeignKey('destination.id'), nullable=False)
    address_name = db.Column(db.String, nullable=False)
    principal_category = db.Column(db.String, nullable=False)
    sub_category_1 = db.Column(db.String, nullable=True)
    sub_category_2 = db.Column(db.String, nullable=True)
    sub_category_3 = db.Column(db.String, nullable=True)


with app.app_context():
    db.drop_all() # this will drop all tables to start fresh
    db.create_all()

    # Read CSV files (address.csv, destination.csv)
    data1 = pd.read_csv('destination.csv', usecols=['id', 'city', 'region', 'country', 'destination'])
    data2 = pd.read_csv('address.csv', usecols=['address_id', 'destination_id', 'address_name', 'principal_category', 'sub_category_1', 'sub_category_2', 'sub_category_3'])

    # Load data into the database from address.csv and destination.csv
    data1.to_sql('destination', db.engine, if_exists='append', index=False)
    data2.to_sql('address', db.engine, if_exists='append', index=False)

@app.route('/', methods=["GET"]) # Fetch all destinations
def index():
    destinations = get_all_destinations()
    return render_template('index.html', destinations=destinations)

@app.route('/selection/<selection_type>/<selection_value>', methods=["GET"])
def handle_selection(selection_type, selection_value):
    if selection_type == "destination":
        results = get_countries(selection_value)
        step = "country"
    elif selection_type == "country":
        results = get_addresses(selection_value)
        step = "address"

    return render_template('selection.html', step=step, items=results, name=selection_value)

def get_all_destinations(): # Guidance from ChatGPT for this function specifically, to understand the logic and then from here I was able to more comfortable tackle the following ones
    result = db.session.execute(text("SELECT DISTINCT destination FROM destination"))
    destinations_set = {row[0] for row in result}
    return [{'name': destination} for destination in sorted(destinations_set)]

def get_countries(destination):
    result = db.session.execute(text("SELECT DISTINCT country FROM destination WHERE destination = :destination"), {'destination': destination})
    return [{'name': row[0]} for row in result]

def get_addresses(country):
    result = db.session.execute(text("""SELECT a.address_name, a.principal_category,
                   a.sub_category_1, a.sub_category_2, a.sub_category_3,
                   d.city, d.region
            FROM address a
            JOIN destination d ON a.destination_id = d.id
            WHERE d.country = :country
        """), {'country': country})

    return [
        {
            'address_name': row[0],
            'principal_category': row[1],
            'sub_category_1': row[2],
            'sub_category_2': row[3],
            'sub_category_3': row[4],
            'city': row[5],
            'region': row[6]
        }
        for row in result
    ]

@app.route('/resources', methods=["GET"])
def articles():
    return render_template('resources.html')

@app.route('/about', methods=["GET"])
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)
