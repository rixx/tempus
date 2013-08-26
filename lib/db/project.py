__author__ = 'rixx'

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base
from .tag import Tag


class Project(Base):
    __tablename__ = "projects"
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
        tag_list = self.get_list(session)

        if tag_list:
            print("The following tags exist: " + self.get_list(session))
        else:
            print("No tags exist")

        user_tag_list = input("Please enter the tags for this project separated by commas: ").split(',')

        for tag in user_tag_list:
            self.tags.append(session.query(Tag).filter(Tag.name == tag).one())

    def remove_tag(self, name, session):
        pass

    def add_tag(self, name, session):
        pass

    def status(self, session):
        pass

    @staticmethod
    def stop_running_project(session):
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
