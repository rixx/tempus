__author__ = 'rixx'

import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from configparser import ConfigParser
import os


config_path = os.path.expanduser('~') + '/.tempus/config'
Base = declarative_base()

#for mapping projects:tags as m:n relation
Base.projects_tags = Table('projects_tags', Base.metadata, \
                           Column('projects_id', Integer, ForeignKey('projects.id')),\
                           Column('tags_id', Integer, ForeignKey('tags.id')))

def get_session():
    try:
        config = ConfigParser()
        config.read(config_path)
        connection_string = config['General']['Connection']
    except:
        print("Please define a connection string in your config file located at "+config_path+".")

    try:
        engine = sqlalchemy.create_engine(connection_string, echo=False)
        Base.metadata.create_all(engine)
    except:
        print("It seems the connection string given in "+config_path+" is invalid. Aborting.")

    Session = sessionmaker(bind=engine)
    return Session()
