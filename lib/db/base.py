""" this module provides the BASE data relevant to the remaining
    sqlalchemy modules in this package aswell as the get_session()
    method returning a valid session with the configured db
"""
__author__ = 'rixx'

import os
import sys
import logging
from configparser import ConfigParser
import sqlalchemy
from sqlalchemy import Column, Integer, ForeignKey, Table
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


LOGGER = logging.getLogger(__name__)
CONFIG_PATH = os.path.expanduser('~') + '/.tempus/config'
BASE = declarative_base()

#for mapping projects:tags as m:n relation
BASE.projects_tags = Table('projects_tags', BASE.metadata,
                           Column('projects_id', Integer, ForeignKey('projects.project_id')),
                           Column('tags_id', Integer, ForeignKey('tags.tag_id')))


def get_session():
    """ read the config file, connect to the given database and return a session with that database"""
    try:
        config = ConfigParser()
        config.read(CONFIG_PATH)
        connection_string = config['General']['Connection']
        LOGGER.debug("Successfully loaded config file at " + CONFIG_PATH + ".")

    except KeyError:
        print("Please define a connection string in your config file located at " + CONFIG_PATH + ".")
        LOGGER.error("Configuration file not found or incomplete. (" + CONFIG_PATH + "). Aborting.")
        sys.exit(-1)

    try:
        engine = sqlalchemy.create_engine(connection_string, echo=False)
        BASE.metadata.create_all(engine)
        LOGGER.debug("Successfully connected to database.")

    except sqlalchemy.exc.ProgrammingError:
        print("It seems the connection string given in " + CONFIG_PATH + " is invalid. Aborting.")
        LOGGER.error("Could not connect to database using the connection string found in " + CONFIG_PATH + " (" + \
                     connection_string + "). Aborting.")
        sys.exit(-1)

    session = sessionmaker(bind=engine)
    return session()
