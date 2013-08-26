__author__ = 'rixx'

from sqlalchemy import Column, Integer, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

#for mapping projects:tags as m:n relation
Base.projects_tags = Table('projects_tags', Base.metadata, \
                           Column('projects_id', Integer, ForeignKey('projects.id')),\
                           Column('tags_id', Integer, ForeignKey('tags.id')))