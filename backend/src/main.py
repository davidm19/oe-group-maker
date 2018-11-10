# from .entities.entity import Session, engine, Base
# from .entities.trip import Trip
#
# # generate database schema
# Base.metadata.create_all(engine)
#
# # start session
# session = Session()
#
# # check for existing data
# trips = session.query(Trip).all()
#
# if len(trips) == 0:
#     # create and persist dummy trip
#     test_trip = Trip("SQLAlchemy Exam", "Test your knowledge about SQLAlchemy.", "script")
#     session.add(test_trip)
#     session.commit()
#     session.close()
#
#     # reload trips
#     trips = session.query(Trip).all()
#
# # show existing trips
# print('### Exams:')
# for trip in trips:
#     print("I think something works")




from flask import Flask, jsonify, request

from entities.entity import Session, engine, Base
from entities.trip import Trip

# from flask_cors import CORS

# creating the Flask application

app = Flask(__name__)
# if needed, generate database schema
Base.metadata.create_all(engine)


@app.route('/trips')
def get_trips():
    # fetching from the database
    session = Session()
    trips_objects = session.query(Trip).all()

    return jsonify(trip_objects.data)


@app.route('/trips', methods=['POST'])
def add_trip():
    session = Session()
    # mount trip object
    posted_trip = Trip(only=('title', 'description'))\
        .load(request.get_json())

    trip = Trip(posted_trip.data, created_by="HTTP post request")

    # persist trip

    session.add(trip)
    session.commit()

    # return created trip
    new_trip = TripSchema().dump(trip).data
    session.close()
    return jsonify(new_trip), 201


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
