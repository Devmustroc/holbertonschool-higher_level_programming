#!/usr/bin/python3
"""
script that lists all State objects from the database hbtn_0e_6_usa
"""

import sqlalchemy
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":

    engine = create_engine('mysql://{}:{}@{}:{}/{}'.format(
        argv[1], argv[2], 'localhost', 3306, argv[3]))
    session = sessionmaker(engine)().query(State).order_by(State.id)
    for state in session:
        print("{}: {}".format(state.id, state.name))
    session.close()
