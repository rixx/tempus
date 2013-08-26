__author__ = 'rixx'

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

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
