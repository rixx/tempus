__author__ = 'rixx'

import logging
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base
from .tag import Tag


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

                if (new_tag):
                    self.tags.append(new_tag)
                else:
                    print("Tag " + tag + " not found, skipping.")

    def remove_tag(self, name, session):
        pass

    def add_tag(self, name, session):
        pass

    def status(self, session):
        pass

    def start(self):
        pass

    def stop(self):
        pass

    @staticmethod
    def get_latest(session):
        current_project = session.query(Project) #und so

        if (current_project):
            current_project.stop()
        else:
            print("Hm, it seems no project was running.")

    @staticmethod
    def get_list(session):

        pass

    @staticmethod
    def get_by_name(name, session):
        pass
