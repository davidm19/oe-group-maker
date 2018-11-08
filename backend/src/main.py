
from .entities.entity import Session, engine, Base
from .entities.trip import Trip

# generate database schema
Base.metadata.create_all(engine)

# start session
session = Session()

# check for existing data
trips = session.query(Trip).all()

if len(trips) == 0:
    # create and persist dummy trip
    python_exam = Trip("Test trip", "script")
    session.add(newTrip)
    session.commit()
    session.close()

    # reload trips
    trips = session.query(Trip).all()

# show existing trips
print('### Trips:')
for trip in trips:
    print(f'({trip.id}) {trip.title} - {trip.description}')
