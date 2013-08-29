"""
tempus usage:
   start {<project name>} - starts the timer. If no project name is given, the last running project is assumed (pause project not included)
   pause - pauses the timer and starts the default pause project
   stop - stops the timer
   list [projects|tags] - gives a list of all projects or tags
   add [project|tag] <name> - adds a project or tag
   remove [project|tag] <name> - removes a project or tag
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
        return True

    else:
        print_usage()
        return False


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
        return True

    else:
        print_usage()
        return False


def stop(args):
    if 0 == len(args):
        Project.stop_running_project(get_session())
    else:
        print_usage()
        return False


def list(args):
     # handles `tempus list projects`
    if "projects" == args[0] and 1 == len(args):
        list = Project.get_list(get_session())
        list = "Project List: " + list
        print(list)
        return True

    # handles `tempus list tags`
    elif "tags" == args[0] and 1 == len(args):
        list = Tag.get_list(get_session())
        list = "Tag List: " + list
        print(list)
        return True

    else:
        print_usage()
        return False


def add(args):
    # handles `tempus add project <project name>`
    #todo add check if project exists already *here*, aswell as inittags functionality!!
    if "project" == args[0] and 2 == len(args):
        session = get_session()
        project = Project(args[1])
        project.init_tags(session)
        project.insert(session)
        return True

    # handles `tempus add tag <tag name>
    elif "tag" == args[0] and 2 == len(args):
        tag = Tag(args[1])
        tag.insert(get_session())
        return True

    else:
        print_usage()
        return False


def remove(args):
    if "project" == args[0] and 2 == len(args):
        session = get_session()
        project = Project.get_by_name(args[1], session)

        if project:
            session.delete(project)
            session.commit()
            return True
        else:
            print("Could not find project.")
            return False

    # handles `tempus add tag <tag name>
    elif "tag" == args[0] and 2 == len(args):
        session = get_session()
        tag = Tag.get_by_name(args[1], session)

        if tag:
            session.delete(tag)
            session.commit()
            return True
        else:
            print("Could not find tag.")
            return False

    else:
        print_usage()
        return False


def tag(args):
    # handles `tempus tag <project name> <tag name>`
    if 2 == len(args):
        session = get_session()
        project = Project.get_by_name(args[0], session)
        tag = Tag.get_by_name(args[1], session)

        if tag and project:
            project.tags.append(tag)
            project.insert(session)
            return True
        else:
            print("Couldn't find project or tag.")
            return False

    else:
        print_usage()
        return False


def untag(args):
    # handles `tempus untag <project name> <tag name>`
    if 2 == len(args):
        session = get_session()
        project = Project.get_by_name(args[0], session)
        tag = Tag.get_by_name(args[1], session)

        if project and tag:

            try:
                project.tags.remove(tag)
                project.insert(session)
                return True
            except:
                print("Project " + project.name + " isn't tagged " + tag.name + ".")
                return False

        else:
            print("Couldn't find project or tag.")
            return False

    else:
        print_usage()
        return False


def rename(args):
    # handles `tempus rename project <project name> <new name>`
    if "project" == args[0] and 3 == len(args):
        session = get_session()

        project = Project.get_by_name(args[1], session)
        new_project = Project.get_by_name(args[2], session)

        if project and not new_project:
            project.name = args[2]
            project.insert(session)
            return True

        else:
            print("Can't find project or new name is already taken.")
            return False

    # handles `tempus rename tag <tag name> <new name>`
    elif "tag" == args[0] and 3 == len(args):
        session = get_session()

        tag = Tag.get_by_name(args[1], session)
        new_tag = Tag.get_by_name(args[2], session)

        if tag and not new_tag:
            tag.name = args[2]
            tag.insert(session)
            return True

        else:
            print("Can't find tag or new name is already taken.")
            return False

    else:
        print_usage()
        return False


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
        return False


def clear(args):
    pass
