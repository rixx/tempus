#!/usr/bin/env python

import os
import sys
import logging
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from lib.orm import Project, Tag, Base

# init():
#   logger starten
#   config einlesen
#   mapping

logfile_path = os.path.expanduser('~') + '/.tempus/log'
config_path = os.path.expanduser('~') + '/.tempus/config'

def getSession():
    logging.basicConfig(filename=logfile_path, level=logging.DEBUG, format="%(asctime)s - %(levelname)s: %(message)s")
    logger = logging.getLogger("tempus")

    #todo: connection string via config
    engine = sqlalchemy.create_engine("mysql+mysqlconnector://tempususer:tempuspw@localhost/tempusdb", echo=False)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    return Session()

#EXAMPLE: new project
#project = Project("blakeks111")
#project.tags.append(Tag(name="bla"))
#session.add(project)

def print_usage():
    pass


if __name__ == "__main__":

    if 1 == len(sys.argv):
        print_usage()

    elif ("start" == sys.argv[1]) and (2 == len(sys.argv)):
        new_project = Project()
        new_project.get_latest()
        new_project.start()
        pass

    elif ("start" == sys.argv[1]) and (3 == len(sys.argv)):
        pass

    elif ("pause" == sys.argv[1]) and (2 == len(sys.argv)):
        pass

    elif ("stop" == sys.argv[1]) and (2 == len(sys.argv)):
        current_project = Project.get_current_project()
        if (current_project):
            current_project.stop()
        else:
            print("Hm, it seems no project was running.")

    elif ("list" == sys.argv[1]) and ("projects" == sys.argv[2]) and (3 == len(sys.argv)):
        pass

    elif ("list" == sys.argv[1]) and ("tags" == sys.argv[2]) and (3 == len(sys.argv)):
        pass

    elif ("add" == sys.argv[1]) and ("project" == sys.argv[2]) and (4 == len(sys.argv)):
        session = getSession()
        new_project = Project(sys.argv[3])
        new_project.init_tags(session)
        new_project.insert(session)

    elif ("add" == sys.argv[1]) and ("tag" == sys.argv[2]) and (4 == len(sys.argv)):
        new_tag = Tag(sys.argv[3])
        new_tag.insert(getSession())

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


