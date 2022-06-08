# flask_rest_api

## My first experience with the Flask framework

This project has implemented CRUD. 
4 functions were written that perform various actions, such as creating, 
reading, updating and deleting objects from the dictionary. 
This project did not use a database because this is my first experience with this framework.

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/KhizhnyakSergey/flask_rest_api
$ cd flask_rest_api
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ python -m venv venv
$ venv\Scripts\activate
```

Then install the dependencies:

```sh
(venv)$ pip install -r requirements.txt
```
Note the `(venv)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `venv`.

Once `pip` has finished downloading the dependencies:
```sh
(venv)$ python app.py
```
And navigate to `http://127.0.0.1:3000/api/courses/1`.
