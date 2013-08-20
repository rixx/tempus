#!/usr/bin/env python

import os
import sys
import logging
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from lib.ORM import Project,Entry,Tag

# init():
#   logger starten
#   config einlesen
#   mapping

logfile_path = os.path.expanduser('~') + '/.tempus/log'
config_path = os.path.expanduser('~') + '/.tempus/config'

logging.basicConfig(filename=logfile_path, level=logging.DEBUG, format="%(asctime)s - %(levelname)s: %(message)s")
logger = logging.getLogger("tempus")

#todo: connection string via config
engine = sqlalchemy.create_engine("mysql+mysqlconnector://tempususer:tempuspw@localhost/tempusdb")
Base = declarative_base()

#create if not exist
Base.metadata.create_all(engine)

#start a session
Session = sessionmaker(bind=engine)
session = Session()

#EXAMPLE: new project
#project = Project("blakeks111")
#project.tags.append(Tag(name="bla"))
#session.add(project)

#EXAMPLE: add tag to project
#tag = session.query(Tag).filter(Tag.name == "bla").first()
#print(vars(tag.projects))
#tag.projects.append(Project(name="hastenichgesehn"))

session.commit()


def print_usage():
    pass


if __name__ == "__main__":

    if 1 == len(sys.argv):
        print_usage()

    elif ("start" == sys.argv[1]) and (2 == len(sys.argv)):
        pass

    elif ("start" == sys.argv[1]) and (3 == len(sys.argv)):
        pass

    elif ("pause" == sys.argv[1]) and (2 == len(sys.argv)):
        pass

    elif ("stop" == sys.argv[1]) and (2 == len(sys.argv)):
        pass

    elif ("list" == sys.argv[1]) and ("projects" == sys.argv[2]) and (3 == len(sys.argv)):
        pass

    elif ("list" == sys.argv[1]) and ("tags" == sys.argv[2]) and (3 == len(sys.argv)):
        pass

    elif ("add" == sys.argv[1]) and ("projects" == sys.argv[2]) and (4 == len(sys.argv)):
        pass

    elif ("add" == sys.argv[1]) and ("tags" == sys.argv[2]) and (4 == len(sys.argv)):
        pass

    elif ("modify" == sys.argv[1]) and ("project" == sys.argv[2]) and ("add" == sys.argv[4]) and ("tag" == sys.argv[5])\
         and (7 == len(sys.argv)):
        pass

    elif ("modify" == sys.argv[1]) and ("project" == sys.argv[2]) and ("remove" == sys.argv[4]) and ("tag" == sys.argv[5]) \
         and (7 == len(sys.argv)):
        pass

    elif ("modify" == sys.argv[1]) and ("project" == sys.argv[2]) and ("rename" == sys.argv[4]) and (6 == len(sys.argv)):
        pass

    elif ("modify" == sys.argv[1]) and ("tag" == sys.argv[2]) and ("rename" == sys.argv[4]) and (6 == len(sys.argv)):
        pass

    elif ("status" == sys.argv[1]) and (2 == len(sys.argv)):
        pass

    elif ("status" == sys.argv[1]) and ("project" == sys.argv[2]) and (4 == len(sys.argv)):
        pass

    elif ("status" == sys.argv[1]) and ("project" == sys.argv[2]) and (4 == len(sys.argv)):
        pass

    else:
        print_usage()


