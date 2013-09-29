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

import logging
from lib.db.entry import Entry
from lib.db.project import Project
from lib.db.tag import Tag
from lib.db.base import get_session


logger = logging.getLogger(__name__)

def print_usage():
    """ prints the module docstring """
    print(__doc__)


def start(args):
    """ handles `tempus start` """
    if len(args) < 2:
        session = get_session()

        if 0 == len(args):
            project = Project.get_latest_project(session)
        else:
            project = Project.get_by_name(args[0], session)

        if project:
            stop([])
            project.start()
            project.insert(session)
            print("Project " + project.name + " now running.")
            return True
        else:
            print("Could not find project.")
            return False

    else:
        print_usage()
        return False


def pause(args):
    """ handles `tempus pause` """
    if 0 == len(args):
        session = get_session()

        if not stop([]):
            print("No project stopped, seems as if you were slacking off already.")

        pause_project = Project.get_by_name("PAUSE", session)

        if pause_project is None:
            pause_project = Project("PAUSE")

        pause_project.start()
        pause_project.insert(session)
        print("Pause begins now.")
        return True

    else:
        print_usage()
        return False


def stop(args):
    """ handles `tempus stop` """
    if 0 == len(args):
        session = get_session()
        project = Project.get_latest(session)

        if project:
            project.stop()
            project.insert(session)
            print("Project " + project.name + " has been stopped.")
            return True
        else:
            return False
    else:
        print_usage()
        return False


def tempus_list(args):
    """ handles `tempus list` """
     # handles `tempus list projects`
    if "projects" == args[0] and 1 == len(args):
        project_list = Project.get_list(get_session())
        project_list = "Project List: " + project_list
        print(project_list)
        return True

    # handles `tempus list tags`
    elif "tags" == args[0] and 1 == len(args):
        tag_list = Tag.get_list(get_session())
        tag_list = "Tag List: " + tag_list
        print(tag_list)
        return True

    else:
        print_usage()
        return False


def add(args):
    """ handles `tempus add project <project name>` """
    #todo add check if project exists already *here*, aswell as inittags functionality!!
    if "project" == args[0] and 2 == len(args):
        session = get_session()
        project = Project(args[1])
        project.init_tags(session)
        project.insert(session)
        return True

    # handles `tempus add tag <tag name>
    elif "tag" == args[0] and 2 == len(args):
        new_tag = Tag(args[1])
        new_tag.insert(get_session())
        return True

    else:
        print_usage()
        return False


def remove(args):
    """ handles `tempus remove` """
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

    elif "tag" == args[0] and 2 == len(args):
        session = get_session()
        rm_tag = Tag.get_by_name(args[1], session)

        if rm_tag:
            session.delete(rm_tag)
            session.commit()
            return True
        else:
            print("Could not find tag.")
            return False

    else:
        print_usage()
        return False


def tag(args):
    """ handles `tempus tag <project name> <tag name>` """
    if 2 == len(args):
        session = get_session()
        project = Project.get_by_name(args[0], session)
        tag_tag = Tag.get_by_name(args[1], session)

        if tag_tag and project:
            project.tags.append(tag_tag)
            project.insert(session)
            return True
        else:
            print("Couldn't find project or tag.")
            return False

    else:
        print_usage()
        return False


def untag(args):
    """ handles `tempus untag <project name> <tag name>` """
    if 2 == len(args):
        session = get_session()
        project = Project.get_by_name(args[0], session)
        tagged_tag = Tag.get_by_name(args[1], session)

        if project and tagged_tag:

            try:
                project.tags.remove(tagged_tag)
                project.insert(session)
                return True
            except Exception as exception:
                print(exception)
                print("Project " + project.name + " isn't tagged " + tagged_tag.name + ".")
                return False

        else:
            print("Couldn't find project or tag.")
            return False

    else:
        print_usage()
        return False


def rename(args):
    """handles `tempus rename` """
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

        old_tag = Tag.get_by_name(args[1], session)
        new_tag = Tag.get_by_name(args[2], session)

        if old_tag and not new_tag:
            old_tag.name = args[2]
            old_tag.insert(session)
            return True

        else:
            print("Can't find tag or new name is already taken.")
            return False

    else:
        print_usage()
        return False


def status(args):
    """ handles `tempus status` """
    if 0 == len(args):
        Entry.status(get_session())

    # handles `tempus status project <project name>`
    elif "project" == args[0] and 2 == len(args):
        try:
            project = Project.get_by_name(args[1], get_session())
            total = project.status_total()
            week = project.status_this_week()
            today = project.status_today()
            print("Today: " + output_seconds(today))
            print("This week: " + output_seconds(week))
            print("Total: " + output_seconds(total))
            return True
        except AttributeError:
            print("Could not find project.")
            return False

    # handles `tempus status tag <tag name>`
    elif "tag" == args[0] and 2 == len(args):
        try:
            status_tag = Tag.get_by_name(args[1], get_session())
            total = status_tag.status_total()
            week = status_tag.status_this_week()
            today = status_tag.status_today()
            print("Today: " + output_seconds(today))
            print("This week: " + output_seconds(week))
            print("Total: " + output_seconds(total))
            return True

        except AttributeError:
            print("Could not find tag.")
            return False

    else:
        print_usage()
        return False


def clear():
    """ deletes all data from the database """
    pass


def output_seconds(seconds):
    """ formats output given in seconds to a human-readable output string """
    minutes = int(seconds/60)
    output = ""

    if minutes > 60:
        hours = int(minutes / 60)
        minutes -= hours * 60
        output += str(hours) + " hours, "

    output += str(minutes) + " minutes"
    return output


