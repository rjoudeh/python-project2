# python-project2

## Web application built using Flask framework and deployed using Docker

### The application is deployed to heroku and it uses `heroku-postgresql`.

The database has one table 'user-app' with the following schema

    _id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    address = Column(String(100), nullable=False)
    age = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    
## `/users` endpoint

The application has one endpoint `https://rjoudeh-python.herokuapp.com/users` which will retrieve the users info as json format from the database.
The retrieval is pagainated. Default retrieve will get the first page with 10 results. Max results per page is 50!

### Custom parameters

You can filter the users list by `age`, `name`, `page` and `per_page`.

### Examples:

https://rjoudeh-python.herokuapp.com/users?age=22

https://rjoudeh-python.herokuapp.com/users?age=22&name=Ma

https://rjoudeh-python.herokuapp.com/users?page=2&per_page=50


## Project structure
#### `main.py` has the flask app creation and the application endpoints.
#### `user.py` has the User Model mapping of the `app_user` db table.
#### `db.py` has the db engine creation and function to get the db session.
