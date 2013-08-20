#!/usr/bin/env python

import os
import sys
import logging
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import sessionmaker, relationship, backref

# init():
#   logger starten
#   config einlesen
#   mapping

logfile_path = os.path.expanduser('~') + '/.tempus/log'
logging.basicConfig(filename=logfile_path, level=logging.DEBUG, format="%(asctime)s - %(levelname)s: %(message)s")
logger = logging.getLogger("tempus")

engine = sqlalchemy.create_engine("mysql+mysqlconnector://tempususer:tempuspw@localhost/tempusdb")
Base = declarative_base()

projects_tags = Table('projects_tags', Base.metadata, Column('project_id', Integer, ForeignKey('projects.id')),\
                      Column('tags_id', Integer, ForeignKey('tags.id')))


class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True)
    name = Column(String(30), unique=True)
    entries = relationship("Entry", backref="projects")
    tags = relationship("Tag", secondary=projects_tags, back_populates="projects")
    entries = relationship("Entry", back_populates="project")

    def __init__(self, name):
        self.name = name

class Entry(Base):
    __tablename__ = "entries"
    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey("projects.id"))
    start = Column(Integer)
    end = Column(Integer)

    project = relationship("Project", back_populates="entries")


class Tag(Base):
    __tablename__ = "tags"
    id = Column(Integer, primary_key=True)
    name = Column(String(20), unique=True)

    projects = relationship("Project", secondary=projects_tags, back_populates="tags")

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

#project = Project("blakeks111")
#project.tags.append(Tag(name="bla"))
#session.add(project)

tag = session.query(Tag).filter(Tag.name == "bla").first()
print(vars(tag.projects))
tag.projects.append(Project(name="hastenichgesehn"))

session.commit()

for class_ in [Project,Entry,Tag]:
    print(class_.__name__)
    for var in vars(class_):
        if var[0] != '_':
            print(var)

    print()


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


