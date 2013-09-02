__author__ = 'rixx'

import logging
import time
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base
from .tag import Tag
from .entry import Entry


class Project(Base):
    __tablename__ = "projects"
    logger = logging.getLogger(__name__)
    id = Column(Integer, primary_key=True)
    name = Column(String(30), unique=True)

    tags = relationship("Tag", secondary=Base.projects_tags, backref="projects")
    entries = relationship("Entry", back_populates="project")

    def __init__(self, name):
        self.name = name

    def insert(self, session):
        try:
            session.add(self)
            session.commit()
        except:
            print("Sorry, the new project could not be added … are you sure it doesn't exist already?")

    def init_tags(self, session):
        tag_list = Tag.get_list(session)

        if tag_list:
            print("The following tags exist: " + tag_list)
        else:
            print("No tags exist")

        user_tag_list = input("Please enter the tags for this project separated by commas: ").split(',')

        for tag in user_tag_list:
            if len(tag) > 0:
                new_tag = Tag.get_by_name(tag, session)

                if new_tag:
                    self.tags.append(new_tag)
                else:
                    print("Tag " + tag + " not found, skipping.")


    def status(self, session):
        pass

    def start(self):
        entry = Entry(int(time.time()))
        self.entries.append(entry)

    def stop(self):
        entry = self.entries[-1]

        if not entry.end:
            entry.end = int(time.time())
        else:
            print("Project wasn't running!")

    @staticmethod
    def get_latest(session):
        try:
            latest_project = session.query(Project).join(Entry).order_by(Entry.start.desc()).first()
            return latest_project
        except:
            return None

    @staticmethod
    def get_list(session):
        query = session.query(Project.name).all()
        return_string = ''

        for project in query:
            if project.name != "PAUSE":
                return_string += project.name + " "

        return return_string

    @staticmethod
    def get_by_name(name, session):
        try:
            project = session.query(Project).filter(Project.name == name).one()
            return project
        except:
            None
