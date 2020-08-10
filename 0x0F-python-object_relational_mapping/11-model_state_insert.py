#!/usr/bin/python3
"""
use sqlalchemy to add Louisiana to database
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
    state = State(name="Louisiana")
    session_help.add(state)
    session_help.commit()
    print("{}".format(state.id))
    session_help.close()
