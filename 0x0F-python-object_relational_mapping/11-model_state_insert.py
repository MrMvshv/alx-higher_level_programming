#!/usr/bin/python3
""" adds a new state.
    to database hbtn_0e_6_usa
    using module Sqlalchemy
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(username, password, dbname))

    Session = sessionmaker(bind=engine)
    session = Session()

    nstate = State(name='Louisiana')
    session.add(nstate)
    session.commit()

    print(nstate.id)
