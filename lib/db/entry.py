__author__ = 'rixx'

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

    @staticmethod
    def status(session):
        pass
