from flask import Flask, jsonify, request

from .entities.entity import Session, engine, Base
from .entities.trip import Trip, TripSchema

from flask_cors import CORS

# creating the Flask application
app = Flask(__name__)

# if needed, generate database schema
Base.metadata.create_all(engine)


@app.route('/trips')
def get_trips():
    # fetching from the database
    session = Session()
    allTrips = session.query(Trip).all()

    # transforming into JSON-serializable objects
    schema = TripSchema(many=True)
    trips = schema.dump(allTrips)

    # serializing as JSON
    session.close()
    return jsonify(trips.data)


@app.route('/trips', methods=['POST'])
def add_trip():
    # mount trip object
    newTrip = TripSchema(only=('title', 'description'))\
        .load(request.get_json())

    trip = Trip(**newTrip.data, created_by="HTTP post request")

    # persist trip
    session = Session()
    session.add(trip)
    session.commit()

    # return created trip
    newTrip = TripSchema().dump(trip).data
    session.close()
    return jsonify(newTrip), 201
