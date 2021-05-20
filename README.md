# **Bhav Copy**

## *Description*

<br>

BSE publishes a "Bhavcopy" (Equity) ZIP every day here: [Bhav Copy](https://www.bseindia.com/markets/MarketInfo/BhavCopy.aspx)

This is a simple web application built using [Django](https://www.djangoproject.com/) and [Vue.js](https://vuejs.org/) that:

* Downloads the equity bhavcopy zip from the above page every day at 18:00 IST for the current date.
* Extracts and parses the CSV file in it.
* Writes the records into Redis with appropriate data structures.
* Renders a simple VueJS frontend with a search box that allows the stored entries to be searched by name and renders a table of results.
* Downloads the results as CSV.
* Search is performed on the backend using Redis.

<br>
<br>

## *Installation*

<br>

Make sure you have installed the following things on your machine

* [Python 3](https://www.python.org/)
* [Redis](https://redis.io/)
* [Node.js](https://nodejs.org/en/)
* [Vue.js](https://vuejs.org/)

<br>

Then install `virtualenv` using the following command 

<br>

```bash
pip install virtualenv
```

<br>

Create the directory where you want to work.

Create a virtual environment in that directory. For that run following command

<br>

```bash
virtualenv venv
```
<br>

Activate that virtual environment using

<br>

```bash
venv\Scripts\activate
```

<br>

After that, you will notice `(venv)` at the left of the command prompt.

Create a separate directory and clone this git repository in that directory.

Then install node packages dependencies using

<br>

```bash
npm install
```

Then build your project using

<br>

```bash
npm run build
```

Then install python packages using

<br>

```bash
pip install -r requirements.txt
```

<br>
<br>

## *Local Setup*

<br>

This is a production code. Please do the following changes to be able to run this code on a local machine.

<br>

Please update the following code in the *db.py* file.

<br>

```python
import os
from .redis_client import RedisClient

redis_client = None

def get_redis_connection():
    global redis_client
    if redis_client is None:
        return RedisClient()
    return redis_client
```

<br>

**Note:** Added some extra files which are ignored by *.gitignore* file but required on a local machine.

<br>
<br>

## *Run on local*

<br>

Before starting your web server run this command to download the [Bhav Copy](https://www.bseindia.com/markets/MarketInfo/BhavCopy.aspx) and store the results in the Redis.

<br>

```bash
python .\api\downloader.py
```

<br>

Alternatively, to set up as a `cron`, you can create a shell script and add it into the crontab.


Now start your webserver using

<br>

```bash
python manage.py runserver
```

<br>

Go to `http://127.0.0.1:8000/` or `http://localhost:8000/`