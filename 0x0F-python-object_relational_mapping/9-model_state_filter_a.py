#!/usr/bin/env python3
"""
script that lists all State objects that contain the letter a from the database hbtn_0e_6_usa
"""

import sqlalchemy
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":

    engine = create_engine(
        f"mysql://{argv[1]}:{argv[2]}@{'localhost'}:{3306}/{argv[3]}")
    Session = sessionmaker(bind=engine)
    session = Session()
    for state in session.query(State).order_by(State.id).filter(State.name.like('%a%')):
        if state:
            print(f"{state.id}: {state.name}")
        else:
            print("Nothing")
    session.close()
