from flask import Flask, jsonify, request

from .entities.entity import Session, engine, Base
from .entities.trip import Trip, TripSchema

from flask_cors import CORS

# creating the Flask application
app = Flask(__name__)
CORS(app)
# if needed, generate database schema
Base.metadata.create_all(engine)


@app.route('/trips')
def get_trips():
    # fetching from the database
    session = Session()
    trip_objects = session.query(Trip).all()

    # transforming into JSON-serializable objects
    schema = TripSchema(many=True)
    trips = schema.dump(trip_objects)

    # serializing as JSON
    session.close()
    return jsonify(trips.data)


@app.route('/trips', methods=['POST'])
def add_trip():
    session = Session()
    # mount trip object
    posted_trip = TripSchema(only=('title', 'description'))\
        .load(request.get_json())

    trip = Trip(**posted_trip.data, created_by="HTTP post request")

    # persist trip

    session.add(trip)
    session.commit()

    # return created trip
    new_trip = TripSchema().dump(trip).data
    session.close()
    return jsonify(new_trip), 201
