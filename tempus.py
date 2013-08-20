#!/usr/bin/env python

import os
import sys
import logging
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

# init():
#   logger starten
#   config einlesen
#   mapping

logfile_path = os.path.expanduser('~') + '/.tempus/log'
logging.basicConfig(filename=logfile_path, level=logging.DEBUG, format="%(asctime)s - %(levelname)s: %(message)s")
logger = logging.getLogger("tempus")

engine = sqlalchemy.create_engine("mysql+mysqlconnector://tempususer:tempuspw@localhost/tempusdb")
Base = declarative_base()

class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True)
    name = Column(String(30))

    def __init__(self, name):
        self.name = name

Base.metadata.create_all(engine)


def print_usage():
    pass


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print_usage()

    elif "start" == sys.argv[1]:
        pass

    elif "pause" == sys.argv[1]:
        pass

    elif "stop" == sys.argv[1]:
        pass

    elif ("list" == sys.argv[1]) and ("projects" == sys.argv[2]):
        pass

    elif ("list" == sys.argv[1]) and ("tags" == sys.argv[2]):
        pass

    elif ("add" == sys.argv[1]) and ("projects" == sys.argv[2]):
        pass

    elif ("add" == sys.argv[1]) and ("tags" == sys.argv[2]):
        pass

    elif "status" == sys.argv[1]:

        if 2 == len(sys.argv):
            pass

        elif ("project" == sys.argv[2]) and (4 == len(sys.argv)):
            pass

        elif ("tag" == sys.argv[2]) and (4 == len(sys.argv)):
            pass

    else:
        print_usage()


