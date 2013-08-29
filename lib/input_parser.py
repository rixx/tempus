"""
tempus usage:
   start {<project name>} - starts the timer. If no project name is given, the last running project is assumed (pause project not included)
   pause - pauses the timer and starts the default pause project
   stop - stops the timer
   list [projects|tags] - givs a list of all projects or tags
   add [project|tag] <name> - adds a project or tag
   [tag|untag] <project name> <tag name> - adds or removes a tag
   rename [project|tag] <old name> <new name> - renames a project or tag
   status {[project|tag] <name>} - either gives general or more specific statistics
   clear - resets the log, all data entries wil be lost, projects and tags are preserved
"""
__author__ = 'rixx'

from lib.db.entry import Entry
from lib.db.project import Project
from lib.db.tag import Tag
from lib.db.base import get_session
import logging


logger = logging.getLogger(__name__)

def print_usage():
    print(__doc__)


def start(args):
    if len(args) < 2:
        session = get_session()

        #either get running project, stop and output, or just … fail?

        if 0 == len(args):
            try:
                project = Project.get_latest(session)
            except:
                print("No prior project has been found. Please specify the project you wish to start.")
                return False

        elif 1 == len(args):
            try:
                project = Project.get_by_name(args[0], session)
            except:
                print("Sorry, couldn't find a project named " + args[0] + ".")
                return False

        project.start()
        project.insert(session)

    else:
        print_usage()


def pause(args):
    if 0 == len(args):
        session = get_session()

        try:
            project = Project.get_latest(session)
            project.stop()
            project.insert(session)
        except:
            print("There was no project to be paused, seems you were slacking off already ;)")
            return False

        pause_project = Project.get_by_name("PAUSE", session)
        pause_project.start()
        pause_project.insert(session)

    else:
        print_usage()


def stop(args):
    if 0 == len(args):
        Project.stop_running_project(get_session())
    else:
        print_usage()


def list(args):
     # handles `tempus list projects`
    if "projects" == args[0] and 1 == len(args):
        list = Project.get_list(get_session())
        list = "Project List: " + list
        print(list)

    # handles `tempus list tags`
    elif "tags" == args[0] and 1 == len(args):
        list = Tag.get_list(get_session())
        list = "Tag List: " + list
        print(list)

    else:
        print_usage()


def add(args):
    # handles `tempus add project <project name>`
    if "project" == args[0] and 2 == len(args):
        session = get_session()
        new_project = Project(args[1])
        new_project.init_tags(session)
        new_project.insert(session)

    # handles `tempus add tag <tag name>
    elif "tag" == args[0] and 2 == len(args):
        new_tag = Tag(args[1])
        new_tag.insert(get_session())

    else:
        print_usage()


def tag(args):
    # handles `tempus tag <project name> <tag name>`
    if 2 == len(args):
        session = get_session()
        project = Project.get_by_name(args[0], session)
        project.add_tag(args[1])
        project.insert(session)

    else:
        print_usage()


def untag(args):
    # handles `tempus untag <project name> <tag name>`
    if 2 == len(args):
        session = get_session()
        project = Project.get_by_name(args[0], session)
        project.remove_tag(args[1])
        project.insert(session)

    else:
        print_usage()

def rename(args):
    # handles `tempus rename project <project name> <new name>`
    if "project" == args[0] and 3 == len(args):
        session = get_session()
        project = Project.get_by_name(args[1], session)
        test = Project.get_by_name(args[2], session)
        project.name = args[2]
        project.insert(session)

    # handles `tempus rename tag <tag name> <new name>`
    elif "tag" == args[0] and 3 == len(args):
        session = get_session()
        tag = Tag.get_by_name(args[1], session)
        test = Tag.get_by_name(args[2], session)
        tag.name = args[2]
        tag.insert(session)

    else:
        print_usage()


def status(args):
    # handles `tempus status`
    if 0 == len(args):
        Entry.status(get_session())

    # handles `tempus status project <project name>`
    elif "project" == args[0] and 2 == len(args):
        project = Project(args[1])
        project.status(get_session())

    # handles `tempus status tag <tag name>`
    elif "tag" == args[0] and 2 == len(args):
        tag = Tag(args[1])
        tag.status(get_session())

    else:
        print_usage()


def clear(args):
    pass
