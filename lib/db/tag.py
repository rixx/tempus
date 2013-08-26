__author__ = 'rixx'

from sqlalchemy import Column, Integer, String
from .base import Base

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