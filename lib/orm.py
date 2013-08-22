__author__ = 'rix'

from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

#for mapping projects:tags as m:n relation
projects_tags = Table('projects_tags', Base.metadata, Column('projects_id', Integer, ForeignKey('projects.id')),\
                      Column('tags_id', Integer, ForeignKey('tags.id')))

class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True)
    name = Column(String(30), unique=True)

    tags = relationship("Tag", secondary=projects_tags, backref="projects")
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
        print("The following tags exist: " + self.get_list(session))

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

class Entry(Base):
    __tablename__ = "entries"
    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey("projects.id"))
    start = Column(Integer)
    end = Column(Integer)

    project = relationship("Project", back_populates="entries")

    @staticmethod
    def status(session):
        pass


class Tag(Base):
    __tablename__ = "tags"
    id = Column(Integer, primary_key=True)
    name = Column(String(20), unique=True)

    def __init__(self,name):
        self.name = name

    def insert(self,session):
        try:
            session.add(self)
            session.commit()
        except:
            print("Sorry, the new tag could not be added … are you sure it doesn't exist already?")

    def status(self, session):
        pass

    @staticmethod
    def get_list(session):
        query = session.query(Tag.name).all()
        return_string = ''

        for tag in query:
            return_string += tag.name + " "

        return return_string

    @staticmethod
    def get_by_name(name, session):
        pass
