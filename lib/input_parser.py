__author__ = 'rixx'

from lib.db.entry import Entry
from lib.db.project import Project
from lib.db.tag import Tag
from lib.db.base import get_session


def print_usage():
    pass

def start(args):
     # handles `tempus start`
    if 0 == len(args):
        new_project = Project()
        new_project.get_latest()
        new_project.start()

    # handles `tempus start <project name>`
    elif 1 == len(args):
        project = Project(args[0])
        project.start()
        project.insert(get_session())

    else:
        print_usage()


def pause(args):
    if 0 == len(args):
        session = get_session()
        Project.stop_running_project(session)
        pause_project = Project("PAUSE")
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
        Project.get_list(get_session())

    # handles `tempus list tags`
    elif "tags" == args[0] and 1 == len(args):
        Tag.get_list(get_session())

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
