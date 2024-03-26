# Tusdatos Challenge

This project consists of two parts, the first will be hosted in the web_scrapping folder where the exercise is documented in a Jupiter notebook to make it easier to test, the second consists of the entire project in general where all the information is exposed using a pager simple, order the information, order by and search for a specific field for a specific value, currently it only works with strings; Additionally, authorization and authentication was implemented with json web token, for testing the unittest library was used with its respective mocks and finally a non-relational database with MongoDB was used.

**Note:** To consume the judicial processes API it is necessary to have an administrator role, to access the user API you will simply need a user and that it be active,

## How to start?🚀

_These instructions will allow you to get a copy of the project up and running on your local machine for development and testing purposes._

### Installation 🔧

First of all we must clone the repository and after that we must create a virtual environment to install all the necessary libraries

```
python3 -m venv venv # Create virtual environment
source venv/bin/activate # Activate environment, may vary in other os
```

Once the environment is active we can install requirements

```
pip install -r requirements.txt
```

With this we would have everything necessary to run the project.

```
uvicorn main:app --reload
```

## Running tests ⚙️

To run a specific test section

```
python tests/test_delete_processes.py 
```

To run a all tests section

```
python -m unittest discover -s tests
```

## Built with 🛠️

_This project was built with the following tools_

* [Python](https://www.python.org/) - Programming language
* [FastAPI](https://fastapi.tiangolo.com/) - Framework
* [MongoDB](https://www.mongodb.com/) - Database


## Wiki 📖

Once you have the project running you can find the documentation here [Docs](http://localhost:8000/docs#/), I will also share the Postman collection with all the methods

![image](https://github.com/jsdnlb/tusdatos-challenge/assets/17171887/26e44dfc-d097-498c-b8c5-585d750ab1d9)


## Developer by ✒️

* **Daniel Buitrago** - Documentation and programming - [jsdnlb](https://github.com/jsdnlb)
---
