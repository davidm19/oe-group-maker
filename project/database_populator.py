from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from test_database_setup import Base, Student, engine

engine = create_engine('sqlite:///test_database.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

student1 = Student(first_name = "Michael", last_name = "Huang")

session.add(student1)
session.commit()

student2 = Student(first_name = "J", last_name = "D")

session.add(student2)
session.commit()
