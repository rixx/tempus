#About

Tempus is CLI time tracking app. It requires Python 3, mysql-connector and SQLAlchemy.

#Usage

* `tempus start [project]` starts the timer. If no project is given, the last running project is assumed. (to be implemented)
* `tempus stop` stops the timer. (to be implemented)
* `tempus pause` stops the timer for the running project and starts the generic pause project. (to be implemented)
* `tempus list [projects|tags]` prints a list of all current projects or tags respectively. (to be implemented)
* `tempus add [project|tag] name` adds a new project or tag respectively. If a new project is added, the user is asked for tags he wants to add. (to be implemented)
* `tempus remove [all| [project|tag] name]` removes everything or a project/tag by name. Gives an "Are you sure?" dialog. (to be implemented)
* `tempus modify project name [add|remove] tag name` adds or removes tags. (to be implemented)
* `tempus modify [project|tag] name rename new_name` renames a tag or project. (to be implemented)
* `tempus status {[project|tag] name} gives general or more specific statistics. (to be implemented)
* `tempus clear` resets the log, all data entries will be lost. Projects and tags are preserved. (to be implemented)

