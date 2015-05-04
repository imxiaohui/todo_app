# todo_app
To do list app to help with learning Django and other development tools.

# endlesstasklist
This is the Django app for the project.

## Problems Solved by Modern To-Do List Apps
This is a list of the features of most to-do list apps that I would like to implement.
- Task listing
- Task tagging
- Priority
- Due dates and times
- Reminders

## Problems with Modern To-Do List Apps
These are the problems I've come across while using to-do list apps that I would like to solve.
- Organization
  - This can be solved with tagging. Most task lists allow you to isolate tasks into separate lists, but I would like to see them all at once, too.
- Scheduling
  - With the help of a duration field for tasks, I can implement a scheduling system to find the best time to get something done.
- Sorting
  - With most apps, sorting is done manually by date, priority, or something else concrete.
  - I'd like to implement a sorting mechanism that takes priority, due date, and duration into account.

More features will be added later if necessary, but these are the core features that I'd like to implement.

# Design Decisions

## Backend
Django is my choice because I need to learn more about it for another, more formal project. This will serve as a testing ground until it is releasable.

## Database
SQLite is my current choice, since this is only a personal project and isn't to the point of production.

## GUI
This is going to be a classical to-do list app frontend. The GUI will not feature anything revolutionary, only a place for the extra fields.

## Workflow
Eventually I will be implementing Travis CI in order to teach myself continuous integration. I'll use this in conjunction with Django's built-in testing features.
