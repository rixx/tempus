__author__ = 'rixx'

import time
import logging
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base


class Entry(Base):
    """ Represent the entries table """
    __tablename__ = "entries"
    logger = logging.getLogger(__name__)

    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey("projects.id"))
    project = relationship("Project", back_populates="entries")

    start = Column(Integer)
    end = Column(Integer)

    def __init__(self, start=int(time.time())):
        """ initialize and assume current time as start time """
        self.start = start

    def length(self):
        """ give the duration of this entry. If unfinished, assume current time as end """
        try:
            return self.end - self.start
        except TypeError:
            return int(time.time()) - self.start

    def stop(self):
        """ stop and assume current time as end """
        self.end = int(time.time())
