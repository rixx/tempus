__author__ = 'rixx'

import logging
from sqlalchemy import Column, Integer, String
from .base import Base


class Tag(Base):
    __tablename__ = "tags"
    logger = logging.getLogger(__name__)
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

    def status_total(self):
        sum_seconds = 0

        for project in self.projects:
            sum_seconds += project.status_total()

        return sum_seconds

    @staticmethod
    def get_list(session):
        query = session.query(Tag.name).all()
        return_string = ''

        for tag in query:
            return_string += tag.name + " "

        return return_string

    @staticmethod
    def get_by_name(name, session):
        try:
            tag = session.query(Tag).filter(Tag.name == name).one()
            return tag
        except:
            return None
