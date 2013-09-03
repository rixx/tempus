__author__ = 'rixx'

import time
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base
import logging


class Entry(Base):
    __tablename__ = "entries"
    id = Column(Integer, primary_key=True)
    logger = logging.getLogger(__name__)
    project_id = Column(Integer, ForeignKey("projects.id"))
    start = Column(Integer)
    end = Column(Integer)

    project = relationship("Project", back_populates="entries")

    def __init__(self, start=int(time.time())):
        self.start = start

    def length(self):
        try:
            return self.end - self.start
        except TypeError:
            return int(time.time()) - self.start

    def stop(self):
        self.end = int(time.time())

    @staticmethod
    def status(session):
        pass
