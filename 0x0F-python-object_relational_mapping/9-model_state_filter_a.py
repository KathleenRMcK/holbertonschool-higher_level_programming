#!/usr/bin/python3
"""
use sqlalchemy to list state objects that contain the letter a
"""


if __name__ == '__main__':

    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    import sys

    engine_help = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session_help = Session()
    states = session.query(State).order_by(State.id)
    for state in states:
        if 'a' in state.name:
            print("{}: {}".format(state.id, state.name))
    session_help.close()
