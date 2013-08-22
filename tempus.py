#!/usr/bin/env python

import os
import sys
import logging
import sqlalchemy
from sqlalchemy.orm import sessionmaker
import lib
from lib.orm import Project, Tag, Base
from configparser import ConfigParser


logfile_path = os.path.expanduser('~') + '/.tempus/log'
config_path = os.path.expanduser('~') + '/.tempus/config'

def get_session():
    logging.basicConfig(filename=logfile_path, level=logging.DEBUG, format="%(asctime)s - %(levelname)s: %(message)s")
    logger = logging.getLogger("tempus")

    config = ConfigParser()


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

    # if tempus is called with no parameter
    if 1 == len(sys.argv):
        print_usage()

    # handles `tempus start`
    elif ("start" == sys.argv[1]) and (2 == len(sys.argv)):
        new_project = Project()
        new_project.get_latest()
        new_project.start()

    # handles `tempus start <project name>`
    elif ("start" == sys.argv[1]) and (3 == len(sys.argv)):
        project = Project(sys.argv[2])
        project.start()
        project.insert(get_session())

    # handles `tempus pause`
    elif ("pause" == sys.argv[1]) and (2 == len(sys.argv)):
        session = get_session()
        Project.stop_running_project(session)
        pause_project = Project("PAUSE")
        pause_project.start()
        pause_project.insert(session)

    # handles `tempus stop`
    elif ("stop" == sys.argv[1]) and (2 == len(sys.argv)):
        Project.stop_running_project(get_session())

    # handles `tempus list projects`
    elif ("list" == sys.argv[1]) and ("projects" == sys.argv[2]) and (3 == len(sys.argv)):
        Project.get_list(get_session())

    # handles `tempus list tags`
    elif ("list" == sys.argv[1]) and ("tags" == sys.argv[2]) and (3 == len(sys.argv)):
        Tag.get_list(get_session())

    # handles `tempus add project <project name>`
    elif ("add" == sys.argv[1]) and ("project" == sys.argv[2]) and (4 == len(sys.argv)):
        session = get_session()
        new_project = Project(sys.argv[3])
        new_project.init_tags(session)
        new_project.insert(session)

    # handles `tempus add tag <tag name>
    elif ("add" == sys.argv[1]) and ("tag" == sys.argv[2]) and (4 == len(sys.argv)):
        new_tag = Tag(sys.argv[3])
        new_tag.insert(get_session())

    # handles `tempus modify project <project name> add tag <tag name>`
    elif ("modify" == sys.argv[1]) and ("project" == sys.argv[2]) and ("add" == sys.argv[4]) and ("tag" == sys.argv[5])\
         and (7 == len(sys.argv)):
        session = get_session()
        project = Project.get_by_name(sys.argv[3], session)
        project.add_tag(sys.argv[6])
        project.insert(session)

    # handles `tempus modify project <project name> remove tag <tag name>`
    elif ("modify" == sys.argv[1]) and ("project" == sys.argv[2]) and ("remove" == sys.argv[4]) and ("tag" == sys.argv[5]) \
         and (7 == len(sys.argv)):
        session = get_session()
        project = Project.get_by_name(sys.argv[3], session)
        project.remove_tag(sys.argv[6])
        project.insert(session)

    # handles `tempus modify project <project name> rename <new name>`
    elif ("modify" == sys.argv[1]) and ("project" == sys.argv[2]) and ("rename" == sys.argv[4]) and (6 == len(sys.argv)):
        session = get_session()
        project = Project.get_by_name(sys.argv[3], session)
        project.name = sys.argv[5]
        project.insert(session)

    # handles `tempus modify tag <tag name> rename <new name>`
    elif ("modify" == sys.argv[1]) and ("tag" == sys.argv[2]) and ("rename" == sys.argv[4]) and (6 == len(sys.argv)):
        session = get_session()
        tag = Tag.get_by_name(sys.argv[3], session)
        tag.name = sys.argv[5]
        tag.insert(session)

    # handles `tempus status`
    elif ("status" == sys.argv[1]) and (2 == len(sys.argv)):
        Entry.status(get_session())

    # handles `tempus status project <project name>`
    elif ("status" == sys.argv[1]) and ("project" == sys.argv[2]) and (4 == len(sys.argv)):
        project = Project(sys.argv[3])
        project.status(get_session())

    # handles `tempus status tag <tag name>`
    elif ("status" == sys.argv[1]) and ("tag" == sys.argv[2]) and (4 == len(sys.argv)):
        tag = Tag(sys.argv[3])
        tag.status(get_session())

    else:
        print_usage()


