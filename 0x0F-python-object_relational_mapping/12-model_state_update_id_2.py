#!/usr/bin/python3

"""
a script that changes the name of a State object from the database
hbtn_0e_6_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from model_state import State, Base
import sys

if __name__ == "__main__":
    """
    Create the engine
    """
    url = ('mysql://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))

    engine = create_engine(url)

    """
    Create a session
    """

    Session = sessionmaker(bind=engine)
    session = Session()

    """
    Write the sql query to be executed below
    """

    """
    update the required state
    """
    user = session.query(State).filter(State.id == 2).first()
    if user:
        user.name = 'New Mexico'
        session.commit()
        session.close()
