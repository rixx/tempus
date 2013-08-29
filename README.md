#About

Tempus is CLI time tracking app. It requires Python 3, mysql-connector and SQLAlchemy.

#Usage

* `tempus start [project]` starts the timer. If no project is given, the last running project is assumed. (to be implemented)
* `tempus stop` stops the timer. (to be implemented)
* `tempus pause` stops the timer for the running project and starts the generic pause project. (to be implemented)
* `tempus list [projects|tags]` prints a list of all current projects or tags respectively.
* `tempus add [project|tag] name` adds a new project or tag respectively. If a new project is added, the user is asked for tags he wants to add.
* `tempus remove [all| [project|tag] name]` removes everything or a project/tag by name. Gives an "Are you sure?" dialog. (to be implemented)
* `tempus [tag|untag] <project name> <tag name>` adds or removes tags to/from a project.
* `tempus rename [project|tag] name new_name` renames a tag or project. (to be implemented)
* `tempus status {[project|tag] name` gives general or more specific statistics. (to be implemented)
* `tempus clear` resets the log, all data entries will be lost. Projects and tags are preserved. (to be implemented)

#Todo
```
[ ] output out of orm
[ ] Handle 0 existing tags on project creation
[ ] Handle projects with no tags
[ ] put loglevel in config, default to warning
[ ] sys.exit(-1) in orm -> throuw CriticalError (for others: UserInputError)
[ ] move Project.init_tags() logic to input_parser

```
