Quote a Lang Crawler
------

Hello! Welcome to this repository!  This project is aimed for helping people learn new languages using quotes. It currently is powered by a Python web crawler which fetches data from WikiQuotes and adds it to the DB.  We're looking for help in order to expand the number of languages supported by the app (currently, we're able to fetch only quotes in French), possibly implementing integrations for social networks and SRS systems, as well as (futurally) having our own approach to it.

What does this crawler do?
------

This is a Python implementation in order to fetch data from [wikiquote](https://en.wikiquote.org/wiki/Main_Page). It populates some data from wikiquotes from author.

This was my first project using Python, I am sure it can be improved in so many ways!

Running the project
------

Using Python 3, install the dependencies in requirements.txt by running

 > `pip install -r requirements.txt`

Then run the project with 

 > `python script.py`


## Running MongoDB

The server tries to connect to a MongoDB instance at port 27017 on localhost. You can do this easily using docker with the following command:

`docker run -it -p27017:27017 --name mongodb -d mongo`

This runs a new container with the last version of the `mongo` image and forwards the local port 27017 to the port 27017 in the container instance with name `mongodb`.


## Running Test

Using Python 3, to run test:

> `python -m unittest tests/Test_crawler.py`

