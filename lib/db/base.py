__author__ = 'rixx'

import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from configparser import ConfigParser
import os
import sys
import logging


logger = logging.getLogger(__name__)
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
        logger.debug("Successfully loaded config file at " + config_path + ".")

    except KeyError:
        print("Please define a connection string in your config file located at "+config_path+".")
        logger.error("Configuration file not found or incomplete. (" + config_path + "). Aborting.")
        sys.exit(-1)

    try:
        engine = sqlalchemy.create_engine(connection_string, echo=False)
        Base.metadata.create_all(engine)
        logger.debug("Successfully connected to database.")

    except sqlalchemy.exc.ProgrammingError:
        print("It seems the connection string given in "+config_path+" is invalid. Aborting.")
        logger.error("Could not connect to database using the connection string found in " + config_path + " (" + \
                       connection_string + "). Aborting.")
        sys.exit(-1)

    Session = sessionmaker(bind=engine)
    return Session()
