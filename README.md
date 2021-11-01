# How to run this app
We assume that python 3, venv, and Flask are installed on your machine. 

- Navigate to your project folder in a bash terminal and create a virtualenvironment 

```
cd movies_flask/
python3 -m venv venv
source venv/bin/activate
```
- Install the project dependencies listed in `requirements.txt`
```
pip install -r requirements.txt
pip3 install -r requirements.txt <- this is for users who have pip3
```
- You'll notice that there are two python files, `movies_table.py` and `create_movies_db.py`. This app uses SQLite in the background to manage queries and ensure fast load times.
– Run `python3 create_movies_db.py` to create an SQLite database from `movies.json`. This will create a `db.sqlite` file in your project directory. 
- Your flask app will now be ready to rock and roll. Run `python3 movies_table.py` to start the development server. In your terminal, you should see something like this, depending on available ports:
```
* Serving Flask app 'movies_table' (lazy loading)
* Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
* Debug mode: on
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
* Restarting with stat
* Debugger is active!
```
- Navigate to the listed port in your favorite browser and search to see if your favorite movie is in the database! You can also go to '.../api/data' to see the juicy JSON data for your own enjoyment.
