### Working With Databases:
* An API wouldn't be much of an API if all it did was pass back hard coded text. Most of the time your API will probably be creating, reading, updating and deleting records of some kind. The most common way to do this is to use relational database, but we could use a new SQL database like Mongo, or some other type of object storage. For our API, we're going to use a relational database because they're easily the most common. We'll be using SQLite for our database.
* We are going to use SQLite
* It is a file base database system (no server required)
* Not softwer installation is required to use SQLite
* We are also going to use an object relational mapper (ORM) called SQLAlchemy.
* Works with Python objects, not SQL
* Allows you to switch your database easily.
* You can control the structure of your database from your code, which can be managed by a revision control system like Git or Subversion
* Supports multiple database platforms.
* We have our database structure in our code, but we need a way to manage our database file. Typically, what you see is a script that creates the database from class definitions, a script that destroys the database so you can start from scratch for testing, and a seed script that enters some initial data for you to work with. With the 1.0 release of Flask, we got a new tool, the Flask command line interface, or CLI. The CLI allows you to run arbitrary commands against your app. This is actually how we're starting our dev web server right now, but PyCharm has handled all those details for us. We'll start by adding a few commands
