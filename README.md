#About

Tempus is CLI time tracking app. It requires Python 3 and SQLAlchemy aswell as some database and corresponding Python 3 drivers (mysql-connector for MySQL).

#Usage

* `tempus start [project]` starts the timer. If no project is given, the last running project is assumed.
* `tempus stop` stops the timer.
* `tempus pause` stops the timer for the running project and starts the generic pause project.
* `tempus list [projects|tags]` prints a list of all current projects or tags respectively.
* `tempus add [project|tag] name` adds a new project or tag respectively. If a new project is added, the user is asked for tags he wants to add.
* `tempus remove [all| [project|tag] name]` removes everything or a project/tag by name.
* `tempus [tag|untag] <project name> <tag name>` adds or removes tags to/from a project.
* `tempus rename [project|tag] name new_name` renames a tag or project.
* `tempus status [project|tag] name` gives general or more specific statistics.
* `tempus clear` resets the log, all data entries will be lost. Projects and tags are preserved. (to be implemented)

#Todo
```
[ ] put loglevel in config, default to warning
[ ] moar logging
[ ] sys.exit(-1) in orm -> throuw CriticalError (for others: UserInputError)
[ ] move Project.init_tags() logic to input_parser
[ ] set down milestones vor 0.2 (e.g. server-client version, flask integration, Android client)

```
