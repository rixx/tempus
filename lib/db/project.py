""" this module provides the sqlalchemy Project class"""
__author__ = 'rixx'

import logging
import datetime
import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base
from .tag import Tag
from .entry import Entry


class Project(Base):
    """ represent projects table """
    __tablename__ = "projects"
    logger = logging.getLogger(__name__)

    id = Column(Integer, primary_key=True)
    name = Column(String(30), unique=True)

    tags = relationship("Tag", secondary=Base.projects_tags, backref="projects")
    entries = relationship("Entry", back_populates="project")

    def __init__(self, name):
        self.name = name

    def insert(self, session):
        """ commit to database """
        try:
            session.add(self)
            session.commit()
        except sqlalchemy.exc.IntegrityError:
            print("Sorry, the new project could not be added.")

    #todo: move logic to input_parser module
    def init_tags(self, session):
        """ initialize tags upon creation"""
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

    def status_total(self):
        """ add up length of all entries to get total status """
        sum_seconds = 0

        for entry in self.entries:
            sum_seconds += entry.length()

        return sum_seconds

    def status_today(self):
        """ add up length of today's entries """
        sum_seconds = 0
        day_start = int(datetime.date.today().strftime("%s"))

        for entry in self.entries:
            if not entry.end or entry.end > day_start:
                if entry.start > day_start:
                    sum_seconds += entry.length()
                else:
                    sum_seconds += entry.end - day_start

        return sum_seconds

    def status_this_week(self):
        """ add up length of this week's entries """
        sum_seconds = 0
        today = datetime.date.today()
        day_start = int((today - datetime.timedelta(days=today.weekday())).strftime("%s"))

        for entry in self.entries:
            if not entry.end or entry.end > day_start:
                if entry.start > day_start:
                    sum_seconds += entry.length()
                else:
                    sum_seconds += entry.end - day_start

        return sum_seconds

    def start(self):
        """ add a new entry, start=now """
        self.entries.append(Entry())

    def stop(self):
        """ add end time to latest entry """
        entry = self.entries[-1]

        if not entry.end:
            entry.stop()
        else:
            print("Project wasn't running!")

    @staticmethod
    def get_latest(session):
        """ get the latest running project, including PAUSE """
        try:
            latest_project = session.query(Project).join(Entry).order_by(Entry.start.desc()).first()
            return latest_project
        except:
            return None

    @staticmethod
    def get_latest_project(session):
        """ get the latest running project, excluding PAUSE """
        try:
            latest_project = session.query(Project).join(Entry).order_by(Entry.start.desc()).filter(Project.name != "PAUSE").first()
            return latest_project
        except:
            return None

    @staticmethod
    def get_list(session):
        """ returns a string containing all project names """
        query = session.query(Project.name).all()
        return_string = ''

        for project in query:
            if project.name != "PAUSE":
                return_string += project.name + " "

        return return_string

    @staticmethod
    def get_by_name(name, session):
        """ returns a project by a given name """
        try:
            project = session.query(Project).filter(Project.name == name).one()
            return project
        except sqlalchemy.orm.exc.NoResultFound:
            return None
