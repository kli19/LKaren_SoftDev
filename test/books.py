
#Ryan Aday
#K26 - APIs
#Period 7
#2018-11-15


import urllib.request, json
from flask import Flask, render_template
from util import parse_API

app = Flask(__name__)#Creates an instance of Flask

@app.route('/')
def reroute():
        #https://www.googleapis.com/books/v1/users/<your-user-id>/bookshelves/<as-coll-id>?key=<api-key>
        #key=AIzaSyBw_R-7c6M1aK6BlLozMRxgoNDdOu0TCWY
        url='https://www.googleapis.com/books/v1/volumes?q=isbn:0747532699'
        with urllib.request.urlopen(url) as testfile, open('dataset.json', 'w') as f:
            f.write(testfile.read().decode())
        kind=parse_API.kind()
        items=parse_API.items()
        return render_template("index1.html", kind=kind, items=items )
if (__name__) == "__main__":#if this file is run directly then the Flask app will run
    app.debug = True#allows changes to directly affect local host without rerunning app
app.run()
