#About

Tempus is CLI time tracking app. It requires Python 3.

#Usage

`tempus start` starts the timer; `tempus pause` and `tempus stop` stops it. 
`tempus status` and `tempus report` gives a summary of the logged times.
`tempus clear` resets the log, all data will be lost.

#Todo
 - [ ] Set up a database
     - [ ] Read up on ORM patterns
     - [ ] Decide on ORM
     - [ ] Decide on DB
     - [ ] Write Data Model
     - [ ] Set up DB
     - [ ] Set up ORM
     - [ ] Regain working capabilities

 - [ ] Move away from daily reset
     - [ ] intelligent reporting
     - [ ] extended reporting on custom time period

 - [ ] Count time per project
     - [ ] Allow implicit and explicit adding of projects
     - [ ] Pause/unpause implies that you don't change projects
     - [ ] start while running implies change of projects
     - [ ] Report on per-project basis aswell as totals

 - [ ] Add minimum work hours
     - [ ] per day/week/month/custom
     - [ ] per project/general
     - [ ] intelligent reporting
